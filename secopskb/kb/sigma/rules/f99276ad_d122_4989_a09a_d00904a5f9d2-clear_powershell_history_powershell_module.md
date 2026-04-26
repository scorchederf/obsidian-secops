---
sigma_id: "f99276ad-d122-4989-a09a-d00904a5f9d2"
title: "Clear PowerShell History - PowerShell Module"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_clear_powershell_history.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_clear_powershell_history.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / ps_module"
aliases:
  - "f99276ad-d122-4989-a09a-d00904a5f9d2"
  - "Clear PowerShell History - PowerShell Module"
attack_technique_ids:
  - "T1070.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Clear PowerShell History - PowerShell Module

Detects keywords that could indicate clearing PowerShell history

## Metadata

- Rule ID: f99276ad-d122-4989-a09a-d00904a5f9d2
- Status: test
- Level: medium
- Author: Ilyas Ochkov, Jonhnathan Ribeiro, Daniil Yugoslavskiy, oscd.community
- Date: 2019-10-25
- Modified: 2022-12-02
- Source Path: rules/windows/powershell/powershell_module/posh_pm_clear_powershell_history.yml

## Logsource

- category: ps_module
- definition: 0ad03ef1-f21b-4a79-8ce8-e6900c54b65b
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.003]]

## Detection

```yaml
selection_1a_payload:
  Payload|contains:
  - del
  - Remove-Item
  - rm
selection_1b_payload:
  Payload|contains: (Get-PSReadlineOption).HistorySavePath
selection_payload_2:
  Payload|contains|all:
  - Set-PSReadlineOption
  - –HistorySaveStyle
  - SaveNothing
selection_payload_3:
  Payload|contains|all:
  - Set-PSReadlineOption
  - -HistorySaveStyle
  - SaveNothing
condition: 1 of selection_payload_* or all of selection_1*
```

## False Positives

- Legitimate PowerShell scripts

## References

- https://gist.github.com/hook-s3c/7363a856c3cdbadeb71085147f042c1a

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_clear_powershell_history.yml)
