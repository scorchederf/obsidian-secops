---
atomic_guid: "2f840dd4-8a2e-4f44-beb3-6b2399ea3771"
title: "Changing RDP Port to Non Standard Port via Powershell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1021.001"
attack_technique_name: "Remote Services: Remote Desktop Protocol"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.001/T1021.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "2f840dd4-8a2e-4f44-beb3-6b2399ea3771"
  - "Changing RDP Port to Non Standard Port via Powershell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Changing RDP Port to Non Standard Port via Powershell

Changing RDP Port to Non Standard Port via Powershell

## Metadata

- Atomic GUID: 2f840dd4-8a2e-4f44-beb3-6b2399ea3771
- Technique: T1021.001: Remote Services: Remote Desktop Protocol
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1021.001/T1021.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1021-remote_services|T1021.001]]

## Input Arguments

### NEW_Remote_Port

- description: New RDP Listening Port
- type: string
- default: 4489

### OLD_Remote_Port

- description: Default RDP Listening Port
- type: string
- default: 3389

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -name "PortNumber" -Value #{NEW_Remote_Port}
New-NetFirewallRule -DisplayName 'RDPPORTLatest-TCP-In' -Profile 'Public' -Direction Inbound -Action Allow -Protocol TCP -LocalPort #{NEW_Remote_Port}
```

### Cleanup

```powershell
Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -name "PortNumber" -Value #{OLD_Remote_Port}
Remove-NetFirewallRule -DisplayName "RDPPORTLatest-TCP-In" -ErrorAction Ignore 
Get-Service TermService | Restart-Service -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.001/T1021.001.yaml)
