---
sigma_id: "970007b7-ce32-49d0-a4a4-fbef016950bd"
title: "Potential Configuration And Service Reconnaissance Via Reg.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_query_registry.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_query_registry.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "970007b7-ce32-49d0-a4a4-fbef016950bd"
  - "Potential Configuration And Service Reconnaissance Via Reg.EXE"
attack_technique_ids:
  - "T1012"
  - "T1007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Configuration And Service Reconnaissance Via Reg.EXE

Detects the usage of "reg.exe" in order to query reconnaissance information from the registry. Adversaries may interact with the Windows registry to gather information about credentials, the system, configuration, and installed software.

## Metadata

- Rule ID: 970007b7-ce32-49d0-a4a4-fbef016950bd
- Status: test
- Level: medium
- Author: Timur Zinniatullin, oscd.community
- Date: 2019-10-21
- Modified: 2023-02-05
- Source Path: rules/windows/process_creation/proc_creation_win_reg_query_registry.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1012-query_registry|T1012]]
- [[kb/attack/techniques/T1007-system_service_discovery|T1007]]

## Detection

```yaml
selection_img:
- Image|endswith: \reg.exe
- OriginalFileName: reg.exe
selection_flag:
  CommandLine|contains: query
selection_key:
  CommandLine|contains:
  - currentVersion\windows
  - winlogon\
  - currentVersion\shellServiceObjectDelayLoad
  - currentVersion\run
  - currentVersion\policies\explorer\run
  - currentcontrolset\services
condition: all of selection_*
```

## False Positives

- Discord

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1012/T1012.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_query_registry.yml)
