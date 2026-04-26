# Build Status

Last stabilization pass: 2026-04-26

## Current Generated Sources

- ATT&CK: 14 tactics, 691 techniques
- Tools: 91 tools
- D3FEND: 271 techniques
- CAR: 102 analytics
- Sigma: 1,484 rules generated from filtered high/critical rules
- Atomic Red Team: 1,790 tests
- ATT&CK technique enrichment: 169 technique pages with generated Detection & Validation sections

## Current Filters

Filters live in `utils/config.py`.

- `BUILD_CAR = True`
- `BUILD_ATOMIC = True`
- `BUILD_SIGMA = True`
- `SIGMA_LEVELS = ["critical", "high"]`
- `SIGMA_PRODUCTS = []`
- `SIGMA_STATUSES = []`
- `ATOMIC_PLATFORMS = []`
- `ATOMIC_EXECUTORS = []`

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

1. LOLBAS under `kb/lolbas/`
2. GTFOBins under `kb/gtfobins/`
3. PayloadsAllTheThings under `kb/payloads/`
4. InternalAllTheThings under `kb/internal/`
5. The Hacker Recipes under `kb/recipes/`
6. Splunk Security Content under `kb/splunk/`
7. Elastic Detection Rules under `kb/elastic/`

See `data-source-integration-plan.md` for the design rules and continuation checklist.
