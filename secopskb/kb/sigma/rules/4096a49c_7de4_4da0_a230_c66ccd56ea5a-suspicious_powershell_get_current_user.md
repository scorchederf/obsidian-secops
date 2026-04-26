---
sigma_id: "4096a49c-7de4-4da0-a230-c66ccd56ea5a"
title: "Suspicious PowerShell Get Current User"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_get_current_user.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_get_current_user.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "low"
logsource: "windows / ps_script"
aliases:
  - "4096a49c-7de4-4da0-a230-c66ccd56ea5a"
  - "Suspicious PowerShell Get Current User"
attack_technique_ids:
  - "T1033"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious PowerShell Get Current User

Detects the use of PowerShell to identify the current logged user.

## Metadata

- Rule ID: 4096a49c-7de4-4da0-a230-c66ccd56ea5a
- Status: test
- Level: low
- Author: frack113
- Date: 2022-04-04
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_get_current_user.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]]

## Detection

```yaml
selection:
  ScriptBlockText|contains:
  - '[System.Environment]::UserName'
  - $env:UserName
  - '[System.Security.Principal.WindowsIdentity]::GetCurrent()'
condition: selection
```

## False Positives

- Legitimate PowerShell scripts

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1033/T1033.md#atomic-test-4---user-discovery-with-env-vars-powershell-script
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1033/T1033.md#atomic-test-5---getcurrent-user-with-powershell-script

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_get_current_user.yml)
