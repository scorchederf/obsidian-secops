---
sigma_id: "1f6b8cd4-3e60-47cc-b282-5aa1cbc9182d"
title: "Remote Access Tool - Team Viewer Session Started On Linux Host"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_remote_access_tools_teamviewer_incoming_connection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_remote_access_tools_teamviewer_incoming_connection.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "low"
logsource: "linux / process_creation"
aliases:
  - "1f6b8cd4-3e60-47cc-b282-5aa1cbc9182d"
  - "Remote Access Tool - Team Viewer Session Started On Linux Host"
attack_technique_ids:
  - "T1133"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Access Tool - Team Viewer Session Started On Linux Host

Detects the command line executed when TeamViewer starts a session started by a remote host.
Once a connection has been started, an investigator can verify the connection details by viewing the "incoming_connections.txt" log file in the TeamViewer folder.

## Metadata

- Rule ID: 1f6b8cd4-3e60-47cc-b282-5aa1cbc9182d
- Status: test
- Level: low
- Author: Josh Nickels, Qi Nan
- Date: 2024-03-11
- Source Path: rules/linux/process_creation/proc_creation_lnx_remote_access_tools_teamviewer_incoming_connection.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1133-external_remote_services|T1133]]

## Detection

```yaml
selection:
  ParentImage|endswith: /TeamViewer_Service
  Image|endswith: /TeamViewer_Desktop
  CommandLine|endswith: /TeamViewer_Desktop --IPCport 5939 --Module 1
condition: selection
```

## False Positives

- Legitimate usage of TeamViewer

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_remote_access_tools_teamviewer_incoming_connection.yml)
