---
sigma_id: "05b2aa93-1210-42c8-8d9a-2fcc13b284f5"
title: "Service Registry Key Deleted Via Reg.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_delete_services.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_delete_services.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "05b2aa93-1210-42c8-8d9a-2fcc13b284f5"
  - "Service Registry Key Deleted Via Reg.EXE"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Service Registry Key Deleted Via Reg.EXE

Detects execution of "reg.exe" commands with the "delete" flag on services registry key. Often used by attacker to remove AV software services

## Metadata

- Rule ID: 05b2aa93-1210-42c8-8d9a-2fcc13b284f5
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-01
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_reg_delete_services.yml

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
  CommandLine|contains: ' delete '
selection_key:
  CommandLine|contains: \SYSTEM\CurrentControlSet\services\
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://www.virustotal.com/gui/file/2bcd5702a7565952c44075ac6fb946c7780526640d1264f692c7664c02c68465

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_delete_services.yml)
