---
sigma_id: "43d91656-a9b2-4541-b7e2-6a9bd3a13f4e"
title: "DSInternals Suspicious PowerShell Cmdlets"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_dsinternals_cmdlets.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_dsinternals_cmdlets.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "43d91656-a9b2-4541-b7e2-6a9bd3a13f4e"
  - "DSInternals Suspicious PowerShell Cmdlets"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects execution and usage of the DSInternals PowerShell module. Which can be used to perform what might be considered as suspicious activity such as dumping DPAPI backup keys or manipulating NTDS.DIT files.
The DSInternals PowerShell Module exposes several internal features of Active Directory and Azure Active Directory. These include FIDO2 and NGC key auditing, offline ntds.dit file manipulation, password auditing, DC recovery from IFM backups and password hash calculation.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - Add-ADDBSidHistory
  - Add-ADNgcKey
  - Add-ADReplNgcKey
  - ConvertFrom-ADManagedPasswordBlob
  - ConvertFrom-GPPrefPassword
  - ConvertFrom-ManagedPasswordBlob
  - ConvertFrom-UnattendXmlPassword
  - ConvertFrom-UnicodePassword
  - ConvertTo-AADHash
  - ConvertTo-GPPrefPassword
  - ConvertTo-KerberosKey
  - ConvertTo-LMHash
  - ConvertTo-MsoPasswordHash
  - ConvertTo-NTHash
  - ConvertTo-OrgIdHash
  - ConvertTo-UnicodePassword
  - Disable-ADDBAccount
  - Enable-ADDBAccount
  - Get-ADDBAccount
  - Get-ADDBBackupKey
  - Get-ADDBDomainController
  - Get-ADDBGroupManagedServiceAccount
  - Get-ADDBKdsRootKey
  - Get-ADDBSchemaAttribute
  - Get-ADDBServiceAccount
  - Get-ADDefaultPasswordPolicy
  - Get-ADKeyCredential
  - Get-ADPasswordPolicy
  - Get-ADReplAccount
  - Get-ADReplBackupKey
  - Get-ADReplicationAccount
  - Get-ADSIAccount
  - Get-AzureADUserEx
  - Get-BootKey
  - Get-KeyCredential
  - Get-LsaBackupKey
  - Get-LsaPolicy
  - Get-SamPasswordPolicy
  - Get-SysKey
  - Get-SystemKey
  - New-ADDBRestoreFromMediaScript
  - New-ADKeyCredential
  - New-ADNgcKey
  - New-NTHashSet
  - Remove-ADDBObject
  - Save-DPAPIBlob
  - Set-ADAccountPasswordHash
  - Set-ADDBAccountPassword
  - Set-ADDBBootKey
  - Set-ADDBDomainController
  - Set-ADDBPrimaryGroup
  - Set-ADDBSysKey
  - Set-AzureADUserEx
  - Set-LsaPolicy
  - Set-SamAccountPasswordHash
  - Set-WinUserPasswordHash
  - Test-ADDBPasswordQuality
  - Test-ADPasswordQuality
  - Test-ADReplPasswordQuality
  - Test-PasswordQuality
  - Unlock-ADDBAccount
  - Write-ADNgcKey
  - Write-ADReplNgcKey
condition: selection
```

## False Positives

- Legitimate usage of DSInternals for administration or audit purpose.

## References

- https://github.com/MichaelGrafnetter/DSInternals/blob/39ee8a69bbdc1cfd12c9afdd7513b4788c4895d4/Src/DSInternals.PowerShell/DSInternals.psd1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_dsinternals_cmdlets.yml)
