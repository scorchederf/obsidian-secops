---
sigma_id: "c79da740-5030-45ec-a2e0-479e824a562c"
title: "System Disk And Volume Reconnaissance Via Wmic.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmic_recon_volume.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_recon_volume.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "c79da740-5030-45ec-a2e0-479e824a562c"
  - "System Disk And Volume Reconnaissance Via Wmic.EXE"
attack_technique_ids:
  - "T1047"
  - "T1082"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# System Disk And Volume Reconnaissance Via Wmic.EXE

An adversary might use WMI to discover information about the system, such as the volume name, size,
free space, and other disk information. This can be done using the 'wmic' command-line utility and has been
observed being used by threat actors such as Volt Typhoon.

## Metadata

- Rule ID: c79da740-5030-45ec-a2e0-479e824a562c
- Status: test
- Level: medium
- Author: Stephen Lincoln '@slincoln-aiq' (AttackIQ)
- Date: 2024-02-02
- Modified: 2025-10-20
- Source Path: rules/windows/process_creation/proc_creation_win_wmic_recon_volume.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]
- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Detection

```yaml
selection_img:
- Image|endswith: \WMIC.exe
- OriginalFileName: wmic.exe
selection_cli:
- CommandLine|contains:
  - ' volumename'
  - ' logicaldisk'
- CommandLine|contains|all:
  - path
  - win32_logicaldisk
- CommandLine|contains|all:
  - ' volume'
  - ' list '
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wmic

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_recon_volume.yml)
