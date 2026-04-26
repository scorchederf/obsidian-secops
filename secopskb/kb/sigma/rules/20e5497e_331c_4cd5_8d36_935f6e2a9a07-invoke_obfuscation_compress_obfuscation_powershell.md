---
sigma_id: "20e5497e-331c-4cd5-8d36-935f6e2a9a07"
title: "Invoke-Obfuscation COMPRESS OBFUSCATION - PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_compress.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_compress.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "20e5497e-331c-4cd5-8d36-935f6e2a9a07"
  - "Invoke-Obfuscation COMPRESS OBFUSCATION - PowerShell"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation COMPRESS OBFUSCATION - PowerShell

Detects Obfuscated Powershell via COMPRESS OBFUSCATION

## Metadata

- Rule ID: 20e5497e-331c-4cd5-8d36-935f6e2a9a07
- Status: test
- Level: medium
- Author: Timur Zinniatullin, oscd.community
- Date: 2020-10-18
- Modified: 2022-11-29
- Source Path: rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_compress.yml

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
  - new-object
  - text.encoding]::ascii
  ScriptBlockText|contains:
  - system.io.compression.deflatestream
  - system.io.streamreader
  ScriptBlockText|endswith: readtoend
condition: selection_4104
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_compress.yml)
