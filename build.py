import os
import requests

# MITRE ATT&CK Python library
# Docs: https://mitreattack-python.readthedocs.io/en/latest/index.html
from mitreattack.stix20 import MitreAttackData

LOG_LEVEL = "DEBUG"  # DEBUG, INFO, ERROR

#region "functions"

def log(message, level="INFO"):
    """
    Simple logger with 3 levels.
    """
    levels = ["DEBUG", "INFO", "ERROR"]

    if levels.index(level) >= levels.index(LOG_LEVEL):
        print(f"[{level}] {message}")


def clear_markdown_files(folder_path):
    """
    Delete all markdown files in a folder so the vault is rebuilt cleanly.
    """
    if not os.path.exists(folder_path):
        return

    for name in os.listdir(folder_path):
        path = os.path.join(folder_path, name)

        if os.path.isfile(path) and name.endswith(".md"):
            os.remove(path)


def make_safe_name(name):
    """
    Convert a name into a safe filename / Obsidian reference.
    """
    safe = name.replace(" ", "_")
    safe = safe.replace("/", "_")
    return safe.lower()


def make_subtechnique_heading(sub_id, sub_name):
    """
    Human-readable heading text shown in the note.
    """
    return f"{sub_id}: {sub_name}"


def make_subtechnique_block_id(sub_id, sub_name):
    """
    Stable Obsidian block ID used for linking.

    Block IDs should only use letters, numbers, and dashes.
    """
    block_id = f"{sub_id}-{sub_name}"
    block_id = block_id.lower()
    block_id = block_id.replace(".", "")
    block_id = block_id.replace(":", "")
    block_id = block_id.replace("/", "-")
    block_id = block_id.replace("\\", "-")
    block_id = block_id.replace(" ", "-")
    block_id = block_id.replace("_", "-")
    return block_id


def make_technique_filename(attack_id, technique_name):
    """
    Build the markdown filename (without .md) for a technique.
    """
    safe_name = make_safe_name(technique_name)
    return f"{attack_id}-{safe_name}"


def make_tool_filename(tool_id, tool_name):
    """
    Build the markdown filename (without .md) for a tool.
    """
    safe_name = make_safe_name(tool_name)

    if tool_id:
        return f"{tool_id}-{safe_name}"

    return safe_name


def build_subtechnique_parent_map(mitre):
    """
    Build a lookup of:
    subtechnique STIX ID -> parent technique object
    """
    subtechnique_parent_map = {}

    for technique in mitre.get_techniques():
        is_subtechnique = getattr(technique, "x_mitre_is_subtechnique", False)

        if not is_subtechnique:
            entries = mitre.get_subtechniques_of_technique(technique.id)

            for entry in entries:
                sub = entry["object"]
                subtechnique_parent_map[sub.id] = technique

    return subtechnique_parent_map


def write_tactic_yaml(f, tactic):
    """
    Write YAML frontmatter for tactic file.
    """
    f.write("---\n")
    f.write(f"id: {tactic.id}\n")
    f.write(f"name: {tactic.name}\n")
    f.write(f"created: {tactic.created}\n")
    f.write(f"modified: {tactic.modified}\n")
    f.write(f"type: {tactic.type}\n")
    f.write(f"x_mitre_version: {tactic.x_mitre_version}\n")
    f.write(f"x_mitre_domains: {', '.join(tactic.x_mitre_domains)}\n")
    f.write("---\n\n")


def write_tactic_properties(f, tactic):
    """
    Write readable properties section.
    """
    f.write("## Properties\n\n")
    f.write(f"- id: {tactic.id}\n")
    f.write(f"- name: {tactic.name}\n")
    f.write(f"- created: {tactic.created}\n")
    f.write(f"- modified: {tactic.modified}\n")
    f.write(f"- type: {tactic.type}\n")
    f.write(f"- x_mitre_version: {tactic.x_mitre_version}\n")
    f.write(f"- x_mitre_domains: {', '.join(tactic.x_mitre_domains)}\n\n")


