---
sigma_id: "bd1c6866-65fc-44b2-be51-5588fcff82b9"
title: "Renamed Msdt.EXE Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_msdt.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_msdt.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "bd1c6866-65fc-44b2-be51-5588fcff82b9"
  - "Renamed Msdt.EXE Execution"
attack_technique_ids:
  - "T1036.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Renamed Msdt.EXE Execution

Detects the execution of a renamed "Msdt.exe" binary

## Metadata

- Rule ID: bd1c6866-65fc-44b2-be51-5588fcff82b9
- Status: test
- Level: high
- Author: pH-T (Nextron Systems)
- Date: 2022-06-03
- Modified: 2023-02-03
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_msdt.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.003]]

## Detection

```yaml
selection:
  OriginalFileName: msdt.exe
filter:
  Image|endswith: \msdt.exe
condition: selection and not filter
```

## False Positives

- Unlikely

## References

- https://lolbas-project.github.io/lolbas/Binaries/Msdt/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_msdt.yml)
