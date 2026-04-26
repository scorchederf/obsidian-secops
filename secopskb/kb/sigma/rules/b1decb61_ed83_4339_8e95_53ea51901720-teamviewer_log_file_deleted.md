---
sigma_id: "b1decb61-ed83-4339-8e95-53ea51901720"
title: "TeamViewer Log File Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_delete/file_delete_win_delete_teamviewer_logs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_delete/file_delete_win_delete_teamviewer_logs.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "low"
logsource: "windows / file_delete"
aliases:
  - "b1decb61-ed83-4339-8e95-53ea51901720"
  - "TeamViewer Log File Deleted"
attack_technique_ids:
  - "T1070.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# TeamViewer Log File Deleted

Detects the deletion of the TeamViewer log files which may indicate an attempt to destroy forensic evidence

## Metadata

- Rule ID: b1decb61-ed83-4339-8e95-53ea51901720
- Status: test
- Level: low
- Author: frack113
- Date: 2022-01-16
- Modified: 2023-02-15
- Source Path: rules/windows/file/file_delete/file_delete_win_delete_teamviewer_logs.yml

## Logsource

- category: file_delete
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.004]]

## Detection

```yaml
selection:
  TargetFilename|contains: \TeamViewer_
  TargetFilename|endswith: .log
filter:
  Image: C:\Windows\system32\svchost.exe
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1070.004/T1070.004.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_delete/file_delete_win_delete_teamviewer_logs.yml)
