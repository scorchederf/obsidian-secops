---
atomic_guid: "15fe436d-e771-4ff3-b655-2dca9ba52834"
title: "Adfind - Enumerate Active Directory Trusts"
framework: "atomic"
generated: "true"
attack_technique_id: "T1482"
attack_technique_name: "Domain Trust Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1482/T1482.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "15fe436d-e771-4ff3-b655-2dca9ba52834"
  - "Adfind - Enumerate Active Directory Trusts"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Adfind - Enumerate Active Directory Trusts

Adfind tool can be used for reconnaissance in an Active directory environment. This example has been documented by ransomware actors enumerating Active Directory Trusts
reference- http://www.joeware.net/freetools/tools/adfind/, https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html

## Metadata

- Atomic GUID: 15fe436d-e771-4ff3-b655-2dca9ba52834
- Technique: T1482: Domain Trust Discovery
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1482/T1482.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1482-domain_trust_discovery|T1482]]

## Input Arguments

### optional_args

- description: Allows defining arguments to add to the adfind command to tailor it to the specific needs of the environment. Use "-arg" notation to add arguments separated by spaces.
- type: string

## Dependencies

AdFind.exe must exist on disk at specified location (PathToAtomicsFolder\..\ExternalPayloads\AdFind.exe)

### Prerequisite Check

```powershell
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\AdFind.exe") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "PathToAtomicsFolder\..\ExternalPayloads\AdFind.exe") -ErrorAction ignore | Out-Null
Invoke-WebRequest -Uri "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1087.002/bin/AdFind.exe" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\AdFind.exe"
```

## Executor

- name: command_prompt

### Command

```cmd
"PathToAtomicsFolder\..\ExternalPayloads\AdFind.exe" #{optional_args} -gcb -sc trustdmp
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1482/T1482.yaml)
