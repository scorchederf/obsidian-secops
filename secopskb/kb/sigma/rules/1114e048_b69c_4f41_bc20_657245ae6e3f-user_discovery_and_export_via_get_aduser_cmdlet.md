---
sigma_id: "1114e048-b69c-4f41-bc20-657245ae6e3f"
title: "User Discovery And Export Via Get-ADUser Cmdlet"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_user_discovery_get_aduser.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_user_discovery_get_aduser.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "1114e048-b69c-4f41-bc20-657245ae6e3f"
  - "User Discovery And Export Via Get-ADUser Cmdlet"
attack_technique_ids:
  - "T1033"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# User Discovery And Export Via Get-ADUser Cmdlet

Detects usage of the Get-ADUser cmdlet to collect user information and output it to a file

## Metadata

- Rule ID: 1114e048-b69c-4f41-bc20-657245ae6e3f
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-09
- Modified: 2022-11-17
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_user_discovery_get_aduser.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
selection_cli:
  CommandLine|contains|all:
  - 'Get-ADUser '
  - ' -Filter \*'
  CommandLine|contains:
  - ' > '
  - ' | Select '
  - Out-File
  - Set-Content
  - Add-Content
condition: all of selection_*
```

## False Positives

- Legitimate admin scripts may use the same technique, it's better to exclude specific computers or users who execute these commands or scripts often

## References

- http://blog.talosintelligence.com/2022/09/lazarus-three-rats.html
- https://www.microsoft.com/en-us/security/blog/2022/10/18/defenders-beware-a-case-for-post-ransomware-investigations/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_user_discovery_get_aduser.yml)
