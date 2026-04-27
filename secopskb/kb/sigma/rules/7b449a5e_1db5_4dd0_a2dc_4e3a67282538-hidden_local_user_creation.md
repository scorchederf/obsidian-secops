---
sigma_id: "7b449a5e-1db5-4dd0-a2dc-4e3a67282538"
title: "Hidden Local User Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_hidden_user_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_hidden_user_creation.yml"
build_date: "2026-04-27 19:13:52"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "7b449a5e-1db5-4dd0-a2dc-4e3a67282538"
  - "Hidden Local User Creation"
attack_technique_ids:
  - "T1136.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the creation of a local hidden user account which should not happen for event ID 4720.

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1136-create_account#^t1136001-local-account|T1136.001: Local Account]]

## Detection

```yaml
selection:
  EventID: 4720
  TargetUserName|endswith: $
filter_main_homegroup:
  TargetUserName: HomeGroupUser$
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://twitter.com/SBousseaden/status/1387743867663958021

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_hidden_user_creation.yml)
