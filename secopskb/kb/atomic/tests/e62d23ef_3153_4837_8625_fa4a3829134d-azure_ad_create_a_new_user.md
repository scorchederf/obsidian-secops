---
atomic_guid: "e62d23ef-3153-4837-8625-fa4a3829134d"
title: "Azure AD - Create a new user"
framework: "atomic"
generated: "true"
attack_technique_id: "T1136.003"
attack_technique_name: "Create Account: Cloud Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.003/T1136.003.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "e62d23ef-3153-4837-8625-fa4a3829134d"
  - "Azure AD - Create a new user"
platforms:
  - "azure-ad"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Creates a new user in Azure AD. Upon successful creation, a new user will be created. Adversaries create new users so that their malicious activity does not interrupt the normal functions of the compromised users and can remain undetected for a long time.

## ATT&CK Mapping

- [[kb/attack/techniques/T1136-create_account#^t1136003-cloud-account|T1136.003: Cloud Account]]

## Input Arguments

### password

- description: Password for the new Azure AD user being created
- type: string
- default: reallylongcredential12345ART-ydsfghsdgfhsdgfhgsdhfg

### username

- description: Display name of the new user to be created in Azure AD
- type: string
- default: atomicredteam

### userprincipalname

- description: User principal name (UPN) for the new Azure user being created format email address
- type: string
- default: atomicredteam@yourdomain.com

## Dependencies

Check if AzureAD PowerShell module is installed

### Prerequisite Check

```powershell
Get-InstalledModule -Name AzureAD
```

### Get Prerequisite

```powershell
echo "use the following to install AzureAD PowerShell module - Install-Module -Name AzureAD -Scope CurrentUser -Repository PSGallery -Force"
```

Check if AzureAD PowerShell module is installed

### Prerequisite Check

```powershell
Update the input arguments so the userprincipalname value is accurate for your environment
```

### Get Prerequisite

```powershell
echo "Update the input arguments in the .yaml file so that the userprincipalname value is accurate for your environment"
```

## Executor

- name: powershell

### Command

```powershell
Connect-AzureAD
$userprincipalname = "#{userprincipalname}"
$username = "#{username}"      
$password = "#{password}"
$PasswordProfile = New-Object -TypeName Microsoft.Open.AzureAD.Model.PasswordProfile
$PasswordProfile.Password = $password
New-AzureADUser -DisplayName $username -PasswordProfile $PasswordProfile -UserPrincipalName $userprincipalname -AccountEnabled $true -MailNickName $username
```

### Cleanup

```powershell
Remove-AzureADUser -ObjectId "#{userprincipalname}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.003/T1136.003.yaml)
