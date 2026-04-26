---
sigma_id: "63c779ba-f638-40a0-a593-ddd45e8b1ddc"
title: "EventLog EVTX File Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_delete/file_delete_win_delete_event_log_files.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_delete/file_delete_win_delete_event_log_files.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / file_delete"
aliases:
  - "63c779ba-f638-40a0-a593-ddd45e8b1ddc"
  - "EventLog EVTX File Deleted"
attack_technique_ids:
  - "T1070"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# EventLog EVTX File Deleted

Detects the deletion of the event log files which may indicate an attempt to destroy forensic evidence

## Metadata

- Rule ID: 63c779ba-f638-40a0-a593-ddd45e8b1ddc
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-15
- Source Path: rules/windows/file/file_delete/file_delete_win_delete_event_log_files.yml

## Logsource

- category: file_delete
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070]]

## Detection

```yaml
selection:
  TargetFilename|startswith: C:\Windows\System32\winevt\Logs\
  TargetFilename|endswith: .evtx
condition: selection
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_delete/file_delete_win_delete_event_log_files.yml)
