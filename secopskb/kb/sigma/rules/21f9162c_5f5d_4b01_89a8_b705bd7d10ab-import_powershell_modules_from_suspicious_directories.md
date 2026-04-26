---
sigma_id: "21f9162c-5f5d-4b01-89a8-b705bd7d10ab"
title: "Import PowerShell Modules From Suspicious Directories"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_import_module_susp_dirs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_import_module_susp_dirs.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "21f9162c-5f5d-4b01-89a8-b705bd7d10ab"
  - "Import PowerShell Modules From Suspicious Directories"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Import PowerShell Modules From Suspicious Directories

Detects powershell scripts that import modules from suspicious directories

## Metadata

- Rule ID: 21f9162c-5f5d-4b01-89a8-b705bd7d10ab
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-07
- Modified: 2023-01-10
- Source Path: rules/windows/powershell/powershell_script/posh_ps_import_module_susp_dirs.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  ScriptBlockText|contains:
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_import_module_susp_dirs.yml)
