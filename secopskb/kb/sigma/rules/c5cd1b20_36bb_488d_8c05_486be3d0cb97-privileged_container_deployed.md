---
sigma_id: "c5cd1b20-36bb-488d-8c05-486be3d0cb97"
title: "Privileged Container Deployed"
framework: "sigma"
generated: "true"
source_path: "rules/application/kubernetes/audit/kubernetes_audit_privileged_pod_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_privileged_pod_creation.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "low"
logsource: "kubernetes / audit / application"
aliases:
  - "c5cd1b20-36bb-488d-8c05-486be3d0cb97"
  - "Privileged Container Deployed"
attack_technique_ids:
  - "T1611"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Privileged Container Deployed

Detects the creation of a "privileged" container, an action which could be indicative of a threat actor mounting a container breakout attacks.
A privileged container is a container that can access the host with all of the root capabilities of the host machine. This allows it to view, interact and modify processes, network operations, IPC calls, the file system, mount points, SELinux configurations etc. as the root user on the host.
Various versions of "privileged" containers can be specified, e.g. by setting the securityContext.privileged flag in the resource specification, setting non-standard Linux capabilities, or configuring the hostNetwork/hostPID fields

## Metadata

- Rule ID: c5cd1b20-36bb-488d-8c05-486be3d0cb97
- Status: test
- Level: low
- Author: Leo Tsaousis (@laripping)
- Date: 2024-03-26
- Source Path: rules/application/kubernetes/audit/kubernetes_audit_privileged_pod_creation.yml

## Logsource

- category: application
- product: kubernetes
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1611-escape_to_host|T1611]]

## Detection

```yaml
selection:
  verb: create
  objectRef.resource: pods
  capabilities: '*'
condition: selection
```

## False Positives

- Unknown

## References

- https://microsoft.github.io/Threat-Matrix-for-Kubernetes/techniques/Privileged%20container/
- https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-kubernetes.html#privilegeescalation-kubernetes-privilegedcontainer
- https://www.elastic.co/guide/en/security/current/kubernetes-pod-created-with-hostnetwork.html
- https://www.elastic.co/guide/en/security/current/kubernetes-container-created-with-excessive-linux-capabilities.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_privileged_pod_creation.yml)
