---
sigma_id: "c625d754-6a3d-4f65-9c9a-536aea960d37"
title: "Permission Check Via Accesschk.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sysinternals_accesschk_check_permissions.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_accesschk_check_permissions.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "c625d754-6a3d-4f65-9c9a-536aea960d37"
  - "Permission Check Via Accesschk.EXE"
attack_technique_ids:
  - "T1069.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Permission Check Via Accesschk.EXE

Detects the usage of the "Accesschk" utility, an access and privilege audit tool developed by SysInternal and often being abused by attacker to verify process privileges

## Metadata

- Rule ID: c625d754-6a3d-4f65-9c9a-536aea960d37
- Status: test
- Level: medium
- Author: Teymur Kheirkhabarov (idea), Mangatas Tondang, oscd.community, Nasreddine Bencherchali (Nextron Systems)
- Date: 2020-10-13
- Modified: 2023-02-20
- Source Path: rules/windows/process_creation/proc_creation_win_sysinternals_accesschk_check_permissions.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.001]]

## Detection

```yaml
selection_img:
- Product|endswith: AccessChk
- Description|contains: Reports effective permissions
- Image|endswith:
  - \accesschk.exe
  - \accesschk64.exe
- OriginalFileName: accesschk.exe
selection_cli:
  CommandLine|contains:
  - 'uwcqv '
  - 'kwsu '
  - 'qwsu '
  - 'uwdqs '
condition: all of selection*
```

## False Positives

- System administrator Usage

## References

- https://speakerdeck.com/heirhabarov/hunting-for-privilege-escalation-in-windows-environment?slide=43
- https://www.youtube.com/watch?v=JGs-aKf2OtU&ab_channel=OFFZONEMOSCOW
- https://github.com/carlospolop/PEASS-ng/blob/fa0f2e17fbc1d86f1fd66338a40e665e7182501d/winPEAS/winPEASbat/winPEAS.bat
- https://github.com/gladiatx0r/Powerless/blob/04f553bbc0c65baf4e57344deff84e3f016e6b51/Powerless.bat

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_accesschk_check_permissions.yml)
