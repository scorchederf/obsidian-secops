---
sigma_id: "ae2bdd58-0681-48ac-be7f-58ab4e593458"
title: "Tamper Windows Defender Remove-MpPreference - ScriptBlockLogging"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_tamper_windows_defender_rem_mp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_tamper_windows_defender_rem_mp.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "ae2bdd58-0681-48ac-be7f-58ab4e593458"
  - "Tamper Windows Defender Remove-MpPreference - ScriptBlockLogging"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Tamper Windows Defender Remove-MpPreference - ScriptBlockLogging

Detects attempts to remove Windows Defender configuration using the 'MpPreference' cmdlet

## Metadata

- Rule ID: ae2bdd58-0681-48ac-be7f-58ab4e593458
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-05
- Source Path: rules/windows/powershell/powershell_script/posh_ps_tamper_windows_defender_rem_mp.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_remove:
  ScriptBlockText|contains: Remove-MpPreference
selection_tamper:
  ScriptBlockText|contains:
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_tamper_windows_defender_rem_mp.yml)
