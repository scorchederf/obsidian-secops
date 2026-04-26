---
sigma_id: "c31364f7-8be6-4b77-8483-dd2b5a7b69a3"
title: "Import PowerShell Modules From Suspicious Directories - ProcCreation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_import_module_susp_dirs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_import_module_susp_dirs.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "c31364f7-8be6-4b77-8483-dd2b5a7b69a3"
  - "Import PowerShell Modules From Suspicious Directories - ProcCreation"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Import PowerShell Modules From Suspicious Directories - ProcCreation

Detects powershell scripts that import modules from suspicious directories

## Metadata

- Rule ID: c31364f7-8be6-4b77-8483-dd2b5a7b69a3
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-10
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_import_module_susp_dirs.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - Import-Module "$Env:Temp\
  - Import-Module '$Env:Temp\
  - Import-Module $Env:Temp\
  - Import-Module "$Env:Appdata\
  - Import-Module '$Env:Appdata\
  - Import-Module $Env:Appdata\
  - Import-Module C:\Users\Public\
  - ipmo "$Env:Temp\
  - ipmo '$Env:Temp\
  - ipmo $Env:Temp\
  - ipmo "$Env:Appdata\
  - ipmo '$Env:Appdata\
  - ipmo $Env:Appdata\
  - ipmo C:\Users\Public\
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1003.002/T1003.002.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_import_module_susp_dirs.yml)
