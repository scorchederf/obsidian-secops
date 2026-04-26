from builds.attack import build_attack
from builds.car import build_car
from builds.indexes import build_indexes
from utils.compare_vaults import compare_vaults
from utils.config import COMPARE_DIFF_FOLDER, COMPARE_REPORT_FILE, NEW_VAULT, OLD_VAULT
from utils.logging_utils import log


def main():
    log("Starting full vault build", "INFO")
    build_attack()
    build_car()
    build_indexes()
    log("Starting vault verification", "INFO")
    result = compare_vaults(OLD_VAULT, NEW_VAULT, COMPARE_REPORT_FILE, COMPARE_DIFF_FOLDER)
    if result["has_mismatches"]:
        log("Vault verification failed", "ERROR")
        log("Read " + COMPARE_REPORT_FILE + " and the files in " + COMPARE_DIFF_FOLDER, "ERROR")
        raise SystemExit(1)
    log("Vault verification passed", "INFO")


if __name__ == "__main__":
    main()
