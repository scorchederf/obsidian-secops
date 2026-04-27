---
sigma_id: "60f6535a-760f-42a9-be3f-c9a0a025906e"
title: "Use of Legacy Authentication Protocols"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/signin_logs/azure_legacy_authentication_protocols.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_legacy_authentication_protocols.yml"
build_date: "2026-04-27 19:13:58"
status: "test"
level: "high"
logsource: "azure / signinlogs"
aliases:
  - "60f6535a-760f-42a9-be3f-c9a0a025906e"
  - "Use of Legacy Authentication Protocols"
attack_technique_ids:
  - "T1078.004"
  - "T1110"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Alert on when legacy authentication has been used on an account

## Logsource

- product: azure
- service: signinlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]]
- [[kb/attack/techniques/T1110-brute_force|T1110: Brute Force]]

## Detection

```yaml
selection:
  ActivityDetails: Sign-ins
  ClientApp:
  - Other client
  - IMAP
  - POP3
  - MAPI
  - SMTP
  - Exchange ActiveSync
  - Exchange Web Services
  Username: UPN
condition: selection
```

## False Positives

- User has been put in acception group so they can use legacy authentication

## References

- https://learn.microsoft.com/en-gb/entra/architecture/security-operations-privileged-accounts

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_legacy_authentication_protocols.yml)
