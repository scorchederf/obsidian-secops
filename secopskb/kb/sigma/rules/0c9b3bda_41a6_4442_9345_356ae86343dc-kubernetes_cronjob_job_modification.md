---
sigma_id: "0c9b3bda-41a6-4442-9345-356ae86343dc"
title: "Kubernetes CronJob/Job Modification"
framework: "sigma"
generated: "true"
source_path: "rules/application/kubernetes/audit/kubernetes_audit_cronjob_modification.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_cronjob_modification.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "kubernetes / audit"
aliases:
  - "0c9b3bda-41a6-4442-9345-356ae86343dc"
  - "Kubernetes CronJob/Job Modification"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Kubernetes CronJob/Job Modification

Detects when a Kubernetes CronJob or Job is created or modified.
A Kubernetes Job creates one or more pods to accomplish a specific task, and a CronJob creates Jobs on a recurring schedule.
An adversary can take advantage of this Kubernetes object to schedule Jobs to run containers that execute malicious code within a cluster, allowing them to achieve persistence.

## Metadata

- Rule ID: 0c9b3bda-41a6-4442-9345-356ae86343dc
- Status: test
- Level: medium
- Author: kelnage
- Date: 2024-07-11
- Source Path: rules/application/kubernetes/audit/kubernetes_audit_cronjob_modification.yml

## Logsource

- product: kubernetes
- service: audit

## Detection

```yaml
selection:
  objectRef.apiGroup: batch
  objectRef.resource:
  - cronjobs
  - jobs
  verb:
  - create
  - delete
  - patch
  - replace
  - update
condition: selection
```

## False Positives

- Modifying a Kubernetes Job or CronJob may need to be done by a system administrator.
- Automated processes may need to take these actions and may need to be filtered.

## References

- https://kubernetes.io/docs/reference/config-api/apiserver-audit.v1/
- https://www.redhat.com/en/blog/protecting-kubernetes-against-mitre-attck-persistence#technique-33-kubernetes-cronjob

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/kubernetes/audit/kubernetes_audit_cronjob_modification.yml)
