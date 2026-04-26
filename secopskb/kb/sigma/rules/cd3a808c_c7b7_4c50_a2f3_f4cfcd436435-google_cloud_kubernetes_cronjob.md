---
sigma_id: "cd3a808c-c7b7-4c50-a2f3-f4cfcd436435"
title: "Google Cloud Kubernetes CronJob"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/gcp/audit/gcp_kubernetes_cronjob.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_kubernetes_cronjob.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "gcp / gcp.audit"
aliases:
  - "cd3a808c-c7b7-4c50-a2f3-f4cfcd436435"
  - "Google Cloud Kubernetes CronJob"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Google Cloud Kubernetes CronJob

Identifies when a Google Cloud Kubernetes CronJob runs in Azure Cloud. Kubernetes Job is a controller that creates one or more pods and ensures that a specified number of them successfully terminate.
Kubernetes Job can be used to run containers that perform finite tasks for batch jobs. Kubernetes CronJob is used to schedule Jobs.
An Adversary may use Kubernetes CronJob for scheduling execution of malicious code that would run as a container in the cluster.

## Metadata

- Rule ID: cd3a808c-c7b7-4c50-a2f3-f4cfcd436435
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-11-22
- Modified: 2022-12-25
- Source Path: rules/cloud/gcp/audit/gcp_kubernetes_cronjob.yml

## Logsource

- product: gcp
- service: gcp.audit

## Detection

```yaml
selection:
  gcp.audit.method_name:
  - io.k8s.api.batch.v*.Job
  - io.k8s.api.batch.v*.CronJob
condition: selection
```

## False Positives

- Google Cloud Kubernetes CronJob/Job may be done by a system administrator.
- If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://cloud.google.com/kubernetes-engine/docs
- https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/
- https://kubernetes.io/docs/concepts/workloads/controllers/job/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_kubernetes_cronjob.yml)
