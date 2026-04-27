"""LOLBAS vault builder."""

import io
import os
import re
import tarfile
from collections import defaultdict
from datetime import datetime

import requests
import yaml

from utils.config import LOLBAS_CATEGORIES, LOLBAS_FUNCTIONS
from utils.files import ensure_folder, read_text_file, remove_folder_if_exists, write_text_file
from utils.logging_utils import log


LOLBAS_TARBALL_URL = "https://github.com/LOLBAS-Project/LOLBAS/archive/refs/heads/master.tar.gz"
LOLBAS_PROJECT_URL = "https://lolbas-project.github.io/"
LOLBAS_REPO_URL = "https://github.com/LOLBAS-Project/LOLBAS"
LOLBAS_REPO_SOURCE_URL_TEMPLATE = "https://github.com/LOLBAS-Project/LOLBAS/blob/master/{source_path}"
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKING_DIR = os.path.join(PROJECT_ROOT, "workingdir")
LOLBAS_SOURCE_DIR = os.path.join(WORKING_DIR, "LOLBAS-master")
VAULT_DIR = os.path.join(PROJECT_ROOT, "secopskb")
KB_DIR = os.path.join(VAULT_DIR, "kb")
LOLBAS_DIR = os.path.join(KB_DIR, "lolbas")
LOLBAS_ENTRIES_DIR = os.path.join(LOLBAS_DIR, "entries")
LOLBAS_CATEGORIES_DIR = os.path.join(LOLBAS_DIR, "categories")
LOLBAS_FUNCTIONS_DIR = os.path.join(LOLBAS_DIR, "functions")
LOLBAS_TECHNIQUES_DIR = os.path.join(LOLBAS_DIR, "techniques")
ATTACK_TECHNIQUES_DIR = os.path.join(KB_DIR, "attack", "techniques")

BASE_NAV = "[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]"
CAR_NAV = "[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]"
SIGMA_NAV = "[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]"
ATOMIC_NAV = "[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]"
LOLBAS_NAV = "[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]"


def make_safe_name(value):
    value = str(value).strip().lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    value = re.sub(r"_+", "_", value)
    return value.strip("_") or "untitled"


def normalize_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return [item for item in value if item not in (None, "")]
    return [value]


def yaml_scalar(value):
    text = str(value).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{text}"'


def yaml_write_line(lines, key, value):
    if value in (None, ""):
        return
    lines.append(f"{key}: {yaml_scalar(value)}")


def yaml_write_list(lines, key, values):
    values = normalize_list(values)
    if not values:
        return
    lines.append(f"{key}:")
    for value in values:
        lines.append(f"  - {yaml_scalar(value)}")


def render_yaml(lines):
    return "---\n" + "\n".join(lines) + "\n---\n\n"


def build_page_start():
    return LOLBAS_NAV + "\n\n"


def safe_extract_archive(archive, destination):
    destination = os.path.abspath(destination)
    for member in archive.getmembers():
        member_path = os.path.abspath(os.path.join(destination, member.name))
        if not member_path.startswith(destination + os.sep):
            raise RuntimeError("Unsafe path in LOLBAS archive: " + member.name)
    archive.extractall(destination)


def download_lolbas_source_if_needed():
    if os.path.isdir(LOLBAS_SOURCE_DIR):
        log("Using cached LOLBAS source", "INFO")
        return

    ensure_folder(WORKING_DIR)
    log("Downloading LOLBAS source", "INFO")
    response = requests.get(LOLBAS_TARBALL_URL, timeout=90)
    response.raise_for_status()

    remove_folder_if_exists(LOLBAS_SOURCE_DIR)
    with tarfile.open(fileobj=io.BytesIO(response.content), mode="r:gz") as archive:
        safe_extract_archive(archive, WORKING_DIR)


def load_lolbas_entries():
    entries = []
    skipped = 0
    for folder, _, filenames in os.walk(LOLBAS_SOURCE_DIR):
        folder_parts = folder.split(os.sep)
        if ".git" in folder_parts or ".github" in folder_parts or "Archive-Old-Version" in folder_parts:
            continue
        filenames.sort()
        for filename in filenames:
            if not filename.endswith((".yml", ".yaml")):
                continue
            filepath = os.path.join(folder, filename)
            source_path = os.path.relpath(filepath, LOLBAS_SOURCE_DIR).replace("\\", "/")
            try:
                with open(filepath, "r", encoding="utf-8") as file:
                    data = yaml.safe_load(file) or {}
            except yaml.YAMLError as error:
                skipped += 1
                log("Skipped invalid LOLBAS YAML " + source_path + ": " + str(error), "ERROR")
                continue
            if not isinstance(data, dict) or not data.get("Name"):
                skipped += 1
                continue
            item = {
                "data": data,
                "source_path": source_path,
                "category": get_source_category(source_path),
            }
            if not lolbas_entry_is_included(item):
                skipped += 1
                continue
            entries.append(item)

    entries.sort(key=lambda item: (item["category"], str(item["data"].get("Name", ""))))
    log("Loaded " + str(len(entries)) + " LOLBAS entries after filters; skipped " + str(skipped), "INFO")
    return entries


