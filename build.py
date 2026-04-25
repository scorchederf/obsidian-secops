import csv
import json
import os
import re
from datetime import datetime

import requests
from urllib.parse import quote

# ============================================================
# SIMPLE MITRE ATT&CK VAULT BUILDER
# ============================================================
# This script builds an Obsidian vault for MITRE ATT&CK.
#
# Design goals:
# - Enterprise ATT&CK only
# - Keep the code simple and readable
# - Avoid advanced Python patterns so a junior developer can maintain it
# - Build local Obsidian links instead of relying on web links for content
#   that exists in the vault
# - Keep the structure ready for future additions such as:
#   - Data Sources
#   - Data Components
#   - MITRE D3FEND
#
# This version reads the ATT&CK STIX JSON directly.
# That makes the data flow much easier to understand than hiding logic inside
# a third-party library.
# ============================================================

# Debug builds are the normal build mode while this project is being developed.
DEBUG_BUILD = True
LOG_LEVEL = "DEBUG" if DEBUG_BUILD else "INFO"  # DEBUG, INFO, ERROR

# Keep full rebuilds enabled so generated pages do not leave stale files behind.
FULL_REBUILD = True
DOWNLOAD_JSON_IF_MISSING = True

# The output root. Open this folder as your Obsidian vault.
VAULT = "secopskb"

# The vault has a simple top-level structure:
# - kb: generated reference content
# - notes: analyst-owned notes created by clicking links in Obsidian
KB_DIR = os.path.join(VAULT, "kb")
NOTES_DIR = os.path.join(VAULT, "notes")

ATTACK_DIR = os.path.join(KB_DIR, "attack")
D3FEND_DIR = os.path.join(KB_DIR, "defend")
TOOLS_DIR = os.path.join(KB_DIR, "tools")

TACTICS_DIR = os.path.join(ATTACK_DIR, "tactics")
TECHNIQUES_DIR = os.path.join(ATTACK_DIR, "techniques")
MITIGATIONS_DIR = os.path.join(ATTACK_DIR, "mitigations")
DATA_SOURCES_DIR = os.path.join(ATTACK_DIR, "data-sources")
DATA_COMPONENTS_DIR = os.path.join(ATTACK_DIR, "data-components")
D3FEND_TECHNIQUES_DIR = os.path.join(D3FEND_DIR, "techniques")

NOTES_ATTACK_DIR = os.path.join(NOTES_DIR, "attack")
NOTES_ATTACK_TACTICS_DIR = os.path.join(NOTES_ATTACK_DIR, "tactics")
NOTES_ATTACK_TECHNIQUES_DIR = os.path.join(NOTES_ATTACK_DIR, "techniques")
NOTES_ATTACK_MITIGATIONS_DIR = os.path.join(NOTES_ATTACK_DIR, "mitigations")
NOTES_ATTACK_DATA_SOURCES_DIR = os.path.join(NOTES_ATTACK_DIR, "data-sources")
NOTES_ATTACK_DATA_COMPONENTS_DIR = os.path.join(NOTES_ATTACK_DIR, "data-components")
NOTES_TOOLS_DIR = os.path.join(NOTES_DIR, "tools")
NOTES_D3FEND_DIR = os.path.join(NOTES_DIR, "defend")
NOTES_D3FEND_TECHNIQUES_DIR = os.path.join(NOTES_D3FEND_DIR, "techniques")

ATTACK_JSON_FILE = "enterprise-attack.json"
WORKING_DIR = "workingdir"
D3FEND_JSON_FILE = os.path.join(WORKING_DIR, "d3fend.json")
D3FEND_OFFENSIVE_ALL_FILE = os.path.join(WORKING_DIR, "d3fend-offensive-techniques-all.json")
D3FEND_OFFENSIVE_DETAILS_DIR = os.path.join(WORKING_DIR, "d3fend-offensive-techniques")
ATTACK_JSON_URL = (
    "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/"
    "enterprise-attack/enterprise-attack.json"
)
D3FEND_JSON_URL = "https://d3fend.mitre.org/ontologies/d3fend.json"
D3FEND_OFFENSIVE_ALL_URL = "https://d3fend.mitre.org/api/offensive-technique/all.json"
D3FEND_OFFENSIVE_DETAIL_URL_TEMPLATE = "https://d3fend.mitre.org/api/offensive-technique/attack/{attack_id}.json"

BUILD_DATE = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
BUILD_SOURCE = "script"
DOMAIN_NAME = "enterprise-attack"
MATRIX_NAME = "enterprise"


# ============================================================
# LOGGING
# ============================================================

def log(message, level="INFO"):
    """
    Simple logger with timestamp and log levels.
    """
    levels = ["DEBUG", "INFO", "ERROR"]

    if levels.index(level) >= levels.index(LOG_LEVEL):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{level}] {message}")


# ============================================================
# FILE HELPERS
# ============================================================

def ensure_folder(path):
    """
    Create a folder if it does not already exist.
    """
    os.makedirs(path, exist_ok=True)



def clear_markdown_files(folder_path):
    """
    Delete all markdown files in a folder.

    This is used during a full rebuild so the vault stays clean.
    """
    if not os.path.exists(folder_path):
        return

    for name in os.listdir(folder_path):
        path = os.path.join(folder_path, name)

        if os.path.isfile(path) and name.endswith(".md"):
            os.remove(path)



def write_text_file_if_changed(filepath, content):
    """
    Write a file only if the content changed.

    This makes repeated test runs faster when FULL_REBUILD is False.
    """
    current = ""

    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            current = f.read()

    if current == content:
        return False

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return True


# ============================================================
# NAME AND LINK HELPERS
# ============================================================

def make_safe_name(name):
    """
    Convert a display name into a safe file name.

    The logic is kept intentionally simple and predictable.
    """
    safe = str(name)
    safe = safe.replace(" ", "_")
    safe = safe.replace("/", "_")
    safe = safe.replace("\\", "_")
    safe = safe.replace(":", "")
    safe = safe.replace("?", "")
    safe = safe.replace('"', "")
    safe = safe.replace("*", "")
    safe = safe.replace("|", "")
    safe = safe.replace("<", "")
    safe = safe.replace(">", "")
    safe = safe.strip("._")
    return safe.lower()



def make_subtechnique_block_id(attack_id, name):
    """
    Build a stable Obsidian block id for a sub-technique section.
    """
    block_id = f"{attack_id}-{name}"
    block_id = block_id.lower()
    block_id = block_id.replace(".", "")
    block_id = block_id.replace(":", "")
    block_id = block_id.replace("/", "-")
    block_id = block_id.replace("\\", "-")
    block_id = block_id.replace(" ", "-")
    block_id = block_id.replace("_", "-")
    return block_id



def make_tactic_filename(attack_id, name):
    return f"{attack_id}-{make_safe_name(name)}"



def make_technique_filename(attack_id, name):
    return f"{attack_id}-{make_safe_name(name)}"



def make_mitigation_filename(attack_id, name):
    return f"{attack_id}-{make_safe_name(name)}"



def make_tool_filename(name):
    return make_safe_name(name)



def make_data_source_filename(attack_id, name):
    return f"{attack_id}-{make_safe_name(name)}"



def make_data_component_filename(attack_id, name):
    return f"{attack_id}-{make_safe_name(name)}"



def make_d3fend_filename(d3fend_id, name):
    return f"{d3fend_id}-{make_safe_name(name)}"



def make_tactic_link(attack_id, name):
    filename = make_tactic_filename(attack_id, name)
    return f"[[{filename}|{attack_id}: {name}]]"



def make_technique_link(attack_id, name):
    filename = make_technique_filename(attack_id, name)
    return f"[[{filename}|{attack_id}: {name}]]"



def make_mitigation_link(attack_id, name):
    filename = make_mitigation_filename(attack_id, name)
    return f"[[{filename}|{attack_id}: {name}]]"



def make_tool_link(name):
    filename = make_tool_filename(name)
    return f"[[{filename}|{name}]]"



def make_data_source_link(attack_id, name):
    filename = make_data_source_filename(attack_id, name)
    return f"[[{filename}|{attack_id}: {name}]]"



def make_data_component_link(attack_id, name):
    filename = make_data_component_filename(attack_id, name)
    return f"[[{filename}|{attack_id}: {name}]]"



def make_d3fend_link(d3fend_id, name):
    filename = make_d3fend_filename(d3fend_id, name)
    return f"[[{filename}|{d3fend_id}: {name}]]"



def make_subtechnique_block_link(parent_attack_id, parent_name, sub_attack_id, sub_name):
    """
    Build a link to a sub-technique block inside the parent technique note.
    """
    parent_file = make_technique_filename(parent_attack_id, parent_name)
    block_id = make_subtechnique_block_id(sub_attack_id, sub_name)
    return f"[[{parent_file}#^{block_id}|{sub_attack_id}: {sub_name}]]"


# ============================================================
# YAML HELPERS
# ============================================================

def yaml_quote(value):
    """
    Write a simple YAML-safe quoted string.
    """
    text = str(value)
    text = text.replace("\\", "\\\\")
    text = text.replace('"', '\\"')
    return f'"{text}"'



def yaml_write_line(lines, key, value):
    """
    Add one YAML line if the value is not empty.
    """
    if value is None:
        return

    if value == "":
        return

    lines.append(f"{key}: {yaml_quote(value)}")



def yaml_write_list(lines, key, items):
    """
    Add a YAML list if it has values.
    """
    if not items:
        return

    lines.append(f"{key}:")

    for item in items:
        lines.append(f"  - {yaml_quote(item)}")



def unique_strings(items):
    """
    Return a de-duplicated list while preserving order.
    """
    result = []

    for item in items:
        if not item:
            continue

        if item in result:
            continue

        result.append(item)

    return result



def build_common_yaml_lines(obj, attack_id, url_value):
    """
    Build YAML lines shared by all note types.

    Imported ATT&CK values are prefixed with mitre_.
    Local build metadata is kept separate.
    """
    lines = []

    yaml_write_line(lines, "mitre_id", attack_id)
    yaml_write_line(lines, "mitre_name", obj.get("name", ""))
    yaml_write_line(lines, "mitre_type", obj.get("type", ""))
    yaml_write_line(lines, "mitre_stix_id", obj.get("id", ""))
    yaml_write_line(lines, "mitre_created", obj.get("created", ""))
    yaml_write_line(lines, "mitre_modified", obj.get("modified", ""))
    yaml_write_line(lines, "mitre_version", obj.get("x_mitre_version", ""))

    domains = obj.get("x_mitre_domains", [])
    yaml_write_list(lines, "mitre_domains", domains)

    yaml_write_line(lines, "mitre_url", url_value)
    yaml_write_line(lines, "framework", "attack")
    yaml_write_line(lines, "generated", "true")
    yaml_write_line(lines, "build_date", BUILD_DATE)
    yaml_write_line(lines, "build_source", BUILD_SOURCE)

    return lines



def render_yaml_block(lines):
    """
    Render a YAML frontmatter block.
    """
    text = "---\n"

    for line in lines:
        text += line + "\n"

    text += "---\n\n"
    return text


# ============================================================
# DATASET HELPERS
# ============================================================

def download_attack_json_if_needed():
    """
    Download the Enterprise ATT&CK JSON file if it does not exist.
    """
    if os.path.exists(ATTACK_JSON_FILE):
        return

    if not DOWNLOAD_JSON_IF_MISSING:
        raise FileNotFoundError(f"Missing local ATT&CK file: {ATTACK_JSON_FILE}")

    log("Downloading Enterprise ATT&CK JSON...", "INFO")
    response = requests.get(ATTACK_JSON_URL, timeout=120)
    response.raise_for_status()

    with open(ATTACK_JSON_FILE, "w", encoding="utf-8") as f:
        f.write(response.text)



