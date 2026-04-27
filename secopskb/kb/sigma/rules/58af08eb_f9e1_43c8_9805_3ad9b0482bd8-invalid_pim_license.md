---
sigma_id: "58af08eb-f9e1-43c8-9805-3ad9b0482bd8"
title: "Invalid PIM License"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/privileged_identity_management/azure_pim_invalid_license.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/privileged_identity_management/azure_pim_invalid_license.yml"
build_date: "2026-04-27 19:13:52"
status: "test"
level: "high"
logsource: "azure / pim"
aliases:
  - "58af08eb-f9e1-43c8-9805-3ad9b0482bd8"
  - "Invalid PIM License"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Identifies when an organization doesn't have the proper license for PIM and is out of compliance.

## Logsource

- product: azure
- service: pim

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078: Valid Accounts]]

## Detection

```yaml
selection:
  riskEventType: invalidLicenseAlertIncident
condition: selection
```

## False Positives

- Investigate if licenses have expired.

## References

- https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-configure-security-alerts#the-organization-doesnt-have-microsoft-entra-premium-p2-or-microsoft-entra-id-governance

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/privileged_identity_management/azure_pim_invalid_license.yml)
