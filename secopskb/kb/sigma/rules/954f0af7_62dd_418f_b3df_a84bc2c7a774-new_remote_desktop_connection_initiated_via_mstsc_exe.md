---
sigma_id: "954f0af7-62dd-418f-b3df-a84bc2c7a774"
title: "New Remote Desktop Connection Initiated Via Mstsc.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mstsc_remote_connection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mstsc_remote_connection.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "954f0af7-62dd-418f-b3df-a84bc2c7a774"
  - "New Remote Desktop Connection Initiated Via Mstsc.EXE"
attack_technique_ids:
  - "T1021.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Remote Desktop Connection Initiated Via Mstsc.EXE

Detects the usage of "mstsc.exe" with the "/v" flag to initiate a connection to a remote server.
Adversaries may use valid accounts to log into a computer using the Remote Desktop Protocol (RDP). The adversary may then perform actions as the logged-on user.

## Metadata

- Rule ID: 954f0af7-62dd-418f-b3df-a84bc2c7a774
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-07
- Modified: 2024-06-04
- Source Path: rules/windows/process_creation/proc_creation_win_mstsc_remote_connection.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.001]]

## Detection

```yaml
selection_img:
- Image|endswith: \mstsc.exe
- OriginalFileName: mstsc.exe
selection_cli:
  CommandLine|contains|windash: ' /v:'
filter_optional_wsl:
  ParentImage: C:\Windows\System32\lxss\wslhost.exe
  CommandLine|contains: C:\ProgramData\Microsoft\WSL\wslg.rdp
condition: all of selection_* and not 1 of filter_optional_*
```

## False Positives

- WSL (Windows Sub System For Linux)

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1021.001/T1021.001.md#t1021001---remote-desktop-protocol
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/mstsc

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mstsc_remote_connection.yml)
