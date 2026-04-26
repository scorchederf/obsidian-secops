---
sigma_id: "992a6cae-db6a-43c8-9cec-76d7195c96fc"
title: "Outbound Network Connection Initiated By Script Interpreter"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_wscript_cscript_outbound_connection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_wscript_cscript_outbound_connection.yml"
build_date: "2026-04-26 15:01:47"
status: "test"
level: "high"
logsource: "windows / network_connection"
aliases:
  - "992a6cae-db6a-43c8-9cec-76d7195c96fc"
  - "Outbound Network Connection Initiated By Script Interpreter"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Outbound Network Connection Initiated By Script Interpreter

Detects a script interpreter wscript/cscript opening a network connection to a non-local network. Adversaries may use script to download malicious payloads.

## Metadata

- Rule ID: 992a6cae-db6a-43c8-9cec-76d7195c96fc
- Status: test
- Level: high
- Author: frack113, Florian Roth (Nextron Systems)
- Date: 2022-08-28
- Modified: 2024-03-13
- Source Path: rules/windows/network_connection/net_connection_win_wscript_cscript_outbound_connection.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection:
  Initiated: 'true'
  Image|endswith:
  - \wscript.exe
  - \cscript.exe
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
  DestinationIp|cidr: 20.0.0.0/11
condition: selection and not 1 of filter_main_*
```

## False Positives

- Legitimate scripts

## References

- https://github.com/redcanaryco/atomic-red-team/blob/28d190330fe44de6ff4767fc400cc10fa7cd6540/atomics/T1105/T1105.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_wscript_cscript_outbound_connection.yml)
