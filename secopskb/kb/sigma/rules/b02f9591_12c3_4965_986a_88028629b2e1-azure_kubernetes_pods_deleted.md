---
sigma_id: "b02f9591-12c3-4965-986a-88028629b2e1"
title: "Azure Kubernetes Pods Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_kubernetes_pods_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_kubernetes_pods_deleted.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "b02f9591-12c3-4965-986a-88028629b2e1"
  - "Azure Kubernetes Pods Deleted"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Kubernetes Pods Deleted

Identifies the deletion of Azure Kubernetes Pods.

## Metadata

- Rule ID: b02f9591-12c3-4965-986a-88028629b2e1
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-07-24
- Modified: 2022-08-23
- Source Path: rules/cloud/azure/activity_logs/azure_kubernetes_pods_deleted.yml

## Logsource

- product: azure
- service: activitylogs

## Detection

```yaml
selection:
  operationName: MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/PODS/DELETE
condition: selection
```

## False Positives

- Pods may be deleted by a system administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Pods deletions from unfamiliar users or hosts should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations#microsoftkubernetes
- https://github.com/elastic/detection-rules/blob/065bf48a9987cd8bd826c098a30ce36e6868ee46/rules/integrations/azure/impact_kubernetes_pod_deleted.toml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_kubernetes_pods_deleted.yml)
