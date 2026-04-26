---
sigma_id: "48739819-8230-4ee3-a8ea-e0289d1fb0ff"
title: "Azure Active Directory Hybrid Health AD FS Service Delete"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_aadhybridhealth_adfs_service_delete.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_aadhybridhealth_adfs_service_delete.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "48739819-8230-4ee3-a8ea-e0289d1fb0ff"
  - "Azure Active Directory Hybrid Health AD FS Service Delete"
attack_technique_ids:
  - "T1578.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Active Directory Hybrid Health AD FS Service Delete

This detection uses azureactivity logs (Administrative category) to identify the deletion of an Azure AD Hybrid health AD FS service instance in a tenant.
A threat actor can create a new AD Health ADFS service and create a fake server to spoof AD FS signing logs.
The health AD FS service can then be deleted after it is not longer needed via HTTP requests to Azure.

## Metadata

- Rule ID: 48739819-8230-4ee3-a8ea-e0289d1fb0ff
- Status: test
- Level: medium
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research), MSTIC
- Date: 2021-08-26
- Modified: 2023-10-11
- Source Path: rules/cloud/azure/activity_logs/azure_aadhybridhealth_adfs_service_delete.yml

## Logsource

- product: azure
- service: activitylogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1578-modify_cloud_compute_infrastructure|T1578.003]]

## Detection

```yaml
selection:
  CategoryValue: Administrative
  ResourceProviderValue: Microsoft.ADHybridHealthService
  ResourceId|contains: AdFederationService
  OperationNameValue: Microsoft.ADHybridHealthService/services/delete
condition: selection
```

## False Positives

- Legitimate AAD Health AD FS service instances being deleted in a tenant

## References

- https://o365blog.com/post/hybridhealthagent/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_aadhybridhealth_adfs_service_delete.yml)
