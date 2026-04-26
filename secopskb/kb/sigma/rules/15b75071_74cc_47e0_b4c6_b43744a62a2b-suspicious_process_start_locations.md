---
sigma_id: "15b75071-74cc-47e0-b4c6-b43744a62a2b"
title: "Suspicious Process Start Locations"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_run_locations.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_run_locations.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "15b75071-74cc-47e0-b4c6-b43744a62a2b"
  - "Suspicious Process Start Locations"
attack_technique_ids:
  - "T1036"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Process Start Locations

Detects suspicious process run from unusual locations

## Metadata

- Rule ID: 15b75071-74cc-47e0-b4c6-b43744a62a2b
- Status: test
- Level: medium
- Author: juju4, Jonhnathan Ribeiro, oscd.community
- Date: 2019-01-16
- Modified: 2022-01-07
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_run_locations.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]

## Detection

```yaml
selection:
- Image|contains:
  - :\RECYCLER\
  - :\SystemVolumeInformation\
- Image|startswith:
  - C:\Windows\Tasks\
  - C:\Windows\debug\
  - C:\Windows\fonts\
  - C:\Windows\help\
  - C:\Windows\drivers\
  - C:\Windows\addins\
  - C:\Windows\cursors\
  - C:\Windows\system32\tasks\
condition: selection
```

## False Positives

- False positives depend on scripts and administrative tools used in the monitored environment

## References

- https://car.mitre.org/wiki/CAR-2013-05-002

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_run_locations.yml)
