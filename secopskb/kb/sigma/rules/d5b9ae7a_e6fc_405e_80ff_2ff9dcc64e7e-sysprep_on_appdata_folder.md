---
sigma_id: "d5b9ae7a-e6fc-405e-80ff-2ff9dcc64e7e"
title: "Sysprep on AppData Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sysprep_appdata.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysprep_appdata.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "d5b9ae7a-e6fc-405e-80ff-2ff9dcc64e7e"
  - "Sysprep on AppData Folder"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Sysprep on AppData Folder

Detects suspicious sysprep process start with AppData folder as target (as used by Trojan Syndicasec in Thrip report by Symantec)

## Metadata

- Rule ID: d5b9ae7a-e6fc-405e-80ff-2ff9dcc64e7e
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2018-06-22
- Modified: 2021-11-27
- Source Path: rules/windows/process_creation/proc_creation_win_sysprep_appdata.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection:
  Image|endswith: \sysprep.exe
  CommandLine|contains: \AppData\
condition: selection
```

## False Positives

- False positives depend on scripts and administrative tools used in the monitored environment

## References

- https://www.symantec.com/blogs/threat-intelligence/thrip-hits-satellite-telecoms-defense-targets
- https://app.any.run/tasks/61a296bb-81ad-4fee-955f-3b399f4aaf4b

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysprep_appdata.yml)
