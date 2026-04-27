---
sigma_id: "8f02c935-effe-45b3-8fc9-ef8696a9e41d"
title: "Non-privileged Usage of Reg or Powershell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_non_priv_reg_or_ps.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_non_priv_reg_or_ps.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "8f02c935-effe-45b3-8fc9-ef8696a9e41d"
  - "Non-privileged Usage of Reg or Powershell"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Non-privileged Usage of Reg or Powershell

Search for usage of reg or Powershell by non-privileged users to modify service configuration in registry

## Metadata

- Rule ID: 8f02c935-effe-45b3-8fc9-ef8696a9e41d
- Status: test
- Level: high
- Author: Teymur Kheirkhabarov (idea), Ryan Plas (rule), oscd.community
- Date: 2020-10-05
- Modified: 2024-12-01
- Source Path: rules/windows/process_creation/proc_creation_win_susp_non_priv_reg_or_ps.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection_cli:
- CommandLine|contains|all:
  - 'reg '
  - add
- CommandLine|contains:
  - powershell
  - set-itemproperty
  - ' sp '
  - new-itemproperty
selection_data:
  IntegrityLevel:
  - Medium
  - S-1-16-8192
  CommandLine|contains|all:
  - ControlSet
  - Services
  CommandLine|contains:
  - ImagePath
  - FailureCommand
  - ServiceDLL
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://image.slidesharecdn.com/kheirkhabarovoffzonefinal-181117201458/95/hunting-for-privilege-escalation-in-windows-environment-20-638.jpg

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_non_priv_reg_or_ps.yml)
