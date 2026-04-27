---
sigma_id: "02030f2f-6199-49ec-b258-ea71b07e03dc"
title: "Malicious PowerShell Commandlets - ProcessCreation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_malicious_cmdlets.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_malicious_cmdlets.yml"
build_date: "2026-04-27 19:13:52"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "02030f2f-6199-49ec-b258-ea71b07e03dc"
  - "Malicious PowerShell Commandlets - ProcessCreation"
attack_technique_ids:
  - "T1482"
  - "T1087"
  - "T1087.001"
  - "T1087.002"
  - "T1069.001"
  - "T1069.002"
  - "T1069"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects Commandlet names from well-known PowerShell exploitation frameworks

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1482-domain_trust_discovery|T1482: Domain Trust Discovery]]
- [[kb/attack/techniques/T1087-account_discovery|T1087: Account Discovery]]
- [[kb/attack/techniques/T1087-account_discovery#^t1087001-local-account|T1087.001: Local Account]]
- [[kb/attack/techniques/T1087-account_discovery#^t1087002-domain-account|T1087.002: Domain Account]]
- [[kb/attack/techniques/T1069-permission_groups_discovery#^t1069001-local-groups|T1069.001: Local Groups]]
- [[kb/attack/techniques/T1069-permission_groups_discovery#^t1069002-domain-groups|T1069.002: Domain Groups]]
- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069: Permission Groups Discovery]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - Add-Exfiltration
  - Add-Persistence
  - Add-RegBackdoor
  - Add-RemoteRegBackdoor
  - Add-ScrnSaveBackdoor
  - Check-VM
  - ConvertTo-Rc4ByteStream
  - Decrypt-Hash
  - Disable-ADIDNSNode
  - Disable-MachineAccount
  - Do-Exfiltration
  - Enable-ADIDNSNode
  - Enable-MachineAccount
  - Enabled-DuplicateToken
  - Exploit-Jboss
  - Export-ADR
  - Export-ADRCSV
  - Export-ADRExcel
  - Export-ADRHTML
  - Export-ADRJSON
  - Export-ADRXML
  - Find-Fruit
  - Find-GPOLocation
  - Find-TrustedDocuments
  - Get-ADIDNS
  - Get-ApplicationHost
  - Get-ChromeDump
  - Get-ClipboardContents
  - Get-FoxDump
  - Get-GPPPassword
  - Get-IndexedItem
  - Get-KerberosAESKey
  - Get-Keystrokes
  - Get-LSASecret
  - Get-MachineAccountAttribute
  - Get-MachineAccountCreator
  - Get-PassHashes
  - Get-RegAlwaysInstallElevated
  - Get-RegAutoLogon
  - Get-RemoteBootKey
  - Get-RemoteCachedCredential
  - Get-RemoteLocalAccountHash
  - Get-RemoteLSAKey
  - Get-RemoteMachineAccountHash
  - Get-RemoteNLKMKey
  - Get-RickAstley
  - Get-Screenshot
  - Get-SecurityPackages
  - Get-ServiceFilePermission
  - Get-ServicePermission
  - Get-ServiceUnquoted
  - Get-SiteListPassword
  - Get-System
  - Get-TimedScreenshot
  - Get-UnattendedInstallFile
  - Get-Unconstrained
  - Get-USBKeystrokes
  - Get-VaultCredential
  - Get-VulnAutoRun
  - Get-VulnSchTask
  - Grant-ADIDNSPermission
  - Gupt-Backdoor
  - HTTP-Login
  - Install-ServiceBinary
  - Install-SSP
  - Invoke-ACLScanner
  - Invoke-ADRecon
  - Invoke-ADSBackdoor
  - Invoke-AgentSmith
  - Invoke-AllChecks
  - Invoke-ARPScan
  - Invoke-AzureHound
  - Invoke-BackdoorLNK
  - Invoke-BadPotato
  - Invoke-BetterSafetyKatz
  - Invoke-BypassUAC
  - Invoke-Carbuncle
  - Invoke-Certify
  - Invoke-ConPtyShell
  - Invoke-CredentialInjection
  - Invoke-DAFT
  - Invoke-DCSync
  - Invoke-DinvokeKatz
  - Invoke-DllInjection
  - Invoke-DNSUpdate
  - Invoke-DNSExfiltrator
  - Invoke-DomainPasswordSpray
  - Invoke-DowngradeAccount
  - Invoke-EgressCheck
  - Invoke-Eyewitness
  - Invoke-FakeLogonScreen
  - Invoke-Farmer
  - Invoke-Get-RBCD-Threaded
  - Invoke-Gopher
  - Invoke-Grouper
  - Invoke-HandleKatz
  - Invoke-ImpersonatedProcess
  - Invoke-ImpersonateSystem
  - Invoke-InteractiveSystemPowerShell
  - Invoke-Internalmonologue
  - Invoke-Inveigh
  - Invoke-InveighRelay
  - Invoke-KrbRelay
  - Invoke-LdapSignCheck
  - Invoke-Lockless
  - Invoke-MalSCCM
  - Invoke-Mimikatz
  - Invoke-Mimikittenz
  - Invoke-MITM6
  - Invoke-NanoDump
  - Invoke-NetRipper
  - Invoke-Nightmare
  - Invoke-NinjaCopy
  - Invoke-OfficeScrape
  - Invoke-OxidResolver
  - Invoke-P0wnedshell
  - Invoke-Paranoia
  - Invoke-PortScan
  - Invoke-PoshRatHttp
  - Invoke-PostExfil
  - Invoke-PowerDump
  - Invoke-PowerDPAPI
  - Invoke-PowerShellTCP
  - Invoke-PowerShellWMI
  - Invoke-PPLDump
  - Invoke-PsExec
  - Invoke-PSInject
  - Invoke-PsUaCme
  - Invoke-ReflectivePEInjection
  - Invoke-ReverseDNSLookup
  - Invoke-Rubeus
  - Invoke-RunAs
  - Invoke-SafetyKatz
  - Invoke-SauronEye
  - Invoke-SCShell
  - Invoke-Seatbelt
  - Invoke-ServiceAbuse
  - Invoke-ShadowSpray
  - Invoke-Sharp
  - Invoke-Shellcode
  - Invoke-SMBScanner
  - Invoke-Snaffler
  - Invoke-Spoolsample
  - Invoke-SpraySinglePassword
  - Invoke-SSHCommand
  - Invoke-StandIn
  - Invoke-StickyNotesExtract
  - Invoke-SystemCommand
  - Invoke-Tasksbackdoor
  - Invoke-Tater
  - Invoke-Thunderfox
  - Invoke-ThunderStruck
  - Invoke-TokenManipulation
  - Invoke-Tokenvator
  - Invoke-TotalExec
  - Invoke-UrbanBishop
  - Invoke-UserHunter
  - Invoke-VoiceTroll
  - Invoke-Whisker
  - Invoke-WinEnum
  - Invoke-winPEAS
  - Invoke-WireTap
  - Invoke-WmiCommand
  - Invoke-WMIExec
  - Invoke-WScriptBypassUAC
  - Invoke-Zerologon
  - MailRaider
  - New-ADIDNSNode
  - New-DNSRecordArray
  - New-HoneyHash
  - New-InMemoryModule
  - New-MachineAccount
  - New-SOASerialNumberArray
  - Out-Minidump
  - Port-Scan
  - PowerBreach
  - 'powercat '
  - PowerUp
  - PowerView
  - Remove-ADIDNSNode
  - Remove-MachineAccount
  - Remove-Update
  - Rename-ADIDNSNode
  - Revoke-ADIDNSPermission
  - Set-ADIDNSNode
  - Set-MacAttribute
  - Set-MachineAccountAttribute
  - Set-Wallpaper
  - Show-TargetScreen
  - Start-CaptureServer
  - Start-Dnscat2
  - Start-WebcamRecorder
  - Veeam-Get-Creds
  - VolumeShadowCopyTools
condition: selection
```

## False Positives

- Unknown

## References

- https://adsecurity.org/?p=2921
- https://github.com/S3cur3Th1sSh1t/PowerSharpPack/tree/master/PowerSharpBinaries
- https://github.com/BC-SECURITY/Invoke-ZeroLogon/blob/111d17c7fec486d9bb23387e2e828b09a26075e4/Invoke-ZeroLogon.ps1
- https://github.com/xorrior/RandomPS-Scripts/blob/848c919bfce4e2d67b626cbcf4404341cfe3d3b6/Get-DXWebcamVideo.ps1
- https://github.com/rvrsh3ll/Misc-Powershell-Scripts/blob/6f23bb41f9675d7e2d32bacccff75e931ae00554/OfficeMemScraper.ps1
- https://github.com/dafthack/DomainPasswordSpray/blob/b13d64a5834694aa73fd2aea9911a83027c465a7/DomainPasswordSpray.ps1
- https://unit42.paloaltonetworks.com/threat-assessment-black-basta-ransomware/
- https://research.nccgroup.com/2022/06/06/shining-the-light-on-black-basta/
- https://github.com/calebstewart/CVE-2021-1675
- https://github.com/BloodHoundAD/BloodHound/blob/0927441f67161cc6dc08a53c63ceb8e333f55874/Collectors/AzureHound.ps1
- https://bloodhound.readthedocs.io/en/latest/data-collection/azurehound.html
- https://github.com/HarmJ0y/DAMP
- https://github.com/samratashok/nishang
- https://github.com/DarkCoderSc/PowerRunAsSystem/
- https://github.com/besimorhino/powercat
- https://github.com/Kevin-Robertson/Powermad
- https://github.com/adrecon/ADRecon
- https://github.com/adrecon/AzureADRecon
- https://github.com/sadshade/veeam-creds/blob/6010eaf31ba41011b58d6af3950cffbf6f5cea32/Veeam-Get-Creds.ps1
- https://github.com/The-Viper-One/Invoke-PowerDPAPI/
- https://github.com/Arno0x/DNSExfiltrator/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_malicious_cmdlets.yml)
