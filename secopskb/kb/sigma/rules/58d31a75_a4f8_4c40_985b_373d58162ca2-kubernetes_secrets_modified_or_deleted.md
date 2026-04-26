---
sigma_id: "58d31a75-a4f8-4c40-985b-373d58162ca2"
title: "Kubernetes Secrets Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/application/kubernetes/audit/kubernetes_audit_secrets_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_secrets_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "kubernetes / audit"
aliases:
  - "58d31a75-a4f8-4c40-985b-373d58162ca2"
  - "Kubernetes Secrets Modified or Deleted"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Kubernetes Secrets Modified or Deleted

Detects when Kubernetes Secrets are Modified or Deleted.

## Metadata

- Rule ID: 58d31a75-a4f8-4c40-985b-373d58162ca2
- Status: test
- Level: medium
- Author: kelnage
- Date: 2024-07-11
- Source Path: rules/application/kubernetes/audit/kubernetes_audit_secrets_modified_or_deleted.yml

## Logsource

- product: kubernetes
- service: audit

## Detection

```yaml
selection:
  objectRef.resource: secrets
  verb:
  - create
  - delete
  - patch
  - replace
  - update
condition: selection
```

## False Positives

- Secrets being modified or deleted may be performed by a system administrator.
- Automated processes may need to take these actions and may need to be filtered.

## References

- https://kubernetes.io/docs/reference/config-api/apiserver-audit.v1/
- https://commandk.dev/blog/guide-to-audit-k8s-secrets-for-compliance/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_secrets_modified_or_deleted.yml)