def write_technique_yaml(tf, technique, attack_id):
    """
    Write YAML frontmatter for a technique file.
    """
    tf.write("---\n")
    tf.write(f"id: {attack_id}\n")
    tf.write(f"name: {technique.name}\n")
    tf.write(f"created: {technique.created}\n")
    tf.write(f"modified: {technique.modified}\n")
    tf.write(f"type: {technique.type}\n")

    if hasattr(technique, "x_mitre_version"):
        tf.write(f"x_mitre_version: {technique.x_mitre_version}\n")

    if hasattr(technique, "x_mitre_domains"):
        tf.write(f"x_mitre_domains: {', '.join(technique.x_mitre_domains)}\n")

    tf.write("---\n\n")


def write_technique_tactic_link(tf, tactic):
    """
    Write the parent tactic link on the technique page.
    """
    tactic_safe = make_safe_name(tactic.name)

    tf.write("## Tactic\n\n")
    tf.write(f"- [[{tactic_safe}|{tactic.name}]]\n\n")


def write_technique_description(tf, technique):
    """
    Write technique description if present.
    """
    if hasattr(technique, "description"):
        tf.write(f"{technique.description}\n\n")


def write_technique_properties(tf, technique, attack_id):
    """
    Write readable properties section for the technique page.
    """
    tf.write("## Properties\n\n")
    tf.write(f"- id: {attack_id}\n")
    tf.write(f"- name: {technique.name}\n")
    tf.write(f"- created: {technique.created}\n")
    tf.write(f"- modified: {technique.modified}\n")
    tf.write(f"- type: {technique.type}\n")

    if hasattr(technique, "x_mitre_version"):
        tf.write(f"- x_mitre_version: {technique.x_mitre_version}\n")

    if hasattr(technique, "x_mitre_domains"):
        tf.write(f"- x_mitre_domains: {', '.join(technique.x_mitre_domains)}\n")

    tf.write("\n")


def write_subtechniques_section(tf, mitre, technique, tactic, attack_id):
    """
    Write the detailed subtechniques section inside a technique file.
    """
    entries = mitre.get_subtechniques_of_technique(technique.id)

    if len(entries) > 0:
        tf.write("## Subtechniques\n\n")

        sub_list = []

        for entry in entries:
            sub = entry["object"]
            sub_id = mitre.get_attack_id(sub.id)
            sub_list.append((sub_id, sub))

        sub_list.sort()

        for sub_id, sub in sub_list:
            heading_text = make_subtechnique_heading(sub_id, sub.name)
            block_id = make_subtechnique_block_id(sub_id, sub.name)

            tf.write(f"### {heading_text}\n\n")
            tf.write(f"^{block_id}\n\n")

            # Backlinks
            parent_safe = make_safe_name(technique.name)
            parent_file = f"{attack_id}-{parent_safe}"
            tactic_safe = make_safe_name(tactic.name)

            tf.write("**Parent Technique**\n")
            tf.write(f"- [[{parent_file}|{attack_id}: {technique.name}]]\n\n")

            tf.write("**Tactic**\n")
            tf.write(f"- [[{tactic_safe}|{tactic.name}]]\n\n")

            if hasattr(sub, "description"):
                tf.write(f"{sub.description}\n\n")

            tf.write("#### Properties\n\n")
            tf.write(f"- id: {sub_id}\n")
            tf.write(f"- name: {sub.name}\n")

            if hasattr(sub, "created"):
                tf.write(f"- created: {sub.created}\n")

            if hasattr(sub, "modified"):
                tf.write(f"- modified: {sub.modified}\n")

            if hasattr(sub, "type"):
                tf.write(f"- type: {sub.type}\n")

            if hasattr(sub, "x_mitre_version"):
                tf.write(f"- x_mitre_version: {sub.x_mitre_version}\n")

            if hasattr(sub, "x_mitre_domains"):
                tf.write(f"- x_mitre_domains: {', '.join(sub.x_mitre_domains)}\n")

            tf.write("\n")


