---
atomic_guid: "2040405c-eea6-4c1c-aef3-c2acc430fac9"
title: "ESXi - VM Discovery using ESXCLI"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "2040405c-eea6-4c1c-aef3-c2acc430fac9"
  - "ESXi - VM Discovery using ESXCLI"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# ESXi - VM Discovery using ESXCLI

An adversary will using ESXCLI to enumerate the Virtual Machines on the host prior to executing power off routine.
[Reference](https://www.crowdstrike.com/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)

## Metadata

- Atomic GUID: 2040405c-eea6-4c1c-aef3-c2acc430fac9
- Technique: T1082: System Information Discovery
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1082/T1082.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Input Arguments

### cli_script

- description: Path to file with discovery commands
- type: path
- default: PathToAtomicsFolder\T1082\src\esx_vmdiscovery.txt

### plink_file

- description: Path to Plink
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\plink.exe

### vm_host

- description: Specify the host name or IP of the ESXi Server
- type: string
- default: atomic.local

### vm_pass

- description: Specify the privilege user password on ESXi Server
- type: string
- default: pass

### vm_user

- description: Specify the privilege user account on ESXi Server
- type: string
- default: root

## Dependencies

Check if plink is available.

### Prerequisite Check

```text
if (Test-Path "#{plink_file}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://the.earth.li/~sgtatham/putty/latest/w64/plink.exe" -OutFile "#{plink_file}"
```

## Executor

- elevation_required: False
- name: command_prompt

### Command

```commandprompt
echo "" | "#{plink_file}" "#{vm_host}" -ssh  -l "#{vm_user}" -pw "#{vm_pass}" -m "#{cli_script}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
