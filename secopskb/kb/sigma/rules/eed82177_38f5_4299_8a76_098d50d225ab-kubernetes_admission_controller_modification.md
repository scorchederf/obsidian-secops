---
sigma_id: "eed82177-38f5-4299-8a76-098d50d225ab"
title: "Kubernetes Admission Controller Modification"
framework: "sigma"
generated: "true"
source_path: "rules/application/kubernetes/audit/kubernetes_audit_change_admission_controller.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_change_admission_controller.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "kubernetes / audit"
aliases:
  - "eed82177-38f5-4299-8a76-098d50d225ab"
  - "Kubernetes Admission Controller Modification"
attack_technique_ids:
  - "T1078"
  - "T1552"
  - "T1552.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Kubernetes Admission Controller Modification

Detects when a modification (create, update or replace) action is taken that affects mutating or validating webhook configurations, as they can be used by an adversary to achieve persistence or exfiltrate access credentials.

## Metadata

- Rule ID: eed82177-38f5-4299-8a76-098d50d225ab
- Status: test
- Level: medium
- Author: kelnage
- Date: 2024-07-11
- Source Path: rules/application/kubernetes/audit/kubernetes_audit_change_admission_controller.yml

## Logsource

- product: kubernetes
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]
- [[kb/attack/techniques/T1552-unsecured_credentials|T1552]]
- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.007]]

## Detection

```yaml
selection:
  objectRef.apiGroup: admissionregistration.k8s.io
  objectRef.resource:
  - mutatingwebhookconfigurations
  - validatingwebhookconfigurations
  verb:
  - create
  - delete
  - patch
  - replace
  - update
condition: selection
```

## False Positives

- Modifying the Kubernetes Admission Controller may need to be done by a system administrator.
- Automated processes may need to take these actions and may need to be filtered.

## References

- https://kubernetes.io/docs/reference/config-api/apiserver-audit.v1/
- https://security.padok.fr/en/blog/kubernetes-webhook-attackers

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_change_admission_controller.yml)
