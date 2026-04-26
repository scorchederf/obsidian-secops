---
sigma_id: "64e8e417-c19a-475a-8d19-98ea705394cc"
title: "Alternate PowerShell Hosts - PowerShell Module"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_alternate_powershell_hosts.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_alternate_powershell_hosts.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / ps_module"
aliases:
  - "64e8e417-c19a-475a-8d19-98ea705394cc"
  - "Alternate PowerShell Hosts - PowerShell Module"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Alternate PowerShell Hosts - PowerShell Module

Detects alternate PowerShell hosts potentially bypassing detections looking for powershell.exe

## Metadata

- Rule ID: 64e8e417-c19a-475a-8d19-98ea705394cc
- Status: test
- Level: medium
- Author: Roberto Rodriguez @Cyb3rWard0g
- Date: 2019-08-11
- Modified: 2025-10-17
- Source Path: rules/windows/powershell/powershell_module/posh_pm_alternate_powershell_hosts.yml

## Logsource

- category: ps_module
- definition: 0ad03ef1-f21b-4a79-8ce8-e6900c54b65b
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  ContextInfo|contains: '*'
filter_powershell:
  ContextInfo|contains:
  - = powershell
  - = C:\Windows\System32\WindowsPowerShell\v1.0\powershell
  - = C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell
  - = C:/Windows/System32/WindowsPowerShell/v1.0/powershell
  - = C:/Windows/SysWOW64/WindowsPowerShell/v1.0/powershell
  - = \\\?\?\C:Windows\System32\WindowsPowerShell\v1.0\powershell
  - = \\\?\?\C:Windows\SysWOW64\WindowsPowerShell\v1.0\powershell
filter_sdiagnhost:
  ContextInfo|contains: = C:\WINDOWS\System32\sdiagnhost.exe -Embedding
filter_citrix:
  ContextInfo|contains: ConfigSyncRun.exe
filter_adace:
  ContextInfo|contains: C:\Windows\system32\dsac.exe
filter_winrm:
  ContextInfo|contains: C:\Windows\system32\wsmprovhost.exe -Embedding
filter_help_update:
  Payload|contains:
  - Update-Help
  - Failed to update Help for the module
condition: selection and not 1 of filter_*
```

## False Positives

- Programs using PowerShell directly without invocation of a dedicated interpreter
- MSP Detection Searcher
- Citrix ConfigSync.ps1

## References

- https://threathunterplaybook.com/hunts/windows/190610-PwshAlternateHosts/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_alternate_powershell_hosts.yml)
