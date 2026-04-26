---
sigma_id: "a5a30a6e-75ca-4233-8b8c-42e0f2037d3b"
title: "Invoke-Obfuscation Via Use Rundll32 - PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_use_rundll32.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_use_rundll32.yml"
build_date: "2026-04-26 15:01:46"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "a5a30a6e-75ca-4233-8b8c-42e0f2037d3b"
  - "Invoke-Obfuscation Via Use Rundll32 - PowerShell"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation Via Use Rundll32 - PowerShell

Detects Obfuscated Powershell via use Rundll32 in Scripts

## Metadata

- Rule ID: a5a30a6e-75ca-4233-8b8c-42e0f2037d3b
- Status: test
- Level: high
- Author: Nikita Nazarov, oscd.community
- Date: 2019-10-08
- Modified: 2022-11-29
- Source Path: rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_use_rundll32.yml

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
  - '&&'
  - rundll32
  - shell32.dll
  - shellexec_rundll
  ScriptBlockText|contains:
  - value
  - invoke
  - comspec
  - iex
condition: selection_4104
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_use_rundll32.yml)
