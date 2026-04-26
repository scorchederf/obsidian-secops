---
sigma_id: "32438676-1dba-4ac7-bf69-b86cba995e05"
title: "GCP Access Policy Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/gcp/audit/gcp_access_policy_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_access_policy_deleted.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "gcp / gcp.audit"
aliases:
  - "32438676-1dba-4ac7-bf69-b86cba995e05"
  - "GCP Access Policy Deleted"
attack_technique_ids:
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# GCP Access Policy Deleted

Detects when an access policy that is applied to a GCP cloud resource is deleted.
An adversary would be able to remove access policies to gain access to a GCP cloud resource.

## Metadata

- Rule ID: 32438676-1dba-4ac7-bf69-b86cba995e05
- Status: test
- Level: medium
- Author: Bryan Lim
- Date: 2024-01-12
- Source Path: rules/cloud/gcp/audit/gcp_access_policy_deleted.yml

## Logsource

- product: gcp
- service: gcp.audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Detection

```yaml
selection:
  data.protoPayload.authorizationInfo.permission:
  - accesscontextmanager.accessPolicies.delete
  - accesscontextmanager.accessPolicies.accessLevels.delete
  - accesscontextmanager.accessPolicies.accessZones.delete
  - accesscontextmanager.accessPolicies.authorizedOrgsDescs.delete
  data.protoPayload.authorizationInfo.granted: 'true'
  data.protoPayload.serviceName: accesscontextmanager.googleapis.com
condition: selection
```

## False Positives

- Legitimate administrative activities

## References

- https://cloud.google.com/access-context-manager/docs/audit-logging
- https://cloud.google.com/logging/docs/audit/understanding-audit-logs
- https://cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_access_policy_deleted.yml)
