"""Atomic Red Team vault builder."""

import io
import os
import re
import tarfile
from collections import defaultdict
from datetime import datetime

import requests
import yaml

from utils.config import ATOMIC_EXECUTORS, ATOMIC_PLATFORMS
from utils.files import ensure_folder, read_text_file, remove_folder_if_exists, write_text_file
from utils.logging_utils import log


ATOMIC_TARBALL_URL = "https://github.com/redcanaryco/atomic-red-team/archive/refs/heads/master.tar.gz"
ATOMIC_REPO_URL_TEMPLATE = "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/{attack_id}/{attack_id}.yaml"
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKING_DIR = os.path.join(PROJECT_ROOT, "workingdir")
ATOMIC_SOURCE_DIR = os.path.join(WORKING_DIR, "atomic-red-team-master")
ATOMIC_SOURCE_ATOMICS_DIR = os.path.join(ATOMIC_SOURCE_DIR, "atomics")
VAULT_DIR = os.path.join(PROJECT_ROOT, "secopskb")
KB_DIR = os.path.join(VAULT_DIR, "kb")
ATOMIC_DIR = os.path.join(KB_DIR, "atomic")
ATOMIC_TESTS_DIR = os.path.join(ATOMIC_DIR, "tests")
ATOMIC_TECHNIQUES_DIR = os.path.join(ATOMIC_DIR, "techniques")
ATOMIC_PLATFORMS_DIR = os.path.join(ATOMIC_DIR, "platforms")
ATOMIC_EXECUTORS_DIR = os.path.join(ATOMIC_DIR, "executors")
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
            raise RuntimeError("Unsafe path in Atomic archive: " + member.name)
    archive.extractall(destination)


def download_atomic_source_if_needed():
    if os.path.isdir(ATOMIC_SOURCE_ATOMICS_DIR):
        log("Using cached Atomic Red Team source", "INFO")
        return

    ensure_folder(WORKING_DIR)
    log("Downloading Atomic Red Team source", "INFO")
    response = requests.get(ATOMIC_TARBALL_URL, timeout=90)
    response.raise_for_status()

    remove_folder_if_exists(ATOMIC_SOURCE_DIR)
    with tarfile.open(fileobj=io.BytesIO(response.content), mode="r:gz") as archive:
        safe_extract_archive(archive, WORKING_DIR)


def load_atomic_tests():
    tests = []
    skipped = 0
    for folder_name in sorted(os.listdir(ATOMIC_SOURCE_ATOMICS_DIR)):
        if not re.match(r"^T\d{4}(?:\.\d{3})?$", folder_name):
            continue
        filepath = os.path.join(ATOMIC_SOURCE_ATOMICS_DIR, folder_name, folder_name + ".yaml")
        if not os.path.exists(filepath):
            continue
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                technique = yaml.safe_load(file) or {}
        except yaml.YAMLError as error:
            skipped += 1
            log("Skipped invalid Atomic YAML " + filepath + ": " + str(error), "ERROR")
            continue

        attack_id = technique.get("attack_technique") or folder_name
        display_name = technique.get("display_name", "")
        for test in normalize_list(technique.get("atomic_tests")):
            if not isinstance(test, dict):
                skipped += 1
                continue
            guid = test.get("auto_generated_guid")
            if not guid:
                skipped += 1
                continue
            if not atomic_test_is_included(test):
                skipped += 1
                continue
            tests.append({
                "attack_id": attack_id,
                "display_name": display_name,
                "test": test,
                "source_path": f"atomics/{attack_id}/{attack_id}.yaml",
            })

    tests.sort(key=lambda item: (item["attack_id"], item["test"].get("name", "")))
    log("Loaded " + str(len(tests)) + " Atomic tests after filters; skipped " + str(skipped), "INFO")
    return tests


def atomic_test_is_included(test):
    platforms = {str(item).lower() for item in normalize_list(test.get("supported_platforms"))}
    executor = str((test.get("executor") or {}).get("name", "") or "").lower()

    if ATOMIC_PLATFORMS and not platforms.intersection({item.lower() for item in ATOMIC_PLATFORMS}):
        return False
    if ATOMIC_EXECUTORS and executor not in {item.lower() for item in ATOMIC_EXECUTORS}:
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


