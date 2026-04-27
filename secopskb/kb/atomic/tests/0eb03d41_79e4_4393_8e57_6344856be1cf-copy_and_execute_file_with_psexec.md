---
atomic_guid: "0eb03d41-79e4-4393-8e57-6344856be1cf"
title: "Copy and Execute File with PsExec"
framework: "atomic"
generated: "true"
attack_technique_id: "T1021.002"
attack_technique_name: "Remote Services: SMB/Windows Admin Shares"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.002/T1021.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "0eb03d41-79e4-4393-8e57-6344856be1cf"
  - "Copy and Execute File with PsExec"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Copy and Execute File with PsExec

Copies a file to a remote host and executes it using PsExec. Requires the download of PsExec from [https://docs.microsoft.com/en-us/sysinternals/downloads/psexec](https://docs.microsoft.com/en-us/sysinternals/downloads/psexec).

## Metadata

- Atomic GUID: 0eb03d41-79e4-4393-8e57-6344856be1cf
- Technique: T1021.002: Remote Services: SMB/Windows Admin Shares
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1021.002/T1021.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]

## Input Arguments

### command_path

- description: File to copy and execute
- type: path
- default: C:\Windows\System32\cmd.exe

### psexec_exe

- description: Path to PsExec
- type: string
- default: PathToAtomicsFolder\..\ExternalPayloads\PsExec.exe

### remote_host

- description: Remote computer to receive the copy and execute the file
- type: string
- default: \\localhost

## Dependencies

PsExec tool from Sysinternals must exist on disk at specified location (#{psexec_exe})

### Prerequisite Check

```powershell
if (Test-Path "#{psexec_exe}") { exit 0} else { exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://download.sysinternals.com/files/PSTools.zip" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\PsTools.zip"
Expand-Archive "PathToAtomicsFolder\..\ExternalPayloads\PsTools.zip" "PathToAtomicsFolder\..\ExternalPayloads\PsTools" -Force
New-Item -ItemType Directory (Split-Path "#{psexec_exe}") -Force | Out-Null
Copy-Item "PathToAtomicsFolder\..\ExternalPayloads\PsTools\PsExec.exe" "#{psexec_exe}" -Force
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
"#{psexec_exe}" #{remote_host} -accepteula -c #{command_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.002/T1021.002.yaml)
