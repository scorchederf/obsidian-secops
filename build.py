import json
import os
import re
from datetime import datetime

import requests

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

LOG_LEVEL = "INFO"  # DEBUG, INFO, ERROR
FULL_REBUILD = True
DOWNLOAD_JSON_IF_MISSING = True

VAULT = "kb"
TACTICS_DIR = os.path.join(VAULT, "tactics")
TECHNIQUES_DIR = os.path.join(VAULT, "techniques")
MITIGATIONS_DIR = os.path.join(VAULT, "mitigations")
TOOLS_DIR = os.path.join(VAULT, "tools")
DATA_SOURCES_DIR = os.path.join(VAULT, "data-sources")
DATA_COMPONENTS_DIR = os.path.join(VAULT, "data-components")

ATTACK_JSON_FILE = "enterprise-attack.json"
ATTACK_JSON_URL = (
    "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/"
    "enterprise-attack/enterprise-attack.json"
)

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



def write_subtechnique_blocks(parent_technique, subtechniques, attack_id_lookup, subtechnique_attack_id_to_parent):
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
    yaml_write_line(yaml_lines, "mitre_shortname", tactic.get("x_mitre_shortname", ""))

    text = render_yaml_block(yaml_lines)
    text += write_h1(f"{attack_id}: {name}")

    description = tactic.get("description", "")
    if description:
        text += description + "\n\n"

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
):
    """
    Build one technique note.
    """
    attack_id = get_attack_id(technique)
    name = technique.get("name", "")

    yaml_lines = build_common_yaml_lines(technique, attack_id, build_technique_url(attack_id))
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

    text = render_yaml_block(yaml_lines)
    text += write_h1(f"{attack_id}: {name}")

    description = technique.get("description", "")
    if description:
        description = clean_mitre_text(description, attack_id_lookup, subtechnique_attack_id_to_parent)
        text += description + "\n\n"

    tactic_links = []
    for phase_name in [phase.get("phase_name", "") for phase in kill_chain_phases]:
        tactic = tactic_lookup.get(phase_name)
        if tactic is not None:
            tactic_links.append(make_tactic_link(get_attack_id(tactic), tactic.get("name", "")))

    text += write_bullet_links("Tactics", tactic_links)
    text += write_subtechnique_blocks(technique, parent_to_subs.get(technique["id"], []), attack_id_lookup, subtechnique_attack_id_to_parent)

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

    text = render_yaml_block(yaml_lines)
    text += write_h1(f"{attack_id}: {name}")

    description = mitigation.get("description", "")
    if description:
        text += description + "\n\n"

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
    aliases = tool.get("x_mitre_aliases", [])
    yaml_write_list(yaml_lines, "mitre_aliases", aliases)

    text = render_yaml_block(yaml_lines)
    text += write_h1(name)

    description = tool.get("description", "")
    if description:
        text += description + "\n\n"

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
    yaml_write_list(yaml_lines, "mitre_platforms", data_source.get("x_mitre_platforms", []))

    component_ids = []
    for component in data_source_to_component_map.get(data_source["id"], []):
        component_attack_id = get_attack_id(component)
        if component_attack_id:
            component_ids.append(component_attack_id)

    yaml_write_list(yaml_lines, "mitre_data_component_ids", component_ids)

    text = render_yaml_block(yaml_lines)
    text += write_h1(f"{attack_id}: {name}")

    description = data_source.get("description", "")
    if description:
        text += description + "\n\n"

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

    parent_source = data_component_to_source_map.get(data_component["id"])
    if parent_source is not None:
        yaml_write_line(yaml_lines, "mitre_data_source_id", get_attack_id(parent_source))
        yaml_write_line(yaml_lines, "mitre_data_source_name", parent_source.get("name", ""))

    text = render_yaml_block(yaml_lines)
    text += write_h1(f"{attack_id}: {name}")

    description = data_component.get("description", "")
    if description:
        text += description + "\n\n"

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

    write_text_file_if_changed(filepath, text)


# ============================================================
# MAIN BUILD
# ============================================================

def prepare_folders():
    """
    Create folders and optionally clear old markdown files.
    """
    folders = [
        VAULT,
        TACTICS_DIR,
        TECHNIQUES_DIR,
        MITIGATIONS_DIR,
        TOOLS_DIR,
        DATA_SOURCES_DIR,
        DATA_COMPONENTS_DIR,
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

    bundle = load_attack_bundle()
    groups = parse_attack_objects(bundle)

    sort_objects_by_attack_id(groups["tactics"])
    sort_objects_by_attack_id(groups["techniques"])
    sort_objects_by_attack_id(groups["mitigations"])
    sort_objects_by_attack_id(groups["tools"])
    sort_objects_by_attack_id(groups["data_sources"])
    sort_objects_by_attack_id(groups["data_components"])

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

    counts = {
        "tactics": len(groups["tactics"]),
        "techniques": len(groups["techniques"]),
        "mitigations": len(groups["mitigations"]),
        "tools": len(groups["tools"]),
        "data_sources": len(groups["data_sources"]),
        "data_components": len(groups["data_components"]),
    }

    write_build_info_note(counts)

    log("Build complete", "INFO")
    log(f"Tactics: {counts['tactics']}", "INFO")
    log(f"Techniques: {counts['techniques']}", "INFO")
    log(f"Mitigations: {counts['mitigations']}", "INFO")
    log(f"Tools: {counts['tools']}", "INFO")
    log(f"Data Sources: {counts['data_sources']}", "INFO")
    log(f"Data Components: {counts['data_components']}", "INFO")


if __name__ == "__main__":
    main()