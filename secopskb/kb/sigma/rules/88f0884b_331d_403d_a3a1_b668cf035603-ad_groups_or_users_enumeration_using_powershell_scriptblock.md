---
sigma_id: "88f0884b-331d-403d-a3a1-b668cf035603"
title: "AD Groups Or Users Enumeration Using PowerShell - ScriptBlock"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_ad_group_reco.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_ad_group_reco.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "low"
logsource: "windows / ps_script"
aliases:
  - "88f0884b-331d-403d-a3a1-b668cf035603"
  - "AD Groups Or Users Enumeration Using PowerShell - ScriptBlock"
attack_technique_ids:
  - "T1069.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AD Groups Or Users Enumeration Using PowerShell - ScriptBlock

Adversaries may attempt to find domain-level groups and permission settings.
The knowledge of domain-level permission groups can help adversaries determine which groups exist and which users belong to a particular group.
Adversaries may use this information to determine which users have elevated permissions, such as domain administrators.

## Metadata

- Rule ID: 88f0884b-331d-403d-a3a1-b668cf035603
- Status: test
- Level: low
- Author: frack113
- Date: 2021-12-15
- Modified: 2022-12-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_ad_group_reco.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.001]]

## Detection

```yaml
test_2:
  ScriptBlockText|contains: get-ADPrincipalGroupMembership
test_7:
  ScriptBlockText|contains|all:
  - get-aduser
  - '-f '
  - '-pr '
  - DoesNotRequirePreAuth
condition: 1 of test_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1069.002/T1069.002.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_ad_group_reco.yml)
