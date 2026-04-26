---
sigma_id: "db885529-903f-4c5d-9864-28fe199e6370"
title: "Computer Discovery And Export Via Get-ADComputer Cmdlet - PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_computer_discovery_get_adcomputer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_computer_discovery_get_adcomputer.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "db885529-903f-4c5d-9864-28fe199e6370"
  - "Computer Discovery And Export Via Get-ADComputer Cmdlet - PowerShell"
attack_technique_ids:
  - "T1033"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Computer Discovery And Export Via Get-ADComputer Cmdlet - PowerShell

Detects usage of the Get-ADComputer cmdlet to collect computer information and output it to a file

## Metadata

- Rule ID: db885529-903f-4c5d-9864-28fe199e6370
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-11-17
- Source Path: rules/windows/powershell/powershell_script/posh_ps_computer_discovery_get_adcomputer.yml

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
  - 'Get-ADComputer '
  - ' -Filter \*'
  ScriptBlockText|contains:
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
- https://www.cisa.gov/uscert/sites/default/files/publications/aa22-320a_joint_csa_iranian_government-sponsored_apt_actors_compromise_federal%20network_deploy_crypto%20miner_credential_harvester.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_computer_discovery_get_adcomputer.yml)
