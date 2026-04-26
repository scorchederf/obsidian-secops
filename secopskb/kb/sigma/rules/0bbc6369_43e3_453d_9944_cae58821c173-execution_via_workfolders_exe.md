---
sigma_id: "0bbc6369-43e3-453d-9944-cae58821c173"
title: "Execution via WorkFolders.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_workfolders.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_workfolders.yml"
build_date: "2026-04-26 17:03:19"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Execution via WorkFolders.exe

Detects using WorkFolders.exe to execute an arbitrary control.exe

## Metadata

- Rule ID: 0bbc6369-43e3-453d-9944-cae58821c173
- Status: test
- Level: high
- Author: Maxime Thiebaut (@0xThiebaut)
- Date: 2021-10-21
- Modified: 2022-12-25
- Source Path: rules/windows/process_creation/proc_creation_win_susp_workfolders.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

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
