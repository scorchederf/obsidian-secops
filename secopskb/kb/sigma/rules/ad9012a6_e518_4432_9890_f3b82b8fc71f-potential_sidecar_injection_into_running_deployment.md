---
sigma_id: "ad9012a6-e518-4432-9890-f3b82b8fc71f"
title: "Potential Sidecar Injection Into Running Deployment"
framework: "sigma"
generated: "true"
source_path: "rules/application/kubernetes/audit/kubernetes_audit_sidecar_injection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_sidecar_injection.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "kubernetes / audit / application"
aliases:
  - "ad9012a6-e518-4432-9890-f3b82b8fc71f"
  - "Potential Sidecar Injection Into Running Deployment"
attack_technique_ids:
  - "T1609"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Sidecar Injection Into Running Deployment

Detects attempts to inject a sidecar container into a running deployment.
A sidecar container is an additional container within a pod, that resides alongside the main container.
One way to add containers to running resources like Deployments/DeamonSets/StatefulSets, is via a "kubectl patch" operation.
By injecting a new container within a legitimate pod, an attacker can run their code and hide their activity, instead of running their own separated pod in the cluster.

## Metadata

- Rule ID: ad9012a6-e518-4432-9890-f3b82b8fc71f
- Status: test
- Level: medium
- Author: Leo Tsaousis (@laripping)
- Date: 2024-03-26
- Source Path: rules/application/kubernetes/audit/kubernetes_audit_sidecar_injection.yml

## Logsource

- category: application
- product: kubernetes
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1609-container_administration_command|T1609]]

## Detection

```yaml
selection:
  verb: patch
  apiGroup: apps
  objectRef.resource: deployments
condition: selection
```

## False Positives

- Unknown

## References

- https://kubernetes.io/docs/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch
- https://microsoft.github.io/Threat-Matrix-for-Kubernetes/techniques/Sidecar%20Injection/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_sidecar_injection.yml)
