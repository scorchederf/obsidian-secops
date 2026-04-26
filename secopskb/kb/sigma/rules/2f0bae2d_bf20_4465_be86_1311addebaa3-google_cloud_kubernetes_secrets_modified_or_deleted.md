---
sigma_id: "2f0bae2d-bf20-4465-be86-1311addebaa3"
title: "Google Cloud Kubernetes Secrets Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/gcp/audit/gcp_kubernetes_secrets_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_kubernetes_secrets_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "gcp / gcp.audit"
aliases:
  - "2f0bae2d-bf20-4465-be86-1311addebaa3"
  - "Google Cloud Kubernetes Secrets Modified or Deleted"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Google Cloud Kubernetes Secrets Modified or Deleted

Identifies when the Secrets are Modified or Deleted.

## Metadata

- Rule ID: 2f0bae2d-bf20-4465-be86-1311addebaa3
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-09
- Modified: 2022-10-09
- Source Path: rules/cloud/gcp/audit/gcp_kubernetes_secrets_modified_or_deleted.yml

## Logsource

- product: gcp
- service: gcp.audit

## Detection

```yaml
selection:
  gcp.audit.method_name:
  - io.k8s.core.v*.secrets.create
  - io.k8s.core.v*.secrets.update
  - io.k8s.core.v*.secrets.patch
  - io.k8s.core.v*.secrets.delete
condition: selection
```

## False Positives

- Secrets being modified or deleted may be performed by a system administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Secrets modified or deleted from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://cloud.google.com/kubernetes-engine/docs/how-to/audit-logging

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_kubernetes_secrets_modified_or_deleted.yml)