def load_attack_bundle():
    """
    Load the ATT&CK STIX bundle from disk.
    """
    with open(ATTACK_JSON_FILE, "r", encoding="utf-8") as f:
        return json.load(f)



def ensure_parent_folder_for_file(filepath):
    """
    Create the parent folder for a file path when one is needed.

    Some cache files live in workingdir. Source files may live beside the
    script. This helper supports both cases.
    """
    folder_path = os.path.dirname(filepath)

    if not folder_path:
        return

    ensure_folder(folder_path)


def download_json_file_if_missing(filepath, url, display_name):
    """
    Download a JSON file only when the local cached copy is missing.

    There is no age or checksum validation yet. If the file exists, the build
    trusts it and uses the cached copy. Delete the file manually when you want
    to force a fresh download.
    """
    if os.path.exists(filepath):
        log(f"Using cached {display_name}: {filepath}", "DEBUG")
        return

    ensure_parent_folder_for_file(filepath)

    log(f"Downloading {display_name}...", "INFO")
    response = requests.get(url, timeout=120)
    response.raise_for_status()

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(response.text)


def download_d3fend_json_if_needed():
    """
    Download the D3FEND ontology JSON file if it is not already cached.
    """
    download_json_file_if_missing(D3FEND_JSON_FILE, D3FEND_JSON_URL, "MITRE D3FEND JSON")



def load_d3fend_bundle():
    """
    Load the D3FEND JSON-LD bundle from disk.
    """
    with open(D3FEND_JSON_FILE, "r", encoding="utf-8") as f:
        return json.load(f)



def download_d3fend_offensive_all_if_needed():
    """
    Download the MITRE D3FEND offensive-technique index JSON if it is not cached.
    """
    download_json_file_if_missing(
        D3FEND_OFFENSIVE_ALL_FILE,
        D3FEND_OFFENSIVE_ALL_URL,
        "MITRE D3FEND offensive-technique index JSON",
    )



def load_d3fend_offensive_all():
    """
    Load the MITRE D3FEND offensive-technique index JSON from disk.
    """
    with open(D3FEND_OFFENSIVE_ALL_FILE, "r", encoding="utf-8") as f:
        return json.load(f)



def ensure_d3fend_offensive_details_folder():
    """
    Create the local cache folder for per-technique D3FEND API responses.
    """
    ensure_folder(D3FEND_OFFENSIVE_DETAILS_DIR)



def build_d3fend_offensive_detail_filepath(attack_id):
    """
    Return the local cache path for one offensive-technique API response.
    """
    filename = attack_id + ".json"
    return os.path.join(D3FEND_OFFENSIVE_DETAILS_DIR, filename)



def download_d3fend_offensive_detail_if_needed(attack_id):
    """
    Download one MITRE D3FEND offensive-technique detail JSON if it does not exist.
    """
    ensure_d3fend_offensive_details_folder()
    filepath = build_d3fend_offensive_detail_filepath(attack_id)

    if os.path.exists(filepath):
        log(f"Using cached D3FEND offensive-technique detail for {attack_id}", "DEBUG")
        return

    url = D3FEND_OFFENSIVE_DETAIL_URL_TEMPLATE.format(attack_id=quote(attack_id, safe=""))

    try:
        response = requests.get(url, timeout=120)
        response.raise_for_status()
    except requests.HTTPError as exc:
        status_code = None

        if exc.response is not None:
            status_code = exc.response.status_code

        if status_code == 404:
            log(f"No D3FEND offensive-technique detail found for {attack_id}", "DEBUG")
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump({}, f)
            return

        raise

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(response.text)



def load_d3fend_offensive_detail(attack_id):
    """
    Load one MITRE D3FEND offensive-technique detail JSON from disk.
    """
    filepath = build_d3fend_offensive_detail_filepath(attack_id)

    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)



def get_attack_id(obj):
    """
    Read the ATT&CK external id from external_references.

    This works for tactics, techniques, mitigations, tools, data sources,
    and data components when the id is present in the dataset.
    """
    refs = obj.get("external_references", [])

    for ref in refs:
        source_name = ref.get("source_name", "")
        external_id = ref.get("external_id", "")

        if not external_id:
            continue

        if source_name.startswith("mitre-"):
            return external_id

    return ""



def is_revoked_or_deprecated(obj):
    """
    Skip revoked and deprecated objects.
    """
    if obj.get("revoked") is True:
        return True

    if obj.get("x_mitre_deprecated") is True:
        return True

    return False



def is_enterprise_object(obj):
    """
    Return True when the object belongs to Enterprise ATT&CK.
    """
    domains = obj.get("x_mitre_domains", [])

    if DOMAIN_NAME in domains:
        return True

    return False



def parse_attack_objects(bundle):
    """
    Split the STIX bundle into simple object groups.

    Data Sources and Data Components are kept even when they do not carry
    x_mitre_domains in the same way as other ATT&CK objects.
    This matters because Enterprise ATT&CK bundles can still contain valid
    Enterprise data source content without that field being populated.
    """
    objects = bundle.get("objects", [])

    tactics = []
    techniques = []
    mitigations = []
    tools = []
    data_sources = []
    data_components = []
    relationships = []

    for obj in objects:
        obj_type = obj.get("type", "")

        if obj_type == "relationship":
            relationships.append(obj)
            continue

        # MITRE currently ships Data Sources in the Enterprise bundle, but the
        # objects themselves are marked deprecated in the source data.
        # We still want them in the vault because they are useful for local
        # linking and for documenting ATT&CK detection coverage.
        #
        # We only skip truly revoked Data Sources.
        if obj_type == "x-mitre-data-source":
            if obj.get("revoked") is True:
                continue

            data_sources.append(obj)
            continue

        if is_revoked_or_deprecated(obj):
            continue

        if obj_type == "x-mitre-tactic":
            if is_enterprise_object(obj):
                tactics.append(obj)
            continue

        if obj_type == "attack-pattern":
            if is_enterprise_object(obj):
                techniques.append(obj)
            continue

        if obj_type == "course-of-action":
            if is_enterprise_object(obj):
                mitigations.append(obj)
            continue

        if obj_type == "tool":
            if is_enterprise_object(obj):
                tools.append(obj)
            continue

        if obj_type == "x-mitre-data-component":
            data_components.append(obj)
            continue

    return {
        "tactics": tactics,
        "techniques": techniques,
        "mitigations": mitigations,
        "tools": tools,
        "data_sources": data_sources,
        "data_components": data_components,
        "relationships": relationships,
    }


# ============================================================
# LOOKUP BUILDERS
# ============================================================

def build_object_lookup(objects):
    """
    Build STIX id -> object.
    """
    lookup = {}

    for obj in objects:
        lookup[obj["id"]] = obj

    return lookup



def build_attack_id_lookup(object_groups):
    """
    Build ATT&CK id -> object.

    This is used for fast local link replacement in descriptions.
    """
    lookup = {}

    group_names = [
        "tactics",
        "techniques",
        "mitigations",
        "tools",
        "data_sources",
        "data_components",
    ]

    for group_name in group_names:
        for obj in object_groups[group_name]:
            attack_id = get_attack_id(obj)

            if attack_id:
                lookup[attack_id] = obj

    return lookup


def build_name_lookup(objects):
    """
    Build lowercase name -> object.

    This is used as a simple fallback when MITRE provides data source names
    directly on a technique but there is no relationship object we can use.
    """
    lookup = {}

    for obj in objects:
        name = obj.get("name", "")

        if not name:
            continue

        lookup[name.strip().lower()] = obj

    return lookup


def build_subtechnique_attack_id_to_parent_map(sub_to_parent):
    """
    Build sub-technique ATT&CK id -> parent technique object.

    This is used when we replace inline MITRE web links in descriptions.
    """
    mapping = {}

    for sub_id in sub_to_parent:
        parent = sub_to_parent[sub_id]
        mapping[sub_id] = parent

    return mapping



def build_tactic_shortname_lookup(tactics):
    """
    Build tactic shortname -> tactic object.
    """
    lookup = {}

    for tactic in tactics:
        short_name = tactic.get("x_mitre_shortname", "")

        if short_name:
            lookup[short_name] = tactic

    return lookup



def build_relationships_by_type(relationships):
    """
    Group relationship objects by relationship_type.
    """
    grouped = {}

    for rel in relationships:
        rel_type = rel.get("relationship_type", "")

        if rel_type not in grouped:
            grouped[rel_type] = []

        grouped[rel_type].append(rel)

    return grouped



def build_subtechnique_maps(techniques, relationships_by_type, technique_lookup):
    """
    Build both:
    - parent technique id -> list of sub-technique objects
    - sub-technique id -> parent technique object
    """
    parent_to_subs = {}
    sub_to_parent = {}

    for technique in techniques:
        parent_to_subs[technique["id"]] = []

    for rel in relationships_by_type.get("subtechnique-of", []):
        source_ref = rel.get("source_ref", "")
        target_ref = rel.get("target_ref", "")

        if source_ref not in technique_lookup:
            continue

        if target_ref not in technique_lookup:
            continue

        sub = technique_lookup[source_ref]
        parent = technique_lookup[target_ref]

        parent_to_subs[target_ref].append(sub)
        sub_to_parent[source_ref] = parent

    for parent_id in parent_to_subs:
        parent_to_subs[parent_id].sort(key=lambda item: get_attack_id(item))

    return parent_to_subs, sub_to_parent



def build_tactic_to_technique_map(tactics, techniques):
    """
    Build tactic STIX id -> parent technique objects.

    We only place parent techniques on tactic pages.
    Sub-techniques are shown under their parent technique.
    """
    mapping = {}

    for tactic in tactics:
        mapping[tactic["id"]] = []

    for technique in techniques:
        if technique.get("x_mitre_is_subtechnique") is True:
            continue

        kill_chain_phases = technique.get("kill_chain_phases", [])

        for phase in kill_chain_phases:
            phase_name = phase.get("phase_name", "")

            for tactic in tactics:
                short_name = tactic.get("x_mitre_shortname", "")

                if phase_name == short_name:
                    mapping[tactic["id"]].append(technique)

    for tactic_id in mapping:
        mapping[tactic_id].sort(key=lambda item: get_attack_id(item))

    return mapping



def build_technique_to_mitigation_map(relationships_by_type, technique_lookup, mitigation_lookup):
    """
    Build technique STIX id -> mitigation objects.
    """
    mapping = {}

    for technique_id in technique_lookup:
        mapping[technique_id] = []

    for rel in relationships_by_type.get("mitigates", []):
        mitigation_id = rel.get("source_ref", "")
        technique_id = rel.get("target_ref", "")

        if mitigation_id not in mitigation_lookup:
            continue

        if technique_id not in technique_lookup:
            continue

        mapping[technique_id].append(mitigation_lookup[mitigation_id])

    for technique_id in mapping:
        rows = []
        seen = set()

        for mitigation in mapping[technique_id]:
            attack_id = get_attack_id(mitigation)
            key = (attack_id, mitigation.get("name", ""))

            if key in seen:
                continue

            seen.add(key)
            rows.append(mitigation)

        rows.sort(key=lambda item: get_attack_id(item))
        mapping[technique_id] = rows

    return mapping



def build_technique_to_tool_map(relationships_by_type, technique_lookup, tool_lookup):
    """
    Build technique STIX id -> tool objects.
    """
    mapping = {}

    for technique_id in technique_lookup:
        mapping[technique_id] = []

    for rel in relationships_by_type.get("uses", []):
        software_id = rel.get("source_ref", "")
        technique_id = rel.get("target_ref", "")

        if software_id not in tool_lookup:
            continue

        if technique_id not in technique_lookup:
            continue

        mapping[technique_id].append(tool_lookup[software_id])

    for technique_id in mapping:
        rows = []
        seen = set()

        for tool in mapping[technique_id]:
            attack_id = get_attack_id(tool)
            key = (attack_id, tool.get("name", ""))

            if key in seen:
                continue

            seen.add(key)
            rows.append(tool)

        rows.sort(key=lambda item: get_attack_id(item))
        mapping[technique_id] = rows

    return mapping