def get_source_category(source_path):
    parts = source_path.split("/")
    if parts and parts[0] == "yml" and len(parts) > 1:
        return parts[1]
    return parts[0] if parts else "uncategorized"


def lolbas_entry_is_included(item):
    category = item["category"].lower()
    functions = {str(value).lower() for value in extract_functions(item)}

    if LOLBAS_CATEGORIES and category not in {value.lower() for value in LOLBAS_CATEGORIES}:
        return False
    if LOLBAS_FUNCTIONS and not functions.intersection({value.lower() for value in LOLBAS_FUNCTIONS}):
        return False
    return True


def build_attack_technique_lookup():
    lookup = {}
    if not os.path.isdir(ATTACK_TECHNIQUES_DIR):
        return lookup

    for filename in os.listdir(ATTACK_TECHNIQUES_DIR):
        if not filename.endswith(".md"):
            continue
        attack_id = filename.split("-", 1)[0]
        if re.match(r"^T\d{4}$", attack_id):
            lookup[attack_id] = os.path.splitext(filename)[0]
    return lookup


def make_attack_link(attack_id, attack_lookup):
    parent_id = attack_id.split(".", 1)[0]
    target = attack_lookup.get(parent_id)
    if not target:
        return attack_id
    return f"[[kb/attack/techniques/{target}|{attack_id}]]"


def extract_commands(data):
    commands = data.get("Commands")
    return [item for item in normalize_list(commands) if isinstance(item, dict)]


def extract_functions(item):
    functions = []
    for command in extract_commands(item["data"]):
        value = command.get("Category") or command.get("Function")
        if value and value not in functions:
            functions.append(value)
    return functions


def extract_techniques(item):
    techniques = []
    for command in extract_commands(item["data"]):
        for value in normalize_list(command.get("MitreID") or command.get("MITRE") or command.get("ATT&CK")):
            value = str(value).strip().upper()
            if re.match(r"^T\d{4}(?:\.\d{3})?$", value) and value not in techniques:
                techniques.append(value)
    return techniques


def make_entry_filename(item):
    name = item["data"].get("Name", "lolbas")
    return make_safe_name(item["category"]) + "-" + make_safe_name(name)


def make_entry_link(item):
    name = item["data"].get("Name", "")
    return f"[[kb/lolbas/entries/{make_entry_filename(item)}|{name}]]"


def write_metadata_section(item):
    data = item["data"]
    text = "## Metadata\n\n"
    rows = [
        ("Category", item["category"]),
        ("Created", data.get("Created", "")),
        ("Author", data.get("Author", "")),
        ("Source Path", item["source_path"]),
    ]
    for label, value in rows:
        if value not in (None, ""):
            text += f"- {label}: {value}\n"
    return text + "\n"


def write_list_section(title, values):
    values = normalize_list(values)
    if not values:
        return ""
    text = f"## {title}\n\n"
    for value in values:
        text += f"- {value}\n"
    return text + "\n"


def write_paths_section(data):
    paths = normalize_list(data.get("Full_Path") or data.get("FullPath") or data.get("Paths"))
    if not paths:
        return ""
    text = "## Paths\n\n"
    for path in paths:
        if isinstance(path, dict):
            for value in path.values():
                if value:
                    text += f"- `{value}`\n"
        else:
            text += f"- `{path}`\n"
    return text + "\n"


def write_commands_section(item, attack_lookup):
    commands = extract_commands(item["data"])
    if not commands:
        return ""
    text = "## Commands\n\n"
    for index, command in enumerate(commands, start=1):
        title = command.get("Category") or command.get("Description") or "Command"
        text += "### " + str(index) + ". " + str(title) + "\n\n"
        if command.get("Description"):
            text += str(command["Description"]).strip() + "\n\n"
        if command.get("Command"):
            text += "```cmd\n" + str(command["Command"]).rstrip() + "\n```\n\n"
        rows = [
            ("Use Case", command.get("Usecase", "")),
            ("Privileges", command.get("Privileges", "")),
            ("Operating System", command.get("OperatingSystem", "")),
        ]
        for label, value in rows:
            if value not in (None, ""):
                text += f"- {label}: {value}\n"
        techniques = []
        for value in normalize_list(command.get("MitreID") or command.get("MITRE") or command.get("ATT&CK")):
            value = str(value).strip().upper()
            if re.match(r"^T\d{4}(?:\.\d{3})?$", value):
                techniques.append(value)
        if techniques:
            text += "- ATT&CK: " + ", ".join(make_attack_link(value, attack_lookup) for value in techniques) + "\n"
        text += "\n"
    return text


