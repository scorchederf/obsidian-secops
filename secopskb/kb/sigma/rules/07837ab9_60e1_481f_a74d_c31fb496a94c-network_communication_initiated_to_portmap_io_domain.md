---
sigma_id: "07837ab9-60e1-481f-a74d-c31fb496a94c"
title: "Network Communication Initiated To Portmap.IO Domain"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_domain_portmap.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_portmap.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / network_connection"
aliases:
  - "07837ab9-60e1-481f-a74d-c31fb496a94c"
  - "Network Communication Initiated To Portmap.IO Domain"
attack_technique_ids:
  - "T1041"
  - "T1090.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Network Communication Initiated To Portmap.IO Domain

Detects an executable accessing the portmap.io domain, which could be a sign of forbidden C2 traffic or data exfiltration by malicious actors

## Metadata

- Rule ID: 07837ab9-60e1-481f-a74d-c31fb496a94c
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2024-05-31
- Source Path: rules/windows/network_connection/net_connection_win_domain_portmap.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1041-exfiltration_over_c2_channel|T1041]]
- [[kb/attack/techniques/T1090-proxy|T1090.002]]

## Detection

```yaml
selection:
  Initiated: 'true'
  DestinationHostname|endswith: .portmap.io
condition: selection
```

## False Positives

- Legitimate use of portmap.io domains

## References

- https://portmap.io/
- https://github.com/rapid7/metasploit-framework/issues/11337
- https://pro.twitter.com/JaromirHorejsi/status/1795001037746761892/photo/2

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_portmap.yml)
