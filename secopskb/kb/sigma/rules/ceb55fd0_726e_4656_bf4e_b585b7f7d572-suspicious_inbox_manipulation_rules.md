---
sigma_id: "ceb55fd0-726e-4656-bf4e-b585b7f7d572"
title: "Suspicious Inbox Manipulation Rules"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/identity_protection/azure_identity_protection_inbox_manipulation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_inbox_manipulation.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "azure / riskdetection"
aliases:
  - "ceb55fd0-726e-4656-bf4e-b585b7f7d572"
  - "Suspicious Inbox Manipulation Rules"
attack_technique_ids:
  - "T1140"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious rules that delete or move messages or folders are set on a user's inbox.

## Logsource

- product: azure
- service: riskdetection

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140: Deobfuscate/Decode Files or Information]]

## Detection

```yaml
selection:
  riskEventType: mcasSuspiciousInboxManipulationRules
condition: selection
```

## False Positives

- Actual mailbox rules that are moving items based on their workflow.

## References

- https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks#suspicious-inbox-manipulation-rules
- https://learn.microsoft.com/en-us/entra/architecture/security-operations-user-accounts#unusual-sign-ins

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_inbox_manipulation.yml)
