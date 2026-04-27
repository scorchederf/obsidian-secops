# Obsidian SecOps Builder

Builds an Obsidian vault for security operations knowledge. The vault uses MITRE ATT&CK as the main behavior spine, then attaches defensive techniques, detection rules, analytics, validation tests, tools, and tradecraft references around those behaviors.

The generated vault currently includes ATT&CK, D3FEND, tools, workspaces, MITRE CAR, Sigma, Atomic Red Team, and LOLBAS. The build backlog also tracks GTFOBins, PayloadsAllTheThings, InternalAllTheThings, The Hacker Recipes, Splunk Security Content, Elastic Detection Rules, Security Datasets, Malware Behavior Catalog, and MITRE Engage in `data-source-integration-plan.md`.

## Use

This project is for educational and defensive security research use only.

## Attribution

This project would not be possible without the maintainers and contributors of the upstream repositories, frameworks, and datasets it builds from. Thank you to the owners and communities behind ATT&CK, D3FEND, MITRE CAR, SigmaHQ, Atomic Red Team, and every source planned for future integration. You are the true heroes.

The builder and documentation in this repository were written with ChatGPT. That is part of the project history, not something to hide.

## Project Aim

The goal is to create an analyst-friendly Obsidian knowledge base where related security content is connected instead of scattered across separate projects. An ATT&CK technique page should become the place to pivot into:

- relevant tools and software,
- D3FEND defensive techniques,
- CAR analytics,
- Sigma detections,
- Atomic Red Team validation tests,
- future LOLBAS, GTFOBins, payload, recipe, dataset, and vendor detection content.

Imported source material should remain in its own source folder. ATT&CK pages should receive compact generated summaries and links, not full copies of every upstream page.

Use `secopskb/workspaces/` for your own notes, investigations, hunt ideas, detection drafts, lab notes, and environment-specific context. Treat `secopskb/kb/` as generated or imported reference material owned by the builders.

## How It Is Built

`run.py` is the main build entry point. It runs the original ATT&CK/D3FEND build through `legacy_build.py`, applies local compatibility patches, then runs modular source builders from `builds/`.

- `run.py` is the entry point.
- Existing build logic is preserved as `legacy_build.py` and patched before execution.
- MITRE tool pages use name-first filenames, for example `xcmd.md`.
- MITRE tool links display name and ATT&CK software id, for example `[[xcmd|xCmd (S0123)]]`.
- The analyst-owned folder is now `workspaces/` instead of `notes/`.
- MITRE CAR analytics are generated from the upstream CAR YAML source.
- Sigma rules are generated from the upstream SigmaHQ rule repository.
- Atomic Red Team validation tests are generated from the upstream atomic-red-team repository.
- LOLBAS entries are generated from the upstream LOLBAS YAML repository.
- ATT&CK technique pages are enriched after source builders run, so generated cross-links can point to CAR, Sigma, Atomic, and future sources.
- The patch validates `legacy_build.py` before executing it.

Generated source folders live under `secopskb/kb/<source>/`. Each source should have an `index.md` that explains what the upstream framework or project is, links to it, summarizes what was imported, and explains how that source relates to the rest of the vault.

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

- `BUILD_CAR`, `BUILD_ATOMIC`, `BUILD_SIGMA`, and `BUILD_LOLBAS` enable or disable generated sections.
- `SIGMA_LEVELS` defaults to `["critical", "high"]` to keep the vault lean.
- `LOLBAS_CATEGORIES` and `LOLBAS_FUNCTIONS` can narrow LOLBAS generation when needed.
- Empty filter lists mean include everything for that dimension.

## Continuing the build

Use `data-source-integration-plan.md` as the build queue and design record. For each new source:

1. Add build flags and filters to `utils/config.py`.
2. Add one builder under `builds/`.
3. Generate into a dedicated `secopskb/kb/<source>/` folder.
4. Wire the builder in `run.py`.
5. Add comparison ignores for the generated folder.
6. Add a source `index.md` description with the upstream project link, imported content scope, and relationship to ATT&CK/tools/detections/validation.
7. Run the builder standalone before running the full build.
8. Run syntax checks and a fenced-code-aware wikilink check.
9. Update this README, `BUILD_STATUS.md`, and the integration plan with counts, filters, and next-build notes.

Keep imported tradecraft sources such as PayloadsAllTheThings, InternalAllTheThings, and The Hacker Recipes in their own folders. ATT&CK technique pages should receive compact generated summary sections and links, not full copied source pages.

## Important cleanup before running v4

If you already ran v2 or v3, remove the old partially patched file first:

```bash
rm -f legacy_build.py
```

This forces a clean download and patch.

v4 should also repair a stale half-patched `legacy_build.py`, but starting clean is better.
