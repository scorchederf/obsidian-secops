---
sigma_id: "6bba49bf-7f8c-47d6-a1bb-6b4dece4640e"
title: "Suspicious RASdial Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rasdial_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rasdial_execution.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "6bba49bf-7f8c-47d6-a1bb-6b4dece4640e"
  - "Suspicious RASdial Activity"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious RASdial Activity

Detects suspicious process related to rasdial.exe

## Metadata

- Rule ID: 6bba49bf-7f8c-47d6-a1bb-6b4dece4640e
- Status: test
- Level: medium
- Author: juju4
- Date: 2019-01-16
- Modified: 2021-11-27
- Source Path: rules/windows/process_creation/proc_creation_win_rasdial_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection:
  Image|endswith: rasdial.exe
condition: selection
```

## False Positives

- False positives depend on scripts and administrative tools used in the monitored environment

## References

- https://twitter.com/subTee/status/891298217907830785

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rasdial_execution.yml)
