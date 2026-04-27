---
atomic_guid: "93ca40d2-336c-446d-bcef-87f14d438018"
title: "Process Injection via Extra Window Memory (EWM) x64 executable"
framework: "atomic"
generated: "true"
attack_technique_id: "T1055.011"
attack_technique_name: "Process Injection: Extra Window Memory Injection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.011/T1055.011.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "93ca40d2-336c-446d-bcef-87f14d438018"
  - "Process Injection via Extra Window Memory (EWM) x64 executable"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Process Injection via Extra Window Memory (EWM) x64 executable

Hooks functions of main process to inject a payload via Extra Window Memory (EWM) injection technique

## Metadata

- Atomic GUID: 93ca40d2-336c-446d-bcef-87f14d438018
- Technique: T1055.011: Process Injection: Extra Window Memory Injection
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1055.011/T1055.011.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1055-process_injection|T1055.011]]

## Input Arguments

### arch

- description: Architecture of payload. One of (x64, x86)
- type: string
- default: x64

### exe_binary

- description: PE binary for EWM injection
- type: path
- default: PathToAtomicsFolder\T1055.011\bin\T1055.011_#{arch}.exe

### payload_file

- description: raw payload to inject
- type: path
- default: PathToAtomicsFolder\T1055.011\bin\payload.exe_#{arch}.bin

## Dependencies

T1055.011x64.exe and payload must exist on disk at specified location (#{exe_binary} and #{payload_file})

### Prerequisite Check

```powershell
if (Test-Path #{exe_binary}) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path #{exe_binary}) -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1055.011/bin/T1055.011_#{arch}.exe" -OutFile "#{exe_binary}" -UseBasicParsing
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1055.011/bin/payload.exe_#{arch}.bin" -OutFile "#{payload_file}" -UseBasicParsing
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
#{exe_binary}
```

### Cleanup

```powershell
Get-Process -Name Notepad -ErrorAction SilentlyContinue | Stop-Process -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.011/T1055.011.yaml)
