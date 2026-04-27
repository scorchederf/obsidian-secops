# Build Status

Last stabilization pass: 2026-04-27

## Current Generated Sources

- ATT&CK: 14 tactics, 691 techniques
- Tools: 91 tools
- D3FEND: 271 techniques
- CAR: 102 analytics
- Sigma: 1,484 rules generated from filtered high/critical rules
- Atomic Red Team: 1,790 tests
- LOLBAS: 236 entries
- ATT&CK technique enrichment: 169 technique pages with generated Detection & Validation sections

## Current Filters

Filters live in `utils/config.py`.

- `BUILD_CAR = True`
- `BUILD_ATOMIC = True`
- `BUILD_SIGMA = True`
- `BUILD_LOLBAS = True`
- `SIGMA_LEVELS = ["critical", "high"]`
- `SIGMA_PRODUCTS = []`
- `SIGMA_STATUSES = []`
- `ATOMIC_PLATFORMS = []`
- `ATOMIC_EXECUTORS = []`
- `LOLBAS_CATEGORIES = []`
- `LOLBAS_FUNCTIONS = []`

Empty filter lists mean include everything for that dimension.

## Stabilization Notes

- Atomic command and cleanup code fences now map executor names to useful markdown languages:
  - `powershell` -> `powershell`
  - `command_prompt` -> `cmd`
  - `bash` and `sh` -> `bash`
  - `manual` -> `text`
- The vault comparison normalizes generated Detection & Validation blocks so intentional technique enrichment does not dominate compare output.
- The vault comparison sorts simple `## Tools` bullet sections before comparing, which suppresses legacy tool-order-only mismatches.

## Known Issues

- `legacy_build.py` is still the large upstream-derived ATT&CK/D3FEND builder. Local wrapper patches keep it usable, but it remains brittle when upstream text changes.
- Generated markdown volume is significant. Keep new source builders filtered by default when the source is noisy.
- Tradecraft-heavy sources should stay in their own folders and link outward. Do not inline full offensive guides into ATT&CK technique pages.

## Next Source Queue

1. GTFOBins under `kb/gtfobins/`
2. PayloadsAllTheThings under `kb/payloads/`
3. InternalAllTheThings under `kb/internal/`
4. The Hacker Recipes under `kb/recipes/`
5. Splunk Security Content under `kb/splunk/`
6. Elastic Detection Rules under `kb/elastic/`

See `data-source-integration-plan.md` for the design rules and continuation checklist.

## Next Build Notes

- Add a short framework/source description to every generated source `index.md`. The index should explain what the framework is, what kind of records were imported, where the upstream project lives, and how this vault relates it to ATT&CK, tools, detections, or validation. For example, the Atomic Red Team index should describe Atomic Red Team, link to the upstream project, summarize that tests are mapped to ATT&CK techniques, and point to platform/executor/technique indexes.
