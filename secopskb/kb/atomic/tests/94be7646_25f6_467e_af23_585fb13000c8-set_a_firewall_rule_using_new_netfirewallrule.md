---
atomic_guid: "94be7646-25f6-467e-af23-585fb13000c8"
title: "Set a firewall rule using New-NetFirewallRule"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.004"
attack_technique_name: "Impair Defenses: Disable or Modify System Firewall"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "94be7646-25f6-467e-af23-585fb13000c8"
  - "Set a firewall rule using New-NetFirewallRule"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Set a firewall rule using New-NetFirewallRule

This test will attempt to create a new inbound/outbound firewall rule using the New-NetFirewallRule commandlet.

## Metadata

- Atomic GUID: 94be7646-25f6-467e-af23-585fb13000c8
- Technique: T1562.004: Impair Defenses: Disable or Modify System Firewall
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1562.004/T1562.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Input Arguments

### action

- description: This is the action
- type: string
- default: allow

### direction

- description: Direction can be Inbound or Outbound
- type: string
- default: Inbound

### local_port

- description: This is the local port you wish to test opening
- type: integer
- default: 21

### protocol

- description: This is the protocol
- type: string
- default: TCP

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
New-NetFirewallRule -DisplayName "New rule" -Direction "#{direction}" -LocalPort "#{local_port}" -Protocol "#{protocol}" -Action "#{action}"
```

### Cleanup

```powershell
Remove-NetFirewallRule -DisplayName "New rule"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml)