def build_data_source_to_component_map(data_sources, data_components):
    """
    Build data source STIX id -> data component objects.

    Data components point to their parent data source by reference.
    """
    mapping = {}

    for data_source in data_sources:
        mapping[data_source["id"]] = []

    for component in data_components:
        source_ref = component.get("x_mitre_data_source_ref", "")

        if source_ref in mapping:
            mapping[source_ref].append(component)

    for source_id in mapping:
        mapping[source_id].sort(key=lambda item: get_attack_id(item))

    return mapping



def build_data_component_to_source_map(data_components, data_source_lookup):
    """
    Build data component STIX id -> parent data source object.
    """
    mapping = {}

    for component in data_components:
        source_ref = component.get("x_mitre_data_source_ref", "")

        if source_ref in data_source_lookup:
            mapping[component["id"]] = data_source_lookup[source_ref]

    return mapping



def build_technique_to_data_component_map(relationships_by_type, technique_lookup, data_component_lookup):
    """
    Build technique STIX id -> data component objects.

    ATT&CK uses 'detects' relationships for Data Components.
    """
    mapping = {}

    for technique_id in technique_lookup:
        mapping[technique_id] = []

    for rel in relationships_by_type.get("detects", []):
        source_ref = rel.get("source_ref", "")
        target_ref = rel.get("target_ref", "")

        # Data Component -> Technique
        if source_ref in data_component_lookup and target_ref in technique_lookup:
            mapping[target_ref].append(data_component_lookup[source_ref])

        # Some datasets may reverse the direction
        if target_ref in data_component_lookup and source_ref in technique_lookup:
            mapping[source_ref].append(data_component_lookup[target_ref])

    for technique_id in mapping:
        rows = []
        seen = set()

        for component in mapping[technique_id]:
            attack_id = get_attack_id(component)
            key = (attack_id, component.get("name", ""))

            if key in seen:
                continue

            seen.add(key)
            rows.append(component)

        rows.sort(key=lambda item: get_attack_id(item))
        mapping[technique_id] = rows

    return mapping



def build_data_component_to_technique_map(technique_to_data_component_map):
    """
    Reverse the technique -> data component map.
    """
    mapping = {}

    for technique_id in technique_to_data_component_map:
        components = technique_to_data_component_map[technique_id]

        for component in components:
            component_id = component["id"]

            if component_id not in mapping:
                mapping[component_id] = []

            mapping[component_id].append(technique_id)

    return mapping



def build_data_source_to_technique_map(data_source_to_component_map, data_component_to_technique_map):
    """
    Build data source STIX id -> technique STIX ids.

    This is derived from:
    Data Source -> Data Components -> Techniques
    """
    mapping = {}

    for source_id in data_source_to_component_map:
        mapping[source_id] = []

        for component in data_source_to_component_map[source_id]:
            component_id = component["id"]
            technique_ids = data_component_to_technique_map.get(component_id, [])

            for technique_id in technique_ids:
                if technique_id not in mapping[source_id]:
                    mapping[source_id].append(technique_id)

        mapping[source_id].sort()

    return mapping


def split_mitre_data_source_value(value):
    """
    Split a MITRE data source string into source and component names.

    Example:
    "Process: Process Creation" -> ("Process", "Process Creation")
    "Cloud Service" -> ("Cloud Service", "")
    """
    if not value:
        return "", ""

    parts = value.split(":", 1)
    source_name = parts[0].strip()
    component_name = ""

    if len(parts) > 1:
        component_name = parts[1].strip()

    return source_name, component_name


# ============================================================
# D3FEND HELPERS
# ============================================================

def get_d3fend_graph_entries(bundle):
    """
    Return the JSON-LD graph entries from the D3FEND ontology file.
    """
    graph = bundle.get("@graph", [])

    if isinstance(graph, list):
        return graph

    return []



def extract_d3fend_id_from_ontology_id(raw_id):
    """
    Extract a usable D3FEND id from an ontology id when possible.
    """
    if not raw_id:
        return ""

    if "#" in raw_id:
        raw_id = raw_id.split("#", 1)[1]

    if ":" in raw_id:
        raw_id = raw_id.split(":", 1)[1]

    if raw_id.startswith("D3"):
        return raw_id

    return ""



def get_d3fend_id(entry):
    """
    Return the D3FEND id such as D3-ANCI.
    """
    value = entry.get("d3f:d3fend-id", "")

    if isinstance(value, str) and value:
        return value

    if isinstance(value, dict):
        inner_value = value.get("@value", "")
        if inner_value:
            return inner_value

    return extract_d3fend_id_from_ontology_id(entry.get("@id", ""))



def get_d3fend_label(entry):
    """
    Return the primary display label for a D3FEND object.
    """
    value = entry.get("rdfs:label", "")

    if isinstance(value, str):
        return value

    if isinstance(value, dict):
        return value.get("@value", "")

    return ""



def get_d3fend_text_value(entry, key_name):
    """
    Read a simple D3FEND text property from a JSON-LD object.
    """
    value = entry.get(key_name, "")

    if isinstance(value, str):
        return value

    if isinstance(value, dict):
        return value.get("@value", "")

    return ""



def get_d3fend_reference_ids(entry, key_name):
    """
    Read referenced ontology ids from a JSON-LD property.
    """
    value = entry.get(key_name)
    ids = []

    if value is None:
        return ids

    values = value
    if not isinstance(values, list):
        values = [values]

    for item in values:
        if isinstance(item, dict):
            ref_id = item.get("@id", "")
            if ref_id:
                ids.append(ref_id)

    return ids



def parse_d3fend_objects(bundle):
    """
    Parse the D3FEND ontology and keep just D3FEND techniques.

    For the first implementation we only keep concrete D3FEND techniques
    with ids that start with D3-. This avoids mixing in analytics, tactics,
    ATT&CK classes, CWE classes, and many other ontology objects.
    """
    techniques = []

    for entry in get_d3fend_graph_entries(bundle):
        d3fend_id = get_d3fend_id(entry)

        if not d3fend_id:
            continue

        if not d3fend_id.startswith("D3-"):
            continue

        label = get_d3fend_label(entry)
        if not label:
            continue

        techniques.append(entry)

    techniques.sort(key=lambda item: get_d3fend_id(item))

    return {
        "techniques": techniques,
    }



def build_d3fend_lookup(entries):
    """
    Build ontology id -> object for D3FEND entries.
    """
    lookup = {}

    for entry in entries:
        entry_id = entry.get("@id", "")
        if entry_id:
            lookup[entry_id] = entry

    return lookup



def build_d3fend_id_lookup(entries):
    """
    Build D3FEND id -> object for D3FEND entries.
    """
    lookup = {}

    for entry in entries:
        d3fend_id = get_d3fend_id(entry)
        if d3fend_id:
            lookup[d3fend_id] = entry

    return lookup



def build_d3fend_alias_lookup(entries):
    """
    Build simple aliases that can resolve D3FEND API references back to
    concrete D3FEND technique ids.
    """
    lookup = {}

    for entry in entries:
        d3fend_id = get_d3fend_id(entry)

        if not d3fend_id:
            continue

        lookup[d3fend_id] = d3fend_id

        ontology_id = entry.get("@id", "")
        if ontology_id:
            lookup[ontology_id] = d3fend_id

            if "#" in ontology_id:
                suffix = ontology_id.split("#", 1)[1]
                lookup[suffix] = d3fend_id
            else:
                lookup[ontology_id] = d3fend_id

        label = get_d3fend_label(entry)
        if label:
            lookup[label] = d3fend_id

    return lookup



def normalize_d3fend_reference(value):
    """
    Normalize one D3FEND reference string into a lookup key.
    """
    if not value:
        return ""

    text = str(value).strip()

    if not text:
        return ""

    if "/" in text and "d3f:" in text:
        text = text.rsplit("/", 1)[-1]

    if "#" in text:
        text = text.split("#", 1)[1]

    return text


def extract_attack_ids_from_text(text):
    """
    Extract ATT&CK technique ids from free text.

    This supports both:
    - T1059
    - T1059.001
    - T1059/001
    """
    values = []

    if not text:
        return values

    text_without_slash_subtechniques = text

    slash_matches = re.findall(r"\b(T\d{4})/(\d{3})\b", text)
    for primary_id, secondary_id in slash_matches:
        slash_text = f"{primary_id}/{secondary_id}"
        attack_id = f"{primary_id}.{secondary_id}"

        if attack_id not in values:
            values.append(attack_id)

        text_without_slash_subtechniques = text_without_slash_subtechniques.replace(slash_text, " ")

    dot_matches = re.findall(r"\bT\d{4}(?:\.\d{3})?\b", text_without_slash_subtechniques)
    for match in dot_matches:
        if match not in values:
            values.append(match)

    return values



def extract_d3fend_ids_from_text(text):
    """
    Extract raw D3FEND references from free text.

    Supported examples:
    - D3-ANCI
    - d3f:ApplicationConfigurationHardening
    - https://d3fend.mitre.org/technique/d3f:ApplicationConfigurationHardening
    """
    values = []

    if not text:
        return values

    upper_matches = re.findall(r"\bD3-[A-Z0-9]+\b", text)
    for match in upper_matches:
        if match not in values:
            values.append(match)

    prefixed_matches = re.findall(r"d3f:[A-Za-z0-9_\-]+", text)
    for match in prefixed_matches:
        if match not in values:
            values.append(match)

    return values



def extract_attack_ids_from_json_data(data, values=None):
    """
    Recursively extract ATT&CK ids from any JSON object.
    """
    if values is None:
        values = []

    if isinstance(data, dict):
        for key in data:
            key_text = str(key)
            for attack_id in extract_attack_ids_from_text(key_text):
                if attack_id not in values:
                    values.append(attack_id)

            extract_attack_ids_from_json_data(data[key], values)

        return values

    if isinstance(data, list):
        for item in data:
            extract_attack_ids_from_json_data(item, values)

        return values

    text = str(data)
    for attack_id in extract_attack_ids_from_text(text):
        if attack_id not in values:
            values.append(attack_id)

    return values



def extract_d3fend_ids_from_json_data(data, values=None):
    """
    Recursively extract raw D3FEND references from any JSON object.
    """
    if values is None:
        values = []

    if isinstance(data, dict):
        for key in data:
            key_text = str(key)
            for d3fend_id in extract_d3fend_ids_from_text(key_text):
                if d3fend_id not in values:
                    values.append(d3fend_id)

            extract_d3fend_ids_from_json_data(data[key], values)

        return values

    if isinstance(data, list):
        for item in data:
            extract_d3fend_ids_from_json_data(item, values)

        return values

    text = str(data)
    for d3fend_id in extract_d3fend_ids_from_text(text):
        if d3fend_id not in values:
            values.append(d3fend_id)

    return values



def resolve_d3fend_references_to_ids(values, d3fend_alias_lookup):
    """
    Resolve raw D3FEND API references to concrete D3FEND ids.
    """
    resolved = []

    for value in values:
        normalized_value = normalize_d3fend_reference(value)

        if not normalized_value:
            continue

        if normalized_value.startswith("D3-"):
            if normalized_value not in resolved:
                resolved.append(normalized_value)
            continue

        d3fend_id = d3fend_alias_lookup.get(normalized_value, "")
        if d3fend_id and d3fend_id not in resolved:
            resolved.append(d3fend_id)

    return resolved



