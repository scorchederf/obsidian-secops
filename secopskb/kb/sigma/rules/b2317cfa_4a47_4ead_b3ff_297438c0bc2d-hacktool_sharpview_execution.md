---
sigma_id: "b2317cfa-4a47-4ead-b3ff-297438c0bc2d"
title: "HackTool - SharpView Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_sharpview.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharpview.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "b2317cfa-4a47-4ead-b3ff-297438c0bc2d"
  - "HackTool - SharpView Execution"
attack_technique_ids:
  - "T1049"
  - "T1069.002"
  - "T1482"
  - "T1135"
  - "T1033"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - SharpView Execution

Adversaries may look for details about the network configuration and settings of systems they access or through information discovery of remote systems

## Metadata

- Rule ID: b2317cfa-4a47-4ead-b3ff-297438c0bc2d
- Status: test
- Level: high
- Author: frack113
- Date: 2021-12-10
- Modified: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_sharpview.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1049-system_network_connections_discovery|T1049]]
- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.002]]
- [[kb/attack/techniques/T1482-domain_trust_discovery|T1482]]
- [[kb/attack/techniques/T1135-network_share_discovery|T1135]]
- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]]

## Detection

```yaml
selection:
- OriginalFileName: SharpView.exe
- Image|endswith: \SharpView.exe
- CommandLine|contains:
  - Add-RemoteConnection
  - Convert-ADName
  - ConvertFrom-SID
  - ConvertFrom-UACValue
  - Convert-SidToName
  - Export-PowerViewCSV
  - Find-DomainObjectPropertyOutlier
  - Find-DomainProcess
  - Find-DomainShare
  - Find-DomainUserEvent
  - Find-DomainUserLocation
  - Find-ForeignGroup
  - Find-ForeignUser
  - Find-GPOComputerAdmin
  - Find-GPOLocation
  - Find-Interesting
  - Find-LocalAdminAccess
  - Find-ManagedSecurityGroups
  - Get-CachedRDPConnection
  - Get-DFSshare
  - Get-DomainComputer
  - Get-DomainController
  - Get-DomainDFSShare
  - Get-DomainDNSRecord
  - Get-DomainFileServer
  - Get-DomainForeign
  - Get-DomainGPO
  - Get-DomainGroup
  - Get-DomainGUIDMap
  - Get-DomainManagedSecurityGroup
  - Get-DomainObject
  - Get-DomainOU
  - Get-DomainPolicy
  - Get-DomainSID
  - Get-DomainSite
  - Get-DomainSPNTicket
  - Get-DomainSubnet
  - Get-DomainTrust
  - Get-DomainUserEvent
  - Get-ForestDomain
  - Get-ForestGlobalCatalog
  - Get-ForestTrust
  - Get-GptTmpl
  - Get-GroupsXML
  - Get-LastLoggedOn
  - Get-LoggedOnLocal
  - Get-NetComputer
  - Get-NetDomain
  - Get-NetFileServer
  - Get-NetForest
  - Get-NetGPO
  - Get-NetGroupMember
  - Get-NetLocalGroup
  - Get-NetLoggedon
  - Get-NetOU
  - Get-NetProcess
  - Get-NetRDPSession
  - Get-NetSession
  - Get-NetShare
  - Get-NetSite
  - Get-NetSubnet
  - Get-NetUser
  - Get-PathAcl
  - Get-PrincipalContext
  - Get-RegistryMountedDrive
  - Get-RegLoggedOn
  - Get-WMIRegCachedRDPConnection
  - Get-WMIRegLastLoggedOn
  - Get-WMIRegMountedDrive
  - Get-WMIRegProxy
  - Invoke-ACLScanner
  - Invoke-CheckLocalAdminAccess
  - Invoke-Kerberoast
  - Invoke-MapDomainTrust
  - Invoke-RevertToSelf
  - Invoke-Sharefinder
  - Invoke-UserImpersonation
  - Remove-DomainObjectAcl
  - Remove-RemoteConnection
  - Request-SPNTicket
  - Set-DomainObject
  - Test-AdminAccess
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/tevora-threat/SharpView/
- https://github.com/PowerShellMafia/PowerSploit/blob/d943001a7defb5e0d1657085a77a0e78609be58f/Recon/PowerView.ps1
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1049/T1049.md#atomic-test-4---system-discovery-using-sharpview

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharpview.yml)
