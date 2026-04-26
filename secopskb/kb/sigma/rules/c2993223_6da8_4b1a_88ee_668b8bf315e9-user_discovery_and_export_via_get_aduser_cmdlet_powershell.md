---
sigma_id: "c2993223-6da8-4b1a-88ee-668b8bf315e9"
title: "User Discovery And Export Via Get-ADUser Cmdlet - PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_user_discovery_get_aduser.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_user_discovery_get_aduser.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "c2993223-6da8-4b1a-88ee-668b8bf315e9"
  - "User Discovery And Export Via Get-ADUser Cmdlet - PowerShell"
attack_technique_ids:
  - "T1033"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# User Discovery And Export Via Get-ADUser Cmdlet - PowerShell

Detects usage of the Get-ADUser cmdlet to collect user information and output it to a file

## Metadata

- Rule ID: c2993223-6da8-4b1a-88ee-668b8bf315e9
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-11-17
- Source Path: rules/windows/powershell/powershell_script/posh_ps_user_discovery_get_aduser.yml

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
  ScriptBlockText|contains|all:
  - 'Get-ADUser '
  - ' -Filter \*'
  ScriptBlockText|contains:
  - ' > '
  - ' | Select '
  - Out-File
  - Set-Content
  - Add-Content
condition: selection
```

## False Positives

- Legitimate admin scripts may use the same technique, it's better to exclude specific computers or users who execute these commands or scripts often

## References

- http://blog.talosintelligence.com/2022/09/lazarus-three-rats.html
- https://www.microsoft.com/en-us/security/blog/2022/10/18/defenders-beware-a-case-for-post-ransomware-investigations/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_user_discovery_get_aduser.yml)