def build_attack_to_d3fend_map(attack_ids, d3fend_alias_lookup):
    """
    Build ATT&CK technique id -> list of D3FEND ids using the MITRE D3FEND
    offensive-technique API.

    The index endpoint tells us which ATT&CK techniques are represented.
    Then we query one detail endpoint per ATT&CK technique and extract D3FEND
    references from that scoped response.
    """
    mapping = {}

    for attack_id in attack_ids:
        download_d3fend_offensive_detail_if_needed(attack_id)
        detail = load_d3fend_offensive_detail(attack_id)
        raw_values = extract_d3fend_ids_from_json_data(detail)
        d3fend_ids = resolve_d3fend_references_to_ids(raw_values, d3fend_alias_lookup)

        if d3fend_ids:
            d3fend_ids.sort()
            mapping[attack_id] = d3fend_ids

    return mapping



def build_d3fend_to_attack_map(attack_to_d3fend_map):
    """
    Build D3FEND id -> list of ATT&CK technique ids.
    """
    mapping = {}

    for attack_id in attack_to_d3fend_map:
        for d3fend_id in attack_to_d3fend_map[attack_id]:
            if d3fend_id not in mapping:
                mapping[d3fend_id] = []

            if attack_id not in mapping[d3fend_id]:
                mapping[d3fend_id].append(attack_id)

    for d3fend_id in mapping:
        mapping[d3fend_id].sort()

    return mapping



def build_d3fend_links_from_attack_id(attack_id, attack_to_d3fend_map, d3fend_id_lookup):
    """
    Build D3FEND links for one ATT&CK technique id.
    """
    links = []

    for d3fend_id in attack_to_d3fend_map.get(attack_id, []):
        entry = d3fend_id_lookup.get(d3fend_id)

        if entry is not None:
            links.append(make_d3fend_link(d3fend_id, get_d3fend_label(entry)))
        else:
            links.append(d3fend_id)

    return links



def build_attack_links_from_ids(attack_ids, attack_id_lookup, subtechnique_attack_id_to_parent):
    """
    Build ATT&CK links from ATT&CK ids.
    """
    links = []

    for attack_id in attack_ids:
        obj = attack_id_lookup.get(attack_id)

        if obj is None:
            links.append(attack_id)
            continue

        if obj.get("type", "") != "attack-pattern":
            links.append(attack_id)
            continue

        if "." in attack_id:
            parent = subtechnique_attack_id_to_parent.get(obj["id"])

            if parent is None:
                links.append(attack_id)
                continue

            links.append(
                make_subtechnique_block_link(
                    get_attack_id(parent),
                    parent.get("name", ""),
                    attack_id,
                    obj.get("name", ""),
                )
            )
        else:
            links.append(make_technique_link(attack_id, obj.get("name", "")))

    return links



def log_sample_mappings(attack_to_d3fend_map, d3fend_to_attack_map):
    """
    Log a small sample of the ATT&CK <-> D3FEND mappings.
    """
    log("Sample ATT&CK to D3FEND mappings:", "INFO")
    count = 0

    for attack_id in sorted(attack_to_d3fend_map.keys()):
        log(f"  {attack_id} -> {attack_to_d3fend_map[attack_id]}", "INFO")
        count += 1

        if count >= 5:
            break

    log("Sample D3FEND to ATT&CK mappings:", "INFO")
    count = 0

    for d3fend_id in sorted(d3fend_to_attack_map.keys()):
        log(f"  {d3fend_id} -> {d3fend_to_attack_map[d3fend_id]}", "INFO")
        count += 1

        if count >= 5:
            break



def build_d3fend_technique_parent_map(techniques, technique_lookup):
    """
    Build D3FEND parent -> children and child -> parent maps.

    Parent relationships are inferred from rdfs:subClassOf when the parent
    is also a D3FEND technique.
    """
    parent_to_children = {}
    child_to_parent = {}

    for technique in techniques:
        technique_id = technique.get("@id", "")
        parent_to_children[technique_id] = []

    for technique in techniques:
        technique_id = technique.get("@id", "")
        parents = get_d3fend_reference_ids(technique, "rdfs:subClassOf")

        for parent_id in parents:
            if parent_id not in technique_lookup:
                continue

            parent_to_children[parent_id].append(technique)
            child_to_parent[technique_id] = technique_lookup[parent_id]
            break

    for parent_id in parent_to_children:
        parent_to_children[parent_id].sort(key=lambda item: get_d3fend_id(item))

    return parent_to_children, child_to_parent



def build_d3fend_url(entry):
    """
    Build the public D3FEND technique URL from the ontology id.
    """
    ontology_id = entry.get("@id", "")

    if not ontology_id:
        return ""

    encoded = quote(ontology_id, safe="")
    return f"https://d3fend.mitre.org/technique/{encoded}/"



def add_common_attack_yaml_fields(yaml_lines, framework_name, object_type, tags):
    """
    Add common framework, object type, and tag fields for ATT&CK notes.
    """
    yaml_write_line(yaml_lines, "framework", framework_name)
    yaml_write_line(yaml_lines, "object_type", object_type)
    yaml_write_line(yaml_lines, "generated", "true")
    yaml_write_list(yaml_lines, "tags", unique_strings(tags))



def build_attack_tags(object_type, include_detection=False, include_telemetry=False):
    """
    Build a small controlled tag set for ATT&CK notes.
    """
    tags = ["attack", object_type]

    if object_type in ["tactic", "technique", "tool"]:
        tags.append("offense")

    if object_type in ["mitigation"]:
        tags.append("defense")
        tags.append("countermeasure")

    if object_type in ["data-source", "data-component"]:
        tags.append("detection")
        tags.append("telemetry")

    if include_detection and "detection" not in tags:
        tags.append("detection")

    if include_telemetry and "telemetry" not in tags:
        tags.append("telemetry")

    return unique_strings(tags)



def build_d3fend_tags():
    """
    Build the controlled tag set for D3FEND technique notes.
    """
    return ["d3fend", "defensive-technique", "defense", "countermeasure"]



def build_notes_tags(parent_framework, parent_object_type):
    """
    Build tags for analyst workspace notes.
    """
    return unique_strings(["notes", "workspace", parent_framework, parent_object_type])



def convert_path_to_wikilink_target(path_value):
    """
    Convert a filesystem path into an Obsidian wiki link target.

    The script writes files under VAULT. In Obsidian that folder is the vault
    root, so links should not include the VAULT folder name.
    """
    target = path_value.replace("\\", "/")
    vault_prefix = VAULT.replace("\\", "/") + "/"

    if target.startswith(vault_prefix):
        target = target[len(vault_prefix):]

    if target.endswith(".md"):
        target = target[:-3]

    return target



def make_workspace_note_filename(object_id, name):
    """
    Build the workspace note filename from the object id and display name.

    Example:
    TA0001 + Initial Access -> TA0001-initial_access-note.md
    """
    safe_name = make_safe_name(name)
    return f"{object_id}-{safe_name}-note"



def build_horizontal_navigation():
    """
    Build a compact navigation row for every generated page.
    """
    text = "[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]\n\n"
    text += "---\n\n"
    return text



def build_workspace_link_section(link_target, alias_text="Open workspace note"):
    """
    Build the analyst workspace area.

    The normal wiki link lets an analyst click through to the note.
    The embed shows the note inline once it exists.
    The script does not create the note file; Obsidian creates it when clicked.
    """
    text = "## Workspace\n\n"
    text += f"- [[{link_target}|{alias_text}]]\n\n"
    text += f"![[{link_target}]]\n\n"
    return text



def build_page_start():
    """
    Build the standard top navigation for generated pages.

    Page-specific descriptions are written immediately after this navigation.
    The workspace block is written after the description so analysts see the
    MITRE context before the embedded workspace note.
    """
    return build_horizontal_navigation()



def build_reference_embed_section(link_target):
    """
    Build the reference embed section for a workspace note.
    """
    text = "## Reference\n\n"
    text += f"![[{link_target}]]\n\n"
    return text



def build_workspace_note_content(title, parent_framework, parent_object_type, parent_id, reference_link_target):
    """
    Build the initial content for a workspace note.
    """
    yaml_lines = []
    yaml_write_line(yaml_lines, "framework", "notes")
    yaml_write_line(yaml_lines, "object_type", "workspace-note")
    yaml_write_line(yaml_lines, "generated", "false")
    yaml_write_line(yaml_lines, "parent_framework", parent_framework)
    yaml_write_line(yaml_lines, "parent_object_type", parent_object_type)
    yaml_write_line(yaml_lines, "parent_id", parent_id)
    yaml_write_line(yaml_lines, "index_exclude", "true")
    yaml_write_list(yaml_lines, "tags", build_notes_tags(parent_framework, parent_object_type))

    text = render_yaml_block(yaml_lines)
    text += write_h1(title)
    text += build_reference_embed_section(reference_link_target)
    text += "## Analyst Notes\n\n"
    text += "## Detection Notes\n\n"
    text += "## Hunting Notes\n\n"
    text += "## Environment Notes\n\n"
    text += "## Alert Tuning\n\n"
    text += "## Gaps\n\n"
    return text



def ensure_workspace_note_if_missing(folder_path, filename_without_extension, content):
    """
    Create a workspace note only if it does not already exist.
    """
    filepath = os.path.join(folder_path, filename_without_extension + ".md")

    if os.path.exists(filepath):
        return

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)



def make_generated_reference_target(folder_path, filename_without_extension):
    """
    Build a vault-root-relative target for the generated reference note.
    """
    return convert_path_to_wikilink_target(os.path.join(folder_path, filename_without_extension + ".md"))



def make_workspace_target(folder_path, object_id, name):
    """
    Build a vault-root-relative target for a workspace note.
    """
    filename = make_workspace_note_filename(object_id, name)
    return convert_path_to_wikilink_target(os.path.join(folder_path, filename + ".md"))



def clean_d3fend_relationship_values(values):
    """
    Remove duplicate and low-value ontology relationship rows.
    """
    cleaned = []

    for value in values:
        if not value:
            continue

        if isinstance(value, str):
            current_value = value.strip()
        else:
            current_value = str(value).strip()

        if not current_value:
            continue

        if current_value.startswith("_:"):
            continue

        if current_value == "d3f:DefensiveTechnique":
            continue

        if current_value.startswith("rdf:"):
            continue

        if current_value.startswith("rdfs:"):
            continue

        if current_value.startswith("owl:"):
            continue

        if current_value in cleaned:
            continue

        cleaned.append(current_value)

    return cleaned



def build_d3fend_yaml_lines(entry):
    """
    Build YAML lines for a D3FEND technique note.
    """
    lines = []

    yaml_write_line(lines, "framework", "d3fend")
    yaml_write_line(lines, "object_type", "defensive-technique")
    yaml_write_line(lines, "generated", "true")
    yaml_write_line(lines, "d3fend_id", get_d3fend_id(entry))
    yaml_write_line(lines, "d3fend_name", get_d3fend_label(entry))
    yaml_write_line(lines, "d3fend_ontology_id", entry.get("@id", ""))
    yaml_write_line(lines, "d3fend_url", build_d3fend_url(entry))
    yaml_write_list(lines, "tags", build_d3fend_tags())
    yaml_write_line(lines, "build_date", BUILD_DATE)
    yaml_write_line(lines, "build_source", BUILD_SOURCE)

    return lines



