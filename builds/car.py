"""MITRE CAR vault builder."""

import io
import os
import re
import tarfile
from collections import defaultdict
from datetime import datetime

import requests
import yaml

from utils.files import ensure_folder, read_text_file, remove_folder_if_exists, write_text_file
from utils.logging_utils import log


CAR_TARBALL_URL = "https://github.com/mitre-attack/car/archive/refs/heads/master.tar.gz"
CAR_ANALYTIC_URL_TEMPLATE = "https://car.mitre.org/analytics/{car_id}/"
CAR_REPO_ANALYTIC_URL_TEMPLATE = "https://github.com/mitre-attack/car/blob/master/analytics/{car_id}.yaml"
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKING_DIR = os.path.join(PROJECT_ROOT, "workingdir")
CAR_SOURCE_DIR = os.path.join(WORKING_DIR, "car-master")
VAULT_DIR = os.path.join(PROJECT_ROOT, "secopskb")
KB_DIR = os.path.join(VAULT_DIR, "kb")
CAR_DIR = os.path.join(KB_DIR, "car")
CAR_ANALYTICS_DIR = os.path.join(CAR_DIR, "analytics")
CAR_BY_TECHNIQUE_DIR = os.path.join(CAR_DIR, "techniques")
ATTACK_TECHNIQUES_DIR = os.path.join(KB_DIR, "attack", "techniques")

OLD_NAV = "[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]"
NEW_NAV = "[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]"


def make_safe_name(value):
    value = value.strip().lower()
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
    return NEW_NAV + "\n\n"


def download_car_source_if_needed():
    analytics_dir = os.path.join(CAR_SOURCE_DIR, "analytics")
    if os.path.isdir(analytics_dir):
        log("Using cached MITRE CAR source", "INFO")
        return

    ensure_folder(WORKING_DIR)
    log("Downloading MITRE CAR source", "INFO")
    response = requests.get(CAR_TARBALL_URL, timeout=60)
    response.raise_for_status()

    remove_folder_if_exists(CAR_SOURCE_DIR)
    with tarfile.open(fileobj=io.BytesIO(response.content), mode="r:gz") as archive:
        safe_extract_car_archive(archive, WORKING_DIR)


def safe_extract_car_archive(archive, destination):
    destination = os.path.abspath(destination)
    for member in archive.getmembers():
        member_path = os.path.abspath(os.path.join(destination, member.name))
        if not member_path.startswith(destination + os.sep):
            raise RuntimeError("Unsafe path in CAR archive: " + member.name)
    archive.extractall(destination)


def load_car_analytics():
    analytics_dir = os.path.join(CAR_SOURCE_DIR, "analytics")
    analytics = []

    for filename in sorted(os.listdir(analytics_dir)):
        if not filename.endswith((".yml", ".yaml")):
            continue
        filepath = os.path.join(analytics_dir, filename)
        with open(filepath, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file) or {}
        if data.get("id"):
            analytics.append(data)

    analytics.sort(key=lambda item: item.get("id", ""))
    return analytics


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


def make_car_filename(analytic):
    car_id = analytic.get("id", "CAR")
    title = analytic.get("title", "")
    return f"{car_id}-{make_safe_name(title)}"


def make_car_link(analytic):
    filename = make_car_filename(analytic)
    return f"[[kb/car/analytics/{filename}|{analytic.get('id')}: {analytic.get('title', '')}]]"


def build_car_id_lookup(analytics):
    return {analytic.get("id"): make_car_filename(analytic) for analytic in analytics if analytic.get("id")}


def replace_car_relative_links(text, car_lookup):
    def replace_match(match):
        label = match.group(1)
        car_id = match.group(2)
        target = car_lookup.get(car_id)
        if not target:
            return match.group(0)
        return f"[[kb/car/analytics/{target}|{label}]]"

    pattern = r"\[([^\]]+)\]\(\.\./(CAR-\d{4}-\d{2}-\d{3})(?:/)?\)"
    return re.sub(pattern, replace_match, text)


def extract_coverage_techniques(analytic):
    techniques = []
    for item in normalize_list(analytic.get("coverage")):
        if not isinstance(item, dict):
            continue
        for attack_id in [item.get("technique")] + normalize_list(item.get("subtechniques")):
            if attack_id and attack_id not in techniques:
                techniques.append(attack_id)
    return techniques


def extract_implementation_types(analytic):
    values = []
    for item in normalize_list(analytic.get("implementations")):
        if not isinstance(item, dict):
            continue
        value = item.get("type")
        if value and value not in values:
            values.append(value)
    return values


def write_metadata_section(analytic):
    rows = []
    rows.append(f"- CAR ID: {analytic.get('id', '')}")
    rows.append(f"- Submission Date: {analytic.get('submission_date', '')}")
    update_date = analytic.get("update_date")
    if update_date:
        rows.append(f"- Update Date: {update_date}")
    rows.append(f"- Information Domain: {analytic.get('information_domain', '')}")
    rows.append("- Analytic Type: " + ", ".join(normalize_list(analytic.get("analytic_types"))))
    rows.append("- Platforms: " + ", ".join(normalize_list(analytic.get("platforms"))))
    rows.append("- Data Subtypes: " + ", ".join(normalize_list(analytic.get("subtypes"))))
    rows.append("- Contributors: " + ", ".join(normalize_list(analytic.get("contributors"))))
    return "## Metadata\n\n" + "\n".join(rows) + "\n\n"


