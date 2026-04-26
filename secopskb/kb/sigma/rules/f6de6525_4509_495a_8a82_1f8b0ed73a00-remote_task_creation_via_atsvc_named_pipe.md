---
sigma_id: "f6de6525-4509-495a-8a82-1f8b0ed73a00"
title: "Remote Task Creation via ATSVC Named Pipe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_atsvc_task.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_atsvc_task.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "f6de6525-4509-495a-8a82-1f8b0ed73a00"
  - "Remote Task Creation via ATSVC Named Pipe"
attack_technique_ids:
  - "T1053.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Task Creation via ATSVC Named Pipe

Detects remote task creation via at.exe or API interacting with ATSVC namedpipe

## Metadata

- Rule ID: f6de6525-4509-495a-8a82-1f8b0ed73a00
- Status: test
- Level: medium
- Author: Samir Bousseaden
- Date: 2019-04-03
- Modified: 2024-08-01
- Source Path: rules/windows/builtin/security/win_security_atsvc_task.yml

## Logsource

- definition: The advanced audit policy setting "Object Access > Audit Detailed File Share" must be configured for Success/Failure
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.002]]

## Detection

```yaml
selection:
  EventID: 5145
  ShareName: \\\\\*\\IPC$
  RelativeTargetName: atsvc
  AccessList|contains: WriteData
condition: selection
```

## False Positives

- Unknown

## References

- https://web.archive.org/web/20230409194125/https://blog.menasec.net/2019/03/threat-hunting-25-scheduled-tasks-for.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_atsvc_task.yml)
