---
sigma_id: "e31bae15-83ed-473e-bf31-faf4f8a17d36"
title: "New Kubernetes Service Account Created"
framework: "sigma"
generated: "true"
source_path: "rules/application/kubernetes/audit/kubernetes_audit_serviceaccount_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_serviceaccount_creation.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "low"
logsource: "kubernetes / audit / application"
aliases:
  - "e31bae15-83ed-473e-bf31-faf4f8a17d36"
  - "New Kubernetes Service Account Created"
attack_technique_ids:
  - "T1136"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Kubernetes Service Account Created

Detects creation of new Kubernetes service account, which could indicate an attacker's attempt to persist within a cluster.

## Metadata

- Rule ID: e31bae15-83ed-473e-bf31-faf4f8a17d36
- Status: test
- Level: low
- Author: Leo Tsaousis (@laripping)
- Date: 2024-03-26
- Source Path: rules/application/kubernetes/audit/kubernetes_audit_serviceaccount_creation.yml

## Logsource

- category: application
- product: kubernetes
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1136-create_account|T1136]]

## Detection

```yaml
selection:
  verb: create
  objectRef.resource: serviceaccounts
condition: selection
```

## False Positives

- Unknown

## References

- https://microsoft.github.io/Threat-Matrix-for-Kubernetes/techniques/container%20service%20account/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_serviceaccount_creation.yml)
