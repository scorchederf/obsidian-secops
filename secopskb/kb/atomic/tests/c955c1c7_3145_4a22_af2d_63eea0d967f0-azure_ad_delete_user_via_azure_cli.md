---
atomic_guid: "c955c1c7-3145-4a22-af2d-63eea0d967f0"
title: "Azure AD - Delete user via Azure CLI"
framework: "atomic"
generated: "true"
attack_technique_id: "T1531"
attack_technique_name: "Account Access Removal"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1531/T1531.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "c955c1c7-3145-4a22-af2d-63eea0d967f0"
  - "Azure AD - Delete user via Azure CLI"
platforms:
  - "azure-ad"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Azure AD - Delete user via Azure CLI

Deletes a user in Azure AD. Adversaries may interrupt availability of system and network resources by inhibiting access to accounts utilized by legitimate users. Accounts may be deleted, locked, or manipulated (excluding changed credentials) to remove access to accounts.

## Metadata

- Atomic GUID: c955c1c7-3145-4a22-af2d-63eea0d967f0
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

Check if Azure CLI is installed and install manually

### Prerequisite Check

```powershell
az account list
```

### Get Prerequisite

```powershell
echo "use the following to install the Azure CLI manually https://aka.ms/installazurecliwindows"
```

Check if Azure CLI is installed and install via PowerShell

### Prerequisite Check

```powershell
az account list
```

### Get Prerequisite

```powershell
echo "use the following to install the Azure CLI $ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest -Uri https://aka.ms/installazurecliwindows -OutFile .\AzureCLI.msi; Start-Process msiexec.exe -Wait -ArgumentList '/I AzureCLI.msi /quiet'; Remove-Item .\AzureCLI.msi"
```

Update the userprincipalname to meet your requirements

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
az login
$userprincipalname = "#{userprincipalname}"
az ad user delete --id $userprincipalname
```

### Cleanup

```powershell
N/A
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1531/T1531.yaml)
