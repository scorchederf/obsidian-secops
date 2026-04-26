---
atomic_guid: "f9c3d0ab-479b-4019-945f-22ace2b1731a"
title: "Search for Passwords in Powershell History"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552"
attack_technique_name: "Unsecured Credentials"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552/T1552.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "f9c3d0ab-479b-4019-945f-22ace2b1731a"
  - "Search for Passwords in Powershell History"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Search for Passwords in Powershell History

Find passwords in the powershell history files
Searching for following strings: "password", "-p", "key", "pwd", "pass"

## Metadata

- Atomic GUID: f9c3d0ab-479b-4019-945f-22ace2b1731a
- Technique: T1552: Unsecured Credentials
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1552/T1552.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
ls -R C:\Users\*\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt | Select-String "password", "-p", "key", "pwd", "pass"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552/T1552.yaml)
