---
sigma_id: "ab70c354-d9ac-4e11-bbb6-ec8e3b153357"
title: "Remote Access Tool - Team Viewer Session Started On Windows Host"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_remote_access_tools_teamviewer_incoming_connection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_teamviewer_incoming_connection.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "ab70c354-d9ac-4e11-bbb6-ec8e3b153357"
  - "Remote Access Tool - Team Viewer Session Started On Windows Host"
attack_technique_ids:
  - "T1133"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Access Tool - Team Viewer Session Started On Windows Host

Detects the command line executed when TeamViewer starts a session started by a remote host.
Once a connection has been started, an investigator can verify the connection details by viewing the "incoming_connections.txt" log file in the TeamViewer folder.

## Metadata

- Rule ID: ab70c354-d9ac-4e11-bbb6-ec8e3b153357
- Status: test
- Level: low
- Author: Josh Nickels, Qi Nan
- Date: 2024-03-11
- Source Path: rules/windows/process_creation/proc_creation_win_remote_access_tools_teamviewer_incoming_connection.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1133-external_remote_services|T1133]]

## Detection

```yaml
selection:
  Image: TeamViewer_Desktop.exe
  ParentImage: TeamViewer_Service.exe
  CommandLine|endswith: TeamViewer_Desktop.exe --IPCport 5939 --Module 1
condition: selection
```

## False Positives

- Legitimate usage of TeamViewer

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_teamviewer_incoming_connection.yml)
