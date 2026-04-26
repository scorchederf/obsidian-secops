---
sigma_id: "737e618a-a410-49b5-bec3-9e55ff7fbc15"
title: "Suspicious Calculator Usage"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_calc_uncommon_exec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_calc_uncommon_exec.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "737e618a-a410-49b5-bec3-9e55ff7fbc15"
  - "Suspicious Calculator Usage"
attack_technique_ids:
  - "T1036"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Calculator Usage

Detects suspicious use of 'calc.exe' with command line parameters or in a suspicious directory, which is likely caused by some PoC or detection evasion.

## Metadata

- Rule ID: 737e618a-a410-49b5-bec3-9e55ff7fbc15
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2019-02-09
- Modified: 2023-11-09
- Source Path: rules/windows/process_creation/proc_creation_win_calc_uncommon_exec.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]

## Detection

```yaml
selection_1:
  CommandLine|contains: '\calc.exe '
selection_2:
  Image|endswith: \calc.exe
filter_main_known_locations:
  Image|contains:
  - :\Windows\System32\
  - :\Windows\SysWOW64\
  - :\Windows\WinSxS\
condition: selection_1 or ( selection_2 and not filter_main_known_locations )
```

## False Positives

- Unknown

## References

- https://twitter.com/ItsReallyNick/status/1094080242686312448

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_calc_uncommon_exec.yml)
