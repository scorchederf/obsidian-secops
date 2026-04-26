---
sigma_id: "0d933542-1f1f-420d-97d4-21b2c3c492d9"
title: "Kubernetes Unauthorized or Unauthenticated Access"
framework: "sigma"
generated: "true"
source_path: "rules/application/kubernetes/audit/kubernetes_audit_unauthorized_unauthenticated_actions.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_unauthorized_unauthenticated_actions.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "low"
logsource: "kubernetes / audit"
aliases:
  - "0d933542-1f1f-420d-97d4-21b2c3c492d9"
  - "Kubernetes Unauthorized or Unauthenticated Access"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Kubernetes Unauthorized or Unauthenticated Access

Detects when a request to the Kubernetes API is rejected due to lack of authorization or due to an expired authentication token being used.
This may indicate an attacker attempting to leverage credentials they have obtained.

## Metadata

- Rule ID: 0d933542-1f1f-420d-97d4-21b2c3c492d9
- Status: test
- Level: low
- Author: kelnage
- Date: 2024-04-12
- Source Path: rules/application/kubernetes/audit/kubernetes_audit_unauthorized_unauthenticated_actions.yml

## Logsource

- product: kubernetes
- service: audit

## Detection

```yaml
selection:
  responseStatus.code:
  - 401
  - 403
condition: selection
```

## False Positives

- A misconfigured RBAC policy, a mistake by a valid user, or a wider issue with authentication tokens can also generate these errors.

## References

- https://kubernetes.io/docs/reference/config-api/apiserver-audit.v1/
- https://www.datadoghq.com/blog/monitor-kubernetes-audit-logs/#monitor-api-authentication-issues

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_unauthorized_unauthenticated_actions.yml)
