---
sigma_id: "10b97915-ec8d-455f-a815-9a78926585f6"
title: "Kubernetes Rolebinding Modification"
framework: "sigma"
generated: "true"
source_path: "rules/application/kubernetes/audit/kubernetes_audit_rolebinding_modification.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_rolebinding_modification.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "kubernetes / audit"
aliases:
  - "10b97915-ec8d-455f-a815-9a78926585f6"
  - "Kubernetes Rolebinding Modification"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Kubernetes Rolebinding Modification

Detects when a Kubernetes Rolebinding is created or modified.

## Metadata

- Rule ID: 10b97915-ec8d-455f-a815-9a78926585f6
- Status: test
- Level: medium
- Author: kelnage
- Date: 2024-07-11
- Source Path: rules/application/kubernetes/audit/kubernetes_audit_rolebinding_modification.yml

## Logsource

- product: kubernetes
- service: audit

## Detection

```yaml
selection:
  objectRef.apiGroup: rbac.authorization.k8s.io
  objectRef.resource:
  - clusterrolebindings
  - rolebindings
  verb:
  - create
  - delete
  - patch
  - replace
  - update
condition: selection
```

## False Positives

- Modifying a Kubernetes Rolebinding may need to be done by a system administrator.
- Automated processes may need to take these actions and may need to be filtered.

## References

- https://kubernetes.io/docs/reference/config-api/apiserver-audit.v1/
- https://medium.com/@seifeddinerajhi/kubernetes-rbac-privilege-escalation-exploits-and-mitigations-26c07629eeab

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_rolebinding_modification.yml)
