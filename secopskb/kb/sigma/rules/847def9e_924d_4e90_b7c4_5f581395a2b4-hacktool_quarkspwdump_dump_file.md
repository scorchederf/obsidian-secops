---
sigma_id: "847def9e-924d-4e90-b7c4-5f581395a2b4"
title: "HackTool - QuarksPwDump Dump File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_hktl_quarkspw_filedump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_hktl_quarkspw_filedump.yml"
build_date: "2026-04-27 19:13:51"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a dump file written by QuarksPwDump password dumper

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]

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
