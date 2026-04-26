---
sigma_id: "c7e91a02-d771-4a6d-a700-42587e0b1095"
title: "Network Connection Initiated By Regsvr32.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_regsvr32_network_activity.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_regsvr32_network_activity.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / network_connection"
aliases:
  - "c7e91a02-d771-4a6d-a700-42587e0b1095"
  - "Network Connection Initiated By Regsvr32.EXE"
attack_technique_ids:
  - "T1559.001"
  - "T1218.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Network Connection Initiated By Regsvr32.EXE

Detects a network connection initiated by "Regsvr32.exe"

## Metadata

- Rule ID: c7e91a02-d771-4a6d-a700-42587e0b1095
- Status: test
- Level: medium
- Author: Dmitriy Lifanov, oscd.community
- Date: 2019-10-25
- Modified: 2023-09-18
- Source Path: rules/windows/network_connection/net_connection_win_regsvr32_network_activity.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1559-inter-process_communication|T1559.001]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.010]]

## Detection

```yaml
selection:
  Initiated: 'true'
  Image|endswith: \regsvr32.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://pentestlab.blog/2017/05/11/applocker-bypass-regsvr32/
- https://oddvar.moe/2017/12/13/applocker-case-study-how-insecure-is-it-really-part-1/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_regsvr32_network_activity.yml)
