---
sigma_id: "def8b624-e08f-4ae1-8612-1ba21190da6b"
title: "Outgoing Logon with New Credentials"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/account_management/win_security_susp_logon_newcredentials.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_susp_logon_newcredentials.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "low"
logsource: "windows / security"
aliases:
  - "def8b624-e08f-4ae1-8612-1ba21190da6b"
  - "Outgoing Logon with New Credentials"
attack_technique_ids:
  - "T1550"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Outgoing Logon with New Credentials

Detects logon events that specify new credentials

## Metadata

- Rule ID: def8b624-e08f-4ae1-8612-1ba21190da6b
- Status: test
- Level: low
- Author: Max Altgelt (Nextron Systems)
- Date: 2022-04-06
- Source Path: rules/windows/builtin/security/account_management/win_security_susp_logon_newcredentials.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1550-use_alternate_authentication_material|T1550]]

## Detection

```yaml
selection:
  EventID: 4624
  LogonType: 9
condition: selection
```

## False Positives

- Legitimate remote administration activity

## References

- https://go.recordedfuture.com/hubfs/reports/mtp-2021-0914.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_susp_logon_newcredentials.yml)
