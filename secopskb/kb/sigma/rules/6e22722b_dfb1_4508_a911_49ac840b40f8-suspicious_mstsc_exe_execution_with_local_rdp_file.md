---
sigma_id: "6e22722b-dfb1-4508-a911-49ac840b40f8"
title: "Suspicious Mstsc.EXE Execution With Local RDP File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mstsc_run_local_rdp_file_susp_location.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mstsc_run_local_rdp_file_susp_location.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "6e22722b-dfb1-4508-a911-49ac840b40f8"
  - "Suspicious Mstsc.EXE Execution With Local RDP File"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Mstsc.EXE Execution With Local RDP File

Detects potential RDP connection via Mstsc using a local ".rdp" file located in suspicious locations.

## Metadata

- Rule ID: 6e22722b-dfb1-4508-a911-49ac840b40f8
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-04-18
- Source Path: rules/windows/process_creation/proc_creation_win_mstsc_run_local_rdp_file_susp_location.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]

## Detection

```yaml
selection_img:
- Image|endswith: \mstsc.exe
- OriginalFileName: mstsc.exe
selection_extension:
  CommandLine|endswith:
  - .rdp
  - .rdp"
selection_paths:
  CommandLine|contains:
  - :\Users\Public\
  - :\Windows\System32\spool\drivers\color
  - ':\Windows\System32\Tasks_Migrated '
  - :\Windows\Tasks\
  - :\Windows\Temp\
  - :\Windows\Tracing\
  - \AppData\Local\Temp\
  - \Downloads\
condition: all of selection_*
```

## False Positives

- Likelihood is related to how often the paths are used in the environment

## References

- https://www.blackhillsinfosec.com/rogue-rdp-revisiting-initial-access-methods/
- https://web.archive.org/web/20230726144748/https://blog.thickmints.dev/mintsights/detecting-rogue-rdp/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mstsc_run_local_rdp_file_susp_location.yml)
