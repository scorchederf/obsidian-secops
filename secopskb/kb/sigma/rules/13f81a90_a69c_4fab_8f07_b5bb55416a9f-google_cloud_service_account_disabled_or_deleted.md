---
sigma_id: "13f81a90-a69c-4fab-8f07-b5bb55416a9f"
title: "Google Cloud Service Account Disabled or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/gcp/audit/gcp_service_account_disabled_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_service_account_disabled_or_deleted.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "gcp / gcp.audit"
aliases:
  - "13f81a90-a69c-4fab-8f07-b5bb55416a9f"
  - "Google Cloud Service Account Disabled or Deleted"
attack_technique_ids:
  - "T1531"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Google Cloud Service Account Disabled or Deleted

Identifies when a service account is disabled or deleted in Google Cloud.

## Metadata

- Rule ID: 13f81a90-a69c-4fab-8f07-b5bb55416a9f
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-14
- Modified: 2022-10-09
- Source Path: rules/cloud/gcp/audit/gcp_service_account_disabled_or_deleted.yml

## Logsource

- product: gcp
- service: gcp.audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1531-account_access_removal|T1531]]

## Detection

```yaml
selection:
  gcp.audit.method_name|endswith:
  - .serviceAccounts.disable
  - .serviceAccounts.delete
condition: selection
```

## False Positives

- Service Account being disabled or deleted may be performed by a system administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Service Account disabled or deleted from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_service_account_disabled_or_deleted.yml)
