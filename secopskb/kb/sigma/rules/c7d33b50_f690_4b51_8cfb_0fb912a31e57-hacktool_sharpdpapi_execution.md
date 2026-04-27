---
sigma_id: "c7d33b50-f690-4b51-8cfb-0fb912a31e57"
title: "HackTool - SharpDPAPI Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_sharp_dpapi_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharp_dpapi_execution.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "c7d33b50-f690-4b51-8cfb-0fb912a31e57"
  - "HackTool - SharpDPAPI Execution"
attack_technique_ids:
  - "T1134.001"
  - "T1134.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# HackTool - SharpDPAPI Execution

Detects the execution of the SharpDPAPI tool based on CommandLine flags and PE metadata.
SharpDPAPI is a C# port of some DPAPI functionality from the Mimikatz project.

## Metadata

- Rule ID: c7d33b50-f690-4b51-8cfb-0fb912a31e57
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2024-06-26
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_sharp_dpapi_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.001]]
- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.003]]

## Detection

```yaml
selection_img:
- Image|endswith: \SharpDPAPI.exe
- OriginalFileName: SharpDPAPI.exe
selection_other_cli:
  CommandLine|contains:
  - ' backupkey '
  - ' blob '
  - ' certificates '
  - ' credentials '
  - ' keepass '
  - ' masterkeys '
  - ' rdg '
  - ' vaults '
selection_other_options_guid:
  CommandLine|contains|all:
  - ' {'
  - '}:'
selection_other_options_flags:
  CommandLine|contains:
  - ' /file:'
  - ' /machine'
  - ' /mkfile:'
  - ' /password:'
  - ' /pvk:'
  - ' /server:'
  - ' /target:'
  - ' /unprotect'
condition: selection_img or (selection_other_cli and 1 of selection_other_options_*)
```

## False Positives

- Unknown

## References

- https://github.com/GhostPack/SharpDPAPI

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharp_dpapi_execution.yml)
