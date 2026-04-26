---
sigma_id: "d58ba5c6-0ed7-4b9d-a433-6878379efda9"
title: "Remote Access Tool - AnyDesk Incoming Connection"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_remote_access_tools_anydesk_incoming_connection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_remote_access_tools_anydesk_incoming_connection.yml"
build_date: "2026-04-26 14:14:34"
status: "experimental"
level: "medium"
logsource: "windows / network_connection"
aliases:
  - "d58ba5c6-0ed7-4b9d-a433-6878379efda9"
  - "Remote Access Tool - AnyDesk Incoming Connection"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Access Tool - AnyDesk Incoming Connection

Detects incoming connections to AnyDesk. This could indicate a potential remote attacker trying to connect to a listening instance of AnyDesk and use it as potential command and control channel.

## Metadata

- Rule ID: d58ba5c6-0ed7-4b9d-a433-6878379efda9
- Status: experimental
- Level: medium
- Author: @d4ns4n_ (Wuerth-Phoenix)
- Date: 2024-09-02
- Modified: 2025-02-24
- Source Path: rules/windows/network_connection/net_connection_win_remote_access_tools_anydesk_incoming_connection.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]

## Detection

```yaml
selection:
  Image|endswith:
  - \AnyDesk.exe
  - \AnyDeskMSI.exe
  Initiated: 'false'
condition: selection
```

## False Positives

- Legitimate incoming connections (e.g. sysadmin activity). Most of the time I would expect outgoing connections (initiated locally).

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1219/T1219.md#atomic-test-2---anydesk-files-detected-test-on-windows
- https://asec.ahnlab.com/en/40263/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_remote_access_tools_anydesk_incoming_connection.yml)
