---
sigma_id: "08249dc0-a28d-4555-8ba5-9255a198e08c"
title: "Local Network Connection Initiated By Script Interpreter"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_wscript_cscript_local_connection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_wscript_cscript_local_connection.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "windows / network_connection"
aliases:
  - "08249dc0-a28d-4555-8ba5-9255a198e08c"
  - "Local Network Connection Initiated By Script Interpreter"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Local Network Connection Initiated By Script Interpreter

Detects a script interpreter (Wscript/Cscript) initiating a local network connection to download or execute a script hosted on a shared folder.

## Metadata

- Rule ID: 08249dc0-a28d-4555-8ba5-9255a198e08c
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-08-28
- Modified: 2024-05-31
- Source Path: rules/windows/network_connection/net_connection_win_wscript_cscript_local_connection.yml

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
  DestinationIp|cidr:
  - 127.0.0.0/8
  - 10.0.0.0/8
  - 172.16.0.0/12
  - 192.168.0.0/16
  - 169.254.0.0/16
  - ::1/128
  - fe80::/10
  - fc00::/7
condition: selection
```

## False Positives

- Legitimate scripts

## References

- https://github.com/redcanaryco/atomic-red-team/blob/28d190330fe44de6ff4767fc400cc10fa7cd6540/atomics/T1105/T1105.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_wscript_cscript_local_connection.yml)
