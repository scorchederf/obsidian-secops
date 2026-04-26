---
sigma_id: "7610a4ea-c06d-495f-a2ac-0a696abcfd3b"
title: "Outbound Network Connection To Public IP Via Winlogon"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_winlogon_net_connections.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_winlogon_net_connections.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / network_connection"
aliases:
  - "7610a4ea-c06d-495f-a2ac-0a696abcfd3b"
  - "Outbound Network Connection To Public IP Via Winlogon"
attack_technique_ids:
  - "T1218.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Outbound Network Connection To Public IP Via Winlogon

Detects a "winlogon.exe" process that initiate network communications with public IP addresses

## Metadata

- Rule ID: 7610a4ea-c06d-495f-a2ac-0a696abcfd3b
- Status: test
- Level: medium
- Author: Christopher Peacock @securepeacock, SCYTHE @scythe_io
- Date: 2023-04-28
- Modified: 2024-03-12
- Source Path: rules/windows/network_connection/net_connection_win_winlogon_net_connections.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Detection

```yaml
selection:
  Image|endswith: \winlogon.exe
  Initiated: 'true'
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

- Communication to other corporate systems that use IP addresses from public address spaces

## References

- https://www.microsoft.com/en-us/security/blog/2023/04/11/guidance-for-investigating-attacks-using-cve-2022-21894-the-blacklotus-campaign/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_winlogon_net_connections.yml)
