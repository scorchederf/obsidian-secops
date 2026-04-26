---
sigma_id: "7034cbbb-cc55-4dc2-8dad-36c0b942e8f1"
title: "Invoke-Obfuscation COMPRESS OBFUSCATION - PowerShell Module"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_via_compress.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_via_compress.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / ps_module"
aliases:
  - "7034cbbb-cc55-4dc2-8dad-36c0b942e8f1"
  - "Invoke-Obfuscation COMPRESS OBFUSCATION - PowerShell Module"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation COMPRESS OBFUSCATION - PowerShell Module

Detects Obfuscated Powershell via COMPRESS OBFUSCATION

## Metadata

- Rule ID: 7034cbbb-cc55-4dc2-8dad-36c0b942e8f1
- Status: test
- Level: medium
- Author: Timur Zinniatullin, oscd.community
- Date: 2020-10-18
- Modified: 2022-11-29
- Source Path: rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_via_compress.yml

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
  - new-object
  - text.encoding]::ascii
  Payload|contains:
  - system.io.compression.deflatestream
  - system.io.streamreader
  Payload|endswith: readtoend
condition: selection_4103
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_invoke_obfuscation_via_compress.yml)
