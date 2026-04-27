---
sigma_id: "2c4523d5-d481-4ed0-8ec3-7fbf0cb41a75"
title: "Driver Load From A Temporary Directory"
framework: "sigma"
generated: "true"
source_path: "rules/windows/driver_load/driver_load_win_susp_temp_use.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/driver_load/driver_load_win_susp_temp_use.yml"
build_date: "2026-04-27 19:13:51"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a driver load from a temporary directory

## Logsource

- category: driver_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]]

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
