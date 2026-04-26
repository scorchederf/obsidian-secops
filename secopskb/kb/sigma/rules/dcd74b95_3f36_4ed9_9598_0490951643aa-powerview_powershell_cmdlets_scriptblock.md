---
sigma_id: "dcd74b95-3f36-4ed9-9598-0490951643aa"
title: "PowerView PowerShell Cmdlets - ScriptBlock"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_powerview_malicious_commandlets.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_powerview_malicious_commandlets.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "dcd74b95-3f36-4ed9-9598-0490951643aa"
  - "PowerView PowerShell Cmdlets - ScriptBlock"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerView PowerShell Cmdlets - ScriptBlock

Detects Cmdlet names from PowerView of the PowerSploit exploitation framework.

## Metadata

- Rule ID: dcd74b95-3f36-4ed9-9598-0490951643aa
- Status: test
- Level: high
- Author: Bhabesh Raj
- Date: 2021-05-18
- Modified: 2023-11-22
- Source Path: rules/windows/powershell/powershell_script/posh_ps_powerview_malicious_commandlets.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  ScriptBlockText|contains:
  - Export-PowerViewCSV
  - Find-DomainLocalGroupMember
  - Find-DomainObjectPropertyOutlier
  - Find-DomainProcess
  - Find-DomainShare
  - Find-DomainUserEvent
  - Find-DomainUserLocation
  - Find-ForeignGroup
  - Find-ForeignUser
  - Find-GPOComputerAdmin
  - Find-GPOLocation
  - Find-InterestingDomain
  - Find-InterestingFile
  - Find-LocalAdminAccess
  - Find-ManagedSecurityGroups
  - Get-CachedRDPConnection
  - Get-DFSshare
  - Get-DomainDFSShare
  - Get-DomainDNSRecord
  - Get-DomainDNSZone
  - Get-DomainFileServer
  - Get-DomainGPOComputerLocalGroupMapping
  - Get-DomainGPOLocalGroup
  - Get-DomainGPOUserLocalGroupMapping
  - Get-LastLoggedOn
  - Get-LoggedOnLocal
  - Get-NetFileServer
  - Get-NetForest
  - Get-NetGPOGroup
  - Get-NetProcess
  - Get-NetRDPSession
  - Get-RegistryMountedDrive
  - Get-RegLoggedOn
  - Get-WMIRegCachedRDPConnection
  - Get-WMIRegLastLoggedOn
  - Get-WMIRegMountedDrive
  - Get-WMIRegProxy
  - Invoke-ACLScanner
  - Invoke-CheckLocalAdminAccess
  - Invoke-EnumerateLocalAdmin
  - Invoke-EventHunter
  - Invoke-FileFinder
  - Invoke-Kerberoast
  - Invoke-MapDomainTrust
  - Invoke-ProcessHunter
  - Invoke-RevertToSelf
  - Invoke-ShareFinder
  - Invoke-UserHunter
  - Invoke-UserImpersonation
  - Remove-RemoteConnection
  - Request-SPNTicket
  - Resolve-IPAddress
condition: selection
```

## False Positives

- Unknown

## References

- https://powersploit.readthedocs.io/en/stable/Recon/README
- https://github.com/PowerShellMafia/PowerSploit/tree/master/Recon
- https://thedfirreport.com/2020/10/08/ryuks-return
- https://adsecurity.org/?p=2277

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_powerview_malicious_commandlets.yml)