def write_detections_section(data):
    detections = normalize_list(data.get("Detection"))
    if not detections:
        return ""
    text = "## Detections\n\n"
    for detection in detections:
        if isinstance(detection, dict):
            for key in sorted(detection.keys()):
                text += f"- {key}: {detection[key]}\n"
        else:
            text += f"- {detection}\n"
    return text + "\n"


def build_lolbas_entry_note(item, attack_lookup):
    data = item["data"]
    techniques = extract_techniques(item)
    functions = extract_functions(item)

    yaml_lines = []
    yaml_write_line(yaml_lines, "title", data.get("Name"))
    yaml_write_line(yaml_lines, "framework", "lolbas")
    yaml_write_line(yaml_lines, "generated", "true")
    yaml_write_line(yaml_lines, "source_path", item["source_path"])
    yaml_write_line(yaml_lines, "source_url", LOLBAS_REPO_SOURCE_URL_TEMPLATE.format(source_path=item["source_path"]))
    yaml_write_line(yaml_lines, "build_date", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    yaml_write_line(yaml_lines, "category", item["category"])
    yaml_write_list(yaml_lines, "aliases", [data.get("Name")])
    yaml_write_list(yaml_lines, "functions", functions)
    yaml_write_list(yaml_lines, "attack_technique_ids", techniques)
    yaml_write_list(yaml_lines, "tags", ["lolbas", "living-off-the-land"])

    text = render_yaml(yaml_lines)
    text += build_page_start()
    text += "# " + str(data.get("Name", "")) + "\n\n"
    if data.get("Description"):
        text += str(data["Description"]).strip() + "\n\n"
    text += write_metadata_section(item)
    text += write_paths_section(data)
    text += write_commands_section(item, attack_lookup)
    text += write_detections_section(data)
    text += write_list_section("Resources", data.get("Resources"))
    text += write_list_section("Acknowledgements", data.get("Acknowledgement") or data.get("Acknowledgements"))
    text += "## Source\n\n"
    text += "- [LOLBAS project](" + LOLBAS_PROJECT_URL + ")\n"
    text += "- [Source YAML](" + LOLBAS_REPO_SOURCE_URL_TEMPLATE.format(source_path=item["source_path"]) + ")\n"
    return text


def build_lolbas_indexes(entries, attack_lookup):
    by_category = defaultdict(list)
    by_function = defaultdict(list)
    by_technique = defaultdict(list)
    for item in entries:
        by_category[item["category"]].append(item)
        for function in extract_functions(item):
            by_function[str(function)].append(item)
        for attack_id in extract_techniques(item):
            by_technique[attack_id].append(item)

    text = build_page_start()
    text += "# LOLBAS\n\n"
    text += "LOLBAS is the Living Off The Land Binaries, Scripts and Libraries project. It is a curated reference of legitimate Windows binaries, scripts, and libraries that can be abused for attacker tradecraft and should be understood by defenders.\n\n"
    text += "This vault imports LOLBAS YAML records into generated notes, maps entries to ATT&CK techniques where upstream mappings exist, and indexes entries by category and function for detection engineering and validation pivots.\n\n"
    text += "## Upstream\n\n"
    text += "- [LOLBAS website](" + LOLBAS_PROJECT_URL + ")\n"
    text += "- [LOLBAS repository](" + LOLBAS_REPO_URL + ")\n\n"
    text += "## Areas\n\n"
    text += f"- [[kb/lolbas/entries/index|Entries]] ({len(entries)})\n"
    text += f"- [[kb/lolbas/categories/index|Entries by Category]] ({len(by_category)})\n"
    text += f"- [[kb/lolbas/functions/index|Entries by Function]] ({len(by_function)})\n"
    text += f"- [[kb/lolbas/techniques/index|Entries by ATT&CK Technique]] ({len(by_technique)})\n"
    write_text_file(os.path.join(LOLBAS_DIR, "index.md"), text)

    text = build_page_start()
    text += "# LOLBAS Entries\n\n"
    for item in entries:
        text += "- " + make_entry_link(item) + "\n"
    write_text_file(os.path.join(LOLBAS_ENTRIES_DIR, "index.md"), text)

    text = build_page_start()
    text += "# LOLBAS Entries by Category\n\n"
    for category in sorted(by_category.keys()):
        text += "## " + category + "\n\n"
        for item in sorted(by_category[category], key=lambda value: value["data"].get("Name", "")):
            text += "- " + make_entry_link(item) + "\n"
        text += "\n"
    write_text_file(os.path.join(LOLBAS_CATEGORIES_DIR, "index.md"), text)

    text = build_page_start()
    text += "# LOLBAS Entries by Function\n\n"
    for function in sorted(by_function.keys()):
        text += "## " + function + "\n\n"
        for item in sorted(by_function[function], key=lambda value: value["data"].get("Name", "")):
            text += "- " + make_entry_link(item) + "\n"
        text += "\n"
    write_text_file(os.path.join(LOLBAS_FUNCTIONS_DIR, "index.md"), text)

    text = build_page_start()
    text += "# LOLBAS Entries by ATT&CK Technique\n\n"
    for attack_id in sorted(by_technique.keys()):
        text += "## " + make_attack_link(attack_id, attack_lookup) + "\n\n"
        for item in sorted(by_technique[attack_id], key=lambda value: value["data"].get("Name", "")):
            text += "- " + make_entry_link(item) + "\n"
        text += "\n"
    write_text_file(os.path.join(LOLBAS_TECHNIQUES_DIR, "index.md"), text)


def update_vault_navigation():
    changed = 0
    for folder, _, filenames in os.walk(VAULT_DIR):
        for filename in filenames:
            if not filename.endswith(".md"):
                continue
            filepath = os.path.join(folder, filename)
            text = read_text_file(filepath)
            new_text = (
                text.replace(ATOMIC_NAV, LOLBAS_NAV)
                .replace(SIGMA_NAV, LOLBAS_NAV)
                .replace(CAR_NAV, LOLBAS_NAV)
                .replace(BASE_NAV, LOLBAS_NAV)
            )
            if new_text != text:
                write_text_file(filepath, new_text)
                changed += 1
    log("Updated LOLBAS navigation in " + str(changed) + " markdown files", "INFO")


def update_root_indexes(entry_count):
    replacements = [
        ("- [[kb/atomic/index|Atomic]]\n", "- [[kb/atomic/index|Atomic]]\n- [[kb/lolbas/index|LOLBAS]]\n"),
        ("- [[kb/atomic/index|Atomic]] (1790 tests)\n", "- [[kb/atomic/index|Atomic]] (1790 tests)\n- [[kb/lolbas/index|LOLBAS]] (" + str(entry_count) + " entries)\n"),
        ("- [[kb/sigma/index|Sigma]]\n", "- [[kb/sigma/index|Sigma]]\n- [[kb/lolbas/index|LOLBAS]]\n"),
        ("- [[kb/sigma/index|Sigma]] (1484 rules)\n", "- [[kb/sigma/index|Sigma]] (1484 rules)\n- [[kb/lolbas/index|LOLBAS]] (" + str(entry_count) + " entries)\n"),
    ]

    for relative_path in ["index.md", os.path.join("kb", "index.md")]:
        filepath = os.path.join(VAULT_DIR, relative_path)
        if not os.path.exists(filepath):
            continue
        text = read_text_file(filepath)
        text = (
            text.replace(ATOMIC_NAV, LOLBAS_NAV)
            .replace(SIGMA_NAV, LOLBAS_NAV)
            .replace(CAR_NAV, LOLBAS_NAV)
            .replace(BASE_NAV, LOLBAS_NAV)
        )
        if relative_path == os.path.join("kb", "index.md"):
            text = re.sub(
                r"- \[\[kb/lolbas/index\|LOLBAS\]\](?: \(\d+ entries\))?",
                "- [[kb/lolbas/index|LOLBAS]] (" + str(entry_count) + " entries)",
                text,
                count=1,
            )
        body_without_nav = text.replace(LOLBAS_NAV, "")
        if "- [[kb/lolbas/index|LOLBAS]]" not in body_without_nav:
            for old, new in replacements:
                if old in text:
                    text = text.replace(old, new, 1)
                    break
        write_text_file(filepath, text)


def build_lolbas():
    log("Starting LOLBAS build", "INFO")
    download_lolbas_source_if_needed()
    entries = load_lolbas_entries()
    attack_lookup = build_attack_technique_lookup()

    remove_folder_if_exists(LOLBAS_DIR)
    ensure_folder(LOLBAS_ENTRIES_DIR)
    ensure_folder(LOLBAS_CATEGORIES_DIR)
    ensure_folder(LOLBAS_FUNCTIONS_DIR)
    ensure_folder(LOLBAS_TECHNIQUES_DIR)

    for item in entries:
        filepath = os.path.join(LOLBAS_ENTRIES_DIR, make_entry_filename(item) + ".md")
        write_text_file(filepath, build_lolbas_entry_note(item, attack_lookup))

    build_lolbas_indexes(entries, attack_lookup)
    update_vault_navigation()
    update_root_indexes(len(entries))
    log("Finished LOLBAS build with " + str(len(entries)) + " entries", "INFO")
