---
sigma_id: "37db85d1-b089-490a-a59a-c7b6f984f480"
title: "Sysmon Discovery Via Default Driver Altitude Using Findstr.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_findstr_sysmon_discovery_via_default_altitude.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_findstr_sysmon_discovery_via_default_altitude.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "37db85d1-b089-490a-a59a-c7b6f984f480"
  - "Sysmon Discovery Via Default Driver Altitude Using Findstr.EXE"
attack_technique_ids:
  - "T1518.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Sysmon Discovery Via Default Driver Altitude Using Findstr.EXE

Detects usage of "findstr" with the argument "385201". Which could indicate potential discovery of an installed Sysinternals Sysmon service using the default driver altitude (even if the name is changed).

## Metadata

- Rule ID: 37db85d1-b089-490a-a59a-c7b6f984f480
- Status: test
- Level: high
- Author: frack113
- Date: 2021-12-16
- Modified: 2023-11-14
- Source Path: rules/windows/process_creation/proc_creation_win_findstr_sysmon_discovery_via_default_altitude.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1518-software_discovery|T1518.001]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \find.exe
  - \findstr.exe
- OriginalFileName:
  - FIND.EXE
  - FINDSTR.EXE
selection_cli:
  CommandLine|contains: ' 385201'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1518.001/T1518.001.md#atomic-test-5---security-software-discovery---sysmon-service

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_findstr_sysmon_discovery_via_default_altitude.yml)
