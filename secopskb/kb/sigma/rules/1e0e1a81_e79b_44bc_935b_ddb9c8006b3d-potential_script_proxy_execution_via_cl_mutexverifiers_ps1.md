---
sigma_id: "1e0e1a81-e79b-44bc-935b-ddb9c8006b3d"
title: "Potential Script Proxy Execution Via CL_Mutexverifiers.ps1"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_cl_mutexverifiers.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_cl_mutexverifiers.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "1e0e1a81-e79b-44bc-935b-ddb9c8006b3d"
  - "Potential Script Proxy Execution Via CL_Mutexverifiers.ps1"
attack_technique_ids:
  - "T1216"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Script Proxy Execution Via CL_Mutexverifiers.ps1

Detects the use of the Microsoft signed script "CL_mutexverifiers" to proxy the execution of additional PowerShell script commands

## Metadata

- Rule ID: 1e0e1a81-e79b-44bc-935b-ddb9c8006b3d
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), oscd.community, Natalia Shornikova, frack113
- Date: 2022-05-21
- Modified: 2023-08-17
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_cl_mutexverifiers.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216]]

## Detection

```yaml
selection_pwsh:
  ParentImage|endswith:
  - \powershell.exe
  - \pwsh.exe
  Image|endswith: \powershell.exe
  CommandLine|contains: ' -nologo -windowstyle minimized -file '
selection_temp:
  CommandLine|contains:
  - \AppData\Local\Temp\
  - \Windows\Temp\
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Scripts/CL_mutexverifiers/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_cl_mutexverifiers.yml)
