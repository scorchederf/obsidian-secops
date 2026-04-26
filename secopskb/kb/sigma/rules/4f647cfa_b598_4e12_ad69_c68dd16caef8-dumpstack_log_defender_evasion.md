---
sigma_id: "4f647cfa-b598-4e12-ad69-c68dd16caef8"
title: "DumpStack.log Defender Evasion"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_dumpstack_log_evasion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_dumpstack_log_evasion.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "critical"
logsource: "windows / process_creation"
aliases:
  - "4f647cfa-b598-4e12-ad69-c68dd16caef8"
  - "DumpStack.log Defender Evasion"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# DumpStack.log Defender Evasion

Detects the use of the filename DumpStack.log to evade Microsoft Defender

## Metadata

- Rule ID: 4f647cfa-b598-4e12-ad69-c68dd16caef8
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems)
- Date: 2022-01-06
- Modified: 2022-06-17
- Source Path: rules/windows/process_creation/proc_creation_win_susp_dumpstack_log_evasion.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  Image|endswith: \DumpStack.log
selection_download:
  CommandLine|contains: ' -o DumpStack.log'
condition: 1 of selection*
```

## False Positives

- Unknown

## References

- https://twitter.com/mrd0x/status/1479094189048713219

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_dumpstack_log_evasion.yml)
