---
sigma_id: "86b896ba-ffa1-4fea-83e3-ee28a4c915c7"
title: "Invoke-Obfuscation Via Stdin - Powershell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_stdin.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_stdin.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "86b896ba-ffa1-4fea-83e3-ee28a4c915c7"
  - "Invoke-Obfuscation Via Stdin - Powershell"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation Via Stdin - Powershell

Detects Obfuscated Powershell via Stdin in Scripts

## Metadata

- Rule ID: 86b896ba-ffa1-4fea-83e3-ee28a4c915c7
- Status: test
- Level: high
- Author: Nikita Nazarov, oscd.community
- Date: 2020-10-12
- Modified: 2024-04-05
- Source Path: rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_stdin.yml

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
  ScriptBlockText|re: (?i)(set).*&&\s?set.*(environment|invoke|\$\{?input).*&&.*"
condition: selection_4104
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_stdin.yml)
