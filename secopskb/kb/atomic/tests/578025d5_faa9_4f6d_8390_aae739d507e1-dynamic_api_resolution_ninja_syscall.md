---
atomic_guid: "578025d5-faa9-4f6d-8390-aae739d507e1"
title: "Dynamic API Resolution-Ninja-syscall"
framework: "atomic"
generated: "true"
attack_technique_id: "T1027.007"
attack_technique_name: "Obfuscated Files or Information: Dynamic API Resolution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.007/T1027.007.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "578025d5-faa9-4f6d-8390-aae739d507e1"
  - "Dynamic API Resolution-Ninja-syscall"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Dynamic API Resolution-Ninja-syscall

This test calls NtCreateFile via API hashing and dynamic syscall resolution. I have dubbed this particular combination of techniques 'Ninja-syscall'. When successful, a new file named 'hello.log' will be created in the default user's temporary folder, which is a common location for a dropper.

## Metadata

- Atomic GUID: 578025d5-faa9-4f6d-8390-aae739d507e1
- Technique: T1027.007: Obfuscated Files or Information: Dynamic API Resolution
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1027.007/T1027.007.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.007]]

## Input Arguments

### exe_binary

- description: PE binary
- type: path
- default: PathToAtomicsFolder\T1027.007\bin\ninja_syscall1.exe

## Dependencies

Portable Executable to run must exist at specified location (#{exe_binary})

### Prerequisite Check

```text
if (Test-Path "#{exe_binary}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory (split-path "#{exe_binary}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1027.007/bin/ninja_syscall1.exe" -OutFile "#{exe_binary}"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Start-Process "#{exe_binary}"
Start-Sleep -Seconds 7
if (Test-Path "C:\Users\Default\AppData\Local\Temp\hello.log") { Remove-Item "C:\Users\Default\AppData\Local\Temp\hello.log" -Force; Write-Host "[+] hello.log removed." }
```

### Cleanup

```powershell
if (Test-Path "C:\Users\Default\AppData\Local\Temp\hello.log") { Remove-Item "C:\Users\Default\AppData\Local\Temp\hello.log" -Force; Write-Host "[+] hello.log removed." }
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.007/T1027.007.yaml)
