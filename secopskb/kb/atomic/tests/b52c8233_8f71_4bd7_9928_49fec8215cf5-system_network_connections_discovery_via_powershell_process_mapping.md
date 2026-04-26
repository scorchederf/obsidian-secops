---
atomic_guid: "b52c8233-8f71-4bd7-9928-49fec8215cf5"
title: "System Network Connections Discovery via PowerShell (Process Mapping)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1049"
attack_technique_name: "System Network Connections Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1049/T1049.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "b52c8233-8f71-4bd7-9928-49fec8215cf5"
  - "System Network Connections Discovery via PowerShell (Process Mapping)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# System Network Connections Discovery via PowerShell (Process Mapping)

Enumerate TCP connections and map to owning process names via PowerShell.

## Metadata

- Atomic GUID: b52c8233-8f71-4bd7-9928-49fec8215cf5
- Technique: T1049: System Network Connections Discovery
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1049/T1049.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1049-system_network_connections_discovery|T1049]]

## Executor

- name: powershell

### Command

```powershell
Get-NetTCPConnection | ForEach-Object {
  $p = Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue
  [pscustomobject]@{
    Local   = "$($_.LocalAddress):$($_.LocalPort)"
    Remote  = "$($_.RemoteAddress):$($_.RemotePort)"
    State   = $_.State
    PID     = $_.OwningProcess
    Process = if ($p) { $p.ProcessName } else { $null }
  }
} | Sort-Object State,Process | Format-Table -AutoSize
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1049/T1049.yaml)
