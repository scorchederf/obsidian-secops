---
sigma_id: "a05baa88-e922-4001-bc4d-8738135f27de"
title: "Process Monitor Driver Creation By Non-Sysinternals Binary"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_sysinternals_procmon_driver_susp_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_sysinternals_procmon_driver_susp_creation.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "a05baa88-e922-4001-bc4d-8738135f27de"
  - "Process Monitor Driver Creation By Non-Sysinternals Binary"
attack_technique_ids:
  - "T1068"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Process Monitor Driver Creation By Non-Sysinternals Binary

Detects creation of the Process Monitor driver by processes other than Process Monitor (procmon) itself.

## Metadata

- Rule ID: a05baa88-e922-4001-bc4d-8738135f27de
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-05
- Source Path: rules/windows/file/file_event/file_event_win_sysinternals_procmon_driver_susp_creation.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1068-exploitation_for_privilege_escalation|T1068]]

## Detection

```yaml
selection:
  TargetFilename|contains: \procmon
  TargetFilename|endswith: .sys
filter_main_process_explorer:
  Image|endswith:
  - \procmon.exe
  - \procmon64.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Some false positives may occur with legitimate renamed process monitor binaries

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_sysinternals_procmon_driver_susp_creation.yml)
