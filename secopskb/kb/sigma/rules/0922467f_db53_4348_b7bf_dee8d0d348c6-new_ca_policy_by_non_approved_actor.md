---
sigma_id: "0922467f-db53-4348-b7bf-dee8d0d348c6"
title: "New CA Policy by Non-approved Actor"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_aad_secops_new_ca_policy_addedby_bad_actor.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_aad_secops_new_ca_policy_addedby_bad_actor.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "azure / auditlogs"
aliases:
  - "0922467f-db53-4348-b7bf-dee8d0d348c6"
  - "New CA Policy by Non-approved Actor"
attack_technique_ids:
  - "T1548"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New CA Policy by Non-approved Actor

Monitor and alert on conditional access changes.

## Metadata

- Rule ID: 0922467f-db53-4348-b7bf-dee8d0d348c6
- Status: test
- Level: medium
- Author: Corissa Koopmans, '@corissalea'
- Date: 2022-07-18
- Source Path: rules/cloud/azure/audit_logs/azure_aad_secops_new_ca_policy_addedby_bad_actor.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548]]

## Detection

```yaml
selection:
  properties.message: Add conditional access policy
condition: selection
```

## False Positives

- Misconfigured role permissions
- Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-infrastructure

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_aad_secops_new_ca_policy_addedby_bad_actor.yml)
