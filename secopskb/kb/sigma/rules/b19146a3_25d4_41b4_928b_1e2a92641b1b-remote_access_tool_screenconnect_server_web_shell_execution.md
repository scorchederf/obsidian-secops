---
sigma_id: "b19146a3-25d4-41b4-928b-1e2a92641b1b"
title: "Remote Access Tool - ScreenConnect Server Web Shell Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_remote_access_tools_screenconnect_webshell.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_screenconnect_webshell.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "b19146a3-25d4-41b4-928b-1e2a92641b1b"
  - "Remote Access Tool - ScreenConnect Server Web Shell Execution"
attack_technique_ids:
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Remote Access Tool - ScreenConnect Server Web Shell Execution

Detects potential web shell execution from the ScreenConnect server process.

## Metadata

- Rule ID: b19146a3-25d4-41b4-928b-1e2a92641b1b
- Status: test
- Level: high
- Author: Jason Rathbun (Blackpoint Cyber)
- Date: 2024-02-26
- Source Path: rules/windows/process_creation/proc_creation_win_remote_access_tools_screenconnect_webshell.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]

## Detection

```yaml
selection:
  ParentImage|endswith: \ScreenConnect.Service.exe
  Image|endswith:
  - \cmd.exe
  - \csc.exe
condition: selection
```

## False Positives

- Unlikely

## References

- https://blackpointcyber.com/resources/blog/breaking-through-the-screen/
- https://www.connectwise.com/company/trust/security-bulletins/connectwise-screenconnect-23.9.8

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_screenconnect_webshell.yml)
