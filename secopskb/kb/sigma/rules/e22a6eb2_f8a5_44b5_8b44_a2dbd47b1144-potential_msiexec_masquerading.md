---
sigma_id: "e22a6eb2-f8a5-44b5-8b44-a2dbd47b1144"
title: "Potential MsiExec Masquerading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_msiexec_masquerading.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msiexec_masquerading.yml"
build_date: "2026-04-26 15:01:48"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e22a6eb2-f8a5-44b5-8b44-a2dbd47b1144"
  - "Potential MsiExec Masquerading"
attack_technique_ids:
  - "T1036.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential MsiExec Masquerading

Detects the execution of msiexec.exe from an uncommon directory

## Metadata

- Rule ID: e22a6eb2-f8a5-44b5-8b44-a2dbd47b1144
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2019-11-14
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_msiexec_masquerading.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.005]]

## Detection

```yaml
selection:
- Image|endswith: \msiexec.exe
- OriginalFileName: \msiexec.exe
filter:
  Image|startswith:
  - C:\Windows\System32\
  - C:\Windows\SysWOW64\
  - C:\Windows\WinSxS\
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://twitter.com/200_okay_/status/1194765831911215104

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msiexec_masquerading.yml)
