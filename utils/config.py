DEBUG_BUILD = True
LOG_LEVEL = "DEBUG" if DEBUG_BUILD else "INFO"
NEW_VAULT = "secopskb"
OLD_VAULT = "secopskb02"
WORKING_DIR = "workingdir"
LEGACY_BUILD_FILE = "legacy_build.py"
LEGACY_BUILD_URL = "https://raw.githubusercontent.com/scorchederf/obsidian-secops/main/build.py"
COMPARE_REPORT_FILE = "vault_compare_report.md"
COMPARE_DIFF_FOLDER = "vault_compare_diffs"
IGNORED_COMPARE_LINE_PREFIXES = [
    "build_date:", "generated:", "last_build:", "last_updated:", "updated:", "created:",
]
IGNORED_COMPARE_REGEXES = [
    r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
    r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z?",
]
