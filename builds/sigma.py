"""SigmaHQ rule vault builder."""

import io
import os
import re
import tarfile
from collections import defaultdict
from datetime import datetime

import requests
import yaml

from utils.config import SIGMA_LEVELS, SIGMA_PRODUCTS, SIGMA_STATUSES
from utils.files import ensure_folder, read_text_file, remove_folder_if_exists, write_text_file
from utils.logging_utils import log


SIGMA_TARBALL_URL = "https://github.com/SigmaHQ/sigma/archive/refs/heads/master.tar.gz"
SIGMA_REPO_RULE_URL_TEMPLATE = "https://github.com/SigmaHQ/sigma/blob/master/{source_path}"
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKING_DIR = os.path.join(PROJECT_ROOT, "workingdir")
SIGMA_SOURCE_DIR = os.path.join(WORKING_DIR, "sigma-master")
SIGMA_RULES_SOURCE_DIR = os.path.join(SIGMA_SOURCE_DIR, "rules")
VAULT_DIR = os.path.join(PROJECT_ROOT, "secopskb")
KB_DIR = os.path.join(VAULT_DIR, "kb")
SIGMA_DIR = os.path.join(KB_DIR, "sigma")
SIGMA_RULES_DIR = os.path.join(SIGMA_DIR, "rules")
SIGMA_TECHNIQUES_DIR = os.path.join(SIGMA_DIR, "techniques")
SIGMA_LOGSOURCES_DIR = os.path.join(SIGMA_DIR, "logsources")
ATOMIC_TESTS_DIR = os.path.join(KB_DIR, "atomic", "tests")
ATTACK_TECHNIQUES_DIR = os.path.join(KB_DIR, "attack", "techniques")

BASE_NAV = "[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]"
CAR_NAV = "[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]"
SIGMA_NAV = "[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]"
ATOMIC_NAV = "[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]"


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
    return ATOMIC_NAV + "\n\n"


def safe_extract_archive(archive, destination):
    destination = os.path.abspath(destination)
    for member in archive.getmembers():
        member_path = os.path.abspath(os.path.join(destination, member.name))
        if not member_path.startswith(destination + os.sep):
            raise RuntimeError("Unsafe path in Sigma archive: " + member.name)
    archive.extractall(destination)


def download_sigma_source_if_needed():
    if os.path.isdir(SIGMA_RULES_SOURCE_DIR):
        log("Using cached SigmaHQ source", "INFO")
        return

    ensure_folder(WORKING_DIR)
    log("Downloading SigmaHQ source", "INFO")
    response = requests.get(SIGMA_TARBALL_URL, timeout=90)
    response.raise_for_status()

    remove_folder_if_exists(SIGMA_SOURCE_DIR)
    with tarfile.open(fileobj=io.BytesIO(response.content), mode="r:gz") as archive:
        safe_extract_archive(archive, WORKING_DIR)


def load_sigma_rules():
    rules = []
    skipped = 0
    for folder, _, filenames in os.walk(SIGMA_RULES_SOURCE_DIR):
        filenames.sort()
        for filename in filenames:
            if not filename.endswith((".yml", ".yaml")):
                continue
            filepath = os.path.join(folder, filename)
            source_path = os.path.relpath(filepath, SIGMA_SOURCE_DIR).replace("\\", "/")
            try:
                with open(filepath, "r", encoding="utf-8") as file:
                    data = yaml.safe_load(file) or {}
            except yaml.YAMLError as error:
                skipped += 1
                log("Skipped invalid Sigma rule " + source_path + ": " + str(error), "ERROR")
                continue
            if not isinstance(data, dict) or not data.get("title"):
                skipped += 1
                continue
            if not sigma_rule_is_included(data):
                skipped += 1
                continue
            rules.append({"data": data, "source_path": source_path})

    rules.sort(key=lambda item: (item["data"].get("title", ""), item["source_path"]))
    log("Loaded " + str(len(rules)) + " Sigma rules after filters; skipped " + str(skipped), "INFO")
    return rules