def build_d3fend_note(
    entry,
    parent_to_children,
    child_to_parent,
    d3fend_lookup,
    d3fend_to_attack_map,
    attack_id_lookup,
    subtechnique_attack_id_to_parent,
):
    """
    Build one D3FEND technique note.
    """
    d3fend_id = get_d3fend_id(entry)
    name = get_d3fend_label(entry)
    ontology_id = entry.get("@id", "")

    yaml_lines = build_d3fend_yaml_lines(entry)
    yaml_write_list(yaml_lines, "attack_technique_ids", d3fend_to_attack_map.get(d3fend_id, []))

    text = render_yaml_block(yaml_lines)
    text += build_page_start()

    definition = get_d3fend_text_value(entry, "d3f:definition")
    if definition:
        text += definition + "\n\n"

    text += build_workspace_link_section(make_workspace_target(NOTES_D3FEND_TECHNIQUES_DIR, d3fend_id, name))

    parent = child_to_parent.get(ontology_id)
    if parent is not None:
        parent_id = get_d3fend_id(parent)
        parent_name = get_d3fend_label(parent)
        text += write_bullet_links("Parent Technique", [make_d3fend_link(parent_id, parent_name)])

    child_links = []
    for child in parent_to_children.get(ontology_id, []):
        child_links.append(make_d3fend_link(get_d3fend_id(child), get_d3fend_label(child)))

    text += write_bullet_links("Child Techniques", child_links)

    attack_links = build_attack_links_from_ids(
        d3fend_to_attack_map.get(d3fend_id, []),
        attack_id_lookup,
        subtechnique_attack_id_to_parent,
    )
    text += write_bullet_links("Related ATT&CK Techniques", attack_links)

    article = get_d3fend_text_value(entry, "d3f:kb-article")
    if article:
        text += "## Knowledge Base Article\n\n"
        text += article + "\n\n"

    see_also_values = []
    for ref_id in get_d3fend_reference_ids(entry, "rdfs:seeAlso"):
        see_also_values.append(ref_id)

    if see_also_values:
        text += write_bullet_values("See Also", see_also_values)

    related_values = []
    for ref_id in get_d3fend_reference_ids(entry, "rdfs:subClassOf"):
        if ref_id == ontology_id:
            continue

        if ref_id in d3fend_lookup:
            related_entry = d3fend_lookup[ref_id]
            related_values.append(make_d3fend_link(get_d3fend_id(related_entry), get_d3fend_label(related_entry)))
        else:
            related_values.append(ref_id)

    related_values = clean_d3fend_relationship_values(related_values)

    if related_values:
        text += write_bullet_values("Ontology Relationships", related_values)

    return text



# ============================================================
# URL HELPERS
# ============================================================

def build_tactic_url(attack_id):
    return f"https://attack.mitre.org/tactics/{attack_id}/"



def build_technique_url(attack_id):
    return f"https://attack.mitre.org/techniques/{attack_id}/"



def build_mitigation_url(attack_id):
    return f"https://attack.mitre.org/mitigations/{attack_id}/"



def build_tool_url(attack_id):
    return f"https://attack.mitre.org/software/{attack_id}/"



def build_data_source_url(attack_id):
    return f"https://attack.mitre.org/datasources/{attack_id}/"


# ============================================================
# DESCRIPTION LINK REPLACEMENT
# ============================================================

def make_local_link_for_attack_object(obj):
    """
    Build the right local Obsidian link for a supported ATT&CK object.
    """
    obj_type = obj.get("type", "")
    attack_id = get_attack_id(obj)
    name = obj.get("name", "")

    if obj_type == "x-mitre-tactic":
        return make_tactic_link(attack_id, name)

    if obj_type == "attack-pattern":
        if attack_id.startswith("T"):
            if "." in attack_id:
                # Sub-techniques are stored as blocks inside parent techniques.
                # We do not try to guess the parent here.
                return ""

            return make_technique_link(attack_id, name)

    if obj_type == "course-of-action":
        return make_mitigation_link(attack_id, name)

    if obj_type == "tool":
        return make_tool_link(name)

    if obj_type == "x-mitre-data-source":
        return make_data_source_link(attack_id, name)

    if obj_type == "x-mitre-data-component":
        return make_data_component_link(attack_id, name)

    return ""


MITRE_LINK_PATTERN = re.compile(
    r"\[([^\]]+)\]\(https://attack\.mitre\.org/([^/]+)/([A-Z]{1,3}[0-9]{4})(?:/([0-9]{3}))?/?\)"
)



def normalize_attack_id_from_url_parts(primary_id, secondary_id):
    """
    Convert URL parts into a normal ATT&CK id.

    Examples:
    T1558 + 001 -> T1558.001
    T1204 + None -> T1204
    """
    if secondary_id:
        return f"{primary_id}.{secondary_id}"

    return primary_id



def make_local_link_for_attack_object(obj, attack_id, subtechnique_attack_id_to_parent):
    """
    Build the right local Obsidian link for a supported ATT&CK object.
    """
    obj_type = obj.get("type", "")
    name = obj.get("name", "")

    if obj_type == "x-mitre-tactic":
        return make_tactic_link(attack_id, name)

    if obj_type == "attack-pattern":
        if attack_id.startswith("T"):
            if "." in attack_id:
                parent = subtechnique_attack_id_to_parent.get(obj["id"])

                if parent is None:
                    return ""

                parent_attack_id = get_attack_id(parent)
                parent_name = parent.get("name", "")
                return make_subtechnique_block_link(parent_attack_id, parent_name, attack_id, name)

            return make_technique_link(attack_id, name)

    if obj_type == "course-of-action":
        return make_mitigation_link(attack_id, name)

    if obj_type == "tool":
        return make_tool_link(name)

    if obj_type == "x-mitre-data-source":
        return make_data_source_link(attack_id, name)

    if obj_type == "x-mitre-data-component":
        return make_data_component_link(attack_id, name)

    return ""



def replace_mitre_links_with_local(text, attack_id_lookup, subtechnique_attack_id_to_parent):
    """
    Replace inline MITRE web links with local Obsidian links when the object
    exists in the vault.
    """
    if not text:
        return text

    def replace_match(match):
        primary_id = match.group(3)
        secondary_id = match.group(4)
        attack_id = normalize_attack_id_from_url_parts(primary_id, secondary_id)
        obj = attack_id_lookup.get(attack_id)

        if obj is None:
            return match.group(0)

        local_link = make_local_link_for_attack_object(obj, attack_id, subtechnique_attack_id_to_parent)

        if local_link:
            return local_link

        return match.group(0)

    return MITRE_LINK_PATTERN.sub(replace_match, text)



def replace_pre_code_block(match):
    """
    Convert one HTML pre/code block to fenced markdown.
    """
    code_text = match.group(1).strip()
    return "\n```\n" + code_text + "\n```\n"



def replace_inline_code(match):
    """
    Convert one HTML inline code segment to markdown inline code.
    """
    code_text = match.group(1).strip()
    return "`" + code_text + "`"



def make_obsidian_compatible_code_blocks(text):
    """
    Convert common HTML code formatting into markdown that Obsidian renders well.

    We keep this simple on purpose.
    """
    if not text:
        return text

    text = re.sub(
        r"<pre><code>(.*?)</code></pre>",
        replace_pre_code_block,
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )

    text = re.sub(
        r"<code>(.*?)</code>",
        replace_inline_code,
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )

    return text



def clean_mitre_text(text, attack_id_lookup, subtechnique_attack_id_to_parent):
    """
    Clean MITRE text for Obsidian.

    Current cleanup:
    - replace MITRE web links with local wiki links
    - convert common HTML code blocks to markdown code blocks
    """
    if not text:
        return text

    text = replace_mitre_links_with_local(text, attack_id_lookup, subtechnique_attack_id_to_parent)
    text = make_obsidian_compatible_code_blocks(text)
    return text


# ============================================================
# NOTE CONTENT HELPERS
# ============================================================

def write_h1(title):
    return f"# {title}\n\n"



def write_bullet_links(title, links):
    """
    Render a markdown section of bullet links.
    """
    if not links:
        return ""

    text = f"## {title}\n\n"

    for link in links:
        text += f"- {link}\n"

    text += "\n"
    return text



def write_bullet_values(title, values):
    """
    Render a markdown section of bullet values.
    """
    if not values:
        return ""

    text = f"## {title}\n\n"

    for value in values:
        text += f"- {value}\n"

    text += "\n"
    return text



def write_subtechnique_blocks(
    parent_technique,
    subtechniques,
    attack_id_lookup,
    subtechnique_attack_id_to_parent,
    attack_to_d3fend_map=None,
    d3fend_id_lookup=None,
):
    """
    Render all sub-technique sections inside a parent technique note.
    """
    if not subtechniques:
        return ""

    text = "## Subtechniques\n\n"

    for sub in subtechniques:
        sub_attack_id = get_attack_id(sub)
        sub_name = sub.get("name", "")
        heading = f"{sub_attack_id}: {sub_name}"
        block_id = make_subtechnique_block_id(sub_attack_id, sub_name)

        text += f"### {heading}\n\n"
        text += f"^{block_id}\n\n"

        description = sub.get("description", "")
        if description:
            description = clean_mitre_text(description, attack_id_lookup, subtechnique_attack_id_to_parent)
            text += description + "\n\n"

    return text



# ============================================================
# NOTE BUILDERS
# ============================================================

def build_tactic_note(tactic, tactic_to_technique_map, parent_to_subs, attack_id_lookup, subtechnique_attack_id_to_parent):
    """
    Build one tactic note.
    """
    attack_id = get_attack_id(tactic)
    name = tactic.get("name", "")

    yaml_lines = build_common_yaml_lines(tactic, attack_id, build_tactic_url(attack_id))
    yaml_write_line(yaml_lines, "object_type", "tactic")
    yaml_write_list(yaml_lines, "tags", build_attack_tags("tactic"))
    yaml_write_line(yaml_lines, "mitre_shortname", tactic.get("x_mitre_shortname", ""))

    text = render_yaml_block(yaml_lines)
    text += build_page_start()

    description = tactic.get("description", "")
    if description:
        text += description + "\n\n"

    text += build_workspace_link_section(make_workspace_target(NOTES_ATTACK_TACTICS_DIR, attack_id, name))

    related_links = []

    for technique in tactic_to_technique_map.get(tactic["id"], []):
        technique_attack_id = get_attack_id(technique)
        technique_name = technique.get("name", "")
        related_links.append({"level": 0, "link": make_technique_link(technique_attack_id, technique_name)})

        for sub in parent_to_subs.get(technique["id"], []):
            sub_attack_id = get_attack_id(sub)
            sub_name = sub.get("name", "")
            related_links.append(
                {
                    "level": 1,
                    "link": make_subtechnique_block_link(
                        technique_attack_id,
                        technique_name,
                        sub_attack_id,
                        sub_name,
                    ),
                }
            )

    text += write_nested_bullet_links("Related Techniques", related_links)
    return text



