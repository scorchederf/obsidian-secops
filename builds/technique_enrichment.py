"""Add compact generated detection and validation sections to ATT&CK techniques."""

import os
import re
from collections import defaultdict

import yaml

from utils.files import read_text_file, write_text_file
from utils.logging_utils import log


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VAULT_DIR = os.path.join(PROJECT_ROOT, "secopskb")
ATTACK_TECHNIQUES_DIR = os.path.join(VAULT_DIR, "kb", "attack", "techniques")
CAR_ANALYTICS_DIR = os.path.join(VAULT_DIR, "kb", "car", "analytics")
SIGMA_RULES_DIR = os.path.join(VAULT_DIR, "kb", "sigma", "rules")
ATOMIC_TESTS_DIR = os.path.join(VAULT_DIR, "kb", "atomic", "tests")
LOLBAS_ENTRIES_DIR = os.path.join(VAULT_DIR, "kb", "lolbas", "entries")

SECTION_START = "<!-- generated-detection-validation-start -->"
SECTION_END = "<!-- generated-detection-validation-end -->"
MAX_SIGMA_RULES = 10
MAX_ATOMIC_TESTS = 10
MAX_LOLBAS_ENTRIES = 10


def normalize_attack_id(attack_id):
    if not attack_id:
        return ""
    return str(attack_id).split(".", 1)[0]


def read_frontmatter(filepath):
    text = read_text_file(filepath)
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    data = yaml.safe_load(text[4:end]) or {}
    return data if isinstance(data, dict) else {}


def make_note_link(filepath, label):
    relative = os.path.relpath(filepath, VAULT_DIR).replace("\\", "/")
    target = os.path.splitext(relative)[0]
    return f"[[{target}|{label}]]"


def list_markdown_files(folder):
    if not os.path.isdir(folder):
        return []
    files = []
    for filename in os.listdir(folder):
        if filename.endswith(".md") and filename != "index.md":
            files.append(os.path.join(folder, filename))
    files.sort()
    return files


def build_technique_file_lookup():
    lookup = {}
    for filepath in list_markdown_files(ATTACK_TECHNIQUES_DIR):
        filename = os.path.basename(filepath)
        attack_id = filename.split("-", 1)[0]
        if re.match(r"^T\d{4}$", attack_id):
            lookup[attack_id] = filepath
    return lookup


def collect_car_links():
    mapping = defaultdict(list)
    for filepath in list_markdown_files(CAR_ANALYTICS_DIR):
        data = read_frontmatter(filepath)
        car_id = data.get("car_id", "")
        title = data.get("title", "")
        label = f"{car_id}: {title}" if car_id else title
        for attack_id in data.get("attack_technique_ids", []) or []:
            parent_id = normalize_attack_id(attack_id)
            if parent_id:
                mapping[parent_id].append(make_note_link(filepath, label))
    return mapping


def collect_sigma_links():
    mapping = defaultdict(list)
    for filepath in list_markdown_files(SIGMA_RULES_DIR):
        data = read_frontmatter(filepath)
        title = data.get("title", "")
        level = data.get("level", "")
        logsource = data.get("logsource", "")
        suffix = []
        if level:
            suffix.append(str(level))
        if logsource:
            suffix.append(str(logsource))
        label = title + (" (" + "; ".join(suffix) + ")" if suffix else "")
        for attack_id in data.get("attack_technique_ids", []) or []:
            parent_id = normalize_attack_id(attack_id)
            if parent_id:
                mapping[parent_id].append(make_note_link(filepath, label))
    return mapping


def collect_atomic_links():
    mapping = defaultdict(list)
    for filepath in list_markdown_files(ATOMIC_TESTS_DIR):
        data = read_frontmatter(filepath)
        attack_id = normalize_attack_id(data.get("attack_technique_id", ""))
        if not attack_id:
            continue
        title = data.get("title", "")
        executor = data.get("executor", "")
        platforms = ", ".join(data.get("platforms", []) or [])
        suffix = []
        if executor:
            suffix.append(str(executor))
        if platforms:
            suffix.append(platforms)
        label = title + (" (" + "; ".join(suffix) + ")" if suffix else "")
        mapping[attack_id].append(make_note_link(filepath, label))
    return mapping


def collect_lolbas_links():
    mapping = defaultdict(list)
    for filepath in list_markdown_files(LOLBAS_ENTRIES_DIR):
        data = read_frontmatter(filepath)
        title = data.get("title", "")
        functions = ", ".join(data.get("functions", []) or [])
        suffix = []
        if functions:
            suffix.append(functions)
        label = title + (" (" + "; ".join(suffix) + ")" if suffix else "")
        for attack_id in data.get("attack_technique_ids", []) or []:
            parent_id = normalize_attack_id(attack_id)
            if parent_id:
                mapping[parent_id].append(make_note_link(filepath, label))
    return mapping


def write_limited_links(title, links, limit):
    if not links:
        return ""
    unique_links = []
    for link in links:
        if link not in unique_links:
            unique_links.append(link)

    text = f"### {title}\n\n"
    for link in unique_links[:limit]:
        text += "- " + link + "\n"
    if len(unique_links) > limit:
        text += f"- {len(unique_links) - limit} more in the generated source index\n"
    return text + "\n"


def build_enrichment_section(attack_id, car_links, sigma_links, atomic_links, lolbas_links):
    if not car_links and not sigma_links and not atomic_links and not lolbas_links:
        return ""
    text = SECTION_START + "\n"
    text += "## Detection & Validation\n\n"
    text += write_limited_links("CAR Analytics", car_links, 20)
    text += write_limited_links("Sigma Rules", sigma_links, MAX_SIGMA_RULES)
    text += write_limited_links("Atomic Tests", atomic_links, MAX_ATOMIC_TESTS)
    text += write_limited_links("LOLBAS Entries", lolbas_links, MAX_LOLBAS_ENTRIES)
    text += SECTION_END + "\n\n"
    return text


def remove_existing_enrichment(text):
    pattern = re.compile(
        r"\n?" + re.escape(SECTION_START) + r".*?" + re.escape(SECTION_END) + r"\n*",
        flags=re.DOTALL,
    )
    return re.sub(pattern, "\n", text)


def insert_enrichment(text, section):
    text = remove_existing_enrichment(text)
    if not section:
        return text
    marker = "\n## Tactics\n"
    if marker in text:
        return text.replace(marker, "\n" + section + marker.lstrip(), 1)
    return text.rstrip() + "\n\n" + section


def build_technique_enrichment():
    log("Starting ATT&CK technique enrichment", "INFO")
    technique_files = build_technique_file_lookup()
    car_by_technique = collect_car_links()
    sigma_by_technique = collect_sigma_links()
    atomic_by_technique = collect_atomic_links()
    lolbas_by_technique = collect_lolbas_links()

    changed = 0
    for attack_id, filepath in technique_files.items():
        section = build_enrichment_section(
            attack_id,
            car_by_technique.get(attack_id, []),
            sigma_by_technique.get(attack_id, []),
            atomic_by_technique.get(attack_id, []),
            lolbas_by_technique.get(attack_id, []),
        )
        old_text = read_text_file(filepath)
        new_text = insert_enrichment(old_text, section)
        if new_text != old_text:
            write_text_file(filepath, new_text)
            changed += 1

    log("Finished ATT&CK technique enrichment; updated " + str(changed) + " files", "INFO")
