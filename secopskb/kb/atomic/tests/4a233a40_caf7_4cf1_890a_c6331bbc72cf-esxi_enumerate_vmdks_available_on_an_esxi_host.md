---
atomic_guid: "4a233a40-caf7-4cf1-890a-c6331bbc72cf"
title: "ESXi - Enumerate VMDKs available on an ESXi Host"
framework: "atomic"
generated: "true"
attack_technique_id: "T1083"
attack_technique_name: "File and Directory Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1083/T1083.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "4a233a40-caf7-4cf1-890a-c6331bbc72cf"
  - "ESXi - Enumerate VMDKs available on an ESXi Host"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# ESXi - Enumerate VMDKs available on an ESXi Host

An adversary uses the find command to enumerate vmdks on an ESXi host.
[Reference](https://www.crowdstrike.com/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)

## Metadata

- Atomic GUID: 4a233a40-caf7-4cf1-890a-c6331bbc72cf
- Technique: T1083: File and Directory Discovery
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1083/T1083.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]

## Input Arguments

### cli_script

- description: Path to script with file discovery commands
- type: path
- default: PathToAtomicsFolder\T1083\src\esxi_file_discovery.txt

### plink_file

- description: Path to Plink
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\plink.exe

### vm_host

- description: Specify the host name of the ESXi Server
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
echo "" | "#{plink_file}" "#{vm_host}" -ssh  -l "#{vm_user}" -pw "#{vm_pass}" -m "#{cli_script}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1083/T1083.yaml)
