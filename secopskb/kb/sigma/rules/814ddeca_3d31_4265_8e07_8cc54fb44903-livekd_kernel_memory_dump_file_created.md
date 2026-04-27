---
sigma_id: "814ddeca-3d31-4265-8e07-8cc54fb44903"
title: "LiveKD Kernel Memory Dump File Created"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_sysinternals_livekd_default_dump_name.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_sysinternals_livekd_default_dump_name.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "814ddeca-3d31-4265-8e07-8cc54fb44903"
  - "LiveKD Kernel Memory Dump File Created"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# LiveKD Kernel Memory Dump File Created

Detects the creation of a file that has the same name as the default LiveKD kernel memory dump.

## Metadata

- Rule ID: 814ddeca-3d31-4265-8e07-8cc54fb44903
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-16
- Source Path: rules/windows/file/file_event/file_event_win_sysinternals_livekd_default_dump_name.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  TargetFilename: C:\Windows\livekd.dmp
condition: selection
```

## False Positives

- In rare occasions administrators might leverage LiveKD to perform live kernel debugging. This should not be allowed on production systems. Investigate and apply additional filters where necessary.

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_sysinternals_livekd_default_dump_name.yml)
