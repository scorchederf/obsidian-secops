---
sigma_id: "cdc8da7d-c303-42f8-b08c-b4ab47230263"
title: "Rundll32 Internet Connection"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_rundll32_net_connections.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_rundll32_net_connections.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / network_connection"
aliases:
  - "cdc8da7d-c303-42f8-b08c-b4ab47230263"
  - "Rundll32 Internet Connection"
attack_technique_ids:
  - "T1218.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Rundll32 Internet Connection

Detects a rundll32 that communicates with public IP addresses

## Metadata

- Rule ID: cdc8da7d-c303-42f8-b08c-b4ab47230263
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2017-11-04
- Modified: 2024-03-13
- Source Path: rules/windows/network_connection/net_connection_win_rundll32_net_connections.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Detection

```yaml
selection:
  Image|endswith: \rundll32.exe
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
filter_main_ms_ranges:
  DestinationIp|cidr:
  - 20.0.0.0/8
  - 51.103.0.0/16
  - 51.104.0.0/16
  - 51.105.0.0/16
filter_main_app_sdb:
  CommandLine|endswith: \system32\PcaSvc.dll,PcaPatchSdbTask
filter_main_azure_managed:
  SourceHostname|endswith: .internal.cloudapp.net
filter_main_svchost_update_processes:
  ParentImage: C:\Windows\System32\svchost.exe
  DestinationPort: 443
condition: selection and not 1 of filter_main_*
```

## False Positives

- Communication to other corporate systems that use IP addresses from public address spaces

## References

- https://www.hybrid-analysis.com/sample/759fb4c0091a78c5ee035715afe3084686a8493f39014aea72dae36869de9ff6?environmentId=100

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_rundll32_net_connections.yml)
