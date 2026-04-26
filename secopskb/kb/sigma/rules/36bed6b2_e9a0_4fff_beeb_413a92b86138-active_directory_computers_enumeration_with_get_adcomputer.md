---
sigma_id: "36bed6b2-e9a0-4fff-beeb-413a92b86138"
title: "Active Directory Computers Enumeration With Get-AdComputer"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_get_adcomputer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_get_adcomputer.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "low"
logsource: "windows / ps_script"
aliases:
  - "36bed6b2-e9a0-4fff-beeb-413a92b86138"
  - "Active Directory Computers Enumeration With Get-AdComputer"
attack_technique_ids:
  - "T1018"
  - "T1087.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Active Directory Computers Enumeration With Get-AdComputer

Detects usage of the "Get-AdComputer" to enumerate Computers or properties within Active Directory.

## Metadata

- Rule ID: 36bed6b2-e9a0-4fff-beeb-413a92b86138
- Status: test
- Level: low
- Author: frack113
- Date: 2022-03-17
- Modified: 2023-07-08
- Source Path: rules/windows/powershell/powershell_script/posh_ps_get_adcomputer.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018]]
- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]

## Detection

```yaml
selection_cmdlet:
  ScriptBlockText|contains: 'Get-AdComputer '
selection_option:
  ScriptBlockText|contains:
  - '-Filter '
  - '-LDAPFilter '
  - '-Properties '
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1018/T1018.md
- https://github.com/redcanaryco/atomic-red-team/blob/02cb591f75064ffe1e0df9ac3ed5972a2e491c97/atomics/T1087.002/T1087.002.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_get_adcomputer.yml)
