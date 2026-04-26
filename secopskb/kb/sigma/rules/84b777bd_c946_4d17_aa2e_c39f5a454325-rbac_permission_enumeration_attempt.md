---
sigma_id: "84b777bd-c946-4d17-aa2e-c39f5a454325"
title: "RBAC Permission Enumeration Attempt"
framework: "sigma"
generated: "true"
source_path: "rules/application/kubernetes/audit/kubernetes_audit_rbac_permisions_listing.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_rbac_permisions_listing.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "low"
logsource: "kubernetes / audit / application"
aliases:
  - "84b777bd-c946-4d17-aa2e-c39f5a454325"
  - "RBAC Permission Enumeration Attempt"
attack_technique_ids:
  - "T1069.003"
  - "T1087.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# RBAC Permission Enumeration Attempt

Detects identities attempting to enumerate their Kubernetes RBAC permissions.
In the early stages of a breach, attackers will aim to list the permissions they have within the compromised environment.
In a Kubernetes cluster, this can be achieved by interacting with the API server, and querying the SelfSubjectAccessReview API via e.g. a "kubectl auth can-i --list" command.
This will enumerate the Role-Based Access Controls (RBAC) rules defining the compromised user's authorization.

## Metadata

- Rule ID: 84b777bd-c946-4d17-aa2e-c39f5a454325
- Status: test
- Level: low
- Author: Leo Tsaousis (@laripping)
- Date: 2024-03-26
- Source Path: rules/application/kubernetes/audit/kubernetes_audit_rbac_permisions_listing.yml

## Logsource

- category: application
- product: kubernetes
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.003]]
- [[kb/attack/techniques/T1087-account_discovery|T1087.004]]

## Detection

```yaml
selection:
  verb: create
  apiGroup: authorization.k8s.io
  objectRef.resource: selfsubjectrulesreviews
condition: selection
```

## False Positives

- Unknown

## References

- https://www.elastic.co/guide/en/security/current/kubernetes-suspicious-self-subject-review.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_rbac_permisions_listing.yml)
