---
sigma_id: "7dc2dedd-7603-461a-bc13-15803d132355"
title: "Uncommon Child Process Of Conhost.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_conhost_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_conhost_susp_child_process.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "7dc2dedd-7603-461a-bc13-15803d132355"
  - "Uncommon Child Process Of Conhost.EXE"
attack_technique_ids:
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Uncommon Child Process Of Conhost.EXE

Detects uncommon "conhost" child processes. This could be a sign of "conhost" usage as a LOLBIN or potential process injection activity.

## Metadata

- Rule ID: 7dc2dedd-7603-461a-bc13-15803d132355
- Status: test
- Level: medium
- Author: omkar72
- Date: 2020-10-25
- Modified: 2023-12-11
- Source Path: rules/windows/process_creation/proc_creation_win_conhost_susp_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection:
  ParentImage|endswith: \conhost.exe
filter_main_conhost:
  Image|endswith: :\Windows\System32\conhost.exe
filter_main_null:
  Image: null
filter_main_empty:
  Image: ''
filter_optional_provider:
  Provider_Name: SystemTraceProvider-Process
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- http://www.hexacorn.com/blog/2020/05/25/how-to-con-your-host/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_conhost_susp_child_process.yml)
