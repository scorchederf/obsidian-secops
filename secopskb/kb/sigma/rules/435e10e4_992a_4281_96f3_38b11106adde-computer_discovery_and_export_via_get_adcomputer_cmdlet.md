---
sigma_id: "435e10e4-992a-4281-96f3-38b11106adde"
title: "Computer Discovery And Export Via Get-ADComputer Cmdlet"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_computer_discovery_get_adcomputer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_computer_discovery_get_adcomputer.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "435e10e4-992a-4281-96f3-38b11106adde"
  - "Computer Discovery And Export Via Get-ADComputer Cmdlet"
attack_technique_ids:
  - "T1033"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Computer Discovery And Export Via Get-ADComputer Cmdlet

Detects usage of the Get-ADComputer cmdlet to collect computer information and output it to a file

## Metadata

- Rule ID: 435e10e4-992a-4281-96f3-38b11106adde
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-11-10
- Modified: 2022-11-17
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_computer_discovery_get_adcomputer.yml

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
  - 'Get-ADComputer '
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
- https://www.cisa.gov/uscert/sites/default/files/publications/aa22-320a_joint_csa_iranian_government-sponsored_apt_actors_compromise_federal%20network_deploy_crypto%20miner_credential_harvester.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_computer_discovery_get_adcomputer.yml)
