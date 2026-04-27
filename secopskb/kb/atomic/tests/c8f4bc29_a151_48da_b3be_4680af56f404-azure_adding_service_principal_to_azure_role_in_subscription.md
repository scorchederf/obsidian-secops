---
atomic_guid: "c8f4bc29-a151-48da-b3be-4680af56f404"
title: "Azure - adding service principal to Azure role in subscription"
framework: "atomic"
generated: "true"
attack_technique_id: "T1098"
attack_technique_name: "Account Manipulation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098/T1098.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "c8f4bc29-a151-48da-b3be-4680af56f404"
  - "Azure - adding service principal to Azure role in subscription"
platforms:
  - "iaas:azure"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Azure - adding service principal to Azure role in subscription

The adversaries want to add service principal to some Azure role, also called Azure resource role. Threat actor 
may be interested primarily in highly privileged roles, e.g. Owner, Contributor.
By default, the role Reader is assigned to service principal in this test.

New-AzRoleAssignment cmdlet could be also use to assign user/service principal to resource, resource group and management group.

The account you use to run the PowerShell command must have Microsoft.Authorization/roleAssignments/write 
(e.g. such as User Access Administrator or Owner) and the Azure Active Directory Graph Directory.Read.All 
and Microsoft Graph Directory.Read.All permissions.

Detection hint - check Operation Name "Create role assignment" in subscriptions Activity Logs.

## Metadata

- Atomic GUID: c8f4bc29-a151-48da-b3be-4680af56f404
- Technique: T1098: Account Manipulation
- Platforms: iaas:azure
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

- description: Name of the targeted Azure role
- type: string
- default: Reader

### service_principal_name

- description: Name of the service principal
- type: string
- default: SuperSP

### subscription

- description: Name of the targeted subscription
- type: string
- default: Azure subscription 1

### username

- description: Azure AD username
- type: string
- default: jonh@contoso.com

## Dependencies

Az.Resources module must be installed.

### Prerequisite Check

```untitled
try {if (Get-InstalledModule -Name Az.Resources -ErrorAction SilentlyContinue) {exit 0} else {exit 1}} catch {exit 1}
```

### Get Prerequisite

```untitled
Install-Module -Name Az.Resources -Force
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
Import-Module -Name Az.Resources
$PWord = ConvertTo-SecureString -String "#{password}" -AsPlainText -Force
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "#{username}", $Pword
Connect-AzAccount -Credential $Credential

$sp = Get-AzADServicePrincipal | where-object {$_.DisplayName -eq "#{service_principal_name}"}
if ($sp -eq $null) { Write-Warning "Service Principal not found"; exit }
$subscription = Get-AzSubscription | where-object {$_.Name -eq "#{subscription}"} 
if ($subscription -eq $null) { Write-Warning "Subscription not found"; exit }
$role = Get-AzRoleDefinition | where-object {$_.Name -eq "#{role_name}"}
if ($role -eq $null) { Write-Warning "Role not found"; exit }

New-AzRoleAssignment -ObjectId $sp.id -RoleDefinitionId $role.id -Scope /subscriptions/$subscription
Write-Host "Service Principal $($sp.DisplayName) was added to $($role.Name) role in subscriptions $($subscriptions.Name)"
```

### Cleanup

```powershell
Import-Module -Name AzureAD -ErrorAction Ignore
$PWord = ConvertTo-SecureString -String "#{password}" -AsPlainText -Force
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "#{username}", $Pword
Connect-AzAccount -Credential $Credential -ErrorAction Ignore

$sp = Get-AzADServicePrincipal | where-object {$_.DisplayName -eq "#{service_principal_name}"}
if ($sp -eq $null) { Write-Warning "Service Principal not found"; exit }
$subscription = Get-AzSubscription | where-object {$_.Name -eq "#{subscription}"} 
if ($subscription -eq $null) { Write-Warning "Subscription not found"; exit }
$role = Get-AzRoleDefinition | where-object {$_.Name -eq "#{role_name}"}
if ($role -eq $null) { Write-Warning "Role not found"; exit }

Remove-AzRoleAssignment -ObjectId $sp.id -RoleDefinitionId $role.id -Scope /subscriptions/$subscription
Write-Host "Service Principal $($sp.DisplayName) was removed from $($role.Name) role in subscriptions $($subscriptions.Name)"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098/T1098.yaml)
