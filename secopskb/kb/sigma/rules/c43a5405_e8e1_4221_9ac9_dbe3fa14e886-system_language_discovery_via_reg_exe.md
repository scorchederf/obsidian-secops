---
sigma_id: "c43a5405-e8e1-4221-9ac9-dbe3fa14e886"
title: "System Language Discovery via Reg.Exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_system_language_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_system_language_discovery.yml"
build_date: "2026-04-26 14:14:37"
status: "experimental"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "c43a5405-e8e1-4221-9ac9-dbe3fa14e886"
  - "System Language Discovery via Reg.Exe"
attack_technique_ids:
  - "T1614.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# System Language Discovery via Reg.Exe

Detects the usage of Reg.Exe to query system language settings.
Attackers may discover the system language to determine the geographic location of victims, customize payloads for specific regions,
or avoid targeting certain locales to evade detection.

## Metadata

- Rule ID: c43a5405-e8e1-4221-9ac9-dbe3fa14e886
- Status: experimental
- Level: medium
- Author: Marco Pedrinazzi (@pedrinazziM) (InTheCyber)
- Date: 2026-01-09
- Source Path: rules/windows/process_creation/proc_creation_win_reg_system_language_discovery.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1614-system_location_discovery|T1614.001]]

## Detection

```yaml
selection_img:
- Image|endswith: \reg.exe
- OriginalFileName: reg.exe
selection_cli:
  CommandLine|contains|all:
  - query
  - Control\Nls\Language
condition: all of selection_*
```

## False Positives

- Unknown

## Simulation

### Discover System Language by Registry Query

- atomic_guid: 631d4cf1-42c9-4209-8fe9-6bd4de9421be
- name: Discover System Language by Registry Query
- technique: T1614.001
- type: atomic-red-team

## References

- https://scythe.io/threat-thursday/threatthursday-darkside-ransomware

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_system_language_discovery.yml)
