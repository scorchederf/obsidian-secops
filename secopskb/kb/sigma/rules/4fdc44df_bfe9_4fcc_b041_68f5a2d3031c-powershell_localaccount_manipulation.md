---
sigma_id: "4fdc44df-bfe9-4fcc-b041-68f5a2d3031c"
title: "Powershell LocalAccount Manipulation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_localuser.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_localuser.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "4fdc44df-bfe9-4fcc-b041-68f5a2d3031c"
  - "Powershell LocalAccount Manipulation"
attack_technique_ids:
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Powershell LocalAccount Manipulation

Adversaries may manipulate accounts to maintain access to victim systems.
Account manipulation may consist of any action that preserves adversary access to a compromised account, such as modifying credentials or permission groups

## Metadata

- Rule ID: 4fdc44df-bfe9-4fcc-b041-68f5a2d3031c
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-12-28
- Source Path: rules/windows/powershell/powershell_script/posh_ps_localuser.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Detection

```yaml
selection:
  ScriptBlockText|contains:
  - Disable-LocalUser
  - Enable-LocalUser
  - Get-LocalUser
  - Set-LocalUser
  - New-LocalUser
  - Rename-LocalUser
  - Remove-LocalUser
condition: selection
```

## False Positives

- Legitimate administrative script

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1098/T1098.md#atomic-test-1---admin-account-manipulate
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/?view=powershell-5.1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_localuser.yml)
