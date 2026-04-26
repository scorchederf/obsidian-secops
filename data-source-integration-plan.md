# Data Source Integration Plan

## Relationship Model

The vault should keep ATT&CK as the primary behavior spine. Other sources should attach to ATT&CK techniques, tools, data sources, platforms, or validation workflows instead of becoming isolated content islands.

- ATT&CK: behavior taxonomy and primary navigation axis.
- CAR: analytic rationale and implementations mapped to ATT&CK.
- Sigma: portable detection rules mapped to ATT&CK, logsource, product, and service.
- Atomic Red Team: executable validation tests mapped to ATT&CK.
- LOLBAS and GTFOBins: abused legitimate binaries mapped to ATT&CK and linked to tools, commands, and Sigma/CAR detections.
- Splunk Security Content and Elastic Detection Rules: vendor-specific detection-as-code mapped to ATT&CK, data sources, and analytic stories.
- Security Datasets: replayable evidence linked to ATT&CK, Sigma, Splunk, Elastic, and CAR validations.
- Malware Behavior Catalog: malware-analysis behavior taxonomy linked to ATT&CK techniques and software pages.
- PayloadsAllTheThings: web exploitation payload and bypass knowledge linked to web-facing ATT&CK techniques, CVEs, CWEs, and defensive detections.
- InternalAllTheThings: internal pentest and Active Directory/cloud tradecraft linked to ATT&CK techniques, tools, and detection/validation content.
- MITRE Engage: deception/denial/adversary engagement objectives linked to ATT&CK techniques and D3FEND defensive techniques.

## Target Vault Areas

- `kb/tools/`: Tools. Keep this top-level folder stable even though the records are ATT&CK software objects, because Sigma, LOLBAS, GTFOBins, and future sources need to reference it as a shared entity index.
- `kb/sigma/`: Sigma rules, indexes by ATT&CK technique and logsource.
- `kb/atomic/`: Atomic Red Team tests, indexes by ATT&CK technique, executor, platform, and dependency.
- `kb/lolbas/`: Windows living-off-the-land binaries, scripts, and libraries.
- `kb/gtfobins/`: Unix living-off-the-land binaries.
- `kb/splunk/`: Splunk analytic stories, detections, data sources, and playbooks.
- `kb/elastic/`: Elastic detection rules and hunting queries.
- `kb/datasets/`: Security Datasets/Mordor event datasets and replay notes.
- `kb/mbc/`: Malware Behavior Catalog objectives and behaviors.
- `kb/payloads/`: PayloadsAllTheThings web payload and bypass notes.
- `kb/internal/`: InternalAllTheThings internal pentest, AD, cloud, and red-team notes.
- `kb/engage/`: MITRE Engage activities and approaches.

## Cross-Link Rules

- Any source with an ATT&CK technique ID links to `kb/attack/techniques`.
- Any source with an ATT&CK software/tool ID links to `kb/tools` where available. Do not merge LOLBAS/GTFOBins into `kb/tools`; cross-link overlapping binaries instead.
- Any source with a D3FEND ID links to `kb/defend/techniques`.
- Detection sources link to relevant data sources and logsource indexes.
- Validation sources link back to the detections they can exercise.
- Payload/tradecraft sources link to detections and tests when a stable technique or tool match exists.

## Implementation Order

1. SigmaHQ Sigma
   - Parse `rules/**/*.yml`.
   - Generate rule pages with metadata, logsource, ATT&CK tags, detection YAML, fields, false positives, references, and simulation metadata.
   - Build indexes by rule, ATT&CK technique, and logsource.

2. Atomic Red Team
   - Parse `atomics/T*/T*.yaml`.
   - Generate test pages and technique indexes.
   - Link tests to Sigma simulation blocks where `atomic_guid` matches.
   - Status: implemented in `kb/atomic/`, with Sigma simulation links resolved to Atomic test pages when GUIDs match.
   - Next build note: map Atomic executor names to markdown code fence languages for commands and cleanup blocks. For example, `powershell` should render as ```powershell, `command_prompt` as ```batch or ```cmd, and `bash`/`sh` as ```bash.

3. LOLBAS and GTFOBins
   - Parse project YAML/Markdown data.
   - Generate binary pages with functions, commands, ATT&CK mappings, and detection references.

4. PayloadsAllTheThings and InternalAllTheThings
   - Import Markdown chapters as curated technique/payload notes.
   - Build topic indexes and best-effort ATT&CK/CWE/CVE links.
   - Keep exploit payload content clearly separated from detection and validation content.

5. Splunk Security Content and Elastic Detection Rules
   - Parse detection YAML/TOML.
   - Link to ATT&CK, logsource/data source, Sigma equivalents, and datasets.

6. Security Datasets
   - Generate dataset pages with platform, telemetry, ATT&CK tags, and source links.
   - Link datasets to detections and Atomic tests where possible.

7. Malware Behavior Catalog and MITRE Engage
   - Import behavior/deception taxonomies.
   - Link MBC to malware/software analysis and Engage to defensive planning paths.

## Safety Notes

PayloadsAllTheThings and InternalAllTheThings contain offensive payloads and tradecraft. Keep them under clearly named `kb/payloads` and `kb/internal` areas, preserve upstream disclaimers, and link them to detection/defense content instead of presenting them as operational runbooks.
