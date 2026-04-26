---
sigma_id: "0322d9f2-289a-47c2-b5e1-b63c90901a3e"
title: "Google Cloud Kubernetes RoleBinding"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/gcp/audit/gcp_kubernetes_rolebinding.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_kubernetes_rolebinding.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "gcp / gcp.audit"
aliases:
  - "0322d9f2-289a-47c2-b5e1-b63c90901a3e"
  - "Google Cloud Kubernetes RoleBinding"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Google Cloud Kubernetes RoleBinding

Detects the creation or patching of potential malicious RoleBinding. This includes RoleBindings and ClusterRoleBinding.

## Metadata

- Rule ID: 0322d9f2-289a-47c2-b5e1-b63c90901a3e
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-09
- Modified: 2022-10-09
- Source Path: rules/cloud/gcp/audit/gcp_kubernetes_rolebinding.yml

## Logsource

- product: gcp
- service: gcp.audit

## Detection

```yaml
selection:
  gcp.audit.method_name:
  - io.k8s.authorization.rbac.v*.clusterrolebindings.create
  - io.k8s.authorization.rbac.v*.rolebindings.create
  - io.k8s.authorization.rbac.v*.clusterrolebindings.patch
  - io.k8s.authorization.rbac.v*.rolebindings.patch
  - io.k8s.authorization.rbac.v*.clusterrolebindings.update
  - io.k8s.authorization.rbac.v*.rolebindings.update
  - io.k8s.authorization.rbac.v*.clusterrolebindings.delete
  - io.k8s.authorization.rbac.v*.rolebindings.delete
condition: selection
```

## False Positives

- RoleBindings and ClusterRoleBinding being modified or deleted may be performed by a system administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- RoleBindings and ClusterRoleBinding modified or deleted from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://github.com/elastic/detection-rules/pull/1267
- https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/cluster-role-v1/#ClusterRole
- https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control
- https://kubernetes.io/docs/reference/access-authn-authz/rbac/
- https://cloud.google.com/kubernetes-engine/docs/how-to/audit-logging

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_kubernetes_rolebinding.yml)
