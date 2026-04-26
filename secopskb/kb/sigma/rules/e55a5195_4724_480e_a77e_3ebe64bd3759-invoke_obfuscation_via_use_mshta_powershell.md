---
sigma_id: "e55a5195-4724-480e-a77e-3ebe64bd3759"
title: "Invoke-Obfuscation Via Use MSHTA - PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_use_mhsta.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_use_mhsta.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "e55a5195-4724-480e-a77e-3ebe64bd3759"
  - "Invoke-Obfuscation Via Use MSHTA - PowerShell"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation Via Use MSHTA - PowerShell

Detects Obfuscated Powershell via use MSHTA in Scripts

## Metadata

- Rule ID: e55a5195-4724-480e-a77e-3ebe64bd3759
- Status: test
- Level: high
- Author: Nikita Nazarov, oscd.community
- Date: 2020-10-08
- Modified: 2022-11-29
- Source Path: rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_use_mhsta.yml

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
  ScriptBlockText|contains|all:
  - set
  - '&&'
  - mshta
  - vbscript:createobject
  - .run
  - (window.close)
condition: selection_4104
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_use_mhsta.yml)
