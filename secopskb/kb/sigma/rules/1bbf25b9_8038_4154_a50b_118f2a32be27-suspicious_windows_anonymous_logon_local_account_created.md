---
sigma_id: "1bbf25b9-8038-4154-a50b-118f2a32be27"
title: "Suspicious Windows ANONYMOUS LOGON Local Account Created"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_local_anon_logon_created.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_local_anon_logon_created.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "1bbf25b9-8038-4154-a50b-118f2a32be27"
  - "Suspicious Windows ANONYMOUS LOGON Local Account Created"
attack_technique_ids:
  - "T1136.001"
  - "T1136.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the creation of suspicious accounts similar to ANONYMOUS LOGON, such as using additional spaces. Created as an covering detection for exclusion of Logon Type 3 from ANONYMOUS LOGON accounts.

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1136-create_account#^t1136001-local-account|T1136.001: Local Account]]
- [[kb/attack/techniques/T1136-create_account#^t1136002-domain-account|T1136.002: Domain Account]]

## Detection

```yaml
selection:
  EventID: 4720
  SamAccountName|contains|all:
  - ANONYMOUS
  - LOGON
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/SBousseaden/status/1189469425482829824

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_local_anon_logon_created.yml)
