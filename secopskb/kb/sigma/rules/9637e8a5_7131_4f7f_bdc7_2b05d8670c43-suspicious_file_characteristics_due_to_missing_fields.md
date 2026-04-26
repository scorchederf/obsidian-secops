---
sigma_id: "9637e8a5-7131-4f7f-bdc7-2b05d8670c43"
title: "Suspicious File Characteristics Due to Missing Fields"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_file_characteristics.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_file_characteristics.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9637e8a5-7131-4f7f-bdc7-2b05d8670c43"
  - "Suspicious File Characteristics Due to Missing Fields"
attack_technique_ids:
  - "T1059.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious File Characteristics Due to Missing Fields

Detects Executables in the Downloads folder without FileVersion,Description,Product,Company likely created with py2exe

## Metadata

- Rule ID: 9637e8a5-7131-4f7f-bdc7-2b05d8670c43
- Status: test
- Level: medium
- Author: Markus Neis, Sander Wiebing
- Date: 2018-11-22
- Modified: 2022-10-09
- Source Path: rules/windows/process_creation/proc_creation_win_susp_file_characteristics.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.006]]

## Detection

```yaml
selection1:
  Description: \?
  FileVersion: \?
selection2:
  Description: \?
  Product: \?
selection3:
  Description: \?
  Company: \?
folder:
  Image|contains: \Downloads\
condition: (selection1 or selection2 or selection3) and folder
```

## False Positives

- Unknown

## References

- https://securelist.com/muddywater/88059/
- https://www.virustotal.com/#/file/276a765a10f98cda1a38d3a31e7483585ca3722ecad19d784441293acf1b7beb/detection

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_file_characteristics.yml)
