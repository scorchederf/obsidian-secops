---
sigma_id: "8c3c76ca-8f8b-4b1d-aaf3-81aebcd367c9"
title: "Creation Exe for Service with Unquoted Path"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_creation_unquoted_service_path.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_creation_unquoted_service_path.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "8c3c76ca-8f8b-4b1d-aaf3-81aebcd367c9"
  - "Creation Exe for Service with Unquoted Path"
attack_technique_ids:
  - "T1547.009"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Creation Exe for Service with Unquoted Path

Adversaries may execute their own malicious payloads by hijacking vulnerable file path references.
Adversaries can take advantage of paths that lack surrounding quotations by placing an executable in a higher level directory within the path, so that Windows will choose the adversary's executable to launch.

## Metadata

- Rule ID: 8c3c76ca-8f8b-4b1d-aaf3-81aebcd367c9
- Status: test
- Level: high
- Author: frack113
- Date: 2021-12-30
- Source Path: rules/windows/file/file_event/file_event_win_creation_unquoted_service_path.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.009]]

## Detection

```yaml
selection:
  TargetFilename: C:\program.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1574.009/T1574.009.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_creation_unquoted_service_path.yml)
