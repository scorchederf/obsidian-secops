---
sigma_id: "af4c87ce-bdda-4215-b998-15220772e993"
title: "Suspicious Process Discovery With Get-Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_get_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_get_process.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "low"
logsource: "windows / ps_script"
aliases:
  - "af4c87ce-bdda-4215-b998-15220772e993"
  - "Suspicious Process Discovery With Get-Process"
attack_technique_ids:
  - "T1057"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Process Discovery With Get-Process

Get the processes that are running on the local computer.

## Metadata

- Rule ID: af4c87ce-bdda-4215-b998-15220772e993
- Status: test
- Level: low
- Author: frack113
- Date: 2022-03-17
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_get_process.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1057-process_discovery|T1057]]

## Detection

```yaml
selection:
  ScriptBlockText|contains: Get-Process
condition: selection
```

## False Positives

- Legitimate PowerShell scripts

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1057/T1057.md#atomic-test-3---process-discovery---get-process
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-process?view=powershell-7.4

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_get_process.yml)