def build_attack_technique_lookup():
    lookup = {}
    if not os.path.isdir(ATTACK_TECHNIQUES_DIR):
        return lookup

    for filename in os.listdir(ATTACK_TECHNIQUES_DIR):
        if not filename.endswith(".md"):
            continue
        attack_id = filename.split("-", 1)[0]
        if re.match(r"^T\d{4}$", attack_id):
            note_stem = os.path.splitext(filename)[0]
            filepath = os.path.join(ATTACK_TECHNIQUES_DIR, filename)
            try:
                text = read_text_file(filepath)
            except OSError:
                text = ""
            technique_name = ""
            if text.startswith("---\n"):
                end = text.find("\n---\n", 4)
                if end != -1:
                    data = yaml.safe_load(text[4:end]) or {}
                    if isinstance(data, dict):
                        technique_name = data.get("mitre_name", "")
            lookup[attack_id] = {
                "target": note_stem,
                "label": attack_id + (": " + technique_name if technique_name else ""),
            }
            for match in re.finditer(r"^### (T\d{4}\.\d{3}): ([^\n]+)\n\n(\^[^\n]+)", text, flags=re.MULTILINE):
                subtechnique_id = match.group(1)
                subtechnique_name = match.group(2).strip()
                anchor = match.group(3).strip()
                lookup[subtechnique_id] = {
                    "target": note_stem + "#" + anchor,
                    "label": subtechnique_id + ": " + subtechnique_name,
                }
    return lookup


def build_atomic_guid_lookup():
    lookup = {}
    if not os.path.isdir(ATOMIC_TESTS_DIR):
        return lookup

    for filename in os.listdir(ATOMIC_TESTS_DIR):
        if not filename.endswith(".md") or filename == "index.md":
            continue
        filepath = os.path.join(ATOMIC_TESTS_DIR, filename)
        try:
            text = read_text_file(filepath)
        except OSError:
            continue
        match = re.search(r'^atomic_guid: "([^"]+)"', text, flags=re.MULTILINE)
        if match:
            lookup[match.group(1)] = os.path.splitext(filename)[0]
    return lookup


def make_attack_link(attack_id, attack_lookup):
    parent_id = attack_id.split(".", 1)[0]
    link_info = attack_lookup.get(attack_id) or attack_lookup.get(parent_id)
    if not link_info:
        return attack_id
    label = link_info.get("label") or attack_id
    if attack_id != parent_id and attack_id not in attack_lookup:
        label = attack_id
    return f"[[kb/attack/techniques/{link_info['target']}|{label}]]"


def extract_attack_techniques(rule):
    techniques = []
    for tag in normalize_list(rule.get("tags")):
        match = re.match(r"attack\.t(\d{4})(?:\.(\d{3}))?$", str(tag).lower())
        if not match:
            continue
        attack_id = "T" + match.group(1)
        if match.group(2):
            attack_id += "." + match.group(2)
        if attack_id not in techniques:
            techniques.append(attack_id)
    return techniques


def extract_attack_software(rule):
    software = []
    for tag in normalize_list(rule.get("tags")):
        match = re.match(r"attack\.s(\d{4})$", str(tag).lower())
        if match:
            software_id = "S" + match.group(1)
            if software_id not in software:
                software.append(software_id)
    return software


def get_logsource_key(rule):
    logsource = rule.get("logsource") or {}
    if not isinstance(logsource, dict):
        return "unspecified"
    values = [
        str(logsource.get("product", "") or "").strip(),
        str(logsource.get("service", "") or "").strip(),
        str(logsource.get("category", "") or "").strip(),
    ]
    values = [value for value in values if value]
    return " / ".join(values) if values else "unspecified"


def get_logsource_product(rule):
    logsource = rule.get("logsource") or {}
    if not isinstance(logsource, dict):
        return ""
    return str(logsource.get("product", "") or "").strip().lower()


