---
sigma_id: "a197e378-d31b-41c0-9635-cfdf1c1bb423"
title: "HackTool - WinRM Access Via Evil-WinRM"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_evil_winrm.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_evil_winrm.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "a197e378-d31b-41c0-9635-cfdf1c1bb423"
  - "HackTool - WinRM Access Via Evil-WinRM"
attack_technique_ids:
  - "T1021.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - WinRM Access Via Evil-WinRM

Adversaries may use Valid Accounts to log into a computer using the Remote Desktop Protocol (RDP). The adversary may then perform actions as the logged-on user.

## Metadata

- Rule ID: a197e378-d31b-41c0-9635-cfdf1c1bb423
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-07
- Modified: 2023-02-13
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_evil_winrm.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.006]]

## Detection

```yaml
selection:
  Image|endswith: \ruby.exe
  CommandLine|contains|all:
  - '-i '
  - '-u '
  - '-p '
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1021.006/T1021.006.md#atomic-test-3---winrm-access-with-evil-winrm
- https://github.com/Hackplayers/evil-winrm

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_evil_winrm.yml)
