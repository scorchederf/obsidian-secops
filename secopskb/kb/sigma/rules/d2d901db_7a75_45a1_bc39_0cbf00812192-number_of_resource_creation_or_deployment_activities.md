---
sigma_id: "d2d901db-7a75-45a1-bc39-0cbf00812192"
title: "Number Of Resource Creation Or Deployment Activities"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_creating_number_of_resources_detection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_creating_number_of_resources_detection.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "d2d901db-7a75-45a1-bc39-0cbf00812192"
  - "Number Of Resource Creation Or Deployment Activities"
attack_technique_ids:
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Number Of Resource Creation Or Deployment Activities

Number of VM creations or deployment activities occur in Azure via the azureactivity log.

## Metadata

- Rule ID: d2d901db-7a75-45a1-bc39-0cbf00812192
- Status: test
- Level: medium
- Author: sawwinnnaung
- Date: 2020-05-07
- Modified: 2023-10-11
- Source Path: rules/cloud/azure/activity_logs/azure_creating_number_of_resources_detection.yml

## Logsource

- product: azure
- service: activitylogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Detection

```yaml
keywords:
- Microsoft.Compute/virtualMachines/write
- Microsoft.Resources/deployments/write
condition: keywords
```

## False Positives

- Valid change

## References

- https://github.com/Azure/Azure-Sentinel/blob/e534407884b1ec5371efc9f76ead282176c9e8bb/Detections/AzureActivity/Creating_Anomalous_Number_Of_Resources_detection.yaml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_creating_number_of_resources_detection.yml)
