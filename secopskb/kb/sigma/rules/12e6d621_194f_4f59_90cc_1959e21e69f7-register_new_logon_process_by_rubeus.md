---
sigma_id: "12e6d621-194f-4f59-90cc-1959e21e69f7"
title: "Register new Logon Process by Rubeus"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_register_new_logon_process_by_rubeus.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_register_new_logon_process_by_rubeus.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "12e6d621-194f-4f59-90cc-1959e21e69f7"
  - "Register new Logon Process by Rubeus"
attack_technique_ids:
  - "T1558.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects potential use of Rubeus via registered new trusted logon process

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets#^t1558003-kerberoasting|T1558.003: Kerberoasting]]

## Detection

```yaml
selection:
  EventID: 4611
  LogonProcessName: User32LogonProcesss
condition: selection
```

## False Positives

- Unknown

## References

- https://posts.specterops.io/hunting-in-active-directory-unconstrained-delegation-forests-trusts-71f2b33688e1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_register_new_logon_process_by_rubeus.yml)
