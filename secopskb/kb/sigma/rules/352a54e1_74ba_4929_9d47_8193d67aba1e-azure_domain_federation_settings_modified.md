---
sigma_id: "352a54e1-74ba-4929-9d47-8193d67aba1e"
title: "Azure Domain Federation Settings Modified"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_federation_modified.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_federation_modified.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / auditlogs"
aliases:
  - "352a54e1-74ba-4929-9d47-8193d67aba1e"
  - "Azure Domain Federation Settings Modified"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Domain Federation Settings Modified

Identifies when an user or application modified the federation settings on the domain.

## Metadata

- Rule ID: 352a54e1-74ba-4929-9d47-8193d67aba1e
- Status: test
- Level: medium
- Author: Austin Songer
- Date: 2021-09-06
- Modified: 2022-06-08
- Source Path: rules/cloud/azure/audit_logs/azure_federation_modified.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  ActivityDisplayName: Set federation settings on domain
condition: selection
```

## False Positives

- Federation Settings being modified or deleted may be performed by a system administrator.
- Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Federation Settings modified from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-monitor-federation-changes

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_federation_modified.yml)
