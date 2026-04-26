---
sigma_id: "f376c8a7-a2d0-4ddc-aa0c-16c17236d962"
title: "HackTool - Bloodhound/Sharphound Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_bloodhound_sharphound.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_bloodhound_sharphound.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f376c8a7-a2d0-4ddc-aa0c-16c17236d962"
  - "HackTool - Bloodhound/Sharphound Execution"
attack_technique_ids:
  - "T1087.001"
  - "T1087.002"
  - "T1482"
  - "T1069.001"
  - "T1069.002"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - Bloodhound/Sharphound Execution

Detects command line parameters used by Bloodhound and Sharphound hack tools

## Metadata

- Rule ID: f376c8a7-a2d0-4ddc-aa0c-16c17236d962
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2019-12-20
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_bloodhound_sharphound.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1087-account_discovery|T1087.001]]
- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]
- [[kb/attack/techniques/T1482-domain_trust_discovery|T1482]]
- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.001]]
- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.002]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_img:
- Product|contains: SharpHound
- Description|contains: SharpHound
- Company|contains:
  - SpecterOps
  - evil corp
- Image|contains:
  - \Bloodhound.exe
  - \SharpHound.exe
selection_cli_1:
  CommandLine|contains:
  - ' -CollectionMethod All '
  - ' --CollectionMethods Session '
  - ' --Loop --Loopduration '
  - ' --PortScanTimeout '
  - '.exe -c All -d '
  - Invoke-Bloodhound
  - Get-BloodHoundData
selection_cli_2:
  CommandLine|contains|all:
  - ' -JsonFolder '
  - ' -ZipFileName '
selection_cli_3:
  CommandLine|contains|all:
  - ' DCOnly '
  - ' --NoSaveCache '
condition: 1 of selection_*
```

## False Positives

- Other programs that use these command line option and accepts an 'All' parameter

## References

- https://github.com/BloodHoundAD/BloodHound
- https://github.com/BloodHoundAD/SharpHound

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_bloodhound_sharphound.yml)
