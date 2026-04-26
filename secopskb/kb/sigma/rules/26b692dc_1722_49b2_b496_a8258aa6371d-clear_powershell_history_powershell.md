---
sigma_id: "26b692dc-1722-49b2-b496-a8258aa6371d"
title: "Clear PowerShell History - PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_clear_powershell_history.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_clear_powershell_history.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "26b692dc-1722-49b2-b496-a8258aa6371d"
  - "Clear PowerShell History - PowerShell"
attack_technique_ids:
  - "T1070.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Clear PowerShell History - PowerShell

Detects keywords that could indicate clearing PowerShell history

## Metadata

- Rule ID: 26b692dc-1722-49b2-b496-a8258aa6371d
- Status: test
- Level: medium
- Author: Ilyas Ochkov, Jonhnathan Ribeiro, Daniil Yugoslavskiy, oscd.community
- Date: 2022-01-25
- Modified: 2022-12-02
- Source Path: rules/windows/powershell/powershell_script/posh_ps_clear_powershell_history.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.003]]

## Detection

```yaml
selection1a:
  ScriptBlockText|contains:
  - del
  - Remove-Item
  - rm
selection1b:
  ScriptBlockText|contains: (Get-PSReadlineOption).HistorySavePath
selection_2:
  ScriptBlockText|contains|all:
  - Set-PSReadlineOption
  - –HistorySaveStyle
  - SaveNothing
selection_3:
  ScriptBlockText|contains|all:
  - Set-PSReadlineOption
  - -HistorySaveStyle
  - SaveNothing
condition: 1 of selection_* or all of selection1*
```

## False Positives

- Legitimate PowerShell scripts

## References

- https://gist.github.com/hook-s3c/7363a856c3cdbadeb71085147f042c1a

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_clear_powershell_history.yml)
