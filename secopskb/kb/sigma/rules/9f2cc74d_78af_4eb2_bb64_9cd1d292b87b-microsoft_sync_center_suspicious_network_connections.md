---
sigma_id: "9f2cc74d-78af-4eb2-bb64-9cd1d292b87b"
title: "Microsoft Sync Center Suspicious Network Connections"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_susp_outbound_mobsync_connection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_susp_outbound_mobsync_connection.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / network_connection"
aliases:
  - "9f2cc74d-78af-4eb2-bb64-9cd1d292b87b"
  - "Microsoft Sync Center Suspicious Network Connections"
attack_technique_ids:
  - "T1055"
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Microsoft Sync Center Suspicious Network Connections

Detects suspicious connections from Microsoft Sync Center to non-private IPs.

## Metadata

- Rule ID: 9f2cc74d-78af-4eb2-bb64-9cd1d292b87b
- Status: test
- Level: medium
- Author: elhoim
- Date: 2022-04-28
- Modified: 2024-03-12
- Source Path: rules/windows/network_connection/net_connection_win_susp_outbound_mobsync_connection.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  Image|endswith: \mobsync.exe
filter_main_local_ranges:
  DestinationIp|cidr:
  - 127.0.0.0/8
  - 10.0.0.0/8
  - 172.16.0.0/12
  - 192.168.0.0/16
  - 169.254.0.0/16
  - ::1/128
  - fe80::/10
  - fc00::/7
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/intelligence-insights-november-2021/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_susp_outbound_mobsync_connection.yml)
