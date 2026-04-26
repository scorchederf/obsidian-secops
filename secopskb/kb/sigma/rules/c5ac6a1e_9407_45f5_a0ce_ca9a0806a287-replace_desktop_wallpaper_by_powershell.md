---
sigma_id: "c5ac6a1e-9407-45f5-a0ce-ca9a0806a287"
title: "Replace Desktop Wallpaper by Powershell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_wallpaper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_wallpaper.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "low"
logsource: "windows / ps_script"
aliases:
  - "c5ac6a1e-9407-45f5-a0ce-ca9a0806a287"
  - "Replace Desktop Wallpaper by Powershell"
attack_technique_ids:
  - "T1491.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Replace Desktop Wallpaper by Powershell

An adversary may deface systems internal to an organization in an attempt to intimidate or mislead users.
This may take the form of modifications to internal websites, or directly to user systems with the replacement of the desktop wallpaper

## Metadata

- Rule ID: c5ac6a1e-9407-45f5-a0ce-ca9a0806a287
- Status: test
- Level: low
- Author: frack113
- Date: 2021-12-26
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_wallpaper.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1491-defacement|T1491.001]]

## Detection

```yaml
selection_1:
  ScriptBlockText|contains|all:
  - Get-ItemProperty
  - 'Registry::'
  - HKEY_CURRENT_USER\Control Panel\Desktop\
  - WallPaper
selection_2:
  ScriptBlockText|contains: SystemParametersInfo(20,0,*,3)
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1491.001/T1491.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_wallpaper.yml)
