---
sigma_id: "5205613d-2a63-4412-a895-3a2458b587b3"
title: "Network Connection Initiated By AddinUtil.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_addinutil_initiated.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_addinutil_initiated.yml"
build_date: "2026-04-27 19:13:53"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a network connection initiated by the Add-In deployment cache updating utility "AddInutil.exe".
This could indicate a potential command and control communication as this tool doesn't usually initiate network activity.

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

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
