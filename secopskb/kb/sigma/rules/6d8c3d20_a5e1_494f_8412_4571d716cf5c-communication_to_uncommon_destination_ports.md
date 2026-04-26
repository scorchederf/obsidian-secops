---
sigma_id: "6d8c3d20-a5e1-494f-8412-4571d716cf5c"
title: "Communication To Uncommon Destination Ports"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_susp_malware_callback_ports_uncommon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_susp_malware_callback_ports_uncommon.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / network_connection"
aliases:
  - "6d8c3d20-a5e1-494f-8412-4571d716cf5c"
  - "Communication To Uncommon Destination Ports"
attack_technique_ids:
  - "T1571"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Communication To Uncommon Destination Ports

Detects programs that connect to uncommon destination ports

## Metadata

- Rule ID: 6d8c3d20-a5e1-494f-8412-4571d716cf5c
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2017-03-19
- Modified: 2024-03-12
- Source Path: rules/windows/network_connection/net_connection_win_susp_malware_callback_ports_uncommon.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1571-non-standard_port|T1571]]

## Detection

```yaml
selection:
  Initiated: 'true'
  DestinationPort:
  - 8080
  - 8888
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
filter_optional_sys_directories:
  Image|startswith:
  - C:\Program Files\
  - C:\Program Files (x86)\
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://docs.google.com/spreadsheets/d/17pSTDNpa0sf6pHeRhusvWG6rThciE8CsXTSlDUAZDyo

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_susp_malware_callback_ports_uncommon.yml)
