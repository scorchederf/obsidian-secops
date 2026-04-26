---
sigma_id: "a80d927d-ac6e-443f-a867-e8d6e3897318"
title: "Creation Of Pod In System Namespace"
framework: "sigma"
generated: "true"
source_path: "rules/application/kubernetes/audit/kubernetes_audit_pod_in_system_namespace.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_pod_in_system_namespace.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "kubernetes / audit / application"
aliases:
  - "a80d927d-ac6e-443f-a867-e8d6e3897318"
  - "Creation Of Pod In System Namespace"
attack_technique_ids:
  - "T1036.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Creation Of Pod In System Namespace

Detects deployments of pods within the kube-system namespace, which could be intended to imitate system pods.
System pods, created by controllers such as Deployments or DaemonSets have random suffixes in their names.
Attackers can use this fact and name their backdoor pods as if they were created by these controllers to avoid detection.
Deployment of such a backdoor container e.g. named kube-proxy-bv61v, could be attempted in the kube-system namespace alongside the other administrative containers.

## Metadata

- Rule ID: a80d927d-ac6e-443f-a867-e8d6e3897318
- Status: test
- Level: medium
- Author: Leo Tsaousis (@laripping)
- Date: 2024-03-26
- Source Path: rules/application/kubernetes/audit/kubernetes_audit_pod_in_system_namespace.yml

## Logsource

- category: application
- product: kubernetes
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.005]]

## Detection

```yaml
selection:
  verb: create
  objectRef.resource: pods
  objectRef.namespace: kube-system
condition: selection
```

## False Positives

- System components such as daemon-set-controller and kube-scheduler also create pods in the kube-system namespace

## References

- https://microsoft.github.io/Threat-Matrix-for-Kubernetes/techniques/Pod%20or%20container%20name%20similarily/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_pod_in_system_namespace.yml)
