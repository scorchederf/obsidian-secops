---
sigma_id: "6c304b02-06e6-402d-8be4-d5833cdf8198"
title: "Potential SentinelOne Shell Context Menu Scan Command Tampering"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_sentinelone_shell_context_tampering.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_sentinelone_shell_context_tampering.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "6c304b02-06e6-402d-8be4-d5833cdf8198"
  - "Potential SentinelOne Shell Context Menu Scan Command Tampering"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential SentinelOne Shell Context Menu Scan Command Tampering

Detects potentially suspicious changes to the SentinelOne context menu scan command by a process other than SentinelOne.

## Metadata

- Rule ID: 6c304b02-06e6-402d-8be4-d5833cdf8198
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2024-03-06
- Source Path: rules/windows/registry/registry_set/registry_set_sentinelone_shell_context_tampering.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection:
  TargetObject|contains: \shell\SentinelOneScan\command\
filter_main_sentinelone_default_scan_binary:
  Details|startswith:
  - C:\Program Files\SentinelOne\Sentinel Agent
  - C:\Program Files (x86)\SentinelOne\Sentinel Agent
  Details|contains: \SentinelScanFromContextMenu.exe
filter_main_sentinelone_binary:
  Image|endswith:
  - C:\Program Files\SentinelOne\
  - C:\Program Files (x86)\SentinelOne\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://mrd0x.com/sentinelone-persistence-via-menu-context/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_sentinelone_shell_context_tampering.yml)
