---
sigma_id: "614cf376-6651-47c4-9dcc-6b9527f749f4"
title: "Suspicious Scheduled Task Update"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_scheduled_task_update.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_scheduled_task_update.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "614cf376-6651-47c4-9dcc-6b9527f749f4"
  - "Suspicious Scheduled Task Update"
attack_technique_ids:
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Scheduled Task Update

Detects update to a scheduled task event that contain suspicious keywords.

## Metadata

- Rule ID: 614cf376-6651-47c4-9dcc-6b9527f749f4
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-12-05
- Source Path: rules/windows/builtin/security/win_security_susp_scheduled_task_update.yml

## Logsource

- definition: The Advanced Audit Policy setting Object Access > Audit Other Object Access Events has to be configured to allow this detection. We also recommend extracting the Command field from the embedded XML in the event data.
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Detection

```yaml
selection_eid:
  EventID: 4702
selection_paths:
  TaskContentNew|contains:
  - \AppData\Local\Temp\
  - \AppData\Roaming\
  - \Users\Public\
  - \WINDOWS\Temp\
  - C:\Temp\
  - \Desktop\
  - \Downloads\
  - \Temporary Internet
  - C:\ProgramData\
  - C:\Perflogs\
selection_commands:
  TaskContentNew|contains:
  - regsvr32
  - rundll32
  - cmd.exe</Command>
  - cmd</Command>
  - '<Arguments>/c '
  - '<Arguments>/k '
  - '<Arguments>/r '
  - powershell
  - pwsh
  - mshta
  - wscript
  - cscript
  - certutil
  - bitsadmin
  - bash.exe
  - 'bash '
  - scrcons
  - 'wmic '
  - wmic.exe
  - forfiles
  - scriptrunner
  - hh.exe
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4698

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_scheduled_task_update.yml)
