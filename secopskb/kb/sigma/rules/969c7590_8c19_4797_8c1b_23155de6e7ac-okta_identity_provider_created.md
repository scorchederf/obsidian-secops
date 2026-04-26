---
sigma_id: "969c7590-8c19-4797-8c1b-23155de6e7ac"
title: "Okta Identity Provider Created"
framework: "sigma"
generated: "true"
source_path: "rules/identity/okta/okta_identity_provider_created.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_identity_provider_created.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "okta / okta"
aliases:
  - "969c7590-8c19-4797-8c1b-23155de6e7ac"
  - "Okta Identity Provider Created"
attack_technique_ids:
  - "T1098.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Okta Identity Provider Created

Detects when a new identity provider is created for Okta.

## Metadata

- Rule ID: 969c7590-8c19-4797-8c1b-23155de6e7ac
- Status: test
- Level: medium
- Author: kelnage
- Date: 2023-09-07
- Source Path: rules/identity/okta/okta_identity_provider_created.yml

## Logsource

- product: okta
- service: okta

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098.001]]

## Detection

```yaml
selection:
  eventtype: system.idp.lifecycle.create
condition: selection
```

## False Positives

- When an admin creates a new, authorised identity provider.

## References

- https://developer.okta.com/docs/reference/api/system-log/
- https://sec.okta.com/articles/2023/08/cross-tenant-impersonation-prevention-and-detection

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_identity_provider_created.yml)
