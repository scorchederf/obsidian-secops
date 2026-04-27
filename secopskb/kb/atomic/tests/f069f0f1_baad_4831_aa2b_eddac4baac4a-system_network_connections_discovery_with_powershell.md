---
atomic_guid: "f069f0f1-baad-4831-aa2b-eddac4baac4a"
title: "System Network Connections Discovery with PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1049"
attack_technique_name: "System Network Connections Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1049/T1049.yaml"
build_date: "2026-04-27 19:12:26"
executor: "powershell"
aliases:
  - "f069f0f1-baad-4831-aa2b-eddac4baac4a"
  - "System Network Connections Discovery with PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Get a listing of network connections.
Upon successful execution, powershell.exe will execute `get-NetTCPConnection`. Results will output via stdout.

## ATT&CK Mapping

- [[kb/attack/techniques/T1049-system_network_connections_discovery|T1049: System Network Connections Discovery]]

## Executor

- name: powershell

### Command

```powershell
Get-NetTCPConnection
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1049/T1049.yaml)
