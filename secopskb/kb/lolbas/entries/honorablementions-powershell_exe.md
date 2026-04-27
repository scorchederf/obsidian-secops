---
title: "Powershell.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/HonorableMentions/PowerShell.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/HonorableMentions/PowerShell.yml"
build_date: "2026-04-27 19:14:21"
category: "HonorableMentions"
aliases:
  - "Powershell.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1059.001"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Powershell.exe is a a task-based command-line shell built on .NET.

## Paths

- `C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe`
- `C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe`

## Commands

### 1. Execute

Set the execution policy to bypass and execute a PowerShell script without warning

```cmd
powershell.exe -ep bypass -file c:\path\to\a\script.ps1
```

- Use Case: Execute PowerShell cmdlets, .NET code, and just about anything else your heart desires
- Privileges: User
- Operating System: Windows 7 and up
- ATT&CK: [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

### 2. Execute

Set the execution policy to bypass and execute a PowerShell command

```cmd
powershell.exe -ep bypass -command "Invoke-AllTheThings..."
```

- Use Case: Execute PowerShell cmdlets, .NET code, and just about anything else your heart desires
- Privileges: User
- Operating System: Windows 7 and up
- ATT&CK: [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

### 3. Execute

Set the execution policy to bypass and execute a very malicious PowerShell encoded command

```cmd
powershell.exe -ep bypass -ec IgBXAGUAIAA8ADMAIABMAE8ATABCAEEAUwAiAA==
```

- Use Case: Execute PowerShell cmdlets, .NET code, and just about anything else your heart desires
- Privileges: User
- Operating System: Windows 7 and up
- ATT&CK: [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/tree/71ae004b32bb3c7fb04714f8a051fc8e5edda68c/rules/windows/powershell

## Resources

- {'Link': 'https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_powershell_exe?view=powershell-5.1'}
- {'Link': 'https://attack.mitre.org/techniques/T1059/001/'}

## Acknowledgements

- {'Person': 'Everyone', 'Handle': '@alltheoffensivecyberers'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/HonorableMentions/PowerShell.yml)
