---
sigma_id: "779c8c12-0eb1-11eb-adc1-0242ac120002"
title: "Invoke-Obfuscation STDIN+ Launcher - Powershell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_stdin.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_stdin.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "779c8c12-0eb1-11eb-adc1-0242ac120002"
  - "Invoke-Obfuscation STDIN+ Launcher - Powershell"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation STDIN+ Launcher - Powershell

Detects Obfuscated use of stdin to execute PowerShell

## Metadata

- Rule ID: 779c8c12-0eb1-11eb-adc1-0242ac120002
- Status: test
- Level: high
- Author: Jonathan Cheong, oscd.community
- Date: 2020-10-15
- Modified: 2024-04-05
- Source Path: rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_stdin.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_4104:
  ScriptBlockText|re: cmd.{0,5}(?:/c|/r).+powershell.+(?:\$?\{?input\}?|noexit).+"
condition: selection_4104
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_stdin.yml)
