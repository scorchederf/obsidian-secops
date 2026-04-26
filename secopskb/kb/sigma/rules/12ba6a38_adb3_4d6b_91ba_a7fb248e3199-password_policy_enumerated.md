---
sigma_id: "12ba6a38-adb3-4d6b-91ba-a7fb248e3199"
title: "Password Policy Enumerated"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_password_policy_enumerated.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_password_policy_enumerated.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "12ba6a38-adb3-4d6b-91ba-a7fb248e3199"
  - "Password Policy Enumerated"
attack_technique_ids:
  - "T1201"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Password Policy Enumerated

Detects when the password policy is enumerated.

## Metadata

- Rule ID: 12ba6a38-adb3-4d6b-91ba-a7fb248e3199
- Status: test
- Level: medium
- Author: Zach Mathis
- Date: 2023-05-19
- Source Path: rules/windows/builtin/security/win_security_password_policy_enumerated.yml

## Logsource

- definition: dfd8c0f4-e6ad-4e07-b91b-f2fca0ddef64
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1201-password_policy_discovery|T1201]]

## Detection

```yaml
selection:
  EventID: 4661
  AccessList|contains: '%%5392'
  ObjectServer: Security Account Manager
condition: selection
```

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4661
- https://github.com/jpalanco/alienvault-ossim/blob/f74359c0c027e42560924b5cff25cdf121e5505a/os-sim/agent/src/ParserUtil.py#L951

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_password_policy_enumerated.yml)
