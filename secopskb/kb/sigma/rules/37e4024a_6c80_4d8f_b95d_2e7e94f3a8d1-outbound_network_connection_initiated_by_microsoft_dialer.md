---
sigma_id: "37e4024a-6c80-4d8f-b95d-2e7e94f3a8d1"
title: "Outbound Network Connection Initiated By Microsoft Dialer"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_dialer_initiated_connection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_dialer_initiated_connection.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / network_connection"
aliases:
  - "37e4024a-6c80-4d8f-b95d-2e7e94f3a8d1"
  - "Outbound Network Connection Initiated By Microsoft Dialer"
attack_technique_ids:
  - "T1071.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects outbound network connection initiated by Microsoft Dialer.
The Microsoft Dialer, also known as Phone Dialer, is a built-in utility application included in various versions of the Microsoft Windows operating system. Its primary function is to provide users with a graphical interface for managing phone calls via a modem or a phone line connected to the computer.
This is an outdated process in the current conext of it's usage and is a common target for info stealers for process injection, and is used to make C2 connections, common example is "Rhadamanthys"

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]]

## Detection

```yaml
selection:
  Image|endswith: :\Windows\System32\dialer.exe
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

- In Modern Windows systems, unable to see legitimate usage of this process, However, if an organization has legitimate purpose for this there can be false positives.

## References

- https://tria.ge/240301-rk34sagf5x/behavioral2
- https://app.any.run/tasks/6720b85b-9c53-4a12-b1dc-73052a78477d
- https://research.checkpoint.com/2023/rhadamanthys-v0-5-0-a-deep-dive-into-the-stealers-components/
- https://strontic.github.io/xcyclopedia/library/dialer.exe-0B69655F912619756C704A0BF716B61F.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_dialer_initiated_connection.yml)
