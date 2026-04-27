---
sigma_id: "efafe0bf-4238-479e-af8f-797bd3490d2d"
title: "Outbound Network Connection Initiated By Cmstp.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_cmstp_initiated_connection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_cmstp_initiated_connection.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / network_connection"
aliases:
  - "efafe0bf-4238-479e-af8f-797bd3490d2d"
  - "Outbound Network Connection Initiated By Cmstp.EXE"
attack_technique_ids:
  - "T1218.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a network connection initiated by Cmstp.EXE
Its uncommon for "cmstp.exe" to initiate an outbound network connection. Investigate the source of such requests to determine if they are malicious.

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218003-cmstp|T1218.003: CMSTP]]

## Detection

```yaml
selection:
  Image|endswith: \cmstp.exe
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

- Unknown

## References

- https://web.archive.org/web/20190720093911/http://www.endurant.io/cmstp/detecting-cmstp-enabled-code-execution-and-uac-bypass-with-sysmon/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_cmstp_initiated_connection.yml)
