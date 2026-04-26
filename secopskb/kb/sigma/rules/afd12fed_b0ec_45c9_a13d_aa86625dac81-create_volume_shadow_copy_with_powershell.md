---
sigma_id: "afd12fed-b0ec-45c9-a13d-aa86625dac81"
title: "Create Volume Shadow Copy with Powershell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_create_volume_shadow_copy.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_create_volume_shadow_copy.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "afd12fed-b0ec-45c9-a13d-aa86625dac81"
  - "Create Volume Shadow Copy with Powershell"
attack_technique_ids:
  - "T1003.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Create Volume Shadow Copy with Powershell

Adversaries may attempt to access or create a copy of the Active Directory domain database in order to steal credential information

## Metadata

- Rule ID: afd12fed-b0ec-45c9-a13d-aa86625dac81
- Status: test
- Level: high
- Author: frack113
- Date: 2022-01-12
- Source Path: rules/windows/powershell/powershell_script/posh_ps_create_volume_shadow_copy.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - Win32_ShadowCopy
  - ).Create(
  - ClientAccessible
condition: selection
```

## False Positives

- Legitimate PowerShell scripts

## References

- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-5.1&viewFallbackFrom=powershell-7

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_create_volume_shadow_copy.yml)
