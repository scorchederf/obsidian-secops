---
sigma_id: "6bfb8fa7-b2e7-4f6c-8d9d-824e5d06ea9e"
title: "Invoke-Obfuscation VAR+ Launcher - PowerShell Module"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_var.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_var.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "high"
logsource: "windows / ps_module"
aliases:
  - "6bfb8fa7-b2e7-4f6c-8d9d-824e5d06ea9e"
  - "Invoke-Obfuscation VAR+ Launcher - PowerShell Module"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation VAR+ Launcher - PowerShell Module

Detects Obfuscated use of Environment Variables to execute PowerShell

## Metadata

- Rule ID: 6bfb8fa7-b2e7-4f6c-8d9d-824e5d06ea9e
- Status: test
- Level: high
- Author: Jonathan Cheong, oscd.community
- Date: 2020-10-15
- Modified: 2024-04-05
- Source Path: rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_var.yml

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
  Payload|re: cmd.{0,5}(?:/c|/r)(?:\s|)"set\s[a-zA-Z]{3,6}.*(?:\{\d\}){1,}\\"\s+?-f(?:.*\)){1,}.*"
condition: selection_4103
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_var.yml)
