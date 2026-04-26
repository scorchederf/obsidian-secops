---
sigma_id: "0718cd72-f316-4aa2-988f-838ea8533277"
title: "Suspicious Start-Process PassThru"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_start_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_start_process.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "0718cd72-f316-4aa2-988f-838ea8533277"
  - "Suspicious Start-Process PassThru"
attack_technique_ids:
  - "T1036.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Start-Process PassThru

Powershell use PassThru option to start in background

## Metadata

- Rule ID: 0718cd72-f316-4aa2-988f-838ea8533277
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-15
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_start_process.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.003]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - Start-Process
  - '-PassThru '
  - '-FilePath '
condition: selection
```

## False Positives

- Legitimate PowerShell scripts

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1036.003/T1036.003.md
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/Start-Process?view=powershell-5.1&viewFallbackFrom=powershell-7

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_start_process.yml)
