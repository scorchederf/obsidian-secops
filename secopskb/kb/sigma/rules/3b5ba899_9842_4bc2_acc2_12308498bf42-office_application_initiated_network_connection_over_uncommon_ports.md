---
sigma_id: "3b5ba899-9842-4bc2-acc2-12308498bf42"
title: "Office Application Initiated Network Connection Over Uncommon Ports"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_office_uncommon_ports.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_office_uncommon_ports.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / network_connection"
aliases:
  - "3b5ba899-9842-4bc2-acc2-12308498bf42"
  - "Office Application Initiated Network Connection Over Uncommon Ports"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Office Application Initiated Network Connection Over Uncommon Ports

Detects an office suit application (Word, Excel, PowerPoint, Outlook) communicating to target systems over uncommon ports.

## Metadata

- Rule ID: 3b5ba899-9842-4bc2-acc2-12308498bf42
- Status: test
- Level: medium
- Author: X__Junior (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-07-12
- Modified: 2025-10-17
- Source Path: rules/windows/network_connection/net_connection_win_office_uncommon_ports.yml

## Logsource

- category: network_connection
- product: windows

## Detection

```yaml
selection:
  Initiated: 'true'
  Image|endswith:
  - \excel.exe
  - \outlook.exe
  - \powerpnt.exe
  - \winword.exe
  - \wordview.exe
filter_main_common_ports:
  DestinationPort:
  - 53
  - 80
  - 139
  - 389
  - 443
  - 445
  - 3268
filter_main_outlook_ports:
  Image|contains: :\Program Files\Microsoft Office\
  Image|endswith: \OUTLOOK.EXE
  DestinationPort:
  - 143
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_office_uncommon_ports.yml)
