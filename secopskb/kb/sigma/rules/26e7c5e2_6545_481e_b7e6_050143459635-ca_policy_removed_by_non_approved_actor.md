---
sigma_id: "26e7c5e2-6545-481e-b7e6-050143459635"
title: "CA Policy Removed by Non Approved Actor"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_aad_secops_ca_policy_removedby_bad_actor.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_aad_secops_ca_policy_removedby_bad_actor.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "azure / auditlogs"
aliases:
  - "26e7c5e2-6545-481e-b7e6-050143459635"
  - "CA Policy Removed by Non Approved Actor"
attack_technique_ids:
  - "T1548"
  - "T1556"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CA Policy Removed by Non Approved Actor

Monitor and alert on conditional access changes where non approved actor removed CA Policy.

## Metadata

- Rule ID: 26e7c5e2-6545-481e-b7e6-050143459635
- Status: test
- Level: medium
- Author: Corissa Koopmans, '@corissalea'
- Date: 2022-07-19
- Source Path: rules/cloud/azure/audit_logs/azure_aad_secops_ca_policy_removedby_bad_actor.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548]]
- [[kb/attack/techniques/T1556-modify_authentication_process|T1556]]

## Detection

```yaml
selection:
  properties.message: Delete conditional access policy
condition: selection
```

## False Positives

- Misconfigured role permissions
- Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-infrastructure#conditional-access

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_aad_secops_ca_policy_removedby_bad_actor.yml)
