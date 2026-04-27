---
sigma_id: "be344333-921d-4c4d-8bb8-e584cf584780"
title: "Potentially Suspicious Event Viewer Child Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_eventvwr_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_eventvwr_susp_child_process.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "be344333-921d-4c4d-8bb8-e584cf584780"
  - "Potentially Suspicious Event Viewer Child Process"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects uncommon or suspicious child processes of "eventvwr.exe" which might indicate a UAC bypass attempt

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]

## Detection

```yaml
selection:
  ParentImage|endswith: \eventvwr.exe
filter_main_generic:
  Image|endswith:
  - :\Windows\System32\mmc.exe
  - :\Windows\System32\WerFault.exe
  - :\Windows\SysWOW64\WerFault.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://enigma0x3.net/2016/08/15/fileless-uac-bypass-using-eventvwr-exe-and-registry-hijacking/
- https://www.hybrid-analysis.com/sample/e122bc8bf291f15cab182a5d2d27b8db1e7019e4e96bb5cdbd1dfe7446f3f51f?environmentId=100

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_eventvwr_susp_child_process.yml)
