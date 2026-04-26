---
sigma_id: "07e3cb2c-0608-410d-be4b-1511cb1a0448"
title: "Tamper Windows Defender Remove-MpPreference"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_remove_mppreference.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_remove_mppreference.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "07e3cb2c-0608-410d-be4b-1511cb1a0448"
  - "Tamper Windows Defender Remove-MpPreference"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Tamper Windows Defender Remove-MpPreference

Detects attempts to remove Windows Defender configurations using the 'MpPreference' cmdlet

## Metadata

- Rule ID: 07e3cb2c-0608-410d-be4b-1511cb1a0448
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-05
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_remove_mppreference.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_remove:
  CommandLine|contains: Remove-MpPreference
selection_tamper:
  CommandLine|contains:
  - '-ControlledFolderAccessProtectedFolders '
  - '-AttackSurfaceReductionRules_Ids '
  - '-AttackSurfaceReductionRules_Actions '
  - '-CheckForSignaturesBeforeRunningScan '
condition: all of selection_*
```

## False Positives

- Legitimate PowerShell scripts

## References

- https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/windows-10-controlled-folder-access-event-search/ba-p/2326088

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_remove_mppreference.yml)
