---
sigma_id: "2c4523d5-d481-4ed0-8ec3-7fbf0cb41a75"
title: "Driver Load From A Temporary Directory"
framework: "sigma"
generated: "true"
source_path: "rules/windows/driver_load/driver_load_win_susp_temp_use.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/driver_load/driver_load_win_susp_temp_use.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "high"
logsource: "windows / driver_load"
aliases:
  - "2c4523d5-d481-4ed0-8ec3-7fbf0cb41a75"
  - "Driver Load From A Temporary Directory"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Driver Load From A Temporary Directory

Detects a driver load from a temporary directory

## Metadata

- Rule ID: 2c4523d5-d481-4ed0-8ec3-7fbf0cb41a75
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2017-02-12
- Modified: 2021-11-27
- Source Path: rules/windows/driver_load/driver_load_win_susp_temp_use.yml

## Logsource

- category: driver_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Detection

```yaml
selection:
  ImageLoaded|contains: \Temp\
condition: selection
```

## False Positives

- There is a relevant set of false positives depending on applications in the environment

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/driver_load/driver_load_win_susp_temp_use.yml)