def sigma_rule_is_included(rule):
    level = str(rule.get("level", "") or "").strip().lower()
    product = get_logsource_product(rule)
    status = str(rule.get("status", "") or "").strip().lower()

    if SIGMA_LEVELS and level not in {item.lower() for item in SIGMA_LEVELS}:
        return False
    if SIGMA_PRODUCTS and product not in {item.lower() for item in SIGMA_PRODUCTS}:
        return False
    if SIGMA_STATUSES and status not in {item.lower() for item in SIGMA_STATUSES}:
        return False
    return True


def make_rule_filename(item):
    rule = item["data"]
    rule_id = rule.get("id") or make_safe_name(item["source_path"])
    return make_safe_name(rule_id) + "-" + make_safe_name(rule.get("title", "sigma_rule"))


def make_rule_link(item):
    rule = item["data"]
    return f"[[kb/sigma/rules/{make_rule_filename(item)}|{rule.get('title', '')}]]"


def write_metadata_section(rule, item):
    text = "## Metadata\n\n"
    rows = [
        ("Rule ID", rule.get("id", "")),
        ("Status", rule.get("status", "")),
        ("Level", rule.get("level", "")),
        ("Author", rule.get("author", "")),
        ("Date", rule.get("date", "")),
        ("Modified", rule.get("modified", "")),
        ("License", rule.get("license", "")),
        ("Source Path", item["source_path"]),
    ]
    for label, value in rows:
        if value not in (None, ""):
            text += f"- {label}: {value}\n"
    return text + "\n"


def write_logsource_section(rule):
    logsource = rule.get("logsource")
    if not isinstance(logsource, dict) or not logsource:
        return ""
    text = "## Logsource\n\n"
    for key in sorted(logsource.keys()):
        text += f"- {key}: {logsource[key]}\n"
    return text + "\n"


def write_attack_section(rule, attack_lookup):
    techniques = extract_attack_techniques(rule)
    software = extract_attack_software(rule)
    if not techniques and not software:
        return ""

    text = "## ATT&CK Mapping\n\n"
    if techniques:
        text += "### Techniques\n\n"
        for attack_id in techniques:
            text += "- " + make_attack_link(attack_id, attack_lookup) + "\n"
        text += "\n"
    if software:
        text += "### Software Tags\n\n"
        for software_id in software:
            text += "- " + software_id + "\n"
        text += "\n"
    return text


def write_list_section(title, values):
    values = normalize_list(values)
    if not values:
        return ""
    text = f"## {title}\n\n"
    for value in values:
        text += f"- {value}\n"
    return text + "\n"


def write_detection_section(rule):
    detection = rule.get("detection")
    if not detection:
        return ""
    return "## Detection\n\n```yaml\n" + yaml.safe_dump(detection, sort_keys=False, allow_unicode=True).rstrip() + "\n```\n\n"


def write_simulation_section(rule, atomic_lookup):
    simulations = normalize_list(rule.get("simulation"))
    if not simulations:
        return ""
    text = "## Simulation\n\n"
    for item in simulations:
        if not isinstance(item, dict):
            text += f"- {item}\n"
            continue
        label = item.get("name") or item.get("type") or "simulation"
        text += f"### {label}\n\n"
        atomic_guid = item.get("atomic_guid")
        if atomic_guid and atomic_guid in atomic_lookup:
            text += f"- Atomic Test: [[kb/atomic/tests/{atomic_lookup[atomic_guid]}|{atomic_guid}]]\n"
        for key in sorted(item.keys()):
            text += f"- {key}: {item[key]}\n"
        text += "\n"
    return text


