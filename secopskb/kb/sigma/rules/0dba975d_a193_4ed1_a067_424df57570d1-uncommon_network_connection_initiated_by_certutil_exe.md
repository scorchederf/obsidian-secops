---
sigma_id: "0dba975d-a193-4ed1-a067-424df57570d1"
title: "Uncommon Network Connection Initiated By Certutil.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_certutil_initiated_connection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_certutil_initiated_connection.yml"
build_date: "2026-04-27 19:13:58"
status: "test"
level: "high"
logsource: "windows / network_connection"
aliases:
  - "0dba975d-a193-4ed1-a067-424df57570d1"
  - "Uncommon Network Connection Initiated By Certutil.EXE"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a network connection initiated by the certutil.exe utility.
Attackers can abuse the utility in order to download malware or additional payloads.

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detection

```yaml
selection:
  Image|endswith: \certutil.exe
  Initiated: 'true'
  DestinationPort:
  - 80
  - 135
  - 443
  - 445
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/certutil

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_certutil_initiated_connection.yml)