def build_technique_note(
    technique,
    parent_to_subs,
    technique_to_mitigation_map,
    technique_to_tool_map,
    technique_to_data_component_map,
    data_component_to_source_map,
    data_source_name_lookup,
    data_component_name_lookup,
    tactic_lookup,
    attack_id_lookup,
    subtechnique_attack_id_to_parent,
    attack_to_d3fend_map,
    d3fend_id_lookup,
):
    """
    Build one technique note.
    """
    attack_id = get_attack_id(technique)
    name = technique.get("name", "")

    yaml_lines = build_common_yaml_lines(technique, attack_id, build_technique_url(attack_id))
    yaml_write_line(yaml_lines, "object_type", "technique")
    yaml_write_line(yaml_lines, "mitre_is_subtechnique", technique.get("x_mitre_is_subtechnique", False))
    yaml_write_list(yaml_lines, "mitre_platforms", technique.get("x_mitre_platforms", []))
    yaml_write_list(yaml_lines, "mitre_permissions_required", technique.get("x_mitre_permissions_required", []))

    tactic_ids = []
    kill_chain_phases = technique.get("kill_chain_phases", [])

    for phase in kill_chain_phases:
        phase_name = phase.get("phase_name", "")
        tactic = tactic_lookup.get(phase_name)

        if tactic is not None:
            tactic_attack_id = get_attack_id(tactic)
            if tactic_attack_id not in tactic_ids:
                tactic_ids.append(tactic_attack_id)

    yaml_write_list(yaml_lines, "mitre_tactic_ids", tactic_ids)
    yaml_write_list(yaml_lines, "mitre_data_source_values", technique.get("x_mitre_data_sources", []))
    yaml_write_list(yaml_lines, "d3fend_ids", attack_to_d3fend_map.get(attack_id, []))

    component_ids = []
    source_ids = []

    for component in technique_to_data_component_map.get(technique["id"], []):
        component_attack_id = get_attack_id(component)
        if component_attack_id and component_attack_id not in component_ids:
            component_ids.append(component_attack_id)

        source = data_component_to_source_map.get(component["id"])
        if source is not None:
            source_attack_id = get_attack_id(source)
            if source_attack_id and source_attack_id not in source_ids:
                source_ids.append(source_attack_id)

    yaml_write_list(yaml_lines, "mitre_data_component_ids", component_ids)
    yaml_write_list(yaml_lines, "mitre_data_source_ids", source_ids)

    include_detection = False
    include_telemetry = False

    if component_ids:
        include_detection = True
        include_telemetry = True

    if source_ids:
        include_detection = True
        include_telemetry = True

    yaml_write_list(yaml_lines, "tags", build_attack_tags("technique", include_detection, include_telemetry))

    text = render_yaml_block(yaml_lines)
    text += build_page_start()

    description = technique.get("description", "")
    if description:
        description = clean_mitre_text(description, attack_id_lookup, subtechnique_attack_id_to_parent)
        text += description + "\n\n"

    text += build_workspace_link_section(make_workspace_target(NOTES_ATTACK_TECHNIQUES_DIR, attack_id, name))

    tactic_links = []
    for phase_name in [phase.get("phase_name", "") for phase in kill_chain_phases]:
        tactic = tactic_lookup.get(phase_name)
        if tactic is not None:
            tactic_links.append(make_tactic_link(get_attack_id(tactic), tactic.get("name", "")))

    text += write_bullet_links("Tactics", tactic_links)

    d3fend_links = build_d3fend_links_from_attack_id(attack_id, attack_to_d3fend_map, d3fend_id_lookup)
    text += write_bullet_links("D3FEND", d3fend_links)

    text += write_subtechnique_blocks(
        technique,
        parent_to_subs.get(technique["id"], []),
        attack_id_lookup,
        subtechnique_attack_id_to_parent,
        attack_to_d3fend_map,
        d3fend_id_lookup,
    )

    mitigation_links = []
    for mitigation in technique_to_mitigation_map.get(technique["id"], []):
        mitigation_links.append(make_mitigation_link(get_attack_id(mitigation), mitigation.get("name", "")))

    text += write_bullet_links("Mitigations", mitigation_links)

    tool_links = []
    for tool in technique_to_tool_map.get(technique["id"], []):
        tool_links.append(make_tool_link(tool.get("name", "")))

    text += write_bullet_links("Tools", tool_links)

    data_source_links = []
    data_component_links = []
    mitre_data_source_values = []
    seen_source_ids = []
    seen_component_ids = []
    seen_data_source_values = []

    for component in technique_to_data_component_map.get(technique["id"], []):
        component_attack_id = get_attack_id(component)
        component_name = component.get("name", "")

        if component_attack_id and component_attack_id not in seen_component_ids:
            seen_component_ids.append(component_attack_id)
            data_component_links.append(make_data_component_link(component_attack_id, component_name))

        source = data_component_to_source_map.get(component["id"])
        if source is not None:
            source_attack_id = get_attack_id(source)
            source_name = source.get("name", "")

            if source_attack_id and source_attack_id not in seen_source_ids:
                seen_source_ids.append(source_attack_id)
                data_source_links.append(make_data_source_link(source_attack_id, source_name))

    for raw_value in technique.get("x_mitre_data_sources", []):
        if raw_value in seen_data_source_values:
            continue

        seen_data_source_values.append(raw_value)
        source_name, component_name = split_mitre_data_source_value(raw_value)

        source_obj = data_source_name_lookup.get(source_name.lower())
        component_obj = data_component_name_lookup.get(component_name.lower())

        if source_obj is not None:
            source_attack_id = get_attack_id(source_obj)
            source_title = source_obj.get("name", "")

            if source_attack_id and source_attack_id not in seen_source_ids:
                seen_source_ids.append(source_attack_id)
                data_source_links.append(make_data_source_link(source_attack_id, source_title))

        elif raw_value not in mitre_data_source_values:
            mitre_data_source_values.append(raw_value)

        if component_name:
            if component_obj is not None:
                component_attack_id = get_attack_id(component_obj)
                component_title = component_obj.get("name", "")

                if component_attack_id and component_attack_id not in seen_component_ids:
                    seen_component_ids.append(component_attack_id)
                    data_component_links.append(make_data_component_link(component_attack_id, component_title))

            elif raw_value not in mitre_data_source_values:
                mitre_data_source_values.append(raw_value)

    text += write_bullet_links("Data Sources", data_source_links)
    text += write_bullet_links("Data Components", data_component_links)
    text += write_bullet_values("MITRE Data Sources", mitre_data_source_values)

    detection = technique.get("x_mitre_detection", "")
    if detection:
        detection = clean_mitre_text(detection, attack_id_lookup, subtechnique_attack_id_to_parent)
        text += "## Detection\n\n"
        text += detection + "\n\n"

    text += write_bullet_values("Platforms", technique.get("x_mitre_platforms", []))
    text += write_bullet_values("Required Permissions", technique.get("x_mitre_permissions_required", []))

    return text



def build_mitigation_note(mitigation, technique_to_mitigation_map, sub_to_parent, technique_lookup, attack_id_lookup, subtechnique_attack_id_to_parent):
    """
    Build one mitigation note.
    """
    attack_id = get_attack_id(mitigation)
    name = mitigation.get("name", "")

    yaml_lines = build_common_yaml_lines(mitigation, attack_id, build_mitigation_url(attack_id))
    yaml_write_line(yaml_lines, "object_type", "mitigation")
    yaml_write_list(yaml_lines, "tags", build_attack_tags("mitigation"))

    text = render_yaml_block(yaml_lines)
    text += build_page_start()

    description = mitigation.get("description", "")
    if description:
        text += description + "\n\n"

    text += build_workspace_link_section(make_workspace_target(NOTES_ATTACK_MITIGATIONS_DIR, attack_id, name))

    links = []
    seen_parent_links = []

    for technique_id in technique_to_mitigation_map:
        for current_mitigation in technique_to_mitigation_map[technique_id]:
            if current_mitigation["id"] != mitigation["id"]:
                continue

            technique = technique_lookup[technique_id]

            if technique.get("x_mitre_is_subtechnique") is True:
                parent = sub_to_parent.get(technique_id)
                if parent is None:
                    continue

                parent_attack_id = get_attack_id(parent)
                parent_name = parent.get("name", "")
                sub_attack_id = get_attack_id(technique)
                sub_name = technique.get("name", "")

                parent_link = make_technique_link(parent_attack_id, parent_name)
                if parent_link not in seen_parent_links:
                    seen_parent_links.append(parent_link)
                    links.append({"level": 0, "link": parent_link})

                links.append(
                    {
                        "level": 1,
                        "link": make_subtechnique_block_link(
                            parent_attack_id,
                            parent_name,
                            sub_attack_id,
                            sub_name,
                        ),
                    }
                )
            else:
                links.append({"level": 0, "link": make_technique_link(get_attack_id(technique), technique.get("name", ""))})

    text += write_nested_bullet_links("Mitigates Techniques", links)
    return text



def build_tool_note(tool, technique_to_tool_map, sub_to_parent, technique_lookup, attack_id_lookup, subtechnique_attack_id_to_parent):
    """
    Build one tool note.
    """
    attack_id = get_attack_id(tool)
    name = tool.get("name", "")

    yaml_lines = build_common_yaml_lines(tool, attack_id, build_tool_url(attack_id))
    yaml_write_line(yaml_lines, "object_type", "tool")
    yaml_write_list(yaml_lines, "tags", build_attack_tags("tool"))
    aliases = tool.get("x_mitre_aliases", [])
    yaml_write_list(yaml_lines, "mitre_aliases", aliases)

    text = render_yaml_block(yaml_lines)
    text += build_page_start()

    description = tool.get("description", "")
    if description:
        text += description + "\n\n"

    text += build_workspace_link_section(make_workspace_target(NOTES_TOOLS_DIR, attack_id, name))

    links = []
    seen_parent_links = []

    for technique_id in technique_to_tool_map:
        for current_tool in technique_to_tool_map[technique_id]:
            if current_tool["id"] != tool["id"]:
                continue

            technique = technique_lookup[technique_id]

            if technique.get("x_mitre_is_subtechnique") is True:
                parent = sub_to_parent.get(technique_id)
                if parent is None:
                    continue

                parent_attack_id = get_attack_id(parent)
                parent_name = parent.get("name", "")
                sub_attack_id = get_attack_id(technique)
                sub_name = technique.get("name", "")

                parent_link = make_technique_link(parent_attack_id, parent_name)
                if parent_link not in seen_parent_links:
                    seen_parent_links.append(parent_link)
                    links.append({"level": 0, "link": parent_link})

                links.append(
                    {
                        "level": 1,
                        "link": make_subtechnique_block_link(
                            parent_attack_id,
                            parent_name,
                            sub_attack_id,
                            sub_name,
                        ),
                    }
                )
            else:
                links.append({"level": 0, "link": make_technique_link(get_attack_id(technique), technique.get("name", ""))})

    text += write_nested_bullet_links("Uses Techniques", links)
    return text



def build_data_source_note(data_source, data_source_to_component_map, data_source_to_technique_map, technique_lookup, attack_id_lookup, subtechnique_attack_id_to_parent):
    """
    Build one data source note.
    """
    attack_id = get_attack_id(data_source)
    name = data_source.get("name", "")

    yaml_lines = build_common_yaml_lines(data_source, attack_id, build_data_source_url(attack_id))
    yaml_write_line(yaml_lines, "object_type", "data-source")
    yaml_write_list(yaml_lines, "tags", build_attack_tags("data-source"))
    yaml_write_list(yaml_lines, "mitre_platforms", data_source.get("x_mitre_platforms", []))

    component_ids = []
    for component in data_source_to_component_map.get(data_source["id"], []):
        component_attack_id = get_attack_id(component)
        if component_attack_id:
            component_ids.append(component_attack_id)

    yaml_write_list(yaml_lines, "mitre_data_component_ids", component_ids)

    text = render_yaml_block(yaml_lines)
    text += build_page_start()

    description = data_source.get("description", "")
    if description:
        text += description + "\n\n"

    text += build_workspace_link_section(make_workspace_target(NOTES_ATTACK_DATA_SOURCES_DIR, attack_id, name))

    component_links = []
    for component in data_source_to_component_map.get(data_source["id"], []):
        component_links.append(make_data_component_link(get_attack_id(component), component.get("name", "")))

    text += write_bullet_links("Data Components", component_links)

    technique_links = []
    for technique_id in data_source_to_technique_map.get(data_source["id"], []):
        technique = technique_lookup.get(technique_id)
        if technique is None:
            continue

        if technique.get("x_mitre_is_subtechnique") is True:
            continue

        technique_links.append(make_technique_link(get_attack_id(technique), technique.get("name", "")))

    text += write_bullet_links("Related Techniques", technique_links)
    return text



