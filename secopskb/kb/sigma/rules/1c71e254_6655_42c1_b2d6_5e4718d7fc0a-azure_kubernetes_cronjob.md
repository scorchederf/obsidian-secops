---
sigma_id: "1c71e254-6655-42c1-b2d6-5e4718d7fc0a"
title: "Azure Kubernetes CronJob"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_kubernetes_cronjob.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_kubernetes_cronjob.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "1c71e254-6655-42c1-b2d6-5e4718d7fc0a"
  - "Azure Kubernetes CronJob"
attack_technique_ids:
  - "T1053.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Kubernetes CronJob

Identifies when a Azure Kubernetes CronJob runs in Azure Cloud. Kubernetes Job is a controller that creates one or more pods and ensures that a specified number of them successfully terminate.
Kubernetes Job can be used to run containers that perform finite tasks for batch jobs. Kubernetes CronJob is used to schedule Jobs.
An Adversary may use Kubernetes CronJob for scheduling execution of malicious code that would run as a container in the cluster.

## Metadata

- Rule ID: 1c71e254-6655-42c1-b2d6-5e4718d7fc0a
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-11-22
- Modified: 2022-12-18
- Source Path: rules/cloud/azure/activity_logs/azure_kubernetes_cronjob.yml

## Logsource

- product: azure
- service: activitylogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.003]]

## Detection

```yaml
selection:
  operationName|startswith:
  - MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/BATCH
  - MICROSOFT.CONTAINERSERVICE/MANAGEDCLUSTERS/BATCH
  operationName|endswith:
  - /CRONJOBS/WRITE
  - /JOBS/WRITE
condition: selection
```

## False Positives

- Azure Kubernetes CronJob/Job may be done by a system administrator.
- If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations#microsoftkubernetes
- https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/
- https://kubernetes.io/docs/concepts/workloads/controllers/job/
- https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_kubernetes_cronjob.yml)
