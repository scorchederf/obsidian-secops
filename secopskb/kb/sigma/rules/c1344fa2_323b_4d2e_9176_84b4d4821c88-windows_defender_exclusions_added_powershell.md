---
sigma_id: "c1344fa2-323b-4d2e-9176-84b4d4821c88"
title: "Windows Defender Exclusions Added - PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_win_defender_exclusions_added.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_win_defender_exclusions_added.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "c1344fa2-323b-4d2e-9176-84b4d4821c88"
  - "Windows Defender Exclusions Added - PowerShell"
attack_technique_ids:
  - "T1562"
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Defender Exclusions Added - PowerShell

Detects modifications to the Windows Defender configuration settings using PowerShell to add exclusions

## Metadata

- Rule ID: c1344fa2-323b-4d2e-9176-84b4d4821c88
- Status: test
- Level: medium
- Author: Tim Rauch, Elastic (idea)
- Date: 2022-09-16
- Modified: 2022-11-26
- Source Path: rules/windows/powershell/powershell_script/posh_ps_win_defender_exclusions_added.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection_args_exc:
  ScriptBlockText|contains:
  - ' -ExclusionPath '
  - ' -ExclusionExtension '
  - ' -ExclusionProcess '
  - ' -ExclusionIpAddress '
selection_args_pref:
  ScriptBlockText|contains:
  - 'Add-MpPreference '
  - 'Set-MpPreference '
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://www.elastic.co/guide/en/security/current/windows-defender-exclusions-added-via-powershell.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_win_defender_exclusions_added.yml)
