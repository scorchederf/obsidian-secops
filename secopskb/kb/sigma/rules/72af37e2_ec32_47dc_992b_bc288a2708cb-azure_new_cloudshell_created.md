---
sigma_id: "72af37e2-ec32-47dc-992b-bc288a2708cb"
title: "Azure New CloudShell Created"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_new_cloudshell_created.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_new_cloudshell_created.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "72af37e2-ec32-47dc-992b-bc288a2708cb"
  - "Azure New CloudShell Created"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure New CloudShell Created

Identifies when a new cloudshell is created inside of Azure portal.

## Metadata

- Rule ID: 72af37e2-ec32-47dc-992b-bc288a2708cb
- Status: test
- Level: medium
- Author: Austin Songer
- Date: 2021-09-21
- Modified: 2022-08-23
- Source Path: rules/cloud/azure/activity_logs/azure_new_cloudshell_created.yml

## Logsource

- product: azure
- service: activitylogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection:
  operationName: MICROSOFT.PORTAL/CONSOLES/WRITE
condition: selection
```

## False Positives

- A new cloudshell may be created by a system administrator.

## References

- https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_new_cloudshell_created.yml)
