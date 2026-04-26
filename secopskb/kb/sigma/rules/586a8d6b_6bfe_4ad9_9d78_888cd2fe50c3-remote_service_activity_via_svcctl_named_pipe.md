---
sigma_id: "586a8d6b-6bfe-4ad9-9d78-888cd2fe50c3"
title: "Remote Service Activity via SVCCTL Named Pipe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_svcctl_remote_service.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_svcctl_remote_service.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "586a8d6b-6bfe-4ad9-9d78-888cd2fe50c3"
  - "Remote Service Activity via SVCCTL Named Pipe"
attack_technique_ids:
  - "T1021.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Service Activity via SVCCTL Named Pipe

Detects remote service activity via remote access to the svcctl named pipe

## Metadata

- Rule ID: 586a8d6b-6bfe-4ad9-9d78-888cd2fe50c3
- Status: test
- Level: medium
- Author: Samir Bousseaden
- Date: 2019-04-03
- Modified: 2024-08-01
- Source Path: rules/windows/builtin/security/win_security_svcctl_remote_service.yml

## Logsource

- definition: The advanced audit policy setting "Object Access > Audit Detailed File Share" must be configured for Success/Failure
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]

## Detection

```yaml
selection:
  EventID: 5145
  ShareName: \\\\\*\\IPC$
  RelativeTargetName: svcctl
  AccessList|contains: WriteData
condition: selection
```

## False Positives

- Unknown

## References

- https://web.archive.org/web/20230329155141/https://blog.menasec.net/2019/03/threat-hunting-26-remote-windows.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_svcctl_remote_service.yml)
