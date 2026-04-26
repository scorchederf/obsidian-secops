---
sigma_id: "a1b0ca4e-7835-413e-8471-3ff2b8a66be6"
title: "Potential Remote Command Execution In Pod Container"
framework: "sigma"
generated: "true"
source_path: "rules/application/kubernetes/audit/kubernetes_audit_exec_into_container.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_exec_into_container.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "kubernetes / audit / application"
aliases:
  - "a1b0ca4e-7835-413e-8471-3ff2b8a66be6"
  - "Potential Remote Command Execution In Pod Container"
attack_technique_ids:
  - "T1609"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Remote Command Execution In Pod Container

Detects attempts to execute remote commands, within a Pod's container using e.g. the "kubectl exec" command.

## Metadata

- Rule ID: a1b0ca4e-7835-413e-8471-3ff2b8a66be6
- Status: test
- Level: medium
- Author: Leo Tsaousis (@laripping)
- Date: 2024-03-26
- Source Path: rules/application/kubernetes/audit/kubernetes_audit_exec_into_container.yml

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
  verb: create
  objectRef.resource: pods
  objectRef.subresource: exec
condition: selection
```

## False Positives

- Legitimate debugging activity. Investigate the identity performing the requests and their authorization.

## References

- https://microsoft.github.io/Threat-Matrix-for-Kubernetes/techniques/Exec%20into%20container/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_exec_into_container.yml)
