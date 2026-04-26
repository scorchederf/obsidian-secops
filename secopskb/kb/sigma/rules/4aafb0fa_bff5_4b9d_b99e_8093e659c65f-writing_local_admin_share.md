---
sigma_id: "4aafb0fa-bff5-4b9d-b99e-8093e659c65f"
title: "Writing Local Admin Share"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_writing_local_admin_share.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_writing_local_admin_share.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "4aafb0fa-bff5-4b9d-b99e-8093e659c65f"
  - "Writing Local Admin Share"
attack_technique_ids:
  - "T1546.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Writing Local Admin Share

Aversaries may use to interact with a remote network share using Server Message Block (SMB).
This technique is used by post-exploitation frameworks.

## Metadata

- Rule ID: 4aafb0fa-bff5-4b9d-b99e-8093e659c65f
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-01
- Modified: 2022-08-13
- Source Path: rules/windows/file/file_event/file_event_win_writing_local_admin_share.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.002]]

## Detection

```yaml
selection:
  TargetFilename|contains|all:
  - \\\\127.0.0
  - \ADMIN$\
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1021.002/T1021.002.md#atomic-test-4---execute-command-writing-output-to-local-admin-share

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_writing_local_admin_share.yml)
