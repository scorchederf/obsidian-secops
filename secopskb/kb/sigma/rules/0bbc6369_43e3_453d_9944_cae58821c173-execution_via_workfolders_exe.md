---
sigma_id: "0bbc6369-43e3-453d-9944-cae58821c173"
title: "Execution via WorkFolders.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_workfolders.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_workfolders.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "0bbc6369-43e3-453d-9944-cae58821c173"
  - "Execution via WorkFolders.exe"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects using WorkFolders.exe to execute an arbitrary control.exe

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detection

```yaml
selection:
  Image|endswith: \control.exe
  ParentImage|endswith: \WorkFolders.exe
filter:
  Image: C:\Windows\System32\control.exe
condition: selection and not filter
```

## False Positives

- Legitimate usage of the uncommon Windows Work Folders feature.

## References

- https://twitter.com/elliotkillick/status/1449812843772227588

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_workfolders.yml)
