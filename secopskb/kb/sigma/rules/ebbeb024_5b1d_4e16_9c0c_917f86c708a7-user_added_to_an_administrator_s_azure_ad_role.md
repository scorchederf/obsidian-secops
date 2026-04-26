---
sigma_id: "ebbeb024-5b1d-4e16-9c0c-917f86c708a7"
title: "User Added to an Administrator's Azure AD Role"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_ad_user_added_to_admin_role.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_ad_user_added_to_admin_role.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "ebbeb024-5b1d-4e16-9c0c-917f86c708a7"
  - "User Added to an Administrator's Azure AD Role"
attack_technique_ids:
  - "T1098.003"
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# User Added to an Administrator's Azure AD Role

User Added to an Administrator's Azure AD Role

## Metadata

- Rule ID: ebbeb024-5b1d-4e16-9c0c-917f86c708a7
- Status: test
- Level: medium
- Author: Raphaël CALVET, @MetallicHack
- Date: 2021-10-04
- Modified: 2022-10-09
- Source Path: rules/cloud/azure/activity_logs/azure_ad_user_added_to_admin_role.yml

## Logsource

- product: azure
- service: activitylogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098.003]]
- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  Operation: Add member to role.
  Workload: AzureActiveDirectory
  ModifiedProperties{}.NewValue|endswith:
  - Admins
  - Administrator
condition: selection
```

## False Positives

- PIM (Privileged Identity Management) generates this event each time 'eligible role' is enabled.

## References

- https://m365internals.com/2021/07/13/what-ive-learned-from-doing-a-year-of-cloud-forensics-in-azure-ad/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_ad_user_added_to_admin_role.yml)
