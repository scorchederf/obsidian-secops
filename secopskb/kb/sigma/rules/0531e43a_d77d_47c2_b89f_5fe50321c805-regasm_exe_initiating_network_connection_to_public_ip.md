---
sigma_id: "0531e43a-d77d-47c2-b89f-5fe50321c805"
title: "RegAsm.EXE Initiating Network Connection To Public IP"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_regasm_network_activity.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_regasm_network_activity.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / network_connection"
aliases:
  - "0531e43a-d77d-47c2-b89f-5fe50321c805"
  - "RegAsm.EXE Initiating Network Connection To Public IP"
attack_technique_ids:
  - "T1218.009"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# RegAsm.EXE Initiating Network Connection To Public IP

Detects "RegAsm.exe" initiating a network connection to public IP adresses

## Metadata

- Rule ID: 0531e43a-d77d-47c2-b89f-5fe50321c805
- Status: test
- Level: medium
- Author: frack113
- Date: 2024-04-25
- Source Path: rules/windows/network_connection/net_connection_win_regasm_network_activity.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.009]]

## Detection

```yaml
selection:
  Initiated: 'true'
  Image|endswith: \regasm.exe
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

- https://app.any.run/tasks/ec207948-4916-47eb-a0f4-4c6abb2e7668/
- https://research.splunk.com/endpoint/07921114-6db4-4e2e-ae58-3ea8a52ae93f/
- https://lolbas-project.github.io/lolbas/Binaries/Regasm/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_regasm_network_activity.yml)
