---
sigma_id: "736ffa74-5f6f-44ca-94ef-1c0df4f51d2a"
title: "HackTool - CrackMapExec File Indicators"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_hktl_crackmapexec_indicators.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_hktl_crackmapexec_indicators.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "736ffa74-5f6f-44ca-94ef-1c0df4f51d2a"
  - "HackTool - CrackMapExec File Indicators"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - CrackMapExec File Indicators

Detects file creation events with filename patterns used by CrackMapExec.

## Metadata

- Rule ID: 736ffa74-5f6f-44ca-94ef-1c0df4f51d2a
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2024-03-11
- Modified: 2024-06-27
- Source Path: rules/windows/file/file_event/file_event_win_hktl_crackmapexec_indicators.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection_path:
  TargetFilename|startswith: C:\Windows\Temp\
selection_names_str:
  TargetFilename|endswith:
  - \temp.ps1
  - \msol.ps1
selection_names_re:
- TargetFilename|re: \\[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\.txt$
- TargetFilename|re: \\[a-zA-Z]{8}\.tmp$
condition: selection_path and 1 of selection_names_*
```

## False Positives

- Unknown

## References

- https://github.com/byt3bl33d3r/CrackMapExec/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_hktl_crackmapexec_indicators.yml)
