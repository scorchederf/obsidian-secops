---
sigma_id: "c1182e02-49a3-481c-b3de-0fadc4091488"
title: "Rare Subscription-level Operations In Azure"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_rare_operations.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_rare_operations.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "c1182e02-49a3-481c-b3de-0fadc4091488"
  - "Rare Subscription-level Operations In Azure"
attack_technique_ids:
  - "T1003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Rare Subscription-level Operations In Azure

Identifies IPs from which users grant access to other users on azure resources and alerts when a previously unseen source IP address is used.

## Metadata

- Rule ID: c1182e02-49a3-481c-b3de-0fadc4091488
- Status: test
- Level: medium
- Author: sawwinnnaung
- Date: 2020-05-07
- Modified: 2023-10-11
- Source Path: rules/cloud/azure/activity_logs/azure_rare_operations.yml

## Logsource

- product: azure
- service: activitylogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]

## Detection

```yaml
keywords:
- Microsoft.DocumentDB/databaseAccounts/listKeys/action
- Microsoft.Maps/accounts/listKeys/action
- Microsoft.Media/mediaservices/listKeys/action
- Microsoft.CognitiveServices/accounts/listKeys/action
- Microsoft.Storage/storageAccounts/listKeys/action
- Microsoft.Compute/snapshots/write
- Microsoft.Network/networkSecurityGroups/write
condition: keywords
```

## False Positives

- Valid change

## References

- https://github.com/Azure/Azure-Sentinel/blob/e534407884b1ec5371efc9f76ead282176c9e8bb/Detections/AzureActivity/RareOperations.yaml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_rare_operations.yml)
