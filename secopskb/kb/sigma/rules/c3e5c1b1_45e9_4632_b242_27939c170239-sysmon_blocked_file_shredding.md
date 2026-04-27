---
sigma_id: "c3e5c1b1-45e9-4632-b242-27939c170239"
title: "Sysmon Blocked File Shredding"
framework: "sigma"
generated: "true"
source_path: "rules/windows/sysmon/sysmon_file_block_shredding.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/sysmon/sysmon_file_block_shredding.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / sysmon"
aliases:
  - "c3e5c1b1-45e9-4632-b242-27939c170239"
  - "Sysmon Blocked File Shredding"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Sysmon Blocked File Shredding

Triggers on any Sysmon "FileBlockShredding" event, which indicates a violation of the configured shredding policy.

## Metadata

- Rule ID: c3e5c1b1-45e9-4632-b242-27939c170239
- Status: test
- Level: high
- Author: frack113
- Date: 2023-07-20
- Source Path: rules/windows/sysmon/sysmon_file_block_shredding.yml

## Logsource

- product: windows
- service: sysmon

## Detection

```yaml
selection:
  EventID: 28
condition: selection
```

## False Positives

- Unlikely

## References

- https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/sysmon/sysmon_file_block_shredding.yml)
