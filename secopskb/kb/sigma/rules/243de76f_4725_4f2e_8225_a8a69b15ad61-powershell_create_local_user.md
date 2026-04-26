---
sigma_id: "243de76f-4725-4f2e-8225-a8a69b15ad61"
title: "PowerShell Create Local User"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_create_local_user.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_create_local_user.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "243de76f-4725-4f2e-8225-a8a69b15ad61"
  - "PowerShell Create Local User"
attack_technique_ids:
  - "T1059.001"
  - "T1136.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell Create Local User

Detects creation of a local user via PowerShell

## Metadata

- Rule ID: 243de76f-4725-4f2e-8225-a8a69b15ad61
- Status: test
- Level: medium
- Author: @ROxPinTeddy
- Date: 2020-04-11
- Modified: 2022-12-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_create_local_user.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1136-create_account|T1136.001]]

## Detection

```yaml
selection:
  ScriptBlockText|contains: New-LocalUser
condition: selection
```

## False Positives

- Legitimate user creation

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1136.001/T1136.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_create_local_user.yml)