def write_mitigations_section(tf, mitre, technique, mitigation_map):
    """
    Write the mitigations section for a technique page.

    The mitigation_map is built once from:
    mitre.get_all_mitigations_mitigating_all_techniques()

    It maps:
    technique STIX ID -> list of RelationshipEntry dicts
    """
    mitigation_entries = mitigation_map.get(technique.id, [])

    if len(mitigation_entries) > 0:
        tf.write("## Mitigations\n\n")

        mitigation_rows = []

        for entry in mitigation_entries:
            mitigation = entry["object"]
            mitigation_attack_id = mitre.get_attack_id(mitigation.id)

            if mitigation_attack_id:
                mitigation_rows.append((mitigation_attack_id, mitigation.name))
            else:
                mitigation_rows.append(("", mitigation.name))

        mitigation_rows.sort()

        for mitigation_attack_id, mitigation_name in mitigation_rows:
            mitigation_safe = make_safe_name(mitigation_name)

            if mitigation_attack_id:
                mitigation_file = f"{mitigation_attack_id}-{mitigation_safe}"
                tf.write(
                    f"- [[{mitigation_file}|{mitigation_attack_id}: {mitigation_name}]]\n"
                )
            else:
                mitigation_file = mitigation_safe
                tf.write(f"- [[{mitigation_file}|{mitigation_name}]]\n")

        tf.write("\n")


def write_operational_sections(tf, technique):
    """
    Write Phase 1 content:
    - Detection
    - Data Sources
    - Platforms
    - Required Permissions
    """

    if hasattr(technique, "x_mitre_detection"):
        if technique.x_mitre_detection:
            tf.write("## Detection\n\n")
            tf.write(f"{technique.x_mitre_detection}\n\n")

    if hasattr(technique, "x_mitre_data_sources"):
        if technique.x_mitre_data_sources:
            tf.write("## Data Sources\n\n")

            for data_source in technique.x_mitre_data_sources:
                tf.write(f"- {data_source}\n")

            tf.write("\n")

    if hasattr(technique, "x_mitre_platforms"):
        if technique.x_mitre_platforms:
            tf.write("## Platforms\n\n")

            for platform in technique.x_mitre_platforms:
                tf.write(f"- {platform}\n")

            tf.write("\n")

    if hasattr(technique, "x_mitre_permissions_required"):
        if technique.x_mitre_permissions_required:
            tf.write("## Required Permissions\n\n")

            for permission in technique.x_mitre_permissions_required:
                tf.write(f"- {permission}\n")

            tf.write("\n")


def write_tools_section(tf, mitre, technique, tool_map):
    """
    Write tool links for a technique page.
    This includes only ATT&CK objects of type 'tool'.
    """
    tool_entries = tool_map.get(technique.id, [])

    if len(tool_entries) > 0:
        tf.write("## Tools\n\n")

        tool_rows = []

        for entry in tool_entries:
            tool = entry["object"]

            if getattr(tool, "type", "") != "tool":
                continue

            tool_id = mitre.get_attack_id(tool.id)
            tool_rows.append((tool_id, tool.name))

        tool_rows.sort()

        seen = set()

        for tool_id, tool_name in tool_rows:
            key = (tool_id, tool_name)

            if key in seen:
                continue

            seen.add(key)

            tool_file = make_tool_filename(tool_id, tool_name)

            if tool_id:
                tf.write(f"- [[{tool_file}|{tool_id}: {tool_name}]]\n")
            else:
                tf.write(f"- [[{tool_file}|{tool_name}]]\n")

        tf.write("\n")


def write_technique_file(
    mitre,
    technique,
    tactic,
    attack_id,
    techniques_dir,
    mitigation_map,
    tool_map
):
    """
    Write one technique markdown file.
    """
    safe_name = make_safe_name(technique.name)
    filename = f"{attack_id}-{safe_name}.md"
    filepath = os.path.join(techniques_dir, filename)

    log(f"Writing technique file: {filename}", "DEBUG")

    with open(filepath, "w", encoding="utf-8") as tf:
        write_technique_yaml(tf, technique, attack_id)
        write_technique_tactic_link(tf, tactic)
        write_technique_description(tf, technique)
        write_technique_properties(tf, technique, attack_id)
        write_subtechniques_section(tf, mitre, technique, tactic, attack_id)
        write_mitigations_section(tf, mitre, technique, mitigation_map)
        write_operational_sections(tf, technique)
        write_tools_section(tf, mitre, technique, tool_map)


def write_mitigation_file(
    mitre,
    mitigation,
    mitigation_map,
    techniques_lookup,
    subtechnique_parent_map,
    mitigations_dir
):
    """
    Creates a markdown file for a mitigation.

    Includes:
    - YAML frontmatter
    - Description
    - Properties
    - Techniques it mitigates

    Parent techniques are linked as normal files.
    Subtechniques are linked as indented block links inside the parent technique file.
    """


    # Only allow real mitigation objects
    if getattr(mitigation, "type", "") != "course-of-action":
        log(f"Skipping non-mitigation object: {getattr(mitigation, 'name', 'unknown')}", "DEBUG")
        return

    mitigation_id = mitre.get_attack_id(mitigation.id)

    # Real mitigations should use Mxxxx IDs
    if not mitigation_id or not mitigation_id.startswith("M"):
        return

    safe_name = make_safe_name(mitigation.name)
    filename = f"{mitigation_id}-{safe_name}.md"
    filepath = os.path.join(mitigations_dir, filename)

    parent_rows = {}
    standalone_parent_ids = []

    # Walk the mitigation map and find all techniques affected by this mitigation
    for technique_id, entries in mitigation_map.items():
        for entry in entries:
            mitigation_obj = entry["object"]

            if mitigation_obj.id == mitigation.id:
                technique = techniques_lookup.get(technique_id)

                if technique is None:
                    continue

                is_subtechnique = getattr(technique, "x_mitre_is_subtechnique", False)

                if not is_subtechnique:
                    parent_attack_id = mitre.get_attack_id(technique.id)
                    parent_file = make_technique_filename(parent_attack_id, technique.name)

                    if technique.id not in parent_rows:
                        parent_rows[technique.id] = {
                            "attack_id": parent_attack_id,
                            "name": technique.name,
                            "file": parent_file,
                            "subs": []
                        }
                        standalone_parent_ids.append(technique.id)
                else:
                    parent = subtechnique_parent_map.get(technique.id)

                    if parent is None:
                        continue

                    parent_attack_id = mitre.get_attack_id(parent.id)
                    parent_file = make_technique_filename(parent_attack_id, parent.name)

                    if parent.id not in parent_rows:
                        parent_rows[parent.id] = {
                            "attack_id": parent_attack_id,
                            "name": parent.name,
                            "file": parent_file,
                            "subs": []
                        }
                        standalone_parent_ids.append(parent.id)

                    sub_attack_id = mitre.get_attack_id(technique.id)
                    block_id = make_subtechnique_block_id(sub_attack_id, technique.name)

                    parent_rows[parent.id]["subs"].append(
                        (sub_attack_id, technique.name, parent_file, block_id)
                    )

    # Do not create empty mitigation files
    if len(parent_rows) == 0:
        log(f"Skipping empty mitigation file: {mitigation_id} {mitigation.name}", "DEBUG")
        return

    log(f"Writing mitigation file: {filename}", "DEBUG")

    with open(filepath, "w", encoding="utf-8") as mf:

        # ---------------------------
        # YAML
        # ---------------------------
        mf.write("---\n")
        mf.write(f"id: {mitigation_id}\n")
        mf.write(f"name: {mitigation.name}\n")

        if hasattr(mitigation, "created"):
            mf.write(f"created: {mitigation.created}\n")

        if hasattr(mitigation, "modified"):
            mf.write(f"modified: {mitigation.modified}\n")

        if hasattr(mitigation, "type"):
            mf.write(f"type: {mitigation.type}\n")

        mf.write("---\n\n")

        # ---------------------------
        # Title + Description
        # ---------------------------
        mf.write(f"# {mitigation.name}\n\n")

        if hasattr(mitigation, "description"):
            mf.write(f"{mitigation.description}\n\n")

        # ---------------------------
        # Properties
        # ---------------------------
        mf.write("## Properties\n\n")
        mf.write(f"- id: {mitigation_id}\n")
        mf.write(f"- name: {mitigation.name}\n")

        if hasattr(mitigation, "created"):
            mf.write(f"- created: {mitigation.created}\n")

        if hasattr(mitigation, "modified"):
            mf.write(f"- modified: {mitigation.modified}\n")

        if hasattr(mitigation, "type"):
            mf.write(f"- type: {mitigation.type}\n")

        mf.write("\n")

        # ---------------------------
        # Techniques mitigated
        # ---------------------------
        mf.write("## Mitigates Techniques\n\n")

        sortable_parents = []

        for parent_id in standalone_parent_ids:
            row = parent_rows[parent_id]
            sortable_parents.append((row["attack_id"], parent_id))

        sortable_parents.sort()

        for _, parent_id in sortable_parents:
            row = parent_rows[parent_id]

            # Parent technique link
            mf.write(f"- [[{row['file']}|{row['attack_id']}: {row['name']}]]\n")

            # Sort subtechniques by ATT&CK ID
            row["subs"].sort()

            for sub_attack_id, sub_name, parent_file, block_id in row["subs"]:
                mf.write(
                    f"    - [[{parent_file}#^{block_id}|{sub_attack_id}: {sub_name}]]\n"
                )

        mf.write("\n")


def write_tool_file(
    mitre,
    tool,
    tool_map,
    techniques_lookup,
    subtechnique_parent_map,
    tools_dir
):
    """
    Create a markdown file for a tool.

    Parent techniques are linked as normal files.
    Subtechniques are linked as indented block links inside the parent technique file.
    """

    tool_id = mitre.get_attack_id(tool.id)
    filename = make_tool_filename(tool_id, tool.name) + ".md"
    filepath = os.path.join(tools_dir, filename)

    log(f"Writing tool file: {filename}", "DEBUG")

    with open(filepath, "w", encoding="utf-8") as tf:
        # ---------------------------
        # YAML
        # ---------------------------
        tf.write("---\n")

        if tool_id:
            tf.write(f"id: {tool_id}\n")

        tf.write(f"name: {tool.name}\n")

        if hasattr(tool, "created"):
            tf.write(f"created: {tool.created}\n")

        if hasattr(tool, "modified"):
            tf.write(f"modified: {tool.modified}\n")

        if hasattr(tool, "type"):
            tf.write(f"type: {tool.type}\n")

        if hasattr(tool, "x_mitre_version"):
            tf.write(f"x_mitre_version: {tool.x_mitre_version}\n")

        if hasattr(tool, "x_mitre_domains"):
            tf.write(f"x_mitre_domains: {', '.join(tool.x_mitre_domains)}\n")

        tf.write("---\n\n")

        # ---------------------------
        # Title + Description
        # ---------------------------
        tf.write(f"# {tool.name}\n\n")

        if hasattr(tool, "description"):
            tf.write(f"{tool.description}\n\n")

        # ---------------------------
        # Properties
        # ---------------------------
        tf.write("## Properties\n\n")

        if tool_id:
            tf.write(f"- id: {tool_id}\n")

        tf.write(f"- name: {tool.name}\n")

        if hasattr(tool, "created"):
            tf.write(f"- created: {tool.created}\n")

        if hasattr(tool, "modified"):
            tf.write(f"- modified: {tool.modified}\n")

        if hasattr(tool, "type"):
            tf.write(f"- type: {tool.type}\n")

        if hasattr(tool, "x_mitre_version"):
            tf.write(f"- x_mitre_version: {tool.x_mitre_version}\n")

        if hasattr(tool, "x_mitre_domains"):
            tf.write(f"- x_mitre_domains: {', '.join(tool.x_mitre_domains)}\n")

        tf.write("\n")

        # ---------------------------
        # Techniques used
        # ---------------------------
        tf.write("## Uses Techniques\n\n")

        parent_rows = {}
        standalone_parent_ids = []

        for technique_id, entries in tool_map.items():
            for entry in entries:
                obj = entry["object"]

                if obj.id == tool.id:
                    technique = techniques_lookup.get(technique_id)

                    if technique is None:
                        continue

                    is_subtechnique = getattr(technique, "x_mitre_is_subtechnique", False)

                    if not is_subtechnique:
                        parent_attack_id = mitre.get_attack_id(technique.id)
                        parent_file = make_technique_filename(parent_attack_id, technique.name)

                        if technique.id not in parent_rows:
                            parent_rows[technique.id] = {
                                "attack_id": parent_attack_id,
                                "name": technique.name,
                                "file": parent_file,
                                "subs": []
                            }
                            standalone_parent_ids.append(technique.id)
                    else:
                        parent = subtechnique_parent_map.get(technique.id)

                        if parent is None:
                            continue

                        parent_attack_id = mitre.get_attack_id(parent.id)
                        parent_file = make_technique_filename(parent_attack_id, parent.name)

                        if parent.id not in parent_rows:
                            parent_rows[parent.id] = {
                                "attack_id": parent_attack_id,
                                "name": parent.name,
                                "file": parent_file,
                                "subs": []
                            }
                            standalone_parent_ids.append(parent.id)

                        sub_attack_id = mitre.get_attack_id(technique.id)
                        block_id = make_subtechnique_block_id(sub_attack_id, technique.name)

                        parent_rows[parent.id]["subs"].append(
                            (sub_attack_id, technique.name, parent_file, block_id)
                        )

        sortable_parents = []

        for parent_id in standalone_parent_ids:
            row = parent_rows[parent_id]
            sortable_parents.append((row["attack_id"], parent_id))

        sortable_parents.sort()

        for _, parent_id in sortable_parents:
            row = parent_rows[parent_id]

            tf.write(f"- [[{row['file']}|{row['attack_id']}: {row['name']}]]\n")

            row["subs"].sort()

            for sub_attack_id, sub_name, parent_file, block_id in row["subs"]:
                tf.write(
                    f"    - [[{parent_file}#^{block_id}|{sub_attack_id}: {sub_name}]]\n"
                )

        tf.write("\n")


#endregion

# ============================================================
# CONFIG
# ============================================================

VAULT = "kb"
TACTICS_DIR = os.path.join(VAULT, "tactics")
TECHNIQUES_DIR = os.path.join(VAULT, "techniques")
MITIGATIONS_DIR = os.path.join(VAULT, "mitigations")
TOOLS_DIR = os.path.join(VAULT, "tools")

local_json = "enterprise-attack.json"

url = "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack.json"


# ============================================================
# SETUP
# ============================================================

# Create directories
os.makedirs(TACTICS_DIR, exist_ok=True)
os.makedirs(TECHNIQUES_DIR, exist_ok=True)
os.makedirs(MITIGATIONS_DIR, exist_ok=True)
os.makedirs(TOOLS_DIR, exist_ok=True)

# remove old files if they exist
clear_markdown_files(TACTICS_DIR)
clear_markdown_files(TECHNIQUES_DIR)
clear_markdown_files(MITIGATIONS_DIR)
clear_markdown_files(TOOLS_DIR)



# Download dataset if missing
if not os.path.exists(local_json):
    log("Downloading MITRE ATT&CK dataset...", "INFO")

    r = requests.get(url)
    r.raise_for_status()

    with open(local_json, "w", encoding="utf-8") as f:
        f.write(r.text)

