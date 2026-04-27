DEBUG_BUILD = True
LOG_LEVEL = "DEBUG" if DEBUG_BUILD else "INFO"
NEW_VAULT = "secopskb"
OLD_VAULT = "secopskb02"
WORKING_DIR = "workingdir"
LEGACY_BUILD_FILE = "legacy_build.py"
LEGACY_BUILD_URL = "https://raw.githubusercontent.com/scorchederf/obsidian-secops/main/build.py"
COMPARE_REPORT_FILE = "vault_compare_report.md"
COMPARE_DIFF_FOLDER = "vault_compare_diffs"

BUILD_CAR = True
BUILD_ATOMIC = True
BUILD_SIGMA = True
BUILD_LOLBAS = True

# Empty lists mean include everything for that dimension.
SIGMA_LEVELS = ["critical", "high"]
SIGMA_PRODUCTS = []
SIGMA_STATUSES = []

ATOMIC_PLATFORMS = []
ATOMIC_EXECUTORS = []

LOLBAS_CATEGORIES = []
LOLBAS_FUNCTIONS = []

IGNORED_COMPARE_LINE_PREFIXES = [
    "build_date:", "generated:", "last_build:", "last_updated:", "updated:", "created:",
]
IGNORED_COMPARE_PATH_PREFIXES = [
    "kb/atomic/",
    "kb/car/",
    "kb/lolbas/",
    "kb/sigma/",
]
IGNORED_COMPARE_EXACT_LINES = [
    "- [[kb/atomic/index|Atomic]]",
    "- [[kb/car/index|CAR]]",
    "- [[kb/car/index|CAR]] (102 analytics)",
    "- [[kb/lolbas/index|LOLBAS]]",
    "- [[kb/sigma/index|Sigma]]",
]
IGNORED_COMPARE_REGEXES = [
    r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
    r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z?",
]