def make_attack_link(attack_id, attack_lookup):
    parent_id = attack_id.split(".", 1)[0]
    link_info = attack_lookup.get(attack_id) or attack_lookup.get(parent_id)
    if not link_info:
        return attack_id
    label = link_info.get("label") or attack_id
    if attack_id != parent_id and attack_id not in attack_lookup:
        label = attack_id
    return f"[[kb/attack/techniques/{link_info['target']}|{label}]]"


def make_test_filename(item):
    test = item["test"]
    return make_safe_name(test.get("auto_generated_guid")) + "-" + make_safe_name(test.get("name", "atomic_test"))


def make_test_link(item):
    test = item["test"]
    return f"[[kb/atomic/tests/{make_test_filename(item)}|{item['attack_id']}: {test.get('name', '')}]]"


def write_metadata_section(item):
    test = item["test"]
    rows = [
        ("Atomic GUID", test.get("auto_generated_guid", "")),
        ("Technique", item["attack_id"] + (": " + item["display_name"] if item["display_name"] else "")),
        ("Platforms", ", ".join(normalize_list(test.get("supported_platforms")))),
        ("Executor", (test.get("executor") or {}).get("name", "")),
        ("Elevation Required", (test.get("executor") or {}).get("elevation_required", "")),
        ("Dependency Executor", test.get("dependency_executor_name", "")),
        ("Source Path", item["source_path"]),
    ]
    text = "## Metadata\n\n"
    for label, value in rows:
        if value not in (None, ""):
            text += f"- {label}: {value}\n"
    return text + "\n"


def write_input_arguments_section(test):
    arguments = test.get("input_arguments")
    if not isinstance(arguments, dict) or not arguments:
        return ""

    text = "## Input Arguments\n\n"
    for name in sorted(arguments.keys()):
        value = arguments[name] or {}
        text += "### " + str(name) + "\n\n"
        if isinstance(value, dict):
            for key in ["description", "type", "default"]:
                if key in value and value[key] not in (None, ""):
                    text += f"- {key}: {value[key]}\n"
        else:
            text += str(value) + "\n"
        text += "\n"
    return text


def write_dependencies_section(test):
    dependencies = normalize_list(test.get("dependencies"))
    if not dependencies:
        return ""

    text = "## Dependencies\n\n"
    for dependency in dependencies:
        if not isinstance(dependency, dict):
            text += "- " + str(dependency) + "\n"
            continue
        if dependency.get("description"):
            text += str(dependency["description"]).strip() + "\n\n"
        fence_language = get_executor_fence_language(test.get("dependency_executor_name", ""))
        if dependency.get("prereq_command"):
            text += "### Prerequisite Check\n\n```" + fence_language + "\n" + str(dependency["prereq_command"]).rstrip() + "\n```\n\n"
        if dependency.get("get_prereq_command"):
            text += "### Get Prerequisite\n\n```" + fence_language + "\n" + str(dependency["get_prereq_command"]).rstrip() + "\n```\n\n"
    return text


def get_executor_fence_language(executor_name):
    normalized = make_safe_name(executor_name).replace("_", "")
    language_map = {
        "bash": "bash",
        "sh": "bash",
        "powershell": "powershell",
        "commandprompt": "cmd",
        "cmd": "cmd",
        "manual": "text",
    }
    return language_map.get(normalized, normalized or "text")


def write_executor_section(test):
    executor = test.get("executor")
    if not isinstance(executor, dict) or not executor:
        return ""

    executor_name = executor.get("name", "executor")
    text = "## Executor\n\n"
    for key in sorted(executor.keys()):
        if key in ["command", "cleanup_command"]:
            continue
        text += f"- {key}: {executor[key]}\n"
    text += "\n"
    if executor.get("command"):
        text += "### Command\n\n```" + get_executor_fence_language(executor_name) + "\n"
        text += str(executor["command"]).rstrip() + "\n```\n\n"
    if executor.get("cleanup_command"):
        text += "### Cleanup\n\n```" + get_executor_fence_language(executor_name) + "\n"
        text += str(executor["cleanup_command"]).rstrip() + "\n```\n\n"
    return text


