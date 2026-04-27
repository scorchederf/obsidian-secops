---
sigma_id: "8d7e392e-9b28-49e1-831d-5949c6281228"
title: "Network Connection Initiated By IMEWDBLD.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_imewdbld.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_imewdbld.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / network_connection"
aliases:
  - "8d7e392e-9b28-49e1-831d-5949c6281228"
  - "Network Connection Initiated By IMEWDBLD.EXE"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a network connection initiated by IMEWDBLD.EXE. This might indicate potential abuse of the utility as a LOLBIN in order to download arbitrary files or additional payloads.

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detection

```yaml
selection:
  Initiated: 'true'
  Image|endswith: \IMEWDBLD.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1105/T1105.md#atomic-test-10---windows---powershell-download
- https://lolbas-project.github.io/lolbas/Binaries/IMEWDBLD/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_imewdbld.yml)
