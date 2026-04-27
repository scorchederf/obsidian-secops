---
atomic_guid: "578025d5-faa9-4f6d-8390-aae739d503e1"
title: "Portable Executable Injection"
framework: "atomic"
generated: "true"
attack_technique_id: "T1055.002"
attack_technique_name: "Process Injection: Portable Executable Injection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.002/T1055.002.yaml"
build_date: "2026-04-27 19:12:26"
executor: "powershell"
aliases:
  - "578025d5-faa9-4f6d-8390-aae739d503e1"
  - "Portable Executable Injection"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test injects a portable executable into a remote Notepad process memory using Portable Executable Injection and base-address relocation techniques. When successful, a message box will appear with the title "Warning" and the content "Atomic Red Team" after a few seconds.

## ATT&CK Mapping

- [[kb/attack/techniques/T1055-process_injection#^t1055002-portable-executable-injection|T1055.002: Portable Executable Injection]]

## Input Arguments

### exe_binary

- description: PE binary
- type: path
- default: PathToAtomicsFolder\T1055.002\bin\RedInjection.exe

## Dependencies

Portable Executable to inject must exist at specified location (#{exe_binary})

### Prerequisite Check

```powershell
if (Test-Path "#{exe_binary}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{exe_binary}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1055.002/bin/RedInjection.exe" -OutFile "#{exe_binary}"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Start-Process "#{exe_binary}"
Start-Sleep -Seconds 7
Get-Process -Name Notepad -ErrorAction SilentlyContinue | Stop-Process -Force
```

### Cleanup

```powershell
Get-Process -Name Notepad -ErrorAction SilentlyContinue | Stop-Process -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.002/T1055.002.yaml)
