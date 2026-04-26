---
sigma_id: "e54f5149-6ba3-49cf-b153-070d24679126"
title: "Invoke-Obfuscation VAR++ LAUNCHER OBFUSCATION - PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_var.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_var.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "e54f5149-6ba3-49cf-b153-070d24679126"
  - "Invoke-Obfuscation VAR++ LAUNCHER OBFUSCATION - PowerShell"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation VAR++ LAUNCHER OBFUSCATION - PowerShell

Detects Obfuscated Powershell via VAR++ LAUNCHER

## Metadata

- Rule ID: e54f5149-6ba3-49cf-b153-070d24679126
- Status: test
- Level: high
- Author: Timur Zinniatullin, oscd.community
- Date: 2020-10-13
- Modified: 2024-04-05
- Source Path: rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_var.yml

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
  ScriptBlockText|re: (?i)&&set.*(\{\d\}){2,}\\"\s+?-f.*&&.*cmd.*/c
condition: selection_4104
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_var.yml)
