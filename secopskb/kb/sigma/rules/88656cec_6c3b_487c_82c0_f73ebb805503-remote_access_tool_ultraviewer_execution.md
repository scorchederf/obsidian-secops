---
sigma_id: "88656cec-6c3b-487c-82c0-f73ebb805503"
title: "Remote Access Tool - UltraViewer Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_remote_access_tools_ultraviewer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_ultraviewer.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "88656cec-6c3b-487c-82c0-f73ebb805503"
  - "Remote Access Tool - UltraViewer Execution"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Access Tool - UltraViewer Execution

An adversary may use legitimate desktop support and remote access software, such as Team Viewer, Go2Assist, LogMein, AmmyyAdmin, etc, to establish an interactive command and control channel to target systems within networks.
These services are commonly used as legitimate technical support software, and may be allowed by application control within a target environment.
Remote access tools like VNC, Ammyy, and Teamviewer are used frequently when compared with other legitimate software commonly used by adversaries. (Citation: Symantec Living off the Land)

## Metadata

- Rule ID: 88656cec-6c3b-487c-82c0-f73ebb805503
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-09-25
- Modified: 2024-03-14
- Source Path: rules/windows/process_creation/proc_creation_win_remote_access_tools_ultraviewer.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]

## Detection

```yaml
selection:
- Product: UltraViewer
- Company: DucFabulous Co,ltd
- OriginalFileName: UltraViewer_Desktop.exe
condition: selection
```

## False Positives

- Legitimate use

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1219/T1219.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_ultraviewer.yml)
