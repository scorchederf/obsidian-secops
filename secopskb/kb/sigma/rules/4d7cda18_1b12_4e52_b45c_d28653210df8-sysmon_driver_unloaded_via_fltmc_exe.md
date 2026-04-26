---
sigma_id: "4d7cda18-1b12-4e52-b45c-d28653210df8"
title: "Sysmon Driver Unloaded Via Fltmc.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_fltmc_unload_driver_sysmon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_fltmc_unload_driver_sysmon.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "4d7cda18-1b12-4e52-b45c-d28653210df8"
  - "Sysmon Driver Unloaded Via Fltmc.EXE"
attack_technique_ids:
  - "T1070"
  - "T1562"
  - "T1562.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Sysmon Driver Unloaded Via Fltmc.EXE

Detects possible Sysmon filter driver unloaded via fltmc.exe

## Metadata

- Rule ID: 4d7cda18-1b12-4e52-b45c-d28653210df8
- Status: test
- Level: high
- Author: Kirill Kiryanov, oscd.community
- Date: 2019-10-23
- Modified: 2023-02-13
- Source Path: rules/windows/process_creation/proc_creation_win_fltmc_unload_driver_sysmon.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070]]
- [[kb/attack/techniques/T1562-impair_defenses|T1562]]
- [[kb/attack/techniques/T1562-impair_defenses|T1562.002]]

## Detection

```yaml
selection_img:
- Image|endswith: \fltMC.exe
- OriginalFileName: fltMC.exe
selection_cli:
  CommandLine|contains|all:
  - unload
  - sysmon
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://www.darkoperator.com/blog/2018/10/5/operating-offensively-against-sysmon

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_fltmc_unload_driver_sysmon.yml)
