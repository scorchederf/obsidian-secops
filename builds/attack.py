"""ATT&CK/D3FEND build wrapper.

Stage 1 keeps the existing large builder intact, but applies small,
controlled patches before execution:

- MITRE tool files are name-first, for example xcmd.md.
- MITRE tool links display both the name and the ATT&CK software id,
  for example [[xcmd|xCmd (S0123)]].
- MITRE tool YAML gets aliases for the ATT&CK id and tool name when possible.
- The analyst-owned folder is named workspaces instead of notes.

This wrapper is deliberately defensive. It validates the patched legacy build
before executing it so half-patched legacy_build.py files fail early with a
useful error instead of failing halfway through a vault build.
"""

import os
import re
import runpy

import requests

from utils.config import LEGACY_BUILD_FILE, LEGACY_BUILD_URL
from utils.files import read_text_file, write_text_file
from utils.logging_utils import log

TOOL_PATCH_MARKER = "# stage1_tool_name_first_patch_applied_v4"
WORKSPACE_PATCH_MARKER = "# stage1_workspaces_patch_applied_v4"


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
    if os.path.exists(LEGACY_BUILD_FILE):
        log("Using local " + LEGACY_BUILD_FILE, "DEBUG")
        return

    log("Downloading current build.py as " + LEGACY_BUILD_FILE, "INFO")
    response = requests.get(LEGACY_BUILD_URL, timeout=120)
    response.raise_for_status()

    with open(LEGACY_BUILD_FILE, "w", encoding="utf-8") as file:
        file.write(response.text)


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

    # Original upstream function.
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

    # Older v2/v3 patched function. Replace it too, because it was not backward
    # compatible and can crash if any old call site remains.
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

    if "def make_tool_link(attack_id_or_name, name=\"\")" in text:
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
    text = read_text_file(LEGACY_BUILD_FILE)

    text = patch_make_tool_link_function(text)
    text = patch_tool_call_sites(text)
    text = patch_tool_aliases(text)

    if TOOL_PATCH_MARKER not in text:
        text = TOOL_PATCH_MARKER + "\n" + text

    write_text_file(LEGACY_BUILD_FILE, text)
    validate_legacy_build_tool_patch()
    log("Applied and validated tool name-first patch", "INFO")


def apply_workspaces_patch():
    text = read_text_file(LEGACY_BUILD_FILE)

    if WORKSPACE_PATCH_MARKER in text:
        log("Workspaces patch marker already present; validating current file", "DEBUG")
        validate_legacy_build_workspaces_patch()
        return

    text = replace_required(
        text,
        'NOTES_DIR = os.path.join(VAULT, "notes")',
        'NOTES_DIR = os.path.join(VAULT, "workspaces")',
        "workspace root folder",
    )

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

    text = WORKSPACE_PATCH_MARKER + "\n" + text
    write_text_file(LEGACY_BUILD_FILE, text)
    validate_legacy_build_workspaces_patch()
    log("Applied and validated workspaces patch", "INFO")


def validate_legacy_build_tool_patch():
    text = read_text_file(LEGACY_BUILD_FILE)

    failures = []

    if 'def make_tool_link(attack_id_or_name, name="")' not in text:
        failures.append("make_tool_link is not backward-compatible")

    if 'def make_tool_link(attack_id, name):' in text:
        failures.append("old non-compatible make_tool_link signature still exists")

    if 'def make_tool_link(name):' in text:
        failures.append("original make_tool_link signature still exists")

    if 'return make_tool_link(name)' in text:
        failures.append("old return make_tool_link(name) call site still exists")

    if 'tool_links.append(make_tool_link(tool.get("name", "")))' in text:
        failures.append("old tool_links.append(make_tool_link(name)) call site still exists")

    if failures:
        message = "legacy_build.py tool patch validation failed:\n- " + "\n- ".join(failures)
        raise RuntimeError(message)

    log("Tool patch validation passed", "DEBUG")


def validate_legacy_build_workspaces_patch():
    text = read_text_file(LEGACY_BUILD_FILE)

    if 'NOTES_DIR = os.path.join(VAULT, "notes")' in text:
        raise RuntimeError("legacy_build.py workspace patch validation failed: NOTES_DIR still points to notes")

    if 'NOTES_DIR = os.path.join(VAULT, "workspaces")' not in text:
        raise RuntimeError("legacy_build.py workspace patch validation failed: NOTES_DIR does not point to workspaces")

    log("Workspaces patch validation passed", "DEBUG")


def build_attack():
    log("Starting ATT&CK/D3FEND legacy build", "INFO")
    download_legacy_build_if_missing()
    apply_tool_name_first_patch()
    apply_workspaces_patch()
    runpy.run_path(LEGACY_BUILD_FILE, run_name="__main__")
    log("Finished ATT&CK/D3FEND legacy build", "INFO")
