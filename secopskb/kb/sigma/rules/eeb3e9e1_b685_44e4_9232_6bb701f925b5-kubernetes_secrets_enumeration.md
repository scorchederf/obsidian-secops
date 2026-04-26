---
sigma_id: "eeb3e9e1-b685-44e4-9232-6bb701f925b5"
title: "Kubernetes Secrets Enumeration"
framework: "sigma"
generated: "true"
source_path: "rules/application/kubernetes/audit/kubernetes_audit_secrets_enumeration.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_secrets_enumeration.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "low"
logsource: "kubernetes / audit / application"
aliases:
  - "eeb3e9e1-b685-44e4-9232-6bb701f925b5"
  - "Kubernetes Secrets Enumeration"
attack_technique_ids:
  - "T1552.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Kubernetes Secrets Enumeration

Detects enumeration of Kubernetes secrets.

## Metadata

- Rule ID: eeb3e9e1-b685-44e4-9232-6bb701f925b5
- Status: test
- Level: low
- Author: Leo Tsaousis (@laripping)
- Date: 2024-03-26
- Source Path: rules/application/kubernetes/audit/kubernetes_audit_secrets_enumeration.yml

## Logsource

- category: application
- product: kubernetes
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.007]]

## Detection

```yaml
selection:
  verb: list
  objectRef.resource: secrets
condition: selection
```

## False Positives

- The Kubernetes dashboard occasionally accesses the kubernetes-dashboard-key-holder secret

## References

- https://microsoft.github.io/Threat-Matrix-for-Kubernetes/techniques/List%20K8S%20secrets/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_secrets_enumeration.yml)
