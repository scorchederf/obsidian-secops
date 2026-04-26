---
sigma_id: "c72aca44-8d52-45ad-8f81-f96c4d3c755e"
title: "Invoke-Obfuscation Via Stdin - PowerShell Module"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_via_stdin.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_via_stdin.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "high"
logsource: "windows / ps_module"
aliases:
  - "c72aca44-8d52-45ad-8f81-f96c4d3c755e"
  - "Invoke-Obfuscation Via Stdin - PowerShell Module"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation Via Stdin - PowerShell Module

Detects Obfuscated Powershell via Stdin in Scripts

## Metadata

- Rule ID: c72aca44-8d52-45ad-8f81-f96c4d3c755e
- Status: test
- Level: high
- Author: Nikita Nazarov, oscd.community
- Date: 2020-10-12
- Modified: 2024-04-05
- Source Path: rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_via_stdin.yml

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
  Payload|re: (?i)(set).*&&\s?set.*(environment|invoke|\$?\{?input).*&&.*"
condition: selection_4103
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_via_stdin.yml)
