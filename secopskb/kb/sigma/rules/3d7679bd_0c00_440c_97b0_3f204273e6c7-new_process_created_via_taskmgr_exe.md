---
sigma_id: "3d7679bd-0c00-440c-97b0-3f204273e6c7"
title: "New Process Created Via Taskmgr.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_taskmgr_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_taskmgr_susp_child_process.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "3d7679bd-0c00-440c-97b0-3f204273e6c7"
  - "New Process Created Via Taskmgr.EXE"
attack_technique_ids:
  - "T1036"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Process Created Via Taskmgr.EXE

Detects the creation of a process via the Windows task manager. This might be an attempt to bypass UAC

## Metadata

- Rule ID: 3d7679bd-0c00-440c-97b0-3f204273e6c7
- Status: test
- Level: low
- Author: Florian Roth (Nextron Systems)
- Date: 2018-03-13
- Modified: 2024-01-18
- Source Path: rules/windows/process_creation/proc_creation_win_taskmgr_susp_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]

## Detection

```yaml
selection:
  ParentImage|endswith: \taskmgr.exe
filter_main_generic:
  Image|endswith:
  - :\Windows\System32\mmc.exe
  - :\Windows\System32\resmon.exe
  - :\Windows\System32\Taskmgr.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Administrative activity

## References

- https://twitter.com/ReneFreingruber/status/1172244989335810049

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_taskmgr_susp_child_process.yml)
