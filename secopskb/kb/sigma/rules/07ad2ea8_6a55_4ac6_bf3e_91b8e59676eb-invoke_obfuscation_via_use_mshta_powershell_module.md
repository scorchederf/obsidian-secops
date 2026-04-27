---
sigma_id: "07ad2ea8-6a55-4ac6-bf3e-91b8e59676eb"
title: "Invoke-Obfuscation Via Use MSHTA - PowerShell Module"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_via_use_mhsta.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_via_use_mhsta.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / ps_module"
aliases:
  - "07ad2ea8-6a55-4ac6-bf3e-91b8e59676eb"
  - "Invoke-Obfuscation Via Use MSHTA - PowerShell Module"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation Via Use MSHTA - PowerShell Module

Detects Obfuscated Powershell via use MSHTA in Scripts

## Metadata

- Rule ID: 07ad2ea8-6a55-4ac6-bf3e-91b8e59676eb
- Status: test
- Level: high
- Author: Nikita Nazarov, oscd.community
- Date: 2020-10-08
- Modified: 2023-01-04
- Source Path: rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_via_use_mhsta.yml

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
selection:
  Payload|contains|all:
  - set
  - '&&'
  - mshta
  - vbscript:createobject
  - .run
  - (window.close)
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_via_use_mhsta.yml)