def write_coverage_section(analytic, attack_lookup):
    coverage = normalize_list(analytic.get("coverage"))
    if not coverage:
        return ""

    text = "## ATT&CK Coverage\n\n"
    for item in coverage:
        if not isinstance(item, dict):
            continue
        technique = item.get("technique", "")
        coverage_value = item.get("coverage", "")
        tactics = ", ".join(normalize_list(item.get("tactics")))
        subtechniques = normalize_list(item.get("subtechniques"))

        line = "- " + make_attack_link(technique, attack_lookup)
        details = []
        if coverage_value:
            details.append("coverage: " + str(coverage_value))
        if tactics:
            details.append("tactics: " + tactics)
        if details:
            line += " (" + "; ".join(details) + ")"
        text += line + "\n"
        for subtechnique in subtechniques:
            text += "  - " + make_attack_link(subtechnique, attack_lookup) + "\n"
    return text + "\n"


def write_implementations_section(analytic, car_lookup):
    implementations = normalize_list(analytic.get("implementations"))
    if not implementations:
        return ""

    text = "## Implementations\n\n"
    for item in implementations:
        if not isinstance(item, dict):
            continue
        implementation_type = item.get("type", "implementation")
        text += f"### {implementation_type}\n\n"
        if item.get("description"):
            description = replace_car_relative_links(str(item["description"]).strip(), car_lookup)
            text += description + "\n\n"
        if item.get("data_model"):
            text += f"- Data Model: {item['data_model']}\n\n"
        if item.get("code"):
            fence_type = make_safe_name(str(implementation_type)).replace("_", "")
            text += f"```{fence_type}\n{str(item['code']).rstrip()}\n```\n\n"
    return text


def write_simple_list_section(title, values):
    values = normalize_list(values)
    if not values:
        return ""
    text = f"## {title}\n\n"
    for value in values:
        text += f"- {value}\n"
    return text + "\n"


def write_unit_tests_section(analytic, car_lookup):
    tests = normalize_list(analytic.get("unit_tests"))
    if not tests:
        return ""

    text = "## Unit Tests\n\n"
    for test in tests:
        if not isinstance(test, dict):
            continue
        if test.get("description"):
            description = replace_car_relative_links(str(test["description"]).strip(), car_lookup)
            text += description + "\n\n"
        configurations = ", ".join(normalize_list(test.get("configurations")))
        if configurations:
            text += f"- Configurations: {configurations}\n\n"
        commands = normalize_list(test.get("commands"))
        if commands:
            text += "```text\n" + "\n".join(str(command) for command in commands) + "\n```\n\n"
    return text


def write_d3fend_section(analytic):
    mappings = normalize_list(analytic.get("d3fend_mappings"))
    if not mappings:
        return ""

    text = "## D3FEND Mappings\n\n"
    for item in mappings:
        if not isinstance(item, dict):
            continue
        d3fend_id = item.get("id", "")
        label = item.get("label", "")
        if d3fend_id and label:
            text += f"- [[kb/defend/techniques/{d3fend_id}-{make_safe_name(label)}|{d3fend_id}: {label}]]\n"
        elif d3fend_id:
            text += f"- {d3fend_id}\n"
    return text + "\n"


