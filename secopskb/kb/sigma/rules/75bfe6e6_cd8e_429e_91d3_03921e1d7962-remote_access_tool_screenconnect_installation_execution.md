---
sigma_id: "75bfe6e6-cd8e-429e-91d3-03921e1d7962"
title: "Remote Access Tool - ScreenConnect Installation Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_remote_access_tools_screenconnect_installation_cli_param.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_screenconnect_installation_cli_param.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "75bfe6e6-cd8e-429e-91d3-03921e1d7962"
  - "Remote Access Tool - ScreenConnect Installation Execution"
attack_technique_ids:
  - "T1133"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Access Tool - ScreenConnect Installation Execution

Detects ScreenConnect program starts that establish a remote access to a system.

## Metadata

- Rule ID: 75bfe6e6-cd8e-429e-91d3-03921e1d7962
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2021-02-11
- Modified: 2024-02-26
- Source Path: rules/windows/process_creation/proc_creation_win_remote_access_tools_screenconnect_installation_cli_param.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1133-external_remote_services|T1133]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - e=Access&
  - y=Guest&
  - '&p='
  - '&c='
  - '&k='
condition: selection
```

## False Positives

- Legitimate use by administrative staff

## References

- https://www.anomali.com/blog/probable-iranian-cyber-actors-static-kitten-conducting-cyberespionage-campaign-targeting-uae-and-kuwait-government-agencies

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_screenconnect_installation_cli_param.yml)
