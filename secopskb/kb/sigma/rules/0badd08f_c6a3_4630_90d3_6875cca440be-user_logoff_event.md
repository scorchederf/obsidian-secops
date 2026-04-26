---
sigma_id: "0badd08f-c6a3-4630-90d3-6875cca440be"
title: "User Logoff Event"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_user_logoff.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_user_logoff.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "informational"
logsource: "windows / security"
aliases:
  - "0badd08f-c6a3-4630-90d3-6875cca440be"
  - "User Logoff Event"
attack_technique_ids:
  - "T1531"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# User Logoff Event

Detects a user log-off activity. Could be used for example to correlate information during forensic investigations

## Metadata

- Rule ID: 0badd08f-c6a3-4630-90d3-6875cca440be
- Status: test
- Level: informational
- Author: frack113
- Date: 2022-10-14
- Source Path: rules/windows/builtin/security/win_security_user_logoff.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1531-account_access_removal|T1531]]

## Detection

```yaml
selection:
  EventID:
  - 4634
  - 4647
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/Yamato-Security/EnableWindowsLogSettings/blob/7f6d755d45ac7cc9fc35b0cbf498e6aa4ef19def/ConfiguringSecurityLogAuditPolicies.md
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4634
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4647

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_user_logoff.yml)
