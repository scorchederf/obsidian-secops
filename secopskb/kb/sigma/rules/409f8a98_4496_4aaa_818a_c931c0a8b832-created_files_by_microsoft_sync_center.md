---
sigma_id: "409f8a98-4496-4aaa-818a-c931c0a8b832"
title: "Created Files by Microsoft Sync Center"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_creation_by_mobsync.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_creation_by_mobsync.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "409f8a98-4496-4aaa-818a-c931c0a8b832"
  - "Created Files by Microsoft Sync Center"
attack_technique_ids:
  - "T1055"
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Created Files by Microsoft Sync Center

This rule detects suspicious files created by Microsoft Sync Center (mobsync)

## Metadata

- Rule ID: 409f8a98-4496-4aaa-818a-c931c0a8b832
- Status: test
- Level: medium
- Author: elhoim
- Date: 2022-04-28
- Modified: 2022-06-02
- Source Path: rules/windows/file/file_event/file_event_win_susp_creation_by_mobsync.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_mobsync:
  Image|endswith: \mobsync.exe
filter_created_file:
  TargetFilename|endswith:
  - .dll
  - .exe
condition: selection_mobsync and filter_created_file
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/intelligence-insights-november-2021/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_creation_by_mobsync.yml)
