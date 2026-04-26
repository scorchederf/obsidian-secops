---
sigma_id: "40967487-139b-4811-81d9-c9767a92aa5a"
title: "Deployment Deleted From Kubernetes Cluster"
framework: "sigma"
generated: "true"
source_path: "rules/application/kubernetes/audit/kubernetes_audit_deployment_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_deployment_deleted.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "low"
logsource: "kubernetes / audit / application"
aliases:
  - "40967487-139b-4811-81d9-c9767a92aa5a"
  - "Deployment Deleted From Kubernetes Cluster"
attack_technique_ids:
  - "T1498"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Deployment Deleted From Kubernetes Cluster

Detects the removal of a deployment from a Kubernetes cluster.
This could indicate disruptive activity aiming to impact business operations.

## Metadata

- Rule ID: 40967487-139b-4811-81d9-c9767a92aa5a
- Status: test
- Level: low
- Author: Leo Tsaousis (@laripping)
- Date: 2024-03-26
- Source Path: rules/application/kubernetes/audit/kubernetes_audit_deployment_deleted.yml

## Logsource

- category: application
- product: kubernetes
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1498-network_denial_of_service|T1498]]

## Detection

```yaml
selection:
  verb: delete
  objectRef.resource: deployments
condition: selection
```

## False Positives

- Unknown

## References

- https://microsoft.github.io/Threat-Matrix-for-Kubernetes/techniques/Data%20destruction/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_deployment_deleted.yml)
