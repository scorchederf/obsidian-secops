---
atomic_guid: "92c40b3f-c406-4d1f-8d2b-c039bf5009e4"
title: "Azure AD - adding service principal to Azure AD role"
framework: "atomic"
generated: "true"
attack_technique_id: "T1098"
attack_technique_name: "Account Manipulation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098/T1098.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "92c40b3f-c406-4d1f-8d2b-c039bf5009e4"
  - "Azure AD - adding service principal to Azure AD role"
platforms:
  - "azure-ad"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Azure AD - adding service principal to Azure AD role

The adversaries want to add service principal to some Azure AD role. Threat actor 
may be interested primarily in highly privileged roles, e.g. Global Administrator, Application Administrator, 
Privileged Authentication Administrator (this role can reset Global Administrator password!).
By default, the role Global Reader is assigned to service principal in this test.

The account you use to run the PowerShell command should have Privileged Role Administrator or Global Administrator role in your Azure AD.

Detection hint - check Activity "Add member to role" in Azure AD Audit Logs. In targer you will also see Service Principal as a type.

## Metadata

- Atomic GUID: 92c40b3f-c406-4d1f-8d2b-c039bf5009e4
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

### service_principal_name

- description: Name of the service principal
- type: string
- default: SuperSP

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

$sp = Get-AzureADServicePrincipal -Filter "DisplayName eq '#{service_principal_name}'"
if ($sp -eq $null) { Write-Warning "Service Principal not found"; exit }
$role = Get-AzureADDirectoryRole -Filter "DisplayName eq '#{role_name}'"
if ($role -eq $null) { Write-Warning "Role not found"; exit }
Add-AzureADDirectoryRoleMember -ObjectId $role.ObjectId -RefObjectId $sp.ObjectId
Write-Host "Service Principal $($sp.DisplayName) was added to $($role.DisplayName)"
```

### Cleanup

```powershell
Import-Module -Name AzureAD -ErrorAction Ignore
$PWord = ConvertTo-SecureString -String "#{password}" -AsPlainText -Force
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "#{username}", $Pword
Connect-AzureAD -Credential $Credential -ErrorAction Ignore

$sp = Get-AzureADServicePrincipal -Filter "DisplayName eq '#{service_principal_name}'"
if ($sp -eq $null) { Write-Warning "Service Principal not found"; exit }
$role = Get-AzureADDirectoryRole -Filter "DisplayName eq '#{role_name}'"
if ($role -eq $null) { Write-Warning "Role not found"; exit }

Remove-AzureADDirectoryRoleMember -ObjectId $role.ObjectId -MemberId $sp.ObjectId
Write-Host "Service Principal $($sp.DisplayName) was removed from $($role.DisplayName) role"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098/T1098.yaml)
