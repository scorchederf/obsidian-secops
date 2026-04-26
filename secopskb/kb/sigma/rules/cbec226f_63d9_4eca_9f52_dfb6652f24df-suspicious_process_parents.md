---
sigma_id: "cbec226f-63d9-4eca-9f52-dfb6652f24df"
title: "Suspicious Process Parents"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_parents.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_parents.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "cbec226f-63d9-4eca-9f52-dfb6652f24df"
  - "Suspicious Process Parents"
attack_technique_ids:
  - "T1036"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Process Parents

Detects suspicious parent processes that should not have any children or should only have a single possible child program

## Metadata

- Rule ID: cbec226f-63d9-4eca-9f52-dfb6652f24df
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-03-21
- Modified: 2022-09-08
- Source Path: rules/windows/process_creation/proc_creation_win_susp_parents.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]

## Detection

```yaml
selection:
  ParentImage|endswith:
  - \minesweeper.exe
  - \winver.exe
  - \bitsadmin.exe
selection_special:
  ParentImage|endswith:
  - \csrss.exe
  - \certutil.exe
  - \eventvwr.exe
  - \calc.exe
  - \notepad.exe
filter_special:
  Image|endswith:
  - \WerFault.exe
  - \wermgr.exe
  - \conhost.exe
  - \mmc.exe
  - \win32calc.exe
  - \notepad.exe
filter_null:
  Image: null
condition: selection or ( selection_special and not 1 of filter_* )
```

## False Positives

- Unknown

## References

- https://twitter.com/x86matthew/status/1505476263464607744?s=12
- https://svch0st.medium.com/stats-from-hunting-cobalt-strike-beacons-c17e56255f9b

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_parents.yml)
