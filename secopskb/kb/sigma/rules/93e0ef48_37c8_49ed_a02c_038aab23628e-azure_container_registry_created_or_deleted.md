---
sigma_id: "93e0ef48-37c8-49ed-a02c-038aab23628e"
title: "Azure Container Registry Created or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_container_registry_created_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_container_registry_created_or_deleted.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "low"
logsource: "azure / activitylogs"
aliases:
  - "93e0ef48-37c8-49ed-a02c-038aab23628e"
  - "Azure Container Registry Created or Deleted"
attack_technique_ids:
  - "T1485"
  - "T1496"
  - "T1489"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Container Registry Created or Deleted

Detects when a Container Registry is created or deleted.

## Metadata

- Rule ID: 93e0ef48-37c8-49ed-a02c-038aab23628e
- Status: test
- Level: low
- Author: Austin Songer @austinsonger
- Date: 2021-08-07
- Modified: 2022-08-23
- Source Path: rules/cloud/azure/activity_logs/azure_container_registry_created_or_deleted.yml

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
  - MICROSOFT.CONTAINERREGISTRY/REGISTRIES/WRITE
  - MICROSOFT.CONTAINERREGISTRY/REGISTRIES/DELETE
condition: selection
```

## False Positives

- Container Registry being created or deleted may be performed by a system administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Container Registry created or deleted from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations#microsoftkubernetes
- https://www.microsoft.com/security/blog/2021/03/23/secure-containerized-environments-with-updated-threat-matrix-for-kubernetes/
- https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes/
- https://medium.com/mitre-engenuity/att-ck-for-containers-now-available-4c2359654bf1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_container_registry_created_or_deleted.yml)
