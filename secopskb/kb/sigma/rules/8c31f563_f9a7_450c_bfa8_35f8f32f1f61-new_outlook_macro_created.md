---
sigma_id: "8c31f563-f9a7-450c-bfa8-35f8f32f1f61"
title: "New Outlook Macro Created"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_office_outlook_macro_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_outlook_macro_creation.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "8c31f563-f9a7-450c-bfa8-35f8f32f1f61"
  - "New Outlook Macro Created"
attack_technique_ids:
  - "T1137"
  - "T1008"
  - "T1546"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Outlook Macro Created

Detects the creation of a macro file for Outlook.

## Metadata

- Rule ID: 8c31f563-f9a7-450c-bfa8-35f8f32f1f61
- Status: test
- Level: medium
- Author: @ScoubiMtl
- Date: 2021-04-05
- Modified: 2023-02-08
- Source Path: rules/windows/file/file_event/file_event_win_office_outlook_macro_creation.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1137-office_application_startup|T1137]]
- [[kb/attack/techniques/T1008-fallback_channels|T1008]]
- [[kb/attack/techniques/T1546-event_triggered_execution|T1546]]

## Detection

```yaml
selection:
  Image|endswith: \outlook.exe
  TargetFilename|endswith: \Microsoft\Outlook\VbaProject.OTM
condition: selection
```

## False Positives

- User genuinely creates a VB Macro for their email

## References

- https://www.mdsec.co.uk/2020/11/a-fresh-outlook-on-mail-based-persistence/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_outlook_macro_creation.yml)
