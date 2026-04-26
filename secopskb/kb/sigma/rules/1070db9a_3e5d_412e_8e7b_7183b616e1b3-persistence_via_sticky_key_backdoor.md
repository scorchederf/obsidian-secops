---
sigma_id: "1070db9a-3e5d-412e-8e7b-7183b616e1b3"
title: "Persistence Via Sticky Key Backdoor"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_sticky_keys_replace.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_sticky_keys_replace.yml"
build_date: "2026-04-26 15:01:47"
status: "test"
level: "critical"
logsource: "windows / process_creation"
aliases:
  - "1070db9a-3e5d-412e-8e7b-7183b616e1b3"
  - "Persistence Via Sticky Key Backdoor"
attack_technique_ids:
  - "T1546.008"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Persistence Via Sticky Key Backdoor

By replacing the sticky keys executable with the local admins CMD executable, an attacker is able to access a privileged windows console session without authenticating to the system.
When the sticky keys are "activated" the privilleged shell is launched.

## Metadata

- Rule ID: 1070db9a-3e5d-412e-8e7b-7183b616e1b3
- Status: test
- Level: critical
- Author: Sreeman
- Date: 2020-02-18
- Modified: 2023-03-07
- Source Path: rules/windows/process_creation/proc_creation_win_cmd_sticky_keys_replace.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.008]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - 'copy '
  - '/y '
  - C:\windows\system32\cmd.exe C:\windows\system32\sethc.exe
condition: selection
```

## False Positives

- Unlikely

## References

- https://www.fireeye.com/blog/threat-research/2017/03/apt29_domain_frontin.html
- https://www.clearskysec.com/wp-content/uploads/2020/02/ClearSky-Fox-Kitten-Campaign-v1.pdf
- https://learn.microsoft.com/en-us/archive/blogs/jonathantrull/detecting-sticky-key-backdoors

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_sticky_keys_replace.yml)
