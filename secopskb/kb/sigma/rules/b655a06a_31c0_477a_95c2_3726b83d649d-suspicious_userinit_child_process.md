---
sigma_id: "b655a06a-31c0-477a-95c2-3726b83d649d"
title: "Suspicious Userinit Child Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_userinit_child.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_userinit_child.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "b655a06a-31c0-477a-95c2-3726b83d649d"
  - "Suspicious Userinit Child Process"
attack_technique_ids:
  - "T1055"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Userinit Child Process

Detects a suspicious child process of userinit

## Metadata

- Rule ID: b655a06a-31c0-477a-95c2-3726b83d649d
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Samir Bousseaden (idea)
- Date: 2019-06-17
- Modified: 2025-10-17
- Source Path: rules/windows/process_creation/proc_creation_win_susp_userinit_child.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055]]

## Detection

```yaml
selection:
  ParentImage|endswith: \userinit.exe
filter_main_netlogon:
  CommandLine|contains: \netlogon\
filter_main_explorer:
- Image|endswith: \explorer.exe
- OriginalFileName: explorer.exe
- CommandLine: C:\Windows\Explorer.EXE
filter_main_null:
  Image: null
condition: selection and not 1 of filter_main_*
```

## False Positives

- Administrative scripts

## References

- https://twitter.com/SBousseaden/status/1139811587760562176

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_userinit_child.yml)
