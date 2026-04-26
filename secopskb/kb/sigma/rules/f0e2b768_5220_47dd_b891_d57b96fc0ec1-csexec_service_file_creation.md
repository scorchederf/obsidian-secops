---
sigma_id: "f0e2b768-5220-47dd-b891-d57b96fc0ec1"
title: "CSExec Service File Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_csexec_service.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_csexec_service.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "f0e2b768-5220-47dd-b891-d57b96fc0ec1"
  - "CSExec Service File Creation"
attack_technique_ids:
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CSExec Service File Creation

Detects default CSExec service filename which indicates CSExec service installation and execution

## Metadata

- Rule ID: f0e2b768-5220-47dd-b891-d57b96fc0ec1
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-08-04
- Source Path: rules/windows/file/file_event/file_event_win_csexec_service.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1569-system_services|T1569.002]]

### Software Tags

- S0029

## Detection

```yaml
selection:
  TargetFilename|endswith: \csexecsvc.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/malcomvetter/CSExec

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_csexec_service.yml)
