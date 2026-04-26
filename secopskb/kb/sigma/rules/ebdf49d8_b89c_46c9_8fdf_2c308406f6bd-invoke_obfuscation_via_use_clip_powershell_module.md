---
sigma_id: "ebdf49d8-b89c-46c9-8fdf-2c308406f6bd"
title: "Invoke-Obfuscation Via Use Clip - PowerShell Module"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_via_use_clip.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_via_use_clip.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "high"
logsource: "windows / ps_module"
aliases:
  - "ebdf49d8-b89c-46c9-8fdf-2c308406f6bd"
  - "Invoke-Obfuscation Via Use Clip - PowerShell Module"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation Via Use Clip - PowerShell Module

Detects Obfuscated Powershell via use Clip.exe in Scripts

## Metadata

- Rule ID: ebdf49d8-b89c-46c9-8fdf-2c308406f6bd
- Status: test
- Level: high
- Author: Nikita Nazarov, oscd.community
- Date: 2020-10-09
- Modified: 2024-04-05
- Source Path: rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_via_use_clip.yml

## Logsource

- category: ps_module
- definition: 0ad03ef1-f21b-4a79-8ce8-e6900c54b65b
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_4103:
  Payload|re: (?i)echo.*clip.*&&.*(Clipboard|i`?n`?v`?o`?k`?e`?)
condition: selection_4103
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_via_use_clip.yml)
