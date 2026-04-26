---
sigma_id: "509e84b9-a71a-40e0-834f-05470369bd1e"
title: "Default RDP Port Changed to Non Standard Port"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_change_rdp_port.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_change_rdp_port.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "509e84b9-a71a-40e0-834f-05470369bd1e"
  - "Default RDP Port Changed to Non Standard Port"
attack_technique_ids:
  - "T1547.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Default RDP Port Changed to Non Standard Port

Detects changes to the default RDP port.
Remote desktop is a common feature in operating systems. It allows a user to log into a remote system using an interactive session with a graphical user interface.
Microsoft refers to its implementation of the Remote Desktop Protocol (RDP) as Remote Desktop Services (RDS).

## Metadata

- Rule ID: 509e84b9-a71a-40e0-834f-05470369bd1e
- Status: test
- Level: high
- Author: frack113
- Date: 2022-01-01
- Modified: 2024-03-25
- Source Path: rules/windows/registry/registry_set/registry_set_change_rdp_port.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.010]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Control\Terminal Server\WinStations\RDP-Tcp\PortNumber
filter_main_port:
  Details: DWORD (0x00000d3d)
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## Simulation

### Changing RDP Port to Non Standard Port via Powershell

- atomic_guid: 2f840dd4-8a2e-4f44-beb3-6b2399ea3771
- name: Changing RDP Port to Non Standard Port via Powershell
- technique: T1021.001
- type: atomic-red-team

### Changing RDP Port to Non Standard Port via Command_Prompt

- atomic_guid: 74ace21e-a31c-4f7d-b540-53e4eb6d1f73
- name: Changing RDP Port to Non Standard Port via Command_Prompt
- technique: T1021.001
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1021.001/T1021.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_change_rdp_port.yml)
