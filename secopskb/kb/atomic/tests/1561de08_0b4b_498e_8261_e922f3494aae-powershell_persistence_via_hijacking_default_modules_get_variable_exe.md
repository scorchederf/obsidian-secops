---
atomic_guid: "1561de08-0b4b-498e-8261-e922f3494aae"
title: "powerShell Persistence via hijacking default modules - Get-Variable.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1574.008"
attack_technique_name: "Hijack Execution Flow: Path Interception by Search Order Hijacking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.008/T1574.008.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "1561de08-0b4b-498e-8261-e922f3494aae"
  - "powerShell Persistence via hijacking default modules - Get-Variable.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Colibri leverages PowerShell in a unique way to maintain persistence after a reboot. Depending on the Windows version, Colibri drops its copy in %APPDATA%\Local\Microsoft\WindowsApps and 
names it Get-Variable.exe for Windows 10 and above.
https://blog.malwarebytes.com/threat-intelligence/2022/04/colibri-loader-combines-task-scheduler-and-powershell-in-clever-persistence-technique/

## ATT&CK Mapping

- [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574008-path-interception-by-search-order-hijacking|T1574.008: Path Interception by Search Order Hijacking]]

## Executor

- name: powershell

### Command

```powershell
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe /out:"$env:localappdata\Microsoft\WindowsApps\Get-Variable.exe" "PathToAtomicsFolder\T1574.008\bin\calc.cs"
Powershell -noprofile
```

### Cleanup

```powershell
Remove-Item "$env:localappdata\Microsoft\WindowsApps\Get-Variable.exe" -ErrorAction Ignore
Stop-Process -Name "calculator"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.008/T1574.008.yaml)
