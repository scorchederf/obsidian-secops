---
sigma_id: "a66bc059-c370-472c-a0d7-f8fd1bf9d583"
title: "Network Connection Initiated By Eqnedt32.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_eqnedt.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_eqnedt.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / network_connection"
aliases:
  - "a66bc059-c370-472c-a0d7-f8fd1bf9d583"
  - "Network Connection Initiated By Eqnedt32.EXE"
attack_technique_ids:
  - "T1203"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects network connections from the Equation Editor process "eqnedt32.exe".

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1203-exploitation_for_client_execution|T1203: Exploitation for Client Execution]]

## Detection

```yaml
selection:
  Image|endswith: \eqnedt32.exe
condition: selection
```

## False Positives

- Unlikely

## References

- https://twitter.com/forensicitguy/status/1513538712986079238
- https://forensicitguy.github.io/xloader-formbook-velvetsweatshop-spreadsheet/
- https://news.sophos.com/en-us/2019/07/18/a-new-equation-editor-exploit-goes-commercial-as-maldoc-attacks-using-it-spike/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_eqnedt.yml)
