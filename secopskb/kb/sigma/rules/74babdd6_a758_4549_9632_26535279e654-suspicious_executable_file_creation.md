---
sigma_id: "74babdd6-a758-4549-9632-26535279e654"
title: "Suspicious Executable File Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_executable_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_executable_creation.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "74babdd6-a758-4549-9632-26535279e654"
  - "Suspicious Executable File Creation"
attack_technique_ids:
  - "T1564"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Executable File Creation

Detect creation of suspicious executable file names.
Some strings look for suspicious file extensions, others look for filenames that exploit unquoted service paths.

## Metadata

- Rule ID: 74babdd6-a758-4549-9632-26535279e654
- Status: test
- Level: high
- Author: frack113
- Date: 2022-09-05
- Modified: 2023-12-11
- Source Path: rules/windows/file/file_event/file_event_win_susp_executable_creation.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564]]

## Detection

```yaml
selection:
  TargetFilename|endswith:
  - :\$Recycle.Bin.exe
  - :\Documents and Settings.exe
  - :\MSOCache.exe
  - :\PerfLogs.exe
  - :\Recovery.exe
  - .bat.exe
  - .sys.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://medium.com/@SumitVerma101/windows-privilege-escalation-part-1-unquoted-service-path-c7a011a8d8ae
- https://app.any.run/tasks/76c69e2d-01e8-49d9-9aea-fb7cc0c4d3ad/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_executable_creation.yml)
