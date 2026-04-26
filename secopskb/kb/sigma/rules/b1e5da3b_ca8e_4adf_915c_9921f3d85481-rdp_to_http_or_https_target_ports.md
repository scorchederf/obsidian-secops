---
sigma_id: "b1e5da3b-ca8e-4adf-915c-9921f3d85481"
title: "RDP to HTTP or HTTPS Target Ports"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_rdp_to_http.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_rdp_to_http.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / network_connection"
aliases:
  - "b1e5da3b-ca8e-4adf-915c-9921f3d85481"
  - "RDP to HTTP or HTTPS Target Ports"
attack_technique_ids:
  - "T1572"
  - "T1021.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# RDP to HTTP or HTTPS Target Ports

Detects svchost hosting RDP termsvcs communicating to target systems on TCP port 80 or 443

## Metadata

- Rule ID: b1e5da3b-ca8e-4adf-915c-9921f3d85481
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-04-29
- Modified: 2022-07-14
- Source Path: rules/windows/network_connection/net_connection_win_rdp_to_http.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1572-protocol_tunneling|T1572]]
- [[kb/attack/techniques/T1021-remote_services|T1021.001]]

## Detection

```yaml
selection:
  Image|endswith: \svchost.exe
  Initiated: 'true'
  SourcePort: 3389
  DestinationPort:
  - 80
  - 443
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/tekdefense/status/1519711183162556416?s=12&t=OTsHCBkQOTNs1k3USz65Zg
- https://www.mandiant.com/resources/bypassing-network-restrictions-through-rdp-tunneling

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_rdp_to_http.yml)
