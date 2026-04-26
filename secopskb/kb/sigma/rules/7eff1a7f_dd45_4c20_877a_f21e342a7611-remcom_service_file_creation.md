---
sigma_id: "7eff1a7f-dd45-4c20-877a-f21e342a7611"
title: "RemCom Service File Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_remcom_service.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_remcom_service.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "7eff1a7f-dd45-4c20-877a-f21e342a7611"
  - "RemCom Service File Creation"
attack_technique_ids:
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# RemCom Service File Creation

Detects default RemCom service filename which indicates RemCom service installation and execution

## Metadata

- Rule ID: 7eff1a7f-dd45-4c20-877a-f21e342a7611
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-08-04
- Source Path: rules/windows/file/file_event/file_event_win_remcom_service.yml

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
  TargetFilename|endswith: \RemComSvc.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/kavika13/RemCom/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_remcom_service.yml)
