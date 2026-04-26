---
sigma_id: "c3edc6a5-d9d4-48d8-930e-aab518390917"
title: "Potential Persistence Via Outlook Form"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_office_outlook_newform.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_outlook_newform.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "c3edc6a5-d9d4-48d8-930e-aab518390917"
  - "Potential Persistence Via Outlook Form"
attack_technique_ids:
  - "T1137.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Persistence Via Outlook Form

Detects the creation of a new Outlook form which can contain malicious code

## Metadata

- Rule ID: c3edc6a5-d9d4-48d8-930e-aab518390917
- Status: test
- Level: high
- Author: Tobias Michalski (Nextron Systems)
- Date: 2021-06-10
- Modified: 2023-02-22
- Source Path: rules/windows/file/file_event/file_event_win_office_outlook_newform.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1137-office_application_startup|T1137.003]]

## Detection

```yaml
selection:
  Image|endswith: \outlook.exe
  TargetFilename|contains:
  - \AppData\Local\Microsoft\FORMS\IPM
  - \Local Settings\Application Data\Microsoft\Forms
condition: selection
```

## False Positives

- Legitimate use of outlook forms

## References

- https://speakerdeck.com/heirhabarov/hunting-for-persistence-via-microsoft-exchange-server-or-outlook?slide=76
- https://speakerdeck.com/heirhabarov/hunting-for-persistence-via-microsoft-exchange-server-or-outlook?slide=79
- https://learn.microsoft.com/en-us/office/vba/outlook/concepts/outlook-forms/create-an-outlook-form
- https://www.slipstick.com/developer/custom-form/clean-outlooks-forms-cache/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_outlook_newform.yml)
