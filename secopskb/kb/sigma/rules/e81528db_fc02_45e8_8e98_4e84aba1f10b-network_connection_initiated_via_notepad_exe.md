---
sigma_id: "e81528db-fc02-45e8-8e98-4e84aba1f10b"
title: "Network Connection Initiated Via Notepad.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_notepad.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_notepad.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / network_connection"
aliases:
  - "e81528db-fc02-45e8-8e98-4e84aba1f10b"
  - "Network Connection Initiated Via Notepad.EXE"
attack_technique_ids:
  - "T1055"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Network Connection Initiated Via Notepad.EXE

Detects a network connection that is initiated by the "notepad.exe" process.
This might be a sign of process injection from a beacon process or something similar.
Notepad rarely initiates a network communication except when printing documents for example.

## Metadata

- Rule ID: e81528db-fc02-45e8-8e98-4e84aba1f10b
- Status: test
- Level: high
- Author: EagleEye Team
- Date: 2020-05-14
- Modified: 2024-02-02
- Source Path: rules/windows/network_connection/net_connection_win_notepad.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055]]

## Detection

```yaml
selection:
  Image|endswith: \notepad.exe
filter_optional_printing:
  DestinationPort: 9100
condition: selection and not 1 of filter_optional_*
```

## False Positives

- Printing documents via notepad might cause communication with the printer via port 9100 or similar.

## References

- https://web.archive.org/web/20200219102749/https://www.sans.org/cyber-security-summit/archives/file/summit-archive-1492186586.pdf
- https://www.cobaltstrike.com/blog/why-is-notepad-exe-connecting-to-the-internet

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_notepad.yml)
