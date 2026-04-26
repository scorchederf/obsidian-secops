---
sigma_id: "402b955c-8fe0-4a8c-b635-622b4ac5f902"
title: "Container With A hostPath Mount Created"
framework: "sigma"
generated: "true"
source_path: "rules/application/kubernetes/audit/kubernetes_audit_hostpath_mount.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_hostpath_mount.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "low"
logsource: "kubernetes / audit / application"
aliases:
  - "402b955c-8fe0-4a8c-b635-622b4ac5f902"
  - "Container With A hostPath Mount Created"
attack_technique_ids:
  - "T1611"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Container With A hostPath Mount Created

Detects creation of a container with a hostPath mount.
A hostPath volume mounts a directory or a file from the node to the container.
Attackers who have permissions to create a new pod in the cluster may create one with a writable hostPath volume and chroot to escape to the underlying node.

## Metadata

- Rule ID: 402b955c-8fe0-4a8c-b635-622b4ac5f902
- Status: test
- Level: low
- Author: Leo Tsaousis (@laripping)
- Date: 2024-03-26
- Source Path: rules/application/kubernetes/audit/kubernetes_audit_hostpath_mount.yml

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
  hostPath: '*'
condition: selection
```

## False Positives

- The DaemonSet controller creates pods with hostPath volumes within the kube-system namespace.

## References

- https://microsoft.github.io/Threat-Matrix-for-Kubernetes/techniques/Writable%20hostPath%20mount/
- https://blog.appsecco.com/kubernetes-namespace-breakout-using-insecure-host-path-volume-part-1-b382f2a6e216

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_hostpath_mount.yml)
