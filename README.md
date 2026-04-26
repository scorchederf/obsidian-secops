# Obsidian SecOps Builder

Builds an Obsidian vault for ATT&CK, D3FEND, tools, workspaces, MITRE CAR, Sigma, and Atomic Red Team.

## What changed

- `run.py` is the entry point.
- Existing build logic is preserved as `legacy_build.py` and patched before execution.
- MITRE tool pages use name-first filenames, for example `xcmd.md`.
- MITRE tool links display name and ATT&CK software id, for example `[[xcmd|xCmd (S0123)]]`.
- The analyst-owned folder is now `workspaces/` instead of `notes/`.
- MITRE CAR analytics are generated from the upstream CAR YAML source.
- Sigma rules are generated from the upstream SigmaHQ rule repository.
- Atomic Red Team validation tests are generated from the upstream atomic-red-team repository.
- The patch validates `legacy_build.py` before executing it.

## Why v4 exists

Earlier packages could skip fixes if `legacy_build.py` already had an old patch marker from a previous failed run. v4 does not trust old markers for the tool patch. It rewrites/validates the tool link function and call sites every time.

## First run

```bash
./setup.sh
source .venv/bin/activate
python run.py
```

## Build filters

Generated sources can be narrowed in `utils/config.py`.

- `BUILD_CAR`, `BUILD_ATOMIC`, and `BUILD_SIGMA` enable or disable generated sections.
- `SIGMA_LEVELS` defaults to `["critical", "high"]` to keep the vault lean.
- Empty filter lists mean include everything for that dimension.

## Important cleanup before running v4

If you already ran v2 or v3, remove the old partially patched file first:

```bash
rm -f legacy_build.py
```

This forces a clean download and patch.

v4 should also repair a stale half-patched `legacy_build.py`, but starting clean is better.

## Verification output

The build compares:

```text
secopskb01
secopskb
```

and writes:

```text
vault_compare_report.md
vault_compare_diffs/
```

Paste those logs back if the compare fails.
