---
sigma_id: "88a22f69-62f9-4b8a-aa00-6b0212f2f05a"
title: "Invoke-Obfuscation Via Use Rundll32 - PowerShell Module"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_via_use_rundll32.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_via_use_rundll32.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / ps_module"
aliases:
  - "88a22f69-62f9-4b8a-aa00-6b0212f2f05a"
  - "Invoke-Obfuscation Via Use Rundll32 - PowerShell Module"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation Via Use Rundll32 - PowerShell Module

Detects Obfuscated Powershell via use Rundll32 in Scripts

## Metadata

- Rule ID: 88a22f69-62f9-4b8a-aa00-6b0212f2f05a
- Status: test
- Level: high
- Author: Nikita Nazarov, oscd.community
- Date: 2019-10-08
- Modified: 2022-11-29
- Source Path: rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_via_use_rundll32.yml

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
  Payload|contains|all:
  - '&&'
  - rundll32
  - shell32.dll
  - shellexec_rundll
  Payload|contains:
  - value
  - invoke
  - comspec
  - iex
condition: selection_4103
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_via_use_rundll32.yml)
