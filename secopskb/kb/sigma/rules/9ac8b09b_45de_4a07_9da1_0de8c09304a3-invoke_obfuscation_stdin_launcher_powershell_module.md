---
sigma_id: "9ac8b09b-45de-4a07-9da1-0de8c09304a3"
title: "Invoke-Obfuscation STDIN+ Launcher - PowerShell Module"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_stdin.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_stdin.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / ps_module"
aliases:
  - "9ac8b09b-45de-4a07-9da1-0de8c09304a3"
  - "Invoke-Obfuscation STDIN+ Launcher - PowerShell Module"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation STDIN+ Launcher - PowerShell Module

Detects Obfuscated use of stdin to execute PowerShell

## Metadata

- Rule ID: 9ac8b09b-45de-4a07-9da1-0de8c09304a3
- Status: test
- Level: high
- Author: Jonathan Cheong, oscd.community
- Date: 2020-10-15
- Modified: 2024-04-05
- Source Path: rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_stdin.yml

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
  Payload|re: cmd.{0,5}(?:/c|/r).+powershell.+(?:\$\{?input\}?|noexit).+"
condition: selection_4103
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_stdin.yml)
