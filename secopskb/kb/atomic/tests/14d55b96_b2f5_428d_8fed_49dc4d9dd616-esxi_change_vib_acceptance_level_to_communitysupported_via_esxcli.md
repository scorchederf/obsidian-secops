---
atomic_guid: "14d55b96-b2f5-428d-8fed-49dc4d9dd616"
title: "ESXi - Change VIB acceptance level to CommunitySupported via ESXCLI"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.010"
attack_technique_name: "Impair Defenses: Downgrade Attack"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.010/T1562.010.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "14d55b96-b2f5-428d-8fed-49dc4d9dd616"
  - "ESXi - Change VIB acceptance level to CommunitySupported via ESXCLI"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# ESXi - Change VIB acceptance level to CommunitySupported via ESXCLI

An adversary will change the VIB acceptance level to CommunitySupported to downgrade the acceptance criteria via ESXCLI. Afterwards an adversary may proceed to installing malicious VIBs on the host.
[Reference](https://www.mandiant.com/resources/blog/esxi-hypervisors-detection-hardening)

## Metadata

- Atomic GUID: 14d55b96-b2f5-428d-8fed-49dc4d9dd616
- Technique: T1562.010: Impair Defenses: Downgrade Attack
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1562.010/T1562.010.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.010]]

## Input Arguments

### cli_script

- description: Path to script with commands to change acceptance level
- type: path
- default: PathToAtomicsFolder\T1562.010\src\esx_community_supported.txt

### plink_file

- description: Path to plink
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

- name: command_prompt

### Command

```cmd
echo "" | "#{plink_file}" "#{vm_host}" -ssh  -l "#{vm_user}" -pw "#{vm_pass}" -m "#{cli_script}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.010/T1562.010.yaml)
