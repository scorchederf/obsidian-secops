---
sigma_id: "cad1fe90-2406-44dc-bd03-59d0b58fe722"
title: "HackTool - NPPSpy Hacktool Usage"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_hktl_nppspy.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_hktl_nppspy.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "cad1fe90-2406-44dc-bd03-59d0b58fe722"
  - "HackTool - NPPSpy Hacktool Usage"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# HackTool - NPPSpy Hacktool Usage

Detects the use of NPPSpy hacktool that stores cleartext passwords of users that logged in to a local file

## Metadata

- Rule ID: cad1fe90-2406-44dc-bd03-59d0b58fe722
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-11-29
- Modified: 2024-06-27
- Source Path: rules/windows/file/file_event/file_event_win_hktl_nppspy.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  TargetFilename|endswith:
  - \NPPSpy.txt
  - \NPPSpy.dll
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1003/T1003.md#atomic-test-2---credential-dumping-with-nppspy
- https://twitter.com/0gtweet/status/1465282548494487554

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_hktl_nppspy.yml)
