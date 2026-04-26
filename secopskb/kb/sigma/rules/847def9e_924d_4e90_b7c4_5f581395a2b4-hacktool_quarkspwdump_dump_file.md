---
sigma_id: "847def9e-924d-4e90-b7c4-5f581395a2b4"
title: "HackTool - QuarksPwDump Dump File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_hktl_quarkspw_filedump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_hktl_quarkspw_filedump.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "critical"
logsource: "windows / file_event"
aliases:
  - "847def9e-924d-4e90-b7c4-5f581395a2b4"
  - "HackTool - QuarksPwDump Dump File"
attack_technique_ids:
  - "T1003.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - QuarksPwDump Dump File

Detects a dump file written by QuarksPwDump password dumper

## Metadata

- Rule ID: 847def9e-924d-4e90-b7c4-5f581395a2b4
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems)
- Date: 2018-02-10
- Modified: 2024-06-27
- Source Path: rules/windows/file/file_event/file_event_win_hktl_quarkspw_filedump.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]

## Detection

```yaml
selection:
  TargetFilename|contains|all:
  - \AppData\Local\Temp\SAM-
  - .dmp
condition: selection
```

## False Positives

- Unknown

## References

- https://jpcertcc.github.io/ToolAnalysisResultSheet/details/QuarksPWDump.htm

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_hktl_quarkspw_filedump.yml)
