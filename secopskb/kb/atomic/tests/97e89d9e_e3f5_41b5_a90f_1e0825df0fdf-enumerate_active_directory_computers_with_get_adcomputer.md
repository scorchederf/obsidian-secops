---
atomic_guid: "97e89d9e-e3f5-41b5-a90f-1e0825df0fdf"
title: "Enumerate Active Directory Computers with Get-AdComputer"
framework: "atomic"
generated: "true"
attack_technique_id: "T1018"
attack_technique_name: "Remote System Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "97e89d9e-e3f5-41b5-a90f-1e0825df0fdf"
  - "Enumerate Active Directory Computers with Get-AdComputer"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Enumerate Active Directory Computers with Get-AdComputer

The following Atomic test will utilize Get-AdComputer to enumerate Computers within Active Directory.
Upon successful execution a listing of Computers will output with their paths in AD.
Reference: https://github.com/MicrosoftDocs/windows-powershell-docs/blob/main/docset/winserver2022-ps/activedirectory/Get-ADComputer.md

## Metadata

- Atomic GUID: 97e89d9e-e3f5-41b5-a90f-1e0825df0fdf
- Technique: T1018: Remote System Discovery
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1018/T1018.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
Get-AdComputer -Filter *
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml)
