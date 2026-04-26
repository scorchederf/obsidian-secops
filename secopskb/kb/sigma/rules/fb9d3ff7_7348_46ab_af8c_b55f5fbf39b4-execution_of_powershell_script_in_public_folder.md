---
sigma_id: "fb9d3ff7-7348-46ab-af8c-b55f5fbf39b4"
title: "Execution of Powershell Script in Public Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_public_folder.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_public_folder.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "fb9d3ff7-7348-46ab-af8c-b55f5fbf39b4"
  - "Execution of Powershell Script in Public Folder"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Execution of Powershell Script in Public Folder

This rule detects execution of PowerShell scripts located in the "C:\Users\Public" folder

## Metadata

- Rule ID: fb9d3ff7-7348-46ab-af8c-b55f5fbf39b4
- Status: test
- Level: high
- Author: Max Altgelt (Nextron Systems)
- Date: 2022-04-06
- Modified: 2022-07-14
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_public_folder.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  CommandLine|contains:
  - -f C:\Users\Public
  - -f "C:\Users\Public
  - -f %Public%
  - -fi C:\Users\Public
  - -fi "C:\Users\Public
  - -fi %Public%
  - -fil C:\Users\Public
  - -fil "C:\Users\Public
  - -fil %Public%
  - -file C:\Users\Public
  - -file "C:\Users\Public
  - -file %Public%
condition: selection
```

## False Positives

- Unlikely

## References

- https://www.mandiant.com/resources/evolution-of-fin7

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_public_folder.yml)
