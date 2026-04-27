---
sigma_id: "3a734d25-df5c-4b99-8034-af1ddb5883a4"
title: "Suspicious Scheduled Task Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_scheduled_task_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_scheduled_task_creation.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "3a734d25-df5c-4b99-8034-af1ddb5883a4"
  - "Suspicious Scheduled Task Creation"
attack_technique_ids:
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious scheduled task creation events. Based on attributes such as paths, commands line flags, etc.

## Logsource

- definition: The Advanced Audit Policy setting Object Access > Audit Other Object Access Events has to be configured to allow this detection. We also recommend extracting the Command field from the embedded XML in the event data.
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]

## Detection

```yaml
selection_eid:
  EventID: 4698
selection_paths:
  TaskContent|contains:
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
  TaskContent|contains:
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_scheduled_task_creation.yml)
