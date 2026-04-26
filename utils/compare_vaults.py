import difflib
import os
import re

from utils.config import (
    IGNORED_COMPARE_EXACT_LINES,
    IGNORED_COMPARE_LINE_PREFIXES,
    IGNORED_COMPARE_PATH_PREFIXES,
    IGNORED_COMPARE_REGEXES,
)
from utils.files import ensure_folder, remove_folder_if_exists, write_text_file
from utils.logging_utils import log


def is_markdown_file(filepath):
    return filepath.lower().endswith(".md")


def get_markdown_files(root_folder):
    files = []
    if not os.path.isdir(root_folder):
        return files
    for folder, folder_names, file_names in os.walk(root_folder):
        folder_names.sort()
        file_names.sort()
        for file_name in file_names:
            full_path = os.path.join(folder, file_name)
            if is_markdown_file(full_path):
                relative_path = os.path.relpath(full_path, root_folder).replace("\\", "/")
                files.append(relative_path)
    files.sort()
    return files


def should_ignore_compare_path(relative_path):
    return any(relative_path.startswith(prefix) for prefix in IGNORED_COMPARE_PATH_PREFIXES)


def normalize_line(line):
    stripped = line.strip()
    if stripped in IGNORED_COMPARE_EXACT_LINES:
        return None
    if "[[kb/car/index|CAR]]" in line:
        line = line.replace(" • [[kb/car/index|CAR]]", "")
    for prefix in IGNORED_COMPARE_LINE_PREFIXES:
        if stripped.startswith(prefix):
            return prefix + " <ignored>"
    normalized = line
    for pattern in IGNORED_COMPARE_REGEXES:
        normalized = re.sub(pattern, "<ignored-datetime>", normalized)
    return normalized


def read_normalized_lines(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        lines = []
        for line in file.read().splitlines():
            normalized = normalize_line(line)
            if normalized is not None:
                lines.append(normalized)
        return lines


def make_diff_filename(relative_path):
    safe = relative_path.replace("/", "_").replace("\\", "_").replace(":", "").replace(" ", "_")
    if safe.endswith(".md"):
        safe = safe[:-3]
    return safe + ".diff"


def compare_single_file(old_file, new_file, relative_path, diff_folder):
    old_lines = read_normalized_lines(old_file)
    new_lines = read_normalized_lines(new_file)
    old_text = "\n".join(old_lines)
    new_text = "\n".join(new_lines)
    result = {
        "relative_path": relative_path,
        "matches": old_text == new_text,
        "old_size": len(old_text.encode("utf-8")),
        "new_size": len(new_text.encode("utf-8")),
        "old_line_count": len(old_lines),
        "new_line_count": len(new_lines),
        "diff_file": "",
    }
    if result["matches"]:
        return result
    diff_lines = list(difflib.unified_diff(old_lines, new_lines, fromfile=old_file, tofile=new_file, lineterm="", n=3))
    diff_path = os.path.join(diff_folder, make_diff_filename(relative_path))
    write_text_file(diff_path, "\n".join(diff_lines) + "\n")
    result["diff_file"] = diff_path.replace("\\", "/")
    return result


def build_report(old_vault, new_vault, only_old, only_new, changed_results):
    lines = [
        "# Vault Comparison Report", "",
        f"old_vault: `{old_vault}`",
        f"new_vault: `{new_vault}`",
        f"only_in_old: `{len(only_old)}`",
        f"only_in_new: `{len(only_new)}`",
        f"changed_files: `{len(changed_results)}`", "",
    ]
    if only_old:
        lines += ["## Files only in old vault", ""] + [f"- `{p}`" for p in only_old] + [""]
    if only_new:
        lines += ["## Files only in new vault", ""] + [f"- `{p}`" for p in only_new] + [""]
    if changed_results:
        lines += ["## Changed markdown files", "", "| File | Old Size | New Size | Old Lines | New Lines | Diff |", "|---|---:|---:|---:|---:|---|"]
        for r in changed_results:
            lines.append(f"| `{r['relative_path']}` | {r['old_size']} | {r['new_size']} | {r['old_line_count']} | {r['new_line_count']} | `{r['diff_file']}` |")
        lines.append("")
    if not only_old and not only_new and not changed_results:
        lines += ["No markdown mismatches found after timestamp normalization.", ""]
    return "\n".join(lines)


def compare_vaults(old_vault, new_vault, report_file, diff_folder):
    log("Comparing " + old_vault + " to " + new_vault, "INFO")
    remove_folder_if_exists(diff_folder)
    ensure_folder(diff_folder)
    old_set = set(get_markdown_files(old_vault))
    new_set = set(get_markdown_files(new_vault))
    old_set = {path for path in old_set if not should_ignore_compare_path(path)}
    new_set = {path for path in new_set if not should_ignore_compare_path(path)}
    only_old = sorted(old_set - new_set)
    only_new = sorted(new_set - old_set)
    changed_results = []
    for relative_path in sorted(old_set & new_set):
        result = compare_single_file(os.path.join(old_vault, relative_path), os.path.join(new_vault, relative_path), relative_path, diff_folder)
        if not result["matches"]:
            changed_results.append(result)
    write_text_file(report_file, build_report(old_vault, new_vault, only_old, only_new, changed_results))
    has_mismatches = bool(only_old or only_new or changed_results)
    log("Comparison found mismatches" if has_mismatches else "Comparison found no markdown mismatches", "ERROR" if has_mismatches else "INFO")
    return {"has_mismatches": has_mismatches, "only_old": only_old, "only_new": only_new, "changed_files": changed_results}


if __name__ == "__main__":
    compare_vaults("secopskb01", "secopskb", "vault_compare_report.md", "vault_compare_diffs")
