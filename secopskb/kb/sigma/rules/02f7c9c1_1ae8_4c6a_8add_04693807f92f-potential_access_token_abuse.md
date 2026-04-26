---
sigma_id: "02f7c9c1-1ae8-4c6a-8add-04693807f92f"
title: "Potential Access Token Abuse"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/account_management/win_security_access_token_abuse.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_access_token_abuse.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "02f7c9c1-1ae8-4c6a-8add-04693807f92f"
  - "Potential Access Token Abuse"
attack_technique_ids:
  - "T1134.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Access Token Abuse

Detects potential token impersonation and theft. Example, when using "DuplicateToken(Ex)" and "ImpersonateLoggedOnUser" with the "LOGON32_LOGON_NEW_CREDENTIALS flag".

## Metadata

- Rule ID: 02f7c9c1-1ae8-4c6a-8add-04693807f92f
- Status: test
- Level: medium
- Author: Michaela Adams, Zach Mathis
- Date: 2022-11-06
- Modified: 2023-04-26
- Source Path: rules/windows/builtin/security/account_management/win_security_access_token_abuse.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.001]]

## Detection

```yaml
selection:
  EventID: 4624
  LogonType: 9
  LogonProcessName: Advapi
  AuthenticationPackageName: Negotiate
  ImpersonationLevel: '%%1833'
condition: selection
```

## False Positives

- Anti-Virus

## References

- https://www.elastic.co/fr/blog/how-attackers-abuse-access-token-manipulation
- https://www.manageengine.com/log-management/cyber-security/access-token-manipulation.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_access_token_abuse.yml)
