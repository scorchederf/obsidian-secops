---
sigma_id: "288a39fc-4914-4831-9ada-270e9dc12cb4"
title: "Azure Active Directory Hybrid Health AD FS New Server"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_aadhybridhealth_adfs_new_server.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_aadhybridhealth_adfs_new_server.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "288a39fc-4914-4831-9ada-270e9dc12cb4"
  - "Azure Active Directory Hybrid Health AD FS New Server"
attack_technique_ids:
  - "T1578"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Active Directory Hybrid Health AD FS New Server

This detection uses azureactivity logs (Administrative category) to identify the creation or update of a server instance in an Azure AD Hybrid health AD FS service.
A threat actor can create a new AD Health ADFS service and create a fake server instance to spoof AD FS signing logs. There is no need to compromise an on-prem AD FS server.
This can be done programmatically via HTTP requests to Azure.

## Metadata

- Rule ID: 288a39fc-4914-4831-9ada-270e9dc12cb4
- Status: test
- Level: medium
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research), MSTIC
- Date: 2021-08-26
- Modified: 2023-10-11
- Source Path: rules/cloud/azure/activity_logs/azure_aadhybridhealth_adfs_new_server.yml

## Logsource

- product: azure
- service: activitylogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1578-modify_cloud_compute_infrastructure|T1578]]

## Detection

```yaml
selection:
  CategoryValue: Administrative
  ResourceProviderValue: Microsoft.ADHybridHealthService
  ResourceId|contains: AdFederationService
  OperationNameValue: Microsoft.ADHybridHealthService/services/servicemembers/action
condition: selection
```

## False Positives

- Legitimate AD FS servers added to an AAD Health AD FS service instance

## References

- https://o365blog.com/post/hybridhealthagent/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_aadhybridhealth_adfs_new_server.yml)
