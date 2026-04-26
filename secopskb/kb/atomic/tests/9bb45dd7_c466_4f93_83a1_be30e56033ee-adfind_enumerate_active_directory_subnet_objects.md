---
atomic_guid: "9bb45dd7-c466-4f93-83a1-be30e56033ee"
title: "Adfind - Enumerate Active Directory Subnet Objects"
framework: "atomic"
generated: "true"
attack_technique_id: "T1016"
attack_technique_name: "System Network Configuration Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016/T1016.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "9bb45dd7-c466-4f93-83a1-be30e56033ee"
  - "Adfind - Enumerate Active Directory Subnet Objects"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Adfind - Enumerate Active Directory Subnet Objects

Adfind tool can be used for reconnaissance in an Active directory environment. This example has been documented by ransomware actors enumerating Active Directory Subnet Objects
reference- http://www.joeware.net/freetools/tools/adfind/, https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html

## Metadata

- Atomic GUID: 9bb45dd7-c466-4f93-83a1-be30e56033ee
- Technique: T1016: System Network Configuration Discovery
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1016/T1016.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1016-system_network_configuration_discovery|T1016]]

## Input Arguments

### optional_args

- description: Allows defining arguments to add to the adfind command to tailor it to the specific needs of the environment. Use "-arg" notation to add arguments separated by spaces.
- type: string

## Dependencies

AdFind.exe must exist on disk at specified location (PathToAtomicsFolder\..\ExternalPayloads\AdFind.exe)

### Prerequisite Check

```text
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\AdFind.exe") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory (split-path "PathToAtomicsFolder\..\ExternalPayloads\AdFind.exe") -ErrorAction ignore | Out-Null
Invoke-WebRequest -Uri "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1087.002/bin/AdFind.exe" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\AdFind.exe"
```

## Executor

- name: command_prompt

### Command

```commandprompt
"PathToAtomicsFolder\..\ExternalPayloads\AdFind.exe" -f (objectcategory=subnet) #{optional_args}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016/T1016.yaml)
