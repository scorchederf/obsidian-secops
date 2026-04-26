---
atomic_guid: "bac8a340-be64-4491-a0cc-0985cb227f5a"
title: "ESXi - Disable Firewall via Esxcli"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.004"
attack_technique_name: "Impair Defenses: Disable or Modify System Firewall"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "bac8a340-be64-4491-a0cc-0985cb227f5a"
  - "ESXi - Disable Firewall via Esxcli"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# ESXi - Disable Firewall via Esxcli

Adversaries may disable the ESXI firewall via ESXCLI

## Metadata

- Atomic GUID: bac8a340-be64-4491-a0cc-0985cb227f5a
- Technique: T1562.004: Impair Defenses: Disable or Modify System Firewall
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1562.004/T1562.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Input Arguments

### password

- description: password used to log into ESXI
- type: string
- default: n/a

### plink_file

- description: Path to Putty
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\plink.exe

### username

- description: username used to log into ESXi
- type: string
- default: root

### vm_host

- description: Specify the host name of the ESXi Server
- type: string
- default: atomic.local

## Dependencies

The plink executable must be found in the ExternalPayloads folder.

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
#{plink_file} -ssh #{vm_host} -l #{username} -pw #{password} -m PathToAtomicsFolder\..\atomics\T1562.004\src\esxi_disable_firewall.txt
```

### Cleanup

```commandprompt
#{plink_file} -ssh #{vm_host} -l #{username} -pw #{password} -m PathToAtomicsFolder\..\atomics\T1562.004\src\esxi_enable_firewall.txt
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml)
