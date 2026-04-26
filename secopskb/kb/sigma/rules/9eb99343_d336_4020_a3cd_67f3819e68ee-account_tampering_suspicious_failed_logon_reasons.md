---
sigma_id: "9eb99343-d336-4020-a3cd-67f3819e68ee"
title: "Account Tampering - Suspicious Failed Logon Reasons"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_failed_logon_reasons.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_failed_logon_reasons.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "9eb99343-d336-4020-a3cd-67f3819e68ee"
  - "Account Tampering - Suspicious Failed Logon Reasons"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Account Tampering - Suspicious Failed Logon Reasons

This method uses uncommon error codes on failed logons to determine suspicious activity and tampering with accounts that have been disabled or somehow restricted.

## Metadata

- Rule ID: 9eb99343-d336-4020-a3cd-67f3819e68ee
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2017-02-19
- Modified: 2025-10-17
- Source Path: rules/windows/builtin/security/win_security_susp_failed_logon_reasons.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection_eid:
  EventID:
  - 4625
  - 4776
selection_status:
- Status:
  - '0xC0000072'
  - '0xC000006F'
  - '0xC0000070'
  - '0xC0000413'
  - '0xC000018C'
  - '0xC000015B'
- SubStatus:
  - '0xC0000072'
  - '0xC000006F'
  - '0xC0000070'
  - '0xC0000413'
  - '0xC000018C'
  - '0xC000015B'
filter:
  SubjectUserSid: S-1-0-0
condition: all of selection_* and not filter
```

## False Positives

- User using a disabled account

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4625
- https://twitter.com/SBousseaden/status/1101431884540710913

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_failed_logon_reasons.yml)
