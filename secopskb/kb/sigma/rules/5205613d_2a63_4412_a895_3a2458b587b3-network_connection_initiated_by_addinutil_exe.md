---
sigma_id: "5205613d-2a63-4412-a895-3a2458b587b3"
title: "Network Connection Initiated By AddinUtil.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_addinutil_initiated.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_addinutil_initiated.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / network_connection"
aliases:
  - "5205613d-2a63-4412-a895-3a2458b587b3"
  - "Network Connection Initiated By AddinUtil.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Network Connection Initiated By AddinUtil.EXE

Detects a network connection initiated by the Add-In deployment cache updating utility "AddInutil.exe".
This could indicate a potential command and control communication as this tool doesn't usually initiate network activity.

## Metadata

- Rule ID: 5205613d-2a63-4412-a895-3a2458b587b3
- Status: test
- Level: high
- Author: Michael McKinley (@McKinleyMike), Tony Latteri (@TheLatteri)
- Date: 2023-09-18
- Modified: 2024-07-16
- Source Path: rules/windows/network_connection/net_connection_win_addinutil_initiated.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  Initiated: 'true'
  Image|endswith: \addinutil.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://www.blue-prints.blog/content/blog/posts/lolbin/addinutil-lolbas.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_addinutil_initiated.yml)
