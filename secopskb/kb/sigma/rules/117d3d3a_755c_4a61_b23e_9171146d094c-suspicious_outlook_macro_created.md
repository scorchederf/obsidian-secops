---
sigma_id: "117d3d3a-755c-4a61-b23e-9171146d094c"
title: "Suspicious Outlook Macro Created"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_office_outlook_susp_macro_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_outlook_susp_macro_creation.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "117d3d3a-755c-4a61-b23e-9171146d094c"
  - "Suspicious Outlook Macro Created"
attack_technique_ids:
  - "T1137"
  - "T1008"
  - "T1546"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the creation of a macro file for Outlook.

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1137-office_application_startup|T1137: Office Application Startup]]
- [[kb/attack/techniques/T1008-fallback_channels|T1008: Fallback Channels]]
- [[kb/attack/techniques/T1546-event_triggered_execution|T1546: Event Triggered Execution]]

## Detection

```yaml
selection:
  TargetFilename|endswith: \Microsoft\Outlook\VbaProject.OTM
filter:
  Image|endswith: \outlook.exe
condition: selection and not filter
```

## False Positives

- Unlikely

## References

- https://www.mdsec.co.uk/2020/11/a-fresh-outlook-on-mail-based-persistence/
- https://speakerdeck.com/heirhabarov/hunting-for-persistence-via-microsoft-exchange-server-or-outlook?slide=53
- https://www.linkedin.com/pulse/outlook-backdoor-using-vba-samir-b-/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_outlook_susp_macro_creation.yml)
