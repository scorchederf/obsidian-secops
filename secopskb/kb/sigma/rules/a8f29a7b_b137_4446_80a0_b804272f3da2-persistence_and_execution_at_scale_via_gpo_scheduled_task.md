---
sigma_id: "a8f29a7b-b137-4446-80a0-b804272f3da2"
title: "Persistence and Execution at Scale via GPO Scheduled Task"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_gpo_scheduledtasks.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_gpo_scheduledtasks.yml"
build_date: "2026-04-26 15:01:47"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "a8f29a7b-b137-4446-80a0-b804272f3da2"
  - "Persistence and Execution at Scale via GPO Scheduled Task"
attack_technique_ids:
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Persistence and Execution at Scale via GPO Scheduled Task

Detect lateral movement using GPO scheduled task, usually used to deploy ransomware at scale

## Metadata

- Rule ID: a8f29a7b-b137-4446-80a0-b804272f3da2
- Status: test
- Level: high
- Author: Samir Bousseaden
- Date: 2019-04-03
- Modified: 2024-09-04
- Source Path: rules/windows/builtin/security/win_security_gpo_scheduledtasks.yml

## Logsource

- definition: The advanced audit policy setting "Object Access > Audit Detailed File Share" must be configured for Success/Failure
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Detection

```yaml
selection_5136:
  EventID: 5136
  AttributeLDAPDisplayName:
  - gPCMachineExtensionNames
  - gPCUserExtensionNames
  AttributeValue|contains:
  - CAB54552-DEEA-4691-817E-ED4A4D1AFC72
  - AADCED64-746C-4633-A97C-D61349046527
selection_5145:
  EventID: 5145
  ShareName|endswith: \SYSVOL
  RelativeTargetName|endswith: ScheduledTasks.xml
  AccessList|contains:
  - WriteData
  - '%%4417'
condition: 1 of selection_*
```

## False Positives

- If the source IP is not localhost then it's super suspicious, better to monitor both local and remote changes to GPO scheduled tasks.

## References

- https://twitter.com/menasec1/status/1106899890377052160
- https://www.secureworks.com/blog/ransomware-as-a-distraction
- https://www.elastic.co/guide/en/security/7.17/prebuilt-rule-0-16-1-scheduled-task-execution-at-scale-via-gpo.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_gpo_scheduledtasks.yml)
