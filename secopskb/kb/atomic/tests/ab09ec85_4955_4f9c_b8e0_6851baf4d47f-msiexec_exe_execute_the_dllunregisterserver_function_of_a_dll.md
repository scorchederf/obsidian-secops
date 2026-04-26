---
atomic_guid: "ab09ec85-4955-4f9c-b8e0-6851baf4d47f"
title: "Msiexec.exe - Execute the DllUnregisterServer function of a DLL"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.007"
attack_technique_name: "Signed Binary Proxy Execution: Msiexec"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.007/T1218.007.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "ab09ec85-4955-4f9c-b8e0-6851baf4d47f"
  - "Msiexec.exe - Execute the DllUnregisterServer function of a DLL"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Msiexec.exe - Execute the DllUnregisterServer function of a DLL

Loads a DLL into msiexec.exe and calls its DllUnregisterServer function. Note: the DLL included in the "bin" folder is only built for 64-bit, so this won't work on a 32-bit OS.

## Metadata

- Atomic GUID: ab09ec85-4955-4f9c-b8e0-6851baf4d47f
- Technique: T1218.007: Signed Binary Proxy Execution: Msiexec
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1218.007/T1218.007.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.007]]

## Input Arguments

### dll_payload

- description: DLL to execute that has an implemented DllUnregisterServer function
- type: path
- default: PathToAtomicsFolder\T1218.007\bin\MSIRunner.dll

### msi_exe

- description: MSIExec File Path
- type: path
- default: c:\windows\system32\msiexec.exe

## Dependencies

The DLL must exist on disk at specified location (#{dll_payload})

### Prerequisite Check

```powershell
if (Test-Path "#{dll_payload}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{dll_payload}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218.007/bin/MSIRunner.dll -OutFile "#{dll_payload}"
```

## Executor

- name: command_prompt

### Command

```cmd
#{msi_exe} /z "#{dll_payload}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.007/T1218.007.yaml)
