---
sigma_id: "551d9c1f-816c-445b-a7a6-7a3864720d60"
title: "Potential Excel.EXE DCOM Lateral Movement Via ActivateMicrosoftApp"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_office_excel_dcom_lateral_movement.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_excel_dcom_lateral_movement.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "551d9c1f-816c-445b-a7a6-7a3864720d60"
  - "Potential Excel.EXE DCOM Lateral Movement Via ActivateMicrosoftApp"
attack_technique_ids:
  - "T1021.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Excel.EXE DCOM Lateral Movement Via ActivateMicrosoftApp

Detects suspicious child processes of Excel which could be an indicator of lateral movement leveraging the "ActivateMicrosoftApp" Excel DCOM object.

## Metadata

- Rule ID: 551d9c1f-816c-445b-a7a6-7a3864720d60
- Status: test
- Level: high
- Author: Aaron Stratton
- Date: 2023-11-13
- Source Path: rules/windows/process_creation/proc_creation_win_office_excel_dcom_lateral_movement.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.003]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \excel.exe
selection_child:
- OriginalFileName:
  - foxprow.exe
  - schdplus.exe
  - winproj.exe
- Image|endswith:
  - \foxprow.exe
  - \schdplus.exe
  - \winproj.exe
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://posts.specterops.io/lateral-movement-abuse-the-power-of-dcom-excel-application-3c016d0d9922
- https://github.com/grayhatkiller/SharpExShell
- https://learn.microsoft.com/en-us/office/vba/api/excel.xlmsapplication

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_excel_dcom_lateral_movement.yml)