def build_data_component_note(data_component, data_component_to_source_map, data_component_to_technique_map, technique_lookup, attack_id_lookup, subtechnique_attack_id_to_parent):
    """
    Build one data component note.
    """
    attack_id = get_attack_id(data_component)
    name = data_component.get("name", "")

    yaml_lines = build_common_yaml_lines(data_component, attack_id, "")
    yaml_write_line(yaml_lines, "object_type", "data-component")
    yaml_write_list(yaml_lines, "tags", build_attack_tags("data-component"))

    parent_source = data_component_to_source_map.get(data_component["id"])
    if parent_source is not None:
        yaml_write_line(yaml_lines, "mitre_data_source_id", get_attack_id(parent_source))
        yaml_write_line(yaml_lines, "mitre_data_source_name", parent_source.get("name", ""))

    text = render_yaml_block(yaml_lines)
    text += build_page_start()

    description = data_component.get("description", "")
    if description:
        text += description + "\n\n"

    text += build_workspace_link_section(make_workspace_target(NOTES_ATTACK_DATA_COMPONENTS_DIR, attack_id, name))

    if parent_source is not None:
        source_link = make_data_source_link(get_attack_id(parent_source), parent_source.get("name", ""))
        text += write_bullet_links("Parent Data Source", [source_link])

    technique_links = []

    for technique_id in data_component_to_technique_map.get(data_component["id"], []):
        technique = technique_lookup.get(technique_id)
        if technique is None:
            continue

        if technique.get("x_mitre_is_subtechnique") is True:
            continue

        technique_links.append(make_technique_link(get_attack_id(technique), technique.get("name", "")))

    text += write_bullet_links("Related Techniques", technique_links)
    return text


# ============================================================
# WRITER HELPERS
# ============================================================

def write_note(folder_path, filename_without_extension, content):
    """
    Write one markdown note.
    """
    filepath = os.path.join(folder_path, filename_without_extension + ".md")
    changed = write_text_file_if_changed(filepath, content)

    if changed:
        log(f"Wrote: {filepath}", "DEBUG")



def write_build_info_note(counts):
    """
    Write a simple build summary note at the root of the vault.
    """
    filepath = os.path.join(VAULT, "_build_info.md")

    text = "# Vault Build Info\n\n"
    text += f"- build_date: {BUILD_DATE}\n"
    text += f"- build_source: {BUILD_SOURCE}\n"
    text += f"- matrix: {MATRIX_NAME}\n"
    text += f"- attack_json_file: {ATTACK_JSON_FILE}\n"
    text += f"- tactics: {counts['tactics']}\n"
    text += f"- techniques: {counts['techniques']}\n"
    text += f"- mitigations: {counts['mitigations']}\n"
    text += f"- tools: {counts['tools']}\n"
    text += f"- data_sources: {counts['data_sources']}\n"
    text += f"- data_components: {counts['data_components']}\n"
    text += f"- d3fend_techniques: {counts['d3fend_techniques']}\n"

    write_text_file_if_changed(filepath, text)




def make_index_link(folder_path, filename_without_extension, alias_text):
    """
    Build a vault-root-relative index link.

    Index pages should be useful navigation pages, not just count summaries.
    This helper keeps index links consistent with the rest of the vault.
    """
    target = make_generated_reference_target(folder_path, filename_without_extension)
    return f"[[{target}|{alias_text}]]"



def write_index_note(folder_path, title, sections):
    """
    Write a generated index note with real navigation links.

    sections is a simple list of dictionaries:
    [
        {"title": "Section", "rows": ["[[link]]", "[[link2]]"]}
    ]
    """
    text = build_horizontal_navigation()
    text += f"# {title}\n\n"

    for section in sections:
        section_title = section.get("title", "")
        rows = section.get("rows", [])

        if section_title:
            text += f"## {section_title}\n\n"

        if not rows:
            text += "_No entries._\n\n"
            continue

        for row in rows:
            if str(row).startswith("    - "):
                text += str(row) + "\n"
            else:
                text += f"- {row}\n"

        text += "\n"

    write_text_file_if_changed(os.path.join(folder_path, "index.md"), text)



def build_tactic_index_rows(tactics):
    """
    Build rows for the tactics index.
    """
    rows = []

    for tactic in tactics:
        attack_id = get_attack_id(tactic)
        name = tactic.get("name", "")
        filename = make_tactic_filename(attack_id, name)
        rows.append(make_index_link(TACTICS_DIR, filename, f"{attack_id}: {name}"))

    return rows



def build_technique_index_rows(techniques, parent_to_subs):
    """
    Build rows for the techniques index.

    Parent techniques link to files. Sub-techniques link to block anchors inside
    their parent technique files because sub-techniques are not separate files.
    """
    rows = []

    for technique in techniques:
        if technique.get("x_mitre_is_subtechnique") is True:
            continue

        attack_id = get_attack_id(technique)
        name = technique.get("name", "")
        filename = make_technique_filename(attack_id, name)
        rows.append(make_index_link(TECHNIQUES_DIR, filename, f"{attack_id}: {name}"))

        for sub in parent_to_subs.get(technique["id"], []):
            sub_attack_id = get_attack_id(sub)
            sub_name = sub.get("name", "")
            sub_link = make_subtechnique_block_link(attack_id, name, sub_attack_id, sub_name)
            rows.append("    - " + sub_link)

    return rows



def build_mitigation_index_rows(mitigations):
    """
    Build rows for the mitigations index.
    """
    rows = []

    for mitigation in mitigations:
        attack_id = get_attack_id(mitigation)
        if not attack_id.startswith("M"):
            continue

        name = mitigation.get("name", "")
        filename = make_mitigation_filename(attack_id, name)
        rows.append(make_index_link(MITIGATIONS_DIR, filename, f"{attack_id}: {name}"))

    return rows



def build_tool_index_rows(tools):
    """
    Build rows for the MITRE tools index.
    """
    rows = []

    for tool in tools:
        name = tool.get("name", "")
        attack_id = get_attack_id(tool)
        filename = make_tool_filename(name)

        if attack_id:
            alias_text = f"{attack_id}: {name}"
        else:
            alias_text = name

        rows.append(make_index_link(TOOLS_DIR, filename, alias_text))

    return rows



def build_data_source_index_rows(data_sources):
    """
    Build rows for the data sources index.
    """
    rows = []

    for data_source in data_sources:
        attack_id = get_attack_id(data_source)
        if not attack_id.startswith("DS"):
            continue

        name = data_source.get("name", "")
        filename = make_data_source_filename(attack_id, name)
        rows.append(make_index_link(DATA_SOURCES_DIR, filename, f"{attack_id}: {name}"))

    return rows



def build_data_component_index_rows(data_components):
    """
    Build rows for the data components index.
    """
    rows = []

    for data_component in data_components:
        attack_id = get_attack_id(data_component)
        if not attack_id.startswith("DC"):
            continue

        name = data_component.get("name", "")
        filename = make_data_component_filename(attack_id, name)
        rows.append(make_index_link(DATA_COMPONENTS_DIR, filename, f"{attack_id}: {name}"))

    return rows



def build_d3fend_index_rows(d3fend_techniques):
    """
    Build rows for the D3FEND techniques index.
    """
    rows = []

    for entry in d3fend_techniques:
        d3fend_id = get_d3fend_id(entry)
        name = get_d3fend_label(entry)
        filename = make_d3fend_filename(d3fend_id, name)
        rows.append(make_index_link(D3FEND_TECHNIQUES_DIR, filename, f"{d3fend_id}: {name}"))

    return rows



def write_root_index_note():
    """
    Write the vault home page.
    """
    write_index_note(
        VAULT,
        "SecOps Knowledge Base",
        [
            {
                "title": "Start Here",
                "rows": [
                    "[[kb/index|Knowledge Base]]",
                    "[[kb/attack/index|ATT&CK]]",
                    "[[kb/tools/index|MITRE Tools]]",
                    "[[kb/defend/index|D3FEND]]",
                    "[[notes/index|Analyst Notes]]",
                ],
            }
        ],
    )



def write_generated_index_notes(groups, d3fend_groups, parent_to_subs, counts):
    """
    Write useful generated index pages.

    These pages are intentionally simple. They provide click paths into the
    generated vault without requiring search or Dataview.
    """
    tactic_rows = build_tactic_index_rows(groups["tactics"])
    technique_rows = build_technique_index_rows(groups["techniques"], parent_to_subs)
    mitigation_rows = build_mitigation_index_rows(groups["mitigations"])
    tool_rows = build_tool_index_rows(groups["tools"])
    data_source_rows = build_data_source_index_rows(groups["data_sources"])
    data_component_rows = build_data_component_index_rows(groups["data_components"])
    d3fend_rows = build_d3fend_index_rows(d3fend_groups["techniques"])

    write_root_index_note()

    write_index_note(
        KB_DIR,
        "Knowledge Base",
        [
            {
                "title": "Generated Reference Areas",
                "rows": [
                    f"[[kb/attack/index|ATT&CK]] ({counts['tactics']} tactics, {counts['techniques']} techniques)",
                    f"[[kb/tools/index|MITRE Tools]] ({counts['tools']} tools)",
                    f"[[kb/defend/index|D3FEND]] ({counts['d3fend_techniques']} techniques)",
                ],
            }
        ],
    )

    write_index_note(
        ATTACK_DIR,
        "ATT&CK",
        [
            {
                "title": "ATT&CK Areas",
                "rows": [
                    f"[[kb/attack/tactics/index|Tactics]] ({counts['tactics']})",
                    f"[[kb/attack/techniques/index|Techniques]] ({counts['techniques']})",
                    f"[[kb/attack/mitigations/index|Mitigations]] ({counts['mitigations']})",
                    f"[[kb/attack/data-sources/index|Data Sources]] ({counts['data_sources']})",
                    f"[[kb/attack/data-components/index|Data Components]] ({counts['data_components']})",
                ],
            }
        ],
    )

    write_index_note(TOOLS_DIR, "MITRE Tools", [{"title": "Tools", "rows": tool_rows}])
    write_index_note(D3FEND_DIR, "D3FEND", [{"title": "Areas", "rows": [f"[[kb/defend/techniques/index|Techniques]] ({counts['d3fend_techniques']})"]}])
    write_index_note(TACTICS_DIR, "ATT&CK Tactics", [{"title": "Tactics", "rows": tactic_rows}])
    write_index_note(TECHNIQUES_DIR, "ATT&CK Techniques", [{"title": "Techniques", "rows": technique_rows}])
    write_index_note(MITIGATIONS_DIR, "ATT&CK Mitigations", [{"title": "Mitigations", "rows": mitigation_rows}])
    write_index_note(DATA_SOURCES_DIR, "ATT&CK Data Sources", [{"title": "Data Sources", "rows": data_source_rows}])
    write_index_note(DATA_COMPONENTS_DIR, "ATT&CK Data Components", [{"title": "Data Components", "rows": data_component_rows}])
    write_index_note(D3FEND_TECHNIQUES_DIR, "D3FEND Techniques", [{"title": "Techniques", "rows": d3fend_rows}])

    write_index_note(
        NOTES_DIR,
        "Analyst Notes",
        [
            {
                "title": "Note Areas",
                "rows": [
                    "[[notes/attack/index|ATT&CK Notes]]",
                    "[[notes/tools/index|Tool Notes]]",
                    "[[notes/defend/index|D3FEND Notes]]",
                ],
            }
        ],
    )

    write_index_note(
        NOTES_ATTACK_DIR,
        "ATT&CK Notes",
        [
            {
                "title": "How to Use",
                "rows": [
                    "Open a generated ATT&CK page, then click its workspace note link.",
                    "The script creates folders only. Obsidian creates note files when links are clicked.",
                ],
            }
        ],
    )

    write_index_note(
        NOTES_TOOLS_DIR,
        "Tool Notes",
        [
            {
                "title": "How to Use",
                "rows": [
                    "Open a generated MITRE tool page, then click its workspace note link.",
                    "Use this area for analyst-owned notes about generated MITRE tools.",
                ],
            }
        ],
    )

    write_index_note(
        NOTES_D3FEND_DIR,
        "D3FEND Notes",
        [
            {
                "title": "How to Use",
                "rows": [
                    "Open a generated D3FEND page, then click its workspace note link.",
                    "Use this area for analyst-owned defensive technique notes.",
                ],
            }
        ],
    )


# ============================================================
# MAIN BUILD
# ============================================================

