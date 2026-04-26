---
sigma_id: "e8314f79-564d-4f79-bc13-fbc0bf2660d8"
title: "Potential PowerShell Obfuscation Using Character Join"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_alias_obfscuation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_alias_obfscuation.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "low"
logsource: "windows / ps_script"
aliases:
  - "e8314f79-564d-4f79-bc13-fbc0bf2660d8"
  - "Potential PowerShell Obfuscation Using Character Join"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential PowerShell Obfuscation Using Character Join

Detects specific techniques often seen used inside of PowerShell scripts to obfscuate Alias creation

## Metadata

- Rule ID: e8314f79-564d-4f79-bc13-fbc0bf2660d8
- Status: test
- Level: low
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-09
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_alias_obfscuation.yml

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
selection:
  ScriptBlockText|contains|all:
  - -Alias
  - ' -Value (-join('
condition: selection
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_alias_obfscuation.yml)
