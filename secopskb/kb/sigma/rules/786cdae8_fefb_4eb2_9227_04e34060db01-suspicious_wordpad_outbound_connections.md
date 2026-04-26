---
sigma_id: "786cdae8-fefb-4eb2-9227-04e34060db01"
title: "Suspicious Wordpad Outbound Connections"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_wordpad_uncommon_ports.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_wordpad_uncommon_ports.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / network_connection"
aliases:
  - "786cdae8-fefb-4eb2-9227-04e34060db01"
  - "Suspicious Wordpad Outbound Connections"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Wordpad Outbound Connections

Detects a network connection initiated by "wordpad.exe" over uncommon destination ports.
This might indicate potential process injection activity from a beacon or similar mechanisms.

## Metadata

- Rule ID: 786cdae8-fefb-4eb2-9227-04e34060db01
- Status: test
- Level: medium
- Author: X__Junior (Nextron Systems)
- Date: 2023-07-12
- Modified: 2023-12-15
- Source Path: rules/windows/network_connection/net_connection_win_wordpad_uncommon_ports.yml

## Logsource

- category: network_connection
- product: windows

## Detection

```yaml
selection:
  Initiated: 'true'
  Image|endswith: \wordpad.exe
filter_main_ports:
  DestinationPort:
  - 80
  - 139
  - 443
  - 445
  - 465
  - 587
  - 993
  - 995
condition: selection and not 1 of filter_main_*
```

## False Positives

- Other ports can be used, apply additional filters accordingly

## References

- https://blogs.blackberry.com/en/2023/07/romcom-targets-ukraine-nato-membership-talks-at-nato-summit

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_wordpad_uncommon_ports.yml)