def prepare_folders():
    """
    Create folders and optionally clear old generated markdown files.

    The notes folders are created so Obsidian has a clean place to create
    analyst notes when links are clicked. The script does not create note files.
    """
    folders = [
        WORKING_DIR,
        VAULT,
        KB_DIR,
        ATTACK_DIR,
        D3FEND_DIR,
        TOOLS_DIR,
        NOTES_DIR,
        NOTES_ATTACK_DIR,
        NOTES_ATTACK_TACTICS_DIR,
        NOTES_ATTACK_TECHNIQUES_DIR,
        NOTES_ATTACK_MITIGATIONS_DIR,
        NOTES_ATTACK_DATA_SOURCES_DIR,
        NOTES_ATTACK_DATA_COMPONENTS_DIR,
        NOTES_TOOLS_DIR,
        NOTES_D3FEND_DIR,
        NOTES_D3FEND_TECHNIQUES_DIR,
        TACTICS_DIR,
        TECHNIQUES_DIR,
        MITIGATIONS_DIR,
        DATA_SOURCES_DIR,
        DATA_COMPONENTS_DIR,
        D3FEND_TECHNIQUES_DIR,
    ]

    for folder in folders:
        ensure_folder(folder)

    if FULL_REBUILD:
        clear_markdown_files(TACTICS_DIR)
        clear_markdown_files(TECHNIQUES_DIR)
        clear_markdown_files(MITIGATIONS_DIR)
        clear_markdown_files(TOOLS_DIR)
        clear_markdown_files(DATA_SOURCES_DIR)
        clear_markdown_files(DATA_COMPONENTS_DIR)
        clear_markdown_files(D3FEND_TECHNIQUES_DIR)



def sort_objects_by_attack_id(objects):
    """
    Sort objects by ATT&CK id for stable output.
    """
    objects.sort(key=lambda item: get_attack_id(item))

def write_nested_bullet_links(title, rows):
    """
    Write nested bullet links.

    Supported input styles:

    1. Flat list of strings:
       ["[[link1]]", "[[link2]]"]

    2. Rows with explicit levels:
       [
           {"level": 0, "link": "[[parent]]"},
           {"level": 1, "link": "[[child]]"},
       ]

    3. Parent/children dictionaries:
       [
           {
               "parent": "[[parent]]",
               "children": ["[[child 1]]", "[[child 2]]"]
           }
       ]
    """
    if not rows:
        return ""

    text = f"## {title}\n\n"

    for row in rows:
        if isinstance(row, str):
            text += f"- {row}\n"
            continue

        if isinstance(row, dict):
            parent = row.get("parent")

            if parent:
                text += f"- {parent}\n"

                children = row.get("children", [])

                for child in children:
                    text += f"    - {child}\n"

                continue

            link = row.get("link")
            level = row.get("level", 0)

            if link:
                if level < 0:
                    level = 0

                indent = "    " * level
                text += f"{indent}- {link}\n"
                continue

        text += f"- {str(row)}\n"

    text += "\n"
    return text

def main():
    log("Starting ATT&CK vault build", "INFO")
    prepare_folders()
    download_attack_json_if_needed()
    download_d3fend_json_if_needed()
    download_d3fend_offensive_all_if_needed()

    bundle = load_attack_bundle()
    groups = parse_attack_objects(bundle)

    d3fend_bundle = load_d3fend_bundle()
    d3fend_groups = parse_d3fend_objects(d3fend_bundle)
    d3fend_offensive_all = load_d3fend_offensive_all()

    sort_objects_by_attack_id(groups["tactics"])
    sort_objects_by_attack_id(groups["techniques"])
    sort_objects_by_attack_id(groups["mitigations"])
    sort_objects_by_attack_id(groups["tools"])
    sort_objects_by_attack_id(groups["data_sources"])
    sort_objects_by_attack_id(groups["data_components"])

    d3fend_lookup = build_d3fend_lookup(d3fend_groups["techniques"])
    d3fend_id_lookup = build_d3fend_id_lookup(d3fend_groups["techniques"])
    d3fend_alias_lookup = build_d3fend_alias_lookup(d3fend_groups["techniques"])
    d3fend_parent_to_children, d3fend_child_to_parent = build_d3fend_technique_parent_map(
        d3fend_groups["techniques"],
        d3fend_lookup,
    )
    attack_ids_from_d3fend_api = extract_attack_ids_from_json_data(d3fend_offensive_all)

    known_attack_ids = []
    for technique in groups["techniques"]:
        current_attack_id = get_attack_id(technique)
        if current_attack_id:
            known_attack_ids.append(current_attack_id)

    filtered_attack_ids = []
    for attack_id in attack_ids_from_d3fend_api:
        if attack_id in known_attack_ids and attack_id not in filtered_attack_ids:
            filtered_attack_ids.append(attack_id)

    if not filtered_attack_ids:
        log("No ATT&CK technique ids were found in the D3FEND offensive-technique index", "ERROR")

    attack_to_d3fend_map = build_attack_to_d3fend_map(filtered_attack_ids, d3fend_alias_lookup)
    d3fend_to_attack_map = build_d3fend_to_attack_map(attack_to_d3fend_map)
    log_sample_mappings(attack_to_d3fend_map, d3fend_to_attack_map)

    tactic_lookup = build_object_lookup(groups["tactics"])
    technique_lookup = build_object_lookup(groups["techniques"])
    mitigation_lookup = build_object_lookup(groups["mitigations"])
    tool_lookup = build_object_lookup(groups["tools"])
    data_source_lookup = build_object_lookup(groups["data_sources"])
    data_component_lookup = build_object_lookup(groups["data_components"])
    data_source_name_lookup = build_name_lookup(groups["data_sources"])
    data_component_name_lookup = build_name_lookup(groups["data_components"])

    attack_id_lookup = build_attack_id_lookup(groups)
    tactic_shortname_lookup = build_tactic_shortname_lookup(groups["tactics"])
    relationships_by_type = build_relationships_by_type(groups["relationships"])

    parent_to_subs, sub_to_parent = build_subtechnique_maps(
        groups["techniques"],
        relationships_by_type,
        technique_lookup,
    )

    tactic_to_technique_map = build_tactic_to_technique_map(groups["tactics"], groups["techniques"])
    technique_to_mitigation_map = build_technique_to_mitigation_map(
        relationships_by_type,
        technique_lookup,
        mitigation_lookup,
    )
    technique_to_tool_map = build_technique_to_tool_map(
        relationships_by_type,
        technique_lookup,
        tool_lookup,
    )
    data_source_to_component_map = build_data_source_to_component_map(
        groups["data_sources"],
        groups["data_components"],
    )
    data_component_to_source_map = build_data_component_to_source_map(
        groups["data_components"],
        data_source_lookup,
    )
    technique_to_data_component_map = build_technique_to_data_component_map(
        relationships_by_type,
        technique_lookup,
        data_component_lookup,
    )
    data_component_to_technique_map = build_data_component_to_technique_map(
        technique_to_data_component_map
    )
    data_source_to_technique_map = build_data_source_to_technique_map(
        data_source_to_component_map,
        data_component_to_technique_map,
    )

    log("Writing tactic notes", "INFO")
    for tactic in groups["tactics"]:
        attack_id = get_attack_id(tactic)
        filename = make_tactic_filename(attack_id, tactic.get("name", ""))
        content = build_tactic_note(tactic, tactic_to_technique_map, parent_to_subs, attack_id_lookup, sub_to_parent)
        write_note(TACTICS_DIR, filename, content)


    log("Writing technique notes", "INFO")
    for technique in groups["techniques"]:
        if technique.get("x_mitre_is_subtechnique") is True:
            continue

        attack_id = get_attack_id(technique)
        filename = make_technique_filename(attack_id, technique.get("name", ""))
        content = build_technique_note(
            technique,
            parent_to_subs,
            technique_to_mitigation_map,
            technique_to_tool_map,
            technique_to_data_component_map,
            data_component_to_source_map,
            data_source_name_lookup,
            data_component_name_lookup,
            tactic_shortname_lookup,
            attack_id_lookup,
            sub_to_parent,
            attack_to_d3fend_map,
            d3fend_id_lookup,
        )
        write_note(TECHNIQUES_DIR, filename, content)


    log("Writing mitigation notes", "INFO")
    for mitigation in groups["mitigations"]:
        attack_id = get_attack_id(mitigation)
        if not attack_id.startswith("M"):
            continue

        filename = make_mitigation_filename(attack_id, mitigation.get("name", ""))
        content = build_mitigation_note(
            mitigation,
            technique_to_mitigation_map,
            sub_to_parent,
            technique_lookup,
            attack_id_lookup,
            sub_to_parent,
        )
        write_note(MITIGATIONS_DIR, filename, content)


    log("Writing tool notes", "INFO")
    for tool in groups["tools"]:
        attack_id = get_attack_id(tool)
        filename = make_tool_filename(tool.get("name", ""))
        content = build_tool_note(
            tool,
            technique_to_tool_map,
            sub_to_parent,
            technique_lookup,
            attack_id_lookup,
            sub_to_parent,
        )
        write_note(TOOLS_DIR, filename, content)


    log("Writing data source notes", "INFO")
    for data_source in groups["data_sources"]:
        attack_id = get_attack_id(data_source)
        if not attack_id.startswith("DS"):
            continue

        filename = make_data_source_filename(attack_id, data_source.get("name", ""))
        content = build_data_source_note(
            data_source,
            data_source_to_component_map,
            data_source_to_technique_map,
            technique_lookup,
            attack_id_lookup,
            sub_to_parent,
        )
        write_note(DATA_SOURCES_DIR, filename, content)


    log("Writing data component notes", "INFO")
    for data_component in groups["data_components"]:
        attack_id = get_attack_id(data_component)
        if not attack_id.startswith("DC"):
            continue

        filename = make_data_component_filename(attack_id, data_component.get("name", ""))
        content = build_data_component_note(
            data_component,
            data_component_to_source_map,
            data_component_to_technique_map,
            technique_lookup,
            attack_id_lookup,
            sub_to_parent,
        )
        write_note(DATA_COMPONENTS_DIR, filename, content)


    log("Writing D3FEND notes", "INFO")
    for entry in d3fend_groups["techniques"]:
        d3fend_id = get_d3fend_id(entry)
        filename = make_d3fend_filename(d3fend_id, get_d3fend_label(entry))
        content = build_d3fend_note(
            entry,
            d3fend_parent_to_children,
            d3fend_child_to_parent,
            d3fend_lookup,
            d3fend_to_attack_map,
            attack_id_lookup,
            sub_to_parent,
        )
        write_note(D3FEND_TECHNIQUES_DIR, filename, content)


    counts = {
        "tactics": len(groups["tactics"]),
        "techniques": len(groups["techniques"]),
        "mitigations": len(groups["mitigations"]),
        "tools": len(groups["tools"]),
        "data_sources": len(groups["data_sources"]),
        "data_components": len(groups["data_components"]),
        "d3fend_techniques": len(d3fend_groups["techniques"]),
        "attack_d3fend_mappings": len(attack_to_d3fend_map),
    }

    write_generated_index_notes(groups, d3fend_groups, parent_to_subs, counts)
    write_build_info_note(counts)

    log("Build complete", "INFO")
    log(f"Tactics: {counts['tactics']}", "INFO")
    log(f"Techniques: {counts['techniques']}", "INFO")
    log(f"Mitigations: {counts['mitigations']}", "INFO")
    log(f"Tools: {counts['tools']}", "INFO")
    log(f"Data Sources: {counts['data_sources']}", "INFO")
    log(f"Data Components: {counts['data_components']}", "INFO")
    log(f"D3FEND Techniques: {counts['d3fend_techniques']}", "INFO")
    log(f"ATT&CK to D3FEND Mappings: {counts['attack_d3fend_mappings']}", "INFO")


if __name__ == "__main__":
    main()