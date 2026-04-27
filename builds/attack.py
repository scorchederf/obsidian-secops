"""ATT&CK/D3FEND build wrapper.

Stage 1 keeps the existing large builder intact, but applies small,
controlled patches before execution:

- MITRE tool files are name-first, for example xcmd.md.
- MITRE tool links display both the name and the ATT&CK software id,
  for example [[xcmd|xCmd (S0123)]].
- MITRE tool YAML gets aliases for the ATT&CK id and tool name when possible.
- MITRE tool links are sorted alphabetically where possible.
- The analyst-owned folder is named workspaces instead of notes.

This wrapper is deliberately defensive. It validates the critical patches before
executing the legacy build. Sorting is also handled after the build as a fallback
so small upstream text drift does not break the whole run.
"""

import os
import re
import runpy

import requests

from utils.config import LEGACY_BUILD_FILE, LEGACY_BUILD_URL, NEW_VAULT
from utils.files import read_text_file, write_text_file
from utils.logging_utils import log

TOOL_PATCH_MARKER = "# stage1_tool_name_first_patch_applied_v6"
WORKSPACE_PATCH_MARKER = "# stage1_workspaces_patch_applied_v6"
TOOLS_LABEL_PATCH_MARKER = "# stage1_tools_label_patch_applied_v2"
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEGACY_BUILD_PATH = os.path.join(PROJECT_ROOT, LEGACY_BUILD_FILE)
VAULT_DIR = os.path.join(PROJECT_ROOT, NEW_VAULT)
SOURCE_DESCRIPTION_START = "<!-- generated-source-description-start -->"
SOURCE_DESCRIPTION_END = "<!-- generated-source-description-end -->"

SOURCE_INDEX_DESCRIPTIONS = {
    os.path.join("kb", "attack", "index.md"): (
        "ATT&CK",
        "MITRE ATT&CK is a knowledge base of adversary tactics, techniques, and procedures based on real-world observations. "
        "This vault uses ATT&CK as the main behavior spine: techniques become the pivot point for tools, D3FEND defensive techniques, CAR analytics, Sigma rules, Atomic Red Team tests, LOLBAS entries, and future sources.\n\n"
        "## Upstream\n\n"
        "- [MITRE ATT&CK](https://attack.mitre.org/)\n"
    ),
    os.path.join("kb", "defend", "index.md"): (
        "D3FEND",
        "MITRE D3FEND is a knowledge graph of defensive cybersecurity techniques and countermeasures. "
        "This vault keeps D3FEND under `kb/defend/` and links it back to ATT&CK where defensive techniques help prevent, detect, isolate, harden, or evict adversary behavior.\n\n"
        "## Upstream\n\n"
        "- [MITRE D3FEND](https://d3fend.mitre.org/)\n"
    ),
    os.path.join("kb", "tools", "index.md"): (
        "Tools",
        "This index contains ATT&CK software objects categorized as tools. These pages describe utilities, frameworks, and legitimate binaries that ATT&CK associates with adversary behavior. "
        "`kb/tools/` is kept as the shared tool index so generated sources such as Sigma, Atomic Red Team, LOLBAS, GTFOBins, and future tradecraft repositories can cross-link to the same entities.\n\n"
        "## Upstream\n\n"
        "- [ATT&CK Software](https://attack.mitre.org/software/)\n"
    ),
}

BACKWARD_COMPATIBLE_TOOL_LINK_FUNCTION = '''def make_tool_link(attack_id_or_name, name=""):
    # Backward-compatible signature.
    # Old call sites used: make_tool_link(name)
    # New call sites use: make_tool_link(attack_id, name)
    if name == "":
        attack_id = ""
        name = attack_id_or_name
    else:
        attack_id = attack_id_or_name

    filename = make_tool_filename(name)
    if attack_id:
        return f"[[{filename}|{name} ({attack_id})]]"
    return f"[[{filename}|{name}]]"'''


def download_legacy_build_if_missing():
    legacy_build_path = os.path.join(PROJECT_ROOT, LEGACY_BUILD_FILE)

    if not os.path.exists(legacy_build_path):
        raise FileNotFoundError(
            legacy_build_path + " is missing. Repo is in inconsistent state."
        )

    log("Using local " + legacy_build_path, "INFO")

def replace_required(text, old, new, description):
    if old not in text:
        raise RuntimeError("Could not patch legacy_build.py section: " + description)
    return text.replace(old, new)


def replace_optional(text, old, new, description):
    if old not in text:
        log("Optional patch section not found: " + description, "DEBUG")
        return text
    log("Patched section: " + description, "DEBUG")
    return text.replace(old, new)


def regex_replace_optional(text, pattern, replacement, description):
    new_text, count = re.subn(pattern, replacement, text, count=1, flags=re.DOTALL)
    if count == 0:
        log("Optional regex patch section not found: " + description, "DEBUG")
        return text
    log("Patched section: " + description, "DEBUG")
    return new_text


def patch_make_tool_link_function(text):
    """Replace either old or half-patched make_tool_link with safe function."""

    original_pattern = (
        r'def make_tool_link\(name\):\s+'
        r'filename = make_tool_filename\(name\)\s+'
        r'return f"\[\[\{filename\}\|\{name\}\]\]"'
    )

    new_text, count = re.subn(
        original_pattern,
        BACKWARD_COMPATIBLE_TOOL_LINK_FUNCTION,
        text,
        count=1,
        flags=re.DOTALL,
    )

    if count > 0:
        log("Patched original make_tool_link function", "DEBUG")
        return new_text

    patched_pattern = (
        r'def make_tool_link\(attack_id, name\):\s+'
        r'filename = make_tool_filename\(name\)\s+'
        r'if attack_id:\s+'
        r'return f"\[\[\{filename\}\|\{name\} \(\{attack_id\}\)\]\]"\s+'
        r'return f"\[\[\{filename\}\|\{name\}\]\]"'
    )

    new_text, count = re.subn(
        patched_pattern,
        BACKWARD_COMPATIBLE_TOOL_LINK_FUNCTION,
        text,
        count=1,
        flags=re.DOTALL,
    )

    if count > 0:
        log("Replaced non-compatible make_tool_link function", "DEBUG")
        return new_text

    if 'def make_tool_link(attack_id_or_name, name="")' in text:
        log("make_tool_link is already backward-compatible", "DEBUG")
        return text

    raise RuntimeError("Could not patch legacy_build.py section: make_tool_link function")


def patch_tool_call_sites(text):
    """Update known call sites where the ATT&CK id is available."""

    text = replace_optional(
        text,
        'if obj_type == "tool":\n        return make_tool_link(name)',
        'if obj_type == "tool":\n        return make_tool_link(attack_id, name)',
        "tool local-link helper call site",
    )

    text = replace_optional(
        text,
        'tool_links.append(make_tool_link(tool.get("name", "")))',
        'tool_links.append(make_tool_link(get_attack_id(tool), tool.get("name", "")))',
        "technique tool links",
    )

    return text


def patch_tool_link_sorting(text):
    """Try to sort generated tool links inside legacy_build.py.

    This patch is deliberately optional. If the exact legacy source block has
    drifted, the build should still run. A post-build markdown sorter also runs
    as a fallback.
    """

    if "tool_links.sort()" in text:
        log("Tool link sorting patch already present", "DEBUG")
        return text

    simple_old = (
        '    for tool in tools:\n'
        '        tool_links.append(make_tool_link(get_attack_id(tool), tool.get("name", "")))\n'
    )
    simple_new = simple_old + '    tool_links.sort()\n'

    if simple_old in text:
        log("Patched section: alphabetical tool link sorting", "DEBUG")
        return text.replace(simple_old, simple_new, 1)

    pattern = (
        r'(?m)^([ ]*)for tool in tools:\n'
        r'([ ]*)tool_links\.append\(make_tool_link\(get_attack_id\(tool\), tool\.get\("name", ""\)\)\)\n'
    )

    replacement = (
        r'\1for tool in tools:\n'
        r'\2tool_links.append(make_tool_link(get_attack_id(tool), tool.get("name", "")))\n'
        r'\1tool_links.sort()\n'
    )

    new_text, count = re.subn(pattern, replacement, text, count=1)
    if count == 0:
        log("Could not patch legacy_build.py alphabetical tool sorting; post-build sorter will run", "ERROR")
        return text

    log("Patched section: alphabetical tool link sorting", "DEBUG")
    return new_text


def patch_tool_aliases(text):
    """Add Obsidian aliases to tool YAML when the expected block exists."""

    if 'yaml_write_list(yaml_lines, "aliases", obsidian_aliases)' in text:
        log("Tool aliases patch already present", "DEBUG")
        return text

    pattern = (
        r'(aliases = tool\.get\("x_mitre_aliases", \[\]\)\s+'
        r'yaml_write_list\(yaml_lines, "mitre_aliases", aliases\)\s+)'
        r'text = render_yaml_block\(yaml_lines\)'
    )

    replacement = (
        '\\1obsidian_aliases = []\n'
        '    if attack_id:\n'
        '        obsidian_aliases.append(attack_id)\n'
        '    if name:\n'
        '        obsidian_aliases.append(name)\n'
        '    for alias in aliases:\n'
        '        if alias not in obsidian_aliases:\n'
        '            obsidian_aliases.append(alias)\n'
        '    yaml_write_list(yaml_lines, "aliases", obsidian_aliases)\n'
        '    text = render_yaml_block(yaml_lines)'
    )

    return regex_replace_optional(text, pattern, replacement, "tool YAML aliases")


def apply_tool_name_first_patch():
    text = read_text_file(LEGACY_BUILD_PATH)

    text = patch_make_tool_link_function(text)
    text = patch_tool_call_sites(text)
    text = patch_tool_link_sorting(text)
    text = patch_tool_aliases(text)

    if TOOL_PATCH_MARKER not in text:
        text = TOOL_PATCH_MARKER + "\n" + text

    write_text_file(LEGACY_BUILD_PATH, text)
    validate_legacy_build_tool_patch()
    log("Applied and validated tool name-first patch", "INFO")


def apply_workspaces_patch():
    """Patch legacy_build.py so analyst-owned files live under workspaces/.

    This function must be safe across repeated runs. Previous packages could
    leave legacy_build.py half-patched, so this handles all three states:

    1. original file points NOTES_DIR at notes
    2. already-patched file points NOTES_DIR at workspaces
    3. marker exists from a previous run
    """

    text = read_text_file(LEGACY_BUILD_PATH)

    notes_line = 'NOTES_DIR = os.path.join(VAULT, "notes")'
    workspaces_line = 'NOTES_DIR = os.path.join(VAULT, "workspaces")'

    if notes_line in text:
        text = text.replace(notes_line, workspaces_line, 1)
        log("Patched workspace root folder", "DEBUG")
    elif workspaces_line in text:
        log("Workspace root folder already points to workspaces", "DEBUG")
    else:
        raise RuntimeError(
            "legacy_build.py workspace patch validation failed: could not find NOTES_DIR root folder line"
        )

    # These replacements are safe on repeated runs. If the text is already
    # changed, replace() simply does nothing.
    text = text.replace("notes/", "workspaces/")
    text = text.replace("[[notes/index|Notes]]", "[[workspaces/index|Workspaces]]")
    text = text.replace("Analyst Notes", "Analyst Workspace")
    text = text.replace("ATT&CK Notes", "ATT&CK Workspaces")
    text = text.replace("Tool Notes", "Tool Workspaces")
    text = text.replace("D3FEND Notes", "D3FEND Workspaces")
    text = text.replace("Note Areas", "Workspace Areas")
    text = text.replace("notes created", "workspaces created")
    text = text.replace("analyst-owned notes", "analyst-owned workspaces")
    text = text.replace("analyst notes", "analyst workspaces")
    text = text.replace("note files", "workspace files")
    text = text.replace("note file", "workspace file")
    text = text.replace("notes about", "workspace notes about")

    text = replace_optional(
        text,
        'return unique_strings(["notes", "workspace", parent_framework, parent_object_type])',
        'return unique_strings(["workspace", parent_framework, parent_object_type])',
        "workspace tag helper",
    )
    text = replace_optional(
        text,
        'yaml_write_line(yaml_lines, "framework", "notes")',
        'yaml_write_line(yaml_lines, "framework", "workspaces")',
        "workspace YAML framework",
    )

    if WORKSPACE_PATCH_MARKER not in text:
        text = WORKSPACE_PATCH_MARKER + "\n" + text

    write_text_file(LEGACY_BUILD_PATH, text)
    validate_legacy_build_workspaces_patch()
    log("Applied and validated workspaces patch", "INFO")


def apply_tools_label_patch():
    """Keep displayed tool labels as Tools without moving files."""

    text = read_text_file(LEGACY_BUILD_PATH)
    text = text.replace("[[kb/tools/index|ATT&CK Software]]", "[[kb/tools/index|Tools]]")
    text = text.replace("[[kb/tools/index|MITRE Tools]]", "[[kb/tools/index|Tools]]")
    text = text.replace("ATT&CK Software", "Tools")
    text = text.replace("MITRE Tools", "Tools")

    if TOOLS_LABEL_PATCH_MARKER not in text:
        text = TOOLS_LABEL_PATCH_MARKER + "\n" + text

    write_text_file(LEGACY_BUILD_PATH, text)
    validate_legacy_build_tools_label_patch()
    log("Applied and validated Tools label patch", "INFO")


def validate_legacy_build_tool_patch():
    text = read_text_file(LEGACY_BUILD_PATH)

    failures = []

    if 'def make_tool_link(attack_id_or_name, name="")' not in text:
        failures.append("make_tool_link is not backward-compatible")

    if "def make_tool_link(attack_id, name):" in text:
        failures.append("old non-compatible make_tool_link signature still exists")

    if "def make_tool_link(name):" in text:
        failures.append("original make_tool_link signature still exists")

    if "return make_tool_link(name)" in text:
        failures.append("old return make_tool_link(name) call site still exists")

    if 'tool_links.append(make_tool_link(tool.get("name", "")))' in text:
        failures.append("old tool_links.append(make_tool_link(name)) call site still exists")

    if failures:
        message = "legacy_build.py tool patch validation failed:\n- " + "\n- ".join(failures)
        raise RuntimeError(message)

    log("Tool patch validation passed", "DEBUG")


def validate_legacy_build_workspaces_patch():
    text = read_text_file(LEGACY_BUILD_PATH)

    if 'NOTES_DIR = os.path.join(VAULT, "notes")' in text:
        raise RuntimeError("legacy_build.py workspace patch validation failed: NOTES_DIR still points to notes")

    if 'NOTES_DIR = os.path.join(VAULT, "workspaces")' not in text:
        raise RuntimeError("legacy_build.py workspace patch validation failed: NOTES_DIR does not point to workspaces")

    log("Workspaces patch validation passed", "DEBUG")


def validate_legacy_build_tools_label_patch():
    text = read_text_file(LEGACY_BUILD_PATH)

    failures = []
    if "[[kb/tools/index|ATT&CK Software]]" in text:
        failures.append("navigation still labels kb/tools as ATT&CK Software")
    if "[[kb/tools/index|MITRE Tools]]" in text:
        failures.append("index links still label kb/tools as MITRE Tools")
    if "MITRE Tools" in text:
        failures.append("MITRE Tools title text still exists")
    if "ATT&CK Software" in text:
        failures.append("ATT&CK Software title text still exists")

    if failures:
        message = "legacy_build.py tools label patch validation failed:\n- " + "\n- ".join(failures)
        raise RuntimeError(message)

    log("Tools label patch validation passed", "DEBUG")


def is_tool_link_line(line):
    stripped = line.strip()
    if not stripped.startswith("- [["):
        return False
    if "|" not in stripped:
        return False
    if "]]" not in stripped:
        return False
    return True


def sort_tool_section_lines(lines):
    """Sort bullet links inside sections named Tools.

    This is a fallback for cases where the source-code patch could not find the
    exact legacy builder block. It only sorts simple bullet links under a Tools
    heading and leaves all other markdown alone.
    """

    output = []
    index = 0
    changed = False

    while index < len(lines):
        line = lines[index]
        output.append(line)

        if line.strip().lower() not in ["## tools", "### tools"]:
            index += 1
            continue

        index += 1
        section_lines = []

        while index < len(lines):
            current = lines[index]
            stripped = current.strip()

            if stripped.startswith("#"):
                break

            section_lines.append(current)
            index += 1

        sortable_lines = []
        other_lines = []

        for section_line in section_lines:
            if is_tool_link_line(section_line):
                sortable_lines.append(section_line)
            else:
                other_lines.append(section_line)

        sorted_lines = sorted(sortable_lines, key=lambda item: item.lower())
        if sorted_lines != sortable_lines:
            changed = True

        if sortable_lines and not other_lines:
            output.extend(sorted_lines)
        else:
            # Conservative mode: only sort if the whole section is simple bullet
            # links and blank lines. This avoids mangling prose or tables.
            safe_to_sort = True
            for section_line in other_lines:
                if section_line.strip() != "":
                    safe_to_sort = False

            if safe_to_sort:
                output.extend(sorted_lines)
                output.extend(other_lines)
            else:
                output.extend(section_lines)

    return output, changed


def sort_generated_tool_sections():
    if not os.path.isdir(NEW_VAULT):
        log("Generated vault not found for post-build tool sorting: " + NEW_VAULT, "DEBUG")
        return

    changed_count = 0

    for folder, folder_names, file_names in os.walk(NEW_VAULT):
        folder_names.sort()
        file_names.sort()

        for file_name in file_names:
            if not file_name.endswith(".md"):
                continue

            path = os.path.join(folder, file_name)
            content = read_text_file(path)
            lines = content.splitlines()
            sorted_lines, changed = sort_tool_section_lines(lines)

            if changed:
                new_content = "\n".join(sorted_lines)
                if content.endswith("\n"):
                    new_content += "\n"
                write_text_file(path, new_content)
                changed_count += 1

    log("Post-build tool section sorting updated " + str(changed_count) + " files", "INFO")


def remove_generated_source_description(text):
    pattern = re.compile(
        r"\n?" + re.escape(SOURCE_DESCRIPTION_START) + r".*?" + re.escape(SOURCE_DESCRIPTION_END) + r"\n*",
        flags=re.DOTALL,
    )
    return re.sub(pattern, "\n", text)


def insert_source_description(text, title, description):
    text = remove_generated_source_description(text)
    block = SOURCE_DESCRIPTION_START + "\n" + description.rstrip() + "\n" + SOURCE_DESCRIPTION_END + "\n\n"
    heading = "# " + title + "\n\n"
    if heading in text:
        return text.replace(heading, heading + block, 1)
    return text.rstrip() + "\n\n" + block


def patch_generated_source_index_descriptions():
    changed_count = 0
    for relative_path, values in SOURCE_INDEX_DESCRIPTIONS.items():
        title, description = values
        filepath = os.path.join(VAULT_DIR, relative_path)
        if not os.path.exists(filepath):
            continue
        old_text = read_text_file(filepath)
        new_text = insert_source_description(old_text, title, description)
        if new_text != old_text:
            write_text_file(filepath, new_text)
            changed_count += 1
    log("Patched generated source index descriptions in " + str(changed_count) + " files", "INFO")


def build_attack():
    log("Starting ATT&CK/D3FEND legacy build", "INFO")
    download_legacy_build_if_missing()
    apply_tool_name_first_patch()
    apply_workspaces_patch()
    apply_tools_label_patch()
    #legacy_build_path = os.path.join(PROJECT_ROOT, LEGACY_BUILD_FILE)
    current_folder = os.getcwd()
    try:
        os.chdir(PROJECT_ROOT)
        runpy.run_path(LEGACY_BUILD_PATH, run_name="__main__")
    finally:
        os.chdir(current_folder)
    sort_generated_tool_sections()
    patch_generated_source_index_descriptions()
    log("Finished ATT&CK/D3FEND legacy build", "INFO")