def build_atomic_test_note(item, attack_lookup):
    test = item["test"]
    platforms = normalize_list(test.get("supported_platforms"))
    executor_name = (test.get("executor") or {}).get("name", "")

    yaml_lines = []
    yaml_write_line(yaml_lines, "atomic_guid", test.get("auto_generated_guid"))
    yaml_write_line(yaml_lines, "title", test.get("name"))
    yaml_write_line(yaml_lines, "framework", "atomic")
    yaml_write_line(yaml_lines, "generated", "true")
    yaml_write_line(yaml_lines, "attack_technique_id", item["attack_id"])
    yaml_write_line(yaml_lines, "attack_technique_name", item["display_name"])
    yaml_write_line(yaml_lines, "source_url", ATOMIC_REPO_URL_TEMPLATE.format(attack_id=item["attack_id"]))
    yaml_write_line(yaml_lines, "build_date", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    yaml_write_line(yaml_lines, "executor", executor_name)
    yaml_write_list(yaml_lines, "aliases", [test.get("auto_generated_guid"), test.get("name")])
    yaml_write_list(yaml_lines, "platforms", platforms)
    yaml_write_list(yaml_lines, "tags", ["atomic", "validation-test"])

    text = render_yaml(yaml_lines)
    text += build_page_start()
    if test.get("description"):
        text += str(test["description"]).strip() + "\n\n"
    text += "## ATT&CK Mapping\n\n"
    text += "- " + make_attack_link(item["attack_id"], attack_lookup) + "\n\n"
    text += write_input_arguments_section(test)
    text += write_dependencies_section(test)
    text += write_executor_section(test)
    text += "## Source\n\n"
    text += "- [Source YAML](" + ATOMIC_REPO_URL_TEMPLATE.format(attack_id=item["attack_id"]) + ")\n"
    return text


def build_atomic_indexes(tests, attack_lookup):
    by_technique = defaultdict(list)
    by_platform = defaultdict(list)
    by_executor = defaultdict(list)
    for item in tests:
        by_technique[item["attack_id"]].append(item)
        for platform in normalize_list(item["test"].get("supported_platforms")):
            by_platform[str(platform)].append(item)
        executor_name = (item["test"].get("executor") or {}).get("name", "unspecified")
        by_executor[str(executor_name or "unspecified")].append(item)

    text = build_page_start()
    text += "# Atomic Red Team\n\n"
    text += "<!-- generated-source-description-start -->\n"
    text += "Atomic Red Team is a library of small, focused tests for emulating ATT&CK techniques in controlled environments. This vault imports Atomic YAML tests, keeps command and dependency blocks with executor-aware code fences, and maps each test back to its ATT&CK technique.\n\n"
    text += "Use Atomic pages as validation references for testing whether detections, analytics, and telemetry collection work as expected. ATT&CK technique pages link to matching Atomic tests, and Sigma simulation metadata links to Atomic tests when GUIDs match.\n\n"
    text += "## Upstream\n\n"
    text += "- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)\n"
    text += "<!-- generated-source-description-end -->\n\n"
    text += "## Areas\n\n"
    text += f"- [[kb/atomic/tests/index|Tests]] ({len(tests)})\n"
    text += f"- [[kb/atomic/techniques/index|Tests by ATT&CK Technique]] ({len(by_technique)})\n"
    text += f"- [[kb/atomic/platforms/index|Tests by Platform]] ({len(by_platform)})\n"
    text += f"- [[kb/atomic/executors/index|Tests by Executor]] ({len(by_executor)})\n"
    write_text_file(os.path.join(ATOMIC_DIR, "index.md"), text)

    text = build_page_start()
    text += "# Atomic Tests\n\n"
    for item in tests:
        text += "- " + make_test_link(item) + "\n"
    write_text_file(os.path.join(ATOMIC_TESTS_DIR, "index.md"), text)

    text = build_page_start()
    text += "# Atomic Tests by ATT&CK Technique\n\n"
    for attack_id in sorted(by_technique.keys()):
        text += "## " + make_attack_link(attack_id, attack_lookup) + "\n\n"
        for item in by_technique[attack_id]:
            text += "- " + make_test_link(item) + "\n"
        text += "\n"
    write_text_file(os.path.join(ATOMIC_TECHNIQUES_DIR, "index.md"), text)

    text = build_page_start()
    text += "# Atomic Tests by Platform\n\n"
    for platform in sorted(by_platform.keys()):
        text += "## " + platform + "\n\n"
        for item in sorted(by_platform[platform], key=lambda value: value["test"].get("name", "")):
            text += "- " + make_test_link(item) + "\n"
        text += "\n"
    write_text_file(os.path.join(ATOMIC_PLATFORMS_DIR, "index.md"), text)

    text = build_page_start()
    text += "# Atomic Tests by Executor\n\n"
    for executor in sorted(by_executor.keys()):
        text += "## " + executor + "\n\n"
        for item in sorted(by_executor[executor], key=lambda value: value["test"].get("name", "")):
            text += "- " + make_test_link(item) + "\n"
        text += "\n"
    write_text_file(os.path.join(ATOMIC_EXECUTORS_DIR, "index.md"), text)


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
    log("Updated Atomic navigation in " + str(changed) + " markdown files", "INFO")


def update_root_indexes(test_count):
    replacements = [
        ("- [[kb/sigma/index|Sigma]]\n", "- [[kb/sigma/index|Sigma]]\n- [[kb/atomic/index|Atomic]]\n"),
        ("- [[kb/sigma/index|Sigma]] (3120 rules)\n", "- [[kb/sigma/index|Sigma]] (3120 rules)\n- [[kb/atomic/index|Atomic]] (" + str(test_count) + " tests)\n"),
        ("- [[kb/car/index|CAR]]\n", "- [[kb/car/index|CAR]]\n- [[kb/atomic/index|Atomic]]\n"),
        ("- [[kb/car/index|CAR]] (102 analytics)\n", "- [[kb/car/index|CAR]] (102 analytics)\n- [[kb/atomic/index|Atomic]] (" + str(test_count) + " tests)\n"),
    ]

    for relative_path in ["index.md", os.path.join("kb", "index.md")]:
        filepath = os.path.join(VAULT_DIR, relative_path)
        if not os.path.exists(filepath):
            continue
        text = read_text_file(filepath)
        text = text.replace(SIGMA_NAV, ATOMIC_NAV).replace(CAR_NAV, ATOMIC_NAV).replace(BASE_NAV, ATOMIC_NAV)
        if relative_path == os.path.join("kb", "index.md"):
            text = re.sub(
                r"- \[\[kb/atomic/index\|Atomic\]\](?: \(\d+ tests\))?",
                "- [[kb/atomic/index|Atomic]] (" + str(test_count) + " tests)",
                text,
                count=1,
            )
        body_without_nav = text.replace(ATOMIC_NAV, "")
        if "- [[kb/atomic/index|Atomic]]" not in body_without_nav:
            for old, new in replacements:
                if old in text:
                    text = text.replace(old, new, 1)
                    break
        write_text_file(filepath, text)


def build_atomic():
    log("Starting Atomic Red Team build", "INFO")
    download_atomic_source_if_needed()
    tests = load_atomic_tests()
    attack_lookup = build_attack_technique_lookup()

    remove_folder_if_exists(ATOMIC_DIR)
    ensure_folder(ATOMIC_TESTS_DIR)
    ensure_folder(ATOMIC_TECHNIQUES_DIR)
    ensure_folder(ATOMIC_PLATFORMS_DIR)
    ensure_folder(ATOMIC_EXECUTORS_DIR)

    for item in tests:
        filepath = os.path.join(ATOMIC_TESTS_DIR, make_test_filename(item) + ".md")
        write_text_file(filepath, build_atomic_test_note(item, attack_lookup))

    build_atomic_indexes(tests, attack_lookup)
    update_vault_navigation()
    update_root_indexes(len(tests))
    log("Finished Atomic Red Team build with " + str(len(tests)) + " tests", "INFO")
