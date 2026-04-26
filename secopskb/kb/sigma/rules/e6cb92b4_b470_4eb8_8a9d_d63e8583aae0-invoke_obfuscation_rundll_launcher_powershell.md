---
sigma_id: "e6cb92b4-b470-4eb8-8a9d-d63e8583aae0"
title: "Invoke-Obfuscation RUNDLL LAUNCHER - PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_rundll.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_rundll.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "e6cb92b4-b470-4eb8-8a9d-d63e8583aae0"
  - "Invoke-Obfuscation RUNDLL LAUNCHER - PowerShell"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation RUNDLL LAUNCHER - PowerShell

Detects Obfuscated Powershell via RUNDLL LAUNCHER

## Metadata

- Rule ID: e6cb92b4-b470-4eb8-8a9d-d63e8583aae0
- Status: test
- Level: medium
- Author: Timur Zinniatullin, oscd.community
- Date: 2020-10-18
- Modified: 2022-11-29
- Source Path: rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_rundll.yml

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
  - rundll32.exe
  - shell32.dll
  - shellexec_rundll
  - powershell
condition: selection_4104
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_rundll.yml)
