---
sigma_id: "1bbf25b9-8038-4154-a50b-118f2a32be27"
title: "Suspicious Windows ANONYMOUS LOGON Local Account Created"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_local_anon_logon_created.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_local_anon_logon_created.yml"
build_date: "2026-04-26 14:14:37"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Windows ANONYMOUS LOGON Local Account Created

Detects the creation of suspicious accounts similar to ANONYMOUS LOGON, such as using additional spaces. Created as an covering detection for exclusion of Logon Type 3 from ANONYMOUS LOGON accounts.

## Metadata

- Rule ID: 1bbf25b9-8038-4154-a50b-118f2a32be27
- Status: test
- Level: high
- Author: James Pemberton / @4A616D6573
- Date: 2019-10-31
- Modified: 2022-10-09
- Source Path: rules/windows/builtin/security/win_security_susp_local_anon_logon_created.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1136-create_account|T1136.001]]
- [[kb/attack/techniques/T1136-create_account|T1136.002]]

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
