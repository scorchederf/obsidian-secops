---
sigma_id: "815bfc17-7fc6-4908-a55e-2f37b98cedb4"
title: "AD Groups Or Users Enumeration Using PowerShell - PoshModule"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_susp_ad_group_reco.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_susp_ad_group_reco.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "low"
logsource: "windows / ps_module"
aliases:
  - "815bfc17-7fc6-4908-a55e-2f37b98cedb4"
  - "AD Groups Or Users Enumeration Using PowerShell - PoshModule"
attack_technique_ids:
  - "T1069.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AD Groups Or Users Enumeration Using PowerShell - PoshModule

Adversaries may attempt to find domain-level groups and permission settings.
The knowledge of domain-level permission groups can help adversaries determine which groups exist and which users belong to a particular group.
Adversaries may use this information to determine which users have elevated permissions, such as domain administrators.

## Metadata

- Rule ID: 815bfc17-7fc6-4908-a55e-2f37b98cedb4
- Status: test
- Level: low
- Author: frack113
- Date: 2021-12-15
- Modified: 2023-01-20
- Source Path: rules/windows/powershell/powershell_module/posh_pm_susp_ad_group_reco.yml

## Logsource

- category: ps_module
- definition: 0ad03ef1-f21b-4a79-8ce8-e6900c54b65b
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.001]]

## Detection

```yaml
selection_ad_principal:
- Payload|contains: get-ADPrincipalGroupMembership
- ContextInfo|contains: get-ADPrincipalGroupMembership
selection_get_aduser:
- Payload|contains|all:
  - get-aduser
  - '-f '
  - '-pr '
  - DoesNotRequirePreAuth
- ContextInfo|contains|all:
  - get-aduser
  - '-f '
  - '-pr '
  - DoesNotRequirePreAuth
condition: 1 of selection_*
```

## False Positives

- Administrator script

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1069.002/T1069.002.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_susp_ad_group_reco.yml)
