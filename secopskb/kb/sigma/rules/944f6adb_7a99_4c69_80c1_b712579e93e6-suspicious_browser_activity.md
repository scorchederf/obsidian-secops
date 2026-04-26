---
sigma_id: "944f6adb-7a99-4c69-80c1-b712579e93e6"
title: "Suspicious Browser Activity"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/identity_protection/azure_identity_protection_suspicious_browser.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_suspicious_browser.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "high"
logsource: "azure / riskdetection"
aliases:
  - "944f6adb-7a99-4c69-80c1-b712579e93e6"
  - "Suspicious Browser Activity"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Browser Activity

Indicates anomalous behavior based on suspicious sign-in activity across multiple tenants from different countries in the same browser

## Metadata

- Rule ID: 944f6adb-7a99-4c69-80c1-b712579e93e6
- Status: test
- Level: high
- Author: Mark Morowczynski '@markmorow', Gloria Lee, '@gleeiamglo'
- Date: 2023-09-03
- Source Path: rules/cloud/azure/identity_protection/azure_identity_protection_suspicious_browser.yml

## Logsource

- product: azure
- service: riskdetection

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  riskEventType: suspiciousBrowser
condition: selection
```

## False Positives

- We recommend investigating the sessions flagged by this detection in the context of other sign-ins from the user.

## References

- https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks#suspicious-browser
- https://learn.microsoft.com/en-us/entra/architecture/security-operations-user-accounts#unusual-sign-ins

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_suspicious_browser.yml)
