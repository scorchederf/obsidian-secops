---
sigma_id: "70ad982f-67c8-40e0-a955-b920c2fa05cb"
title: "Suspicious IO.FileStream"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_iofilestream.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_iofilestream.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "70ad982f-67c8-40e0-a955-b920c2fa05cb"
  - "Suspicious IO.FileStream"
attack_technique_ids:
  - "T1070.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious IO.FileStream

Open a handle on the drive volume via the \\.\ DOS device path specifier and perform direct access read of the first few bytes of the volume.

## Metadata

- Rule ID: 70ad982f-67c8-40e0-a955-b920c2fa05cb
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-09
- Modified: 2022-03-05
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_iofilestream.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.003]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - New-Object
  - IO.FileStream
  - \\\\.\\
condition: selection
```

## False Positives

- Legitimate PowerShell scripts

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1006/T1006.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_iofilestream.yml)