# Load MITRE dataset
mitre = MitreAttackData(local_json)

# Build mitigation lookup once.
# Maps technique STIX ID -> list of mitigation relationship entries.
mitigation_map = mitre.get_all_mitigations_mitigating_all_techniques()

# Build tool lookup once.
# This includes software relationships, so we filter to type == "tool" later.
tool_map = mitre.get_all_software_using_all_techniques()

# Build technique lookup by STIX ID
techniques_lookup = {}

for t in mitre.get_techniques():
    techniques_lookup[t.id] = t

# Build subtechnique -> parent technique lookup
subtechnique_parent_map = build_subtechnique_parent_map(mitre)


# ============================================================
# MAIN LOOP
# ============================================================

for tactic in mitre.get_tactics():
    filename = make_safe_name(tactic.name) + ".md"
    filepath = os.path.join(TACTICS_DIR, filename)

    log(f"Processing tactic: {tactic.name}", "INFO")

    with open(filepath, "w", encoding="utf-8") as f:
        write_tactic_yaml(f, tactic)

        f.write(f"# {tactic.name}\n\n")
        f.write(f"{tactic.description}\n\n")

        write_tactic_properties(f, tactic)

        f.write("## Related Techniques\n\n")

        shortname = tactic.x_mitre_shortname
        domain = tactic.x_mitre_domains[0]

        techniques = mitre.get_techniques_by_tactic(shortname, domain)

        parents = []

        for t in techniques:
            if not getattr(t, "x_mitre_is_subtechnique", False):
                attack_id = mitre.get_attack_id(t.id)
                parents.append((attack_id, t))

        parents.sort()

        for attack_id, technique in parents:
            safe_name = make_safe_name(technique.name)
            link_name = f"{attack_id}-{safe_name}"

            # Parent technique link
            f.write(f"- [[{link_name}|{attack_id}: {technique.name}]]\n")

            # Generate technique file
            write_technique_file(
                mitre,
                technique,
                tactic,
                attack_id,
                TECHNIQUES_DIR,
                mitigation_map,
                tool_map
            )

            # Subtechnique links under the technique on the tactic page
            entries = mitre.get_subtechniques_of_technique(technique.id)

            if len(entries) > 0:
                subs = []

                for entry in entries:
                    sub = entry["object"]
                    sub_id = mitre.get_attack_id(sub.id)
                    subs.append((sub_id, sub))

                subs.sort()

                for sub_id, sub in subs:
                    parent_safe = make_safe_name(technique.name)
                    parent_file = f"{attack_id}-{parent_safe}"

                    block_id = make_subtechnique_block_id(sub_id, sub.name)

                    f.write(
                        f"    - [[{parent_file}#^{block_id}|{sub_id}: {sub.name}]]\n"
                    )


# ============================================================
# MITIGATION FILE GENERATION
# ============================================================

for mitigation in mitre.get_mitigations(remove_revoked_deprecated=True):
    if getattr(mitigation, "type", "") == "course-of-action":
        write_mitigation_file(
            mitre,
            mitigation,
            mitigation_map,
            techniques_lookup,
            subtechnique_parent_map,
            MITIGATIONS_DIR
        )


# ============================================================
# TOOL FILE GENERATION
# ============================================================

for software in mitre.get_software():
    if getattr(software, "type", "") == "tool":
        write_tool_file(
            mitre,
            software,
            tool_map,
            techniques_lookup,
            subtechnique_parent_map,
            TOOLS_DIR
        )