---
atomic_guid: "0e65ae27-5385-46b4-98ac-607a8ee82261"
title: "Azure AD - adding user to Azure AD role"
framework: "atomic"
generated: "true"
attack_technique_id: "T1098"
attack_technique_name: "Account Manipulation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098/T1098.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "0e65ae27-5385-46b4-98ac-607a8ee82261"
  - "Azure AD - adding user to Azure AD role"
platforms:
  - "azure-ad"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Azure AD - adding user to Azure AD role

The adversaries want to add user to some Azure AD role. Threat actor 
may be interested primarily in highly privileged roles, e.g. Global Administrator, Application Administrator, 
Privileged Authentication Administrator (this role can reset Global Administrator password!).
By default, the role Global Reader is assigned to the user principal in this test.

The account you use to run the PowerShell command should have Privileged Role Administrator or Global Administrator role in your Azure AD.

Detection hint - check Activity "Add member to role" in Azure AD Audit Logs. In targer you will also see User as a type.

## Metadata

- Atomic GUID: 0e65ae27-5385-46b4-98ac-607a8ee82261
- Technique: T1098: Account Manipulation
- Platforms: azure-ad
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1098/T1098.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Input Arguments

### password

- description: Azure AD password
- type: string
- default: p4sswd

### role_name

- description: Name of the targeted Azure AD role
- type: string
- default: Global Reader

### user_principal_name

- description: Display Name, or User Principal Name, of the targeted user principal
- type: string
- default: SuperUser

### username

- description: Azure AD username
- type: string
- default: jonh@contoso.com

## Dependencies

AzureAD module must be installed.

### Prerequisite Check

```untitled
try {if (Get-InstalledModule -Name AzureAD -ErrorAction SilentlyContinue) {exit 0} else {exit 1}} catch {exit 1}
```

### Get Prerequisite

```untitled
Install-Module -Name AzureAD -Force
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
Import-Module -Name AzureAD
$PWord = ConvertTo-SecureString -String "#{password}" -AsPlainText -Force
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "#{username}", $Pword
Connect-AzureAD -Credential $Credential

$user = Get-AzureADUser -Filter "DisplayName eq '#{user_principal_name}' or UserPrincipalName eq '#{user_principal_name}'"
if ($user -eq $null) { Write-Warning "User not found"; exit }
$role = Get-AzureADDirectoryRole -Filter "DisplayName eq '#{role_name}'"
if ($role -eq $null) { Write-Warning "Role not found"; exit }
Add-AzureADDirectoryRoleMember -ObjectId $role.ObjectId -RefObjectId $user.ObjectId
Write-Host "User $($user.DisplayName) was added to $($role.DisplayName) role"
```

### Cleanup

```powershell
Import-Module -Name AzureAD -ErrorAction Ignore
$PWord = ConvertTo-SecureString -String "#{password}" -AsPlainText -Force
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "#{username}", $Pword
Connect-AzureAD -Credential $Credential -ErrorAction Ignore

$user = Get-AzureADUser -Filter "DisplayName eq '#{user_principal_name}' or UserPrincipalName eq '#{user_principal_name}'"
if ($user -eq $null) { Write-Warning "User not found"; exit }
$role = Get-AzureADDirectoryRole -Filter "DisplayName eq '#{role_name}'"
if ($role -eq $null) { Write-Warning "Role not found"; exit }

Remove-AzureADDirectoryRoleMember -ObjectId $role.ObjectId -MemberId $user.ObjectId
Write-Host "User $($user.DisplayName) was removed from $($role.DisplayName) role"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098/T1098.yaml)
