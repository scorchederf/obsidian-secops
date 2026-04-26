---
sigma_id: "e9b61244-893f-427c-b287-3e708f321c6b"
title: "Potential Privilege Escalation Using Symlink Between Osk and Cmd"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_mklink_osk_cmd.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_mklink_osk_cmd.yml"
build_date: "2026-04-26 15:01:49"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e9b61244-893f-427c-b287-3e708f321c6b"
  - "Potential Privilege Escalation Using Symlink Between Osk and Cmd"
attack_technique_ids:
  - "T1546.008"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Privilege Escalation Using Symlink Between Osk and Cmd

Detects the creation of a symbolic link between "cmd.exe" and the accessibility on-screen keyboard binary (osk.exe) using "mklink". This technique provides an elevated command prompt to the user from the login screen without the need to log in.

## Metadata

- Rule ID: e9b61244-893f-427c-b287-3e708f321c6b
- Status: test
- Level: high
- Author: frack113
- Date: 2022-12-11
- Modified: 2022-12-20
- Source Path: rules/windows/process_creation/proc_creation_win_cmd_mklink_osk_cmd.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.008]]

## Detection

```yaml
selection_img:
- Image|endswith: \cmd.exe
- OriginalFileName: Cmd.Exe
selection_cli:
  CommandLine|contains|all:
  - mklink
  - \osk.exe
  - \cmd.exe
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/5c1e6f1b4fafd01c8d1ece85f510160fc1275fbf/atomics/T1546.008/T1546.008.md
- https://ss64.com/nt/mklink.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_mklink_osk_cmd.yml)
