---
sigma_id: "05b3e303-faf0-4f4a-9b30-46cc13e69152"
title: "Potential Persistence Via PowerShell User Profile Using Add-Content"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_user_profile_tampering.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_user_profile_tampering.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "05b3e303-faf0-4f4a-9b30-46cc13e69152"
  - "Potential Persistence Via PowerShell User Profile Using Add-Content"
attack_technique_ids:
  - "T1546.013"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Persistence Via PowerShell User Profile Using Add-Content

Detects calls to "Add-Content" cmdlet in order to modify the content of the user profile and potentially adding suspicious commands for persistence

## Metadata

- Rule ID: 05b3e303-faf0-4f4a-9b30-46cc13e69152
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-08-18
- Modified: 2023-05-04
- Source Path: rules/windows/powershell/powershell_script/posh_ps_user_profile_tampering.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.013]]

## Detection

```yaml
selection_add:
  ScriptBlockText|contains: Add-Content $profile
selection_options:
  ScriptBlockText|contains:
  - '-Value "IEX '
  - -Value "Invoke-Expression
  - -Value "Invoke-WebRequest
  - -Value "Start-Process
  - '-Value ''IEX '
  - -Value 'Invoke-Expression
  - -Value 'Invoke-WebRequest
  - -Value 'Start-Process
condition: all of selection_*
```

## False Positives

- Legitimate administration and tuning scripts that aim to add functionality to a user PowerShell session

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1546.013/T1546.013.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_user_profile_tampering.yml)
