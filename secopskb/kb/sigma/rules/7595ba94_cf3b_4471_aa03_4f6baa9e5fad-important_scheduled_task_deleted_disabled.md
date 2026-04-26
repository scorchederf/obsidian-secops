---
sigma_id: "7595ba94-cf3b-4471-aa03-4f6baa9e5fad"
title: "Important Scheduled Task Deleted/Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_scheduled_task_delete_or_disable.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_scheduled_task_delete_or_disable.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "7595ba94-cf3b-4471-aa03-4f6baa9e5fad"
  - "Important Scheduled Task Deleted/Disabled"
attack_technique_ids:
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Important Scheduled Task Deleted/Disabled

Detects when adversaries stop services or processes by deleting or disabling their respective scheduled tasks in order to conduct data destructive activities

## Metadata

- Rule ID: 7595ba94-cf3b-4471-aa03-4f6baa9e5fad
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-12-05
- Modified: 2023-03-13
- Source Path: rules/windows/builtin/security/win_security_susp_scheduled_task_delete_or_disable.yml

## Logsource

- definition: The Advanced Audit Policy setting Object Access > Audit Other Object Access Events has to be configured to allow this detection. We also recommend extracting the Command field from the embedded XML in the event data.
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Detection

```yaml
selection:
  EventID:
  - 4699
  - 4701
  TaskName|contains:
  - \Windows\SystemRestore\SR
  - \Windows\Windows Defender\
  - \Windows\BitLocker
  - \Windows\WindowsBackup\
  - \Windows\WindowsUpdate\
  - \Windows\UpdateOrchestrator\Schedule
  - \Windows\ExploitGuard
filter_sys_username:
  EventID: 4699
  SubjectUserName|endswith: $
  TaskName|contains: \Windows\Windows Defender\
condition: selection and not 1 of filter_*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4699
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4701

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_scheduled_task_delete_or_disable.yml)
