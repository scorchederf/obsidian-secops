---
sigma_id: "fc0e89b5-adb0-43c1-b749-c12a10ec37de"
title: "SafeBoot Registry Key Deleted Via Reg.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_delete_safeboot.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_delete_safeboot.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "fc0e89b5-adb0-43c1-b749-c12a10ec37de"
  - "SafeBoot Registry Key Deleted Via Reg.EXE"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# SafeBoot Registry Key Deleted Via Reg.EXE

Detects execution of "reg.exe" commands with the "delete" flag on safe boot registry keys. Often used by attacker to prevent safeboot execution of security products

## Metadata

- Rule ID: fc0e89b5-adb0-43c1-b749-c12a10ec37de
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), Tim Shelton
- Date: 2022-08-08
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_reg_delete_safeboot.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_img:
- Image|endswith: reg.exe
- OriginalFileName: reg.exe
selection_delete:
  CommandLine|contains|all:
  - ' delete '
  - \SYSTEM\CurrentControlSet\Control\SafeBoot
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://www.trendmicro.com/en_us/research/22/e/avoslocker-ransomware-variant-abuses-driver-file-to-disable-anti-Virus-scans-log4shell.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_delete_safeboot.yml)
