---
sigma_id: "3132570d-cab2-4561-9ea6-1743644b2290"
title: "Kubernetes Events Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/application/kubernetes/audit/kubernetes_audit_events_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_events_deleted.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "kubernetes / audit / application"
aliases:
  - "3132570d-cab2-4561-9ea6-1743644b2290"
  - "Kubernetes Events Deleted"
attack_technique_ids:
  - "T1070"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Kubernetes Events Deleted

Detects when events are deleted in Kubernetes.
An adversary may delete Kubernetes events in an attempt to evade detection.

## Metadata

- Rule ID: 3132570d-cab2-4561-9ea6-1743644b2290
- Status: test
- Level: medium
- Author: Leo Tsaousis (@laripping)
- Date: 2024-03-26
- Source Path: rules/application/kubernetes/audit/kubernetes_audit_events_deleted.yml

## Logsource

- category: application
- product: kubernetes
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070]]

## Detection

```yaml
selection:
  verb: delete
  objectRef.resource: events
condition: selection
```

## False Positives

- Unknown

## References

- https://microsoft.github.io/Threat-Matrix-for-Kubernetes/techniques/Delete%20K8S%20events/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_events_deleted.yml)
