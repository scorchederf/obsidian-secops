---
sigma_id: "114e7f1c-f137-48c8-8f54-3088c24ce4b9"
title: "Remote Access Tool - AnyDesk Silent Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_remote_access_tools_anydesk_silent_install.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_anydesk_silent_install.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "114e7f1c-f137-48c8-8f54-3088c24ce4b9"
  - "Remote Access Tool - AnyDesk Silent Installation"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Access Tool - AnyDesk Silent Installation

Detects AnyDesk Remote Desktop silent installation. Which can be used by attackers to gain remote access.

## Metadata

- Rule ID: 114e7f1c-f137-48c8-8f54-3088c24ce4b9
- Status: test
- Level: high
- Author: Ján Trenčanský
- Date: 2021-08-06
- Modified: 2023-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_remote_access_tools_anydesk_silent_install.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - --install
  - --start-with-win
  - --silent
condition: selection
```

## False Positives

- Legitimate deployment of AnyDesk

## References

- https://twitter.com/TheDFIRReport/status/1423361119926816776?s=20
- https://support.anydesk.com/Automatic_Deployment

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_anydesk_silent_install.yml)
