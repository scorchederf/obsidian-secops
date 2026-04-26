---
sigma_id: "20384606-a124-4fec-acbb-8bd373728613"
title: "Suspicious Network Connection Binary No CommandLine"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_susp_binary_no_cmdline.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_susp_binary_no_cmdline.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "high"
logsource: "windows / network_connection"
aliases:
  - "20384606-a124-4fec-acbb-8bd373728613"
  - "Suspicious Network Connection Binary No CommandLine"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Network Connection Binary No CommandLine

Detects suspicious network connections made by a well-known Windows binary run with no command line parameters

## Metadata

- Rule ID: 20384606-a124-4fec-acbb-8bd373728613
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-07-03
- Source Path: rules/windows/network_connection/net_connection_win_susp_binary_no_cmdline.yml

## Logsource

- category: network_connection
- product: windows

## Detection

```yaml
selection:
  Initiated: 'true'
  Image|endswith:
  - \regsvr32.exe
  - \rundll32.exe
  - \dllhost.exe
  CommandLine|endswith:
  - \regsvr32.exe
  - \rundll32.exe
  - \dllhost.exe
filter_no_cmdline:
  CommandLine: ''
filter_null:
  CommandLine: null
condition: selection and not 1 of filter*
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/raspberry-robin/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_susp_binary_no_cmdline.yml)
