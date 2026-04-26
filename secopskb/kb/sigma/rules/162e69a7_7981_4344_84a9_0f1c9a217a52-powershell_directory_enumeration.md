---
sigma_id: "162e69a7-7981-4344-84a9-0f1c9a217a52"
title: "Powershell Directory Enumeration"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_directory_enum.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_directory_enum.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "162e69a7-7981-4344-84a9-0f1c9a217a52"
  - "Powershell Directory Enumeration"
attack_technique_ids:
  - "T1083"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Powershell Directory Enumeration

Detects technique used by MAZE ransomware to enumerate directories using Powershell

## Metadata

- Rule ID: 162e69a7-7981-4344-84a9-0f1c9a217a52
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-03-17
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_directory_enum.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - foreach
  - Get-ChildItem
  - '-Path '
  - '-ErrorAction '
  - SilentlyContinue
  - 'Out-File '
  - -append
condition: selection
```

## False Positives

- Legitimate PowerShell scripts

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1083/T1083.md
- https://www.mandiant.com/resources/tactics-techniques-procedures-associated-with-maze-ransomware-incidents

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_directory_enum.yml)
