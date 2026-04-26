---
atomic_guid: "4f577511-dc1c-4045-bcb8-75d2457f01f4"
title: "Azure AD - Delete user via Azure AD PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1531"
attack_technique_name: "Account Access Removal"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1531/T1531.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "4f577511-dc1c-4045-bcb8-75d2457f01f4"
  - "Azure AD - Delete user via Azure AD PowerShell"
platforms:
  - "azure-ad"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Azure AD - Delete user via Azure AD PowerShell

Deletes a user in Azure AD. Adversaries may interrupt availability of system and network resources by inhibiting access to accounts utilized by legitimate users. Accounts may be deleted, locked, or manipulated (excluding changed credentials) to remove access to accounts.

## Metadata

- Atomic GUID: 4f577511-dc1c-4045-bcb8-75d2457f01f4
- Technique: T1531: Account Access Removal
- Platforms: azure-ad
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1531/T1531.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1531-account_access_removal|T1531]]

## Input Arguments

### userprincipalname

- description: User principal name (UPN) for the Azure user being deleted
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
Remove-AzureADUser -ObjectId $userprincipalname
```

### Cleanup

```powershell
N/A
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1531/T1531.yaml)
