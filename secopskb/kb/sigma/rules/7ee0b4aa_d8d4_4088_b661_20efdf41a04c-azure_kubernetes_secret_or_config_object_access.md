---
sigma_id: "7ee0b4aa-d8d4-4088-b661-20efdf41a04c"
title: "Azure Kubernetes Secret or Config Object Access"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_kubernetes_secret_or_config_object_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_kubernetes_secret_or_config_object_access.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "7ee0b4aa-d8d4-4088-b661-20efdf41a04c"
  - "Azure Kubernetes Secret or Config Object Access"
attack_technique_ids:
  - "T1485"
  - "T1496"
  - "T1489"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Kubernetes Secret or Config Object Access

Identifies when a Kubernetes account access a sensitive objects such as configmaps or secrets.

## Metadata

- Rule ID: 7ee0b4aa-d8d4-4088-b661-20efdf41a04c
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-07
- Modified: 2022-08-23
- Source Path: rules/cloud/azure/activity_logs/azure_kubernetes_secret_or_config_object_access.yml

## Logsource

- product: azure
- service: activitylogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1485-data_destruction|T1485]]
- [[kb/attack/techniques/T1496-resource_hijacking|T1496]]
- [[kb/attack/techniques/T1489-service_stop|T1489]]

## Detection

```yaml
selection:
  operationName:
  - MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/CONFIGMAPS/WRITE
  - MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/CONFIGMAPS/DELETE
  - MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/SECRETS/WRITE
  - MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/SECRETS/DELETE
condition: selection
```

## False Positives

- Sensitive objects may be accessed by a system administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment. Sensitive objects accessed from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations#microsoftkubernetes
- https://www.microsoft.com/security/blog/2021/03/23/secure-containerized-environments-with-updated-threat-matrix-for-kubernetes/
- https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes/
- https://medium.com/mitre-engenuity/att-ck-for-containers-now-available-4c2359654bf1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_kubernetes_secret_or_config_object_access.yml)
