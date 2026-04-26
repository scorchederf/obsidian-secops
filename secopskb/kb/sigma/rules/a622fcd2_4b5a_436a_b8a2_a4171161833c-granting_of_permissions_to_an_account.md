---
sigma_id: "a622fcd2-4b5a-436a-b8a2-a4171161833c"
title: "Granting Of Permissions To An Account"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_granting_permission_detection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_granting_permission_detection.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "a622fcd2-4b5a-436a-b8a2-a4171161833c"
  - "Granting Of Permissions To An Account"
attack_technique_ids:
  - "T1098.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Granting Of Permissions To An Account

Identifies IPs from which users grant access to other users on azure resources and alerts when a previously unseen source IP address is used.

## Metadata

- Rule ID: a622fcd2-4b5a-436a-b8a2-a4171161833c
- Status: test
- Level: medium
- Author: sawwinnnaung
- Date: 2020-05-07
- Modified: 2023-10-11
- Source Path: rules/cloud/azure/activity_logs/azure_granting_permission_detection.yml

## Logsource

- product: azure
- service: activitylogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098.003]]

## Detection

```yaml
keywords:
- Microsoft.Authorization/roleAssignments/write
condition: keywords
```

## False Positives

- Valid change

## References

- https://github.com/Azure/Azure-Sentinel/blob/e534407884b1ec5371efc9f76ead282176c9e8bb/Detections/AzureActivity/Granting_Permissions_To_Account_detection.yaml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_granting_permission_detection.yml)
