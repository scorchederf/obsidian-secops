---
sigma_id: "27e4f1d6-ae72-4ea0-8a67-77a73a289c3d"
title: "Suspicious Inbox Forwarding Identity Protection"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/identity_protection/azure_identity_protection_inbox_forwarding_rule.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_inbox_forwarding_rule.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "azure / riskdetection"
aliases:
  - "27e4f1d6-ae72-4ea0-8a67-77a73a289c3d"
  - "Suspicious Inbox Forwarding Identity Protection"
attack_technique_ids:
  - "T1114.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Indicates suspicious rules such as an inbox rule that forwards a copy of all emails to an external address

## Logsource

- product: azure
- service: riskdetection

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1114-email_collection#^t1114003-email-forwarding-rule|T1114.003: Email Forwarding Rule]]

## Detection

```yaml
selection:
  riskEventType: suspiciousInboxForwarding
condition: selection
```

## False Positives

- A legitimate forwarding rule.

## References

- https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks#suspicious-inbox-forwarding
- https://learn.microsoft.com/en-us/entra/architecture/security-operations-user-accounts#unusual-sign-ins

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_inbox_forwarding_rule.yml)