def build_car_note(analytic, attack_lookup, car_lookup):
    car_id = analytic.get("id", "")
    title = analytic.get("title", "")
    coverage_ids = extract_coverage_techniques(analytic)
    implementation_types = extract_implementation_types(analytic)

    yaml_lines = []
    yaml_write_line(yaml_lines, "car_id", car_id)
    yaml_write_line(yaml_lines, "title", title)
    yaml_write_line(yaml_lines, "framework", "car")
    yaml_write_line(yaml_lines, "generated", "true")
    yaml_write_line(yaml_lines, "source_url", CAR_ANALYTIC_URL_TEMPLATE.format(car_id=car_id))
    yaml_write_line(yaml_lines, "repo_url", CAR_REPO_ANALYTIC_URL_TEMPLATE.format(car_id=car_id))
    yaml_write_line(yaml_lines, "build_date", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    yaml_write_list(yaml_lines, "aliases", [car_id, title])
    yaml_write_list(yaml_lines, "attack_technique_ids", coverage_ids)
    yaml_write_list(yaml_lines, "platforms", analytic.get("platforms"))
    yaml_write_list(yaml_lines, "implementation_types", implementation_types)
    yaml_write_list(yaml_lines, "tags", ["car", "analytic", "detection"])

    text = render_yaml(yaml_lines)
    text += build_page_start()
    if analytic.get("description"):
        description = replace_car_relative_links(str(analytic["description"]).strip(), car_lookup)
        text += description + "\n\n"
    text += write_coverage_section(analytic, attack_lookup)
    text += write_implementations_section(analytic, car_lookup)
    text += write_simple_list_section("Data Model References", analytic.get("data_model_references"))
    text += write_unit_tests_section(analytic, car_lookup)
    text += write_d3fend_section(analytic)
    text += "## Source\n\n"
    text += f"- [CAR website]({CAR_ANALYTIC_URL_TEMPLATE.format(car_id=car_id)})\n"
    text += f"- [Source YAML]({CAR_REPO_ANALYTIC_URL_TEMPLATE.format(car_id=car_id)})\n"
    return text


def build_car_indexes(analytics):
    analytic_rows = [make_car_link(analytic) for analytic in analytics]
    by_technique = defaultdict(list)
    for analytic in analytics:
        for attack_id in extract_coverage_techniques(analytic):
            by_technique[attack_id].append(analytic)

    text = build_page_start()
    text += "# CAR\n\n"
    text += "<!-- generated-source-description-start -->\n"
    text += "MITRE Cyber Analytics Repository is a library of analytics that describe how to detect adversary behavior using data models, logic, and implementations. This vault imports CAR analytics from the upstream YAML source and maps them to ATT&CK techniques where CAR provides coverage metadata.\n\n"
    text += "Use CAR pages as analytic design references, then pivot from ATT&CK technique pages into related Sigma rules, Atomic Red Team tests, LOLBAS entries, and other validation or detection content.\n\n"
    text += "## Upstream\n\n"
    text += "- [MITRE CAR](https://car.mitre.org/)\n"
    text += "- [CAR repository](https://github.com/mitre-attack/car)\n"
    text += "<!-- generated-source-description-end -->\n\n"
    text += "## Areas\n\n"
    text += f"- [[kb/car/analytics/index|Analytics]] ({len(analytics)})\n"
    text += f"- [[kb/car/techniques/index|Analytics by ATT&CK Technique]] ({len(by_technique)})\n"
    write_text_file(os.path.join(CAR_DIR, "index.md"), text)

    text = build_page_start()
    text += "# CAR Analytics\n\n"
    for row in analytic_rows:
        text += "- " + row + "\n"
    write_text_file(os.path.join(CAR_ANALYTICS_DIR, "index.md"), text)

    attack_lookup = build_attack_technique_lookup()
    text = build_page_start()
    text += "# CAR Analytics by ATT&CK Technique\n\n"
    for attack_id in sorted(by_technique.keys()):
        text += f"## {make_attack_link(attack_id, attack_lookup)}\n\n"
        for analytic in sorted(by_technique[attack_id], key=lambda item: item.get("id", "")):
            text += "- " + make_car_link(analytic) + "\n"
        text += "\n"
    write_text_file(os.path.join(CAR_BY_TECHNIQUE_DIR, "index.md"), text)


def update_vault_navigation():
    changed = 0
    for folder, _, filenames in os.walk(VAULT_DIR):
        for filename in filenames:
            if not filename.endswith(".md"):
                continue
            filepath = os.path.join(folder, filename)
            text = read_text_file(filepath)
            new_text = text.replace(OLD_NAV, NEW_NAV)
            if new_text != text:
                write_text_file(filepath, new_text)
                changed += 1
    log("Updated CAR navigation in " + str(changed) + " markdown files", "INFO")


def update_root_indexes(car_count):
    replacements = [
        ("- [[kb/defend/index|D3FEND]] (271 techniques)\n", "- [[kb/defend/index|D3FEND]] (271 techniques)\n- [[kb/car/index|CAR]] (" + str(car_count) + " analytics)\n"),
        ("- [[kb/defend/index|D3FEND]]\n", "- [[kb/defend/index|D3FEND]]\n- [[kb/car/index|CAR]]\n"),
    ]
    for relative_path in ["index.md", os.path.join("kb", "index.md")]:
        filepath = os.path.join(VAULT_DIR, relative_path)
        if not os.path.exists(filepath):
            continue
        text = read_text_file(filepath)
        text = text.replace(OLD_NAV, NEW_NAV)
        body_without_nav = text.replace(NEW_NAV, "")
        if "- [[kb/car/index|CAR]]" not in body_without_nav:
            for old, new in replacements:
                if old in text:
                    text = text.replace(old, new, 1)
                    break
        write_text_file(filepath, text)


def build_car():
    log("Starting CAR build", "INFO")
    download_car_source_if_needed()
    analytics = load_car_analytics()
    attack_lookup = build_attack_technique_lookup()
    car_lookup = build_car_id_lookup(analytics)

    remove_folder_if_exists(CAR_DIR)
    ensure_folder(CAR_ANALYTICS_DIR)
    ensure_folder(CAR_BY_TECHNIQUE_DIR)

    for analytic in analytics:
        filename = make_car_filename(analytic) + ".md"
        filepath = os.path.join(CAR_ANALYTICS_DIR, filename)
        write_text_file(filepath, build_car_note(analytic, attack_lookup, car_lookup))

    build_car_indexes(analytics)
    update_vault_navigation()
    update_root_indexes(len(analytics))
    log("Finished CAR build with " + str(len(analytics)) + " analytics", "INFO")
