---
sigma_id: "5f699bc5-5446-4a4a-a0b7-5ef2885a3eb4"
title: "RDP Over Reverse SSH Tunnel"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_rdp_reverse_tunnel.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_rdp_reverse_tunnel.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / network_connection"
aliases:
  - "5f699bc5-5446-4a4a-a0b7-5ef2885a3eb4"
  - "RDP Over Reverse SSH Tunnel"
attack_technique_ids:
  - "T1572"
  - "T1021.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects svchost hosting RDP termsvcs communicating with the loopback address and on TCP port 3389

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1572-protocol_tunneling|T1572: Protocol Tunneling]]
- [[kb/attack/techniques/T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]]

## Detection

```yaml
selection_img:
  Image|endswith: \svchost.exe
  Initiated: 'true'
  SourcePort: 3389
selection_destination:
  DestinationIp|cidr:
  - 127.0.0.0/8
  - ::1/128
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://twitter.com/cyb3rops/status/1096842275437625346

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_rdp_reverse_tunnel.yml)