def build_sigma_rule_note(item, attack_lookup, atomic_lookup):
    rule = item["data"]
    techniques = extract_attack_techniques(rule)

    yaml_lines = []
    yaml_write_line(yaml_lines, "sigma_id", rule.get("id"))
    yaml_write_line(yaml_lines, "title", rule.get("title"))
    yaml_write_line(yaml_lines, "framework", "sigma")
    yaml_write_line(yaml_lines, "generated", "true")
    yaml_write_line(yaml_lines, "source_path", item["source_path"])
    yaml_write_line(yaml_lines, "source_url", SIGMA_REPO_RULE_URL_TEMPLATE.format(source_path=item["source_path"]))
    yaml_write_line(yaml_lines, "build_date", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    yaml_write_line(yaml_lines, "status", rule.get("status"))
    yaml_write_line(yaml_lines, "level", rule.get("level"))
    yaml_write_line(yaml_lines, "logsource", get_logsource_key(rule))
    yaml_write_list(yaml_lines, "aliases", [rule.get("id"), rule.get("title")])
    yaml_write_list(yaml_lines, "attack_technique_ids", techniques)
    yaml_write_list(yaml_lines, "tags", ["sigma", "detection-rule"])

    text = render_yaml(yaml_lines)
    text += build_page_start()
    if rule.get("description"):
        text += str(rule["description"]).strip() + "\n\n"
    text += write_logsource_section(rule)
    text += write_attack_section(rule, attack_lookup)
    text += write_detection_section(rule)
    text += write_list_section("Fields", rule.get("fields"))
    text += write_list_section("False Positives", rule.get("falsepositives") or rule.get("false positives"))
    text += write_simulation_section(rule, atomic_lookup)
    text += write_list_section("References", rule.get("references"))
    text += "## Source\n\n"
    text += "- [Source YAML](" + SIGMA_REPO_RULE_URL_TEMPLATE.format(source_path=item["source_path"]) + ")\n"
    return text


def build_sigma_indexes(rules, attack_lookup):
    by_technique = defaultdict(list)
    by_logsource = defaultdict(list)
    by_level = defaultdict(int)
    for item in rules:
        rule = item["data"]
        for attack_id in extract_attack_techniques(rule):
            by_technique[attack_id].append(item)
        by_logsource[get_logsource_key(rule)].append(item)
        by_level[str(rule.get("level", "unspecified") or "unspecified")] += 1

    text = build_page_start()
    text += "# Sigma\n\n"
    text += "<!-- generated-source-description-start -->\n"
    text += "Sigma is a generic detection rule format for describing log-based detections in a SIEM-independent way. This vault imports filtered SigmaHQ rules from the upstream rule repository, preserves rule metadata and detection YAML, and maps rules to ATT&CK techniques and logsources where those tags exist.\n\n"
    text += "Use Sigma pages as portable detection references. ATT&CK technique pages link back to matching Sigma rules, and Sigma simulation metadata links to Atomic Red Team tests when upstream rule metadata includes a matching Atomic GUID.\n\n"
    text += "## Upstream\n\n"
    text += "- [SigmaHQ](https://github.com/SigmaHQ/sigma)\n"
    text += "- [Sigma project](https://sigmahq.io/)\n"
    text += "<!-- generated-source-description-end -->\n\n"
    text += "## Areas\n\n"
    text += f"- [[kb/sigma/rules/index|Rules]] ({len(rules)})\n"
    text += f"- [[kb/sigma/techniques/index|Rules by ATT&CK Technique]] ({len(by_technique)})\n"
    text += f"- [[kb/sigma/logsources/index|Rules by Logsource]] ({len(by_logsource)})\n\n"
    text += "## Levels\n\n"
    for level in sorted(by_level.keys()):
        text += f"- {level}: {by_level[level]}\n"
    write_text_file(os.path.join(SIGMA_DIR, "index.md"), text)

    text = build_page_start()
    text += "# Sigma Rules\n\n"
    for item in rules:
        text += "- " + make_rule_link(item) + "\n"
    write_text_file(os.path.join(SIGMA_RULES_DIR, "index.md"), text)

    text = build_page_start()
    text += "# Sigma Rules by ATT&CK Technique\n\n"
    for attack_id in sorted(by_technique.keys()):
        text += "## " + make_attack_link(attack_id, attack_lookup) + "\n\n"
        for item in sorted(by_technique[attack_id], key=lambda value: value["data"].get("title", "")):
            text += "- " + make_rule_link(item) + "\n"
        text += "\n"
    write_text_file(os.path.join(SIGMA_TECHNIQUES_DIR, "index.md"), text)

    text = build_page_start()
    text += "# Sigma Rules by Logsource\n\n"
    for logsource in sorted(by_logsource.keys()):
        text += "## " + logsource + "\n\n"
        for item in sorted(by_logsource[logsource], key=lambda value: value["data"].get("title", "")):
            text += "- " + make_rule_link(item) + "\n"
        text += "\n"
    write_text_file(os.path.join(SIGMA_LOGSOURCES_DIR, "index.md"), text)


def update_vault_navigation():
    changed = 0
    for folder, _, filenames in os.walk(VAULT_DIR):
        for filename in filenames:
            if not filename.endswith(".md"):
                continue
            filepath = os.path.join(folder, filename)
            text = read_text_file(filepath)
            new_text = text.replace(SIGMA_NAV, ATOMIC_NAV).replace(CAR_NAV, ATOMIC_NAV).replace(BASE_NAV, ATOMIC_NAV)
            if new_text != text:
                write_text_file(filepath, new_text)
                changed += 1
    log("Updated Sigma navigation in " + str(changed) + " markdown files", "INFO")


def update_root_indexes(rule_count):
    replacements = [
        ("- [[kb/car/index|CAR]]\n", "- [[kb/car/index|CAR]]\n- [[kb/sigma/index|Sigma]]\n"),
        ("- [[kb/car/index|CAR]] (102 analytics)\n", "- [[kb/car/index|CAR]] (102 analytics)\n- [[kb/sigma/index|Sigma]] (" + str(rule_count) + " rules)\n"),
        ("- [[kb/defend/index|D3FEND]]\n", "- [[kb/defend/index|D3FEND]]\n- [[kb/sigma/index|Sigma]]\n"),
        ("- [[kb/defend/index|D3FEND]] (271 techniques)\n", "- [[kb/defend/index|D3FEND]] (271 techniques)\n- [[kb/sigma/index|Sigma]] (" + str(rule_count) + " rules)\n"),
    ]

    for relative_path in ["index.md", os.path.join("kb", "index.md")]:
        filepath = os.path.join(VAULT_DIR, relative_path)
        if not os.path.exists(filepath):
            continue
        text = read_text_file(filepath)
        text = text.replace(SIGMA_NAV, ATOMIC_NAV).replace(CAR_NAV, ATOMIC_NAV).replace(BASE_NAV, ATOMIC_NAV)
        if relative_path == os.path.join("kb", "index.md"):
            text = re.sub(
                r"- \[\[kb/sigma/index\|Sigma\]\](?: \(\d+ rules\))?",
                "- [[kb/sigma/index|Sigma]] (" + str(rule_count) + " rules)",
                text,
                count=1,
            )
        body_without_nav = text.replace(ATOMIC_NAV, "")
        if "- [[kb/sigma/index|Sigma]]" not in body_without_nav:
            for old, new in replacements:
                if old in text:
                    text = text.replace(old, new, 1)
                    break
        write_text_file(filepath, text)


def build_sigma():
    log("Starting Sigma build", "INFO")
    download_sigma_source_if_needed()
    rules = load_sigma_rules()
    attack_lookup = build_attack_technique_lookup()
    atomic_lookup = build_atomic_guid_lookup()

    remove_folder_if_exists(SIGMA_DIR)
    ensure_folder(SIGMA_RULES_DIR)
    ensure_folder(SIGMA_TECHNIQUES_DIR)
    ensure_folder(SIGMA_LOGSOURCES_DIR)

    for item in rules:
        filepath = os.path.join(SIGMA_RULES_DIR, make_rule_filename(item) + ".md")
        write_text_file(filepath, build_sigma_rule_note(item, attack_lookup, atomic_lookup))

    build_sigma_indexes(rules, attack_lookup)
    update_vault_navigation()
    update_root_indexes(len(rules))
    log("Finished Sigma build with " + str(len(rules)) + " rules", "INFO")
