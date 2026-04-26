---
sigma_id: "f772cee9-b7c2-4cb2-8f07-49870adc02e0"
title: "Malicious Nishang PowerShell Commandlets"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_nishang_malicious_commandlets.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_nishang_malicious_commandlets.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "f772cee9-b7c2-4cb2-8f07-49870adc02e0"
  - "Malicious Nishang PowerShell Commandlets"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Malicious Nishang PowerShell Commandlets

Detects Commandlet names and arguments from the Nishang exploitation framework

## Metadata

- Rule ID: f772cee9-b7c2-4cb2-8f07-49870adc02e0
- Status: test
- Level: high
- Author: Alec Costello
- Date: 2019-05-16
- Modified: 2023-01-16
- Source Path: rules/windows/powershell/powershell_script/posh_ps_nishang_malicious_commandlets.yml

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
  - Add-ConstrainedDelegationBackdoor
  - Copy-VSS
  - Create-MultipleSessions
  - DataToEncode
  - DNS_TXT_Pwnage
  - Do-Exfiltration-Dns
  - Download_Execute
  - Download-Execute-PS
  - DownloadAndExtractFromRemoteRegistry
  - DumpCerts
  - DumpCreds
  - DumpHashes
  - Enable-DuplicateToken
  - Enable-Duplication
  - Execute-Command-MSSQL
  - Execute-DNSTXT-Code
  - Execute-OnTime
  - ExetoText
  - exfill
  - ExfilOption
  - FakeDC
  - FireBuster
  - FireListener
  - 'Get-Information '
  - Get-PassHints
  - Get-Web-Credentials
  - Get-WebCredentials
  - Get-WLAN-Keys
  - HTTP-Backdoor
  - Invoke-AmsiBypass
  - Invoke-BruteForce
  - Invoke-CredentialsPhish
  - Invoke-Decode
  - Invoke-Encode
  - Invoke-Interceptor
  - Invoke-JSRatRegsvr
  - Invoke-JSRatRundll
  - Invoke-MimikatzWDigestDowngrade
  - Invoke-NetworkRelay
  - Invoke-PowerShellIcmp
  - Invoke-PowerShellUdp
  - Invoke-Prasadhak
  - Invoke-PSGcat
  - Invoke-PsGcatAgent
  - Invoke-SessionGopher
  - Invoke-SSIDExfil
  - LoggedKeys
  - Nishang
  - NotAllNameSpaces
  - Out-CHM
  - OUT-DNSTXT
  - Out-HTA
  - Out-RundllCommand
  - Out-SCF
  - Out-SCT
  - Out-Shortcut
  - Out-WebQuery
  - Out-Word
  - Parse_Keys
  - Password-List
  - Powerpreter
  - Remove-Persistence
  - Remove-PoshRat
  - Remove-Update
  - Run-EXEonRemote
  - Set-DCShadowPermissions
  - Set-RemotePSRemoting
  - Set-RemoteWMI
  - Shellcode32
  - Shellcode64
  - StringtoBase64
  - TexttoExe
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/samratashok/nishang

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_nishang_malicious_commandlets.yml)
