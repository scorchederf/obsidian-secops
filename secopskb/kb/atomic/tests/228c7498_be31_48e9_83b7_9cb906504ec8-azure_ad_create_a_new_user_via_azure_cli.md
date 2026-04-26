---
atomic_guid: "228c7498-be31-48e9-83b7-9cb906504ec8"
title: "Azure AD - Create a new user via Azure CLI"
framework: "atomic"
generated: "true"
attack_technique_id: "T1136.003"
attack_technique_name: "Create Account: Cloud Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.003/T1136.003.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "228c7498-be31-48e9-83b7-9cb906504ec8"
  - "Azure AD - Create a new user via Azure CLI"
platforms:
  - "azure-ad"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Azure AD - Create a new user via Azure CLI

Creates a new user in Azure AD via the Azure CLI. Upon successful creation, a new user will be created. Adversaries create new users so that their malicious activity does not interrupt the normal functions of the compromised users and can remain undetected for a long time.

## Metadata

- Atomic GUID: 228c7498-be31-48e9-83b7-9cb906504ec8
- Technique: T1136.003: Create Account: Cloud Account
- Platforms: azure-ad
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1136.003/T1136.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1136-create_account|T1136.003]]

## Input Arguments

### password

- description: Password for the new Azure AD user being created
- type: string
- default: reallylongcredential12345ART-ydsfghsdgfhsdgfhgsdhfg

### username

- description: Display name of the new user to be created in Azure AD
- type: string
- default: atomicredteam

### userprincipalname

- description: User principal name (UPN) for the new Azure user being created format email address
- type: string
- default: atomicredteam@yourdomain.com

## Dependencies

Check if Azure CLI is installed and install manually

### Prerequisite Check

```text
az account list
```

### Get Prerequisite

```text
echo "use the following to install the Azure CLI manually https://aka.ms/installazurecliwindows"
```

Check if Azure CLI is installed and install via PowerShell

### Prerequisite Check

```text
az account list
```

### Get Prerequisite

```text
echo "use the following to install the Azure CLI $ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest -Uri https://aka.ms/installazurecliwindows -OutFile .\AzureCLI.msi; Start-Process msiexec.exe -Wait -ArgumentList '/I AzureCLI.msi /quiet'; Remove-Item .\AzureCLI.msi"
```

Update the userprincipalname to meet your requirements

### Prerequisite Check

```text
Update the input arguments so the userprincipalname value is accurate for your environment
```

### Get Prerequisite

```text
echo "Update the input arguments in the .yaml file so that the userprincipalname value is accurate for your environment"
```

## Executor

- name: powershell

### Command

```powershell
az login
$userprincipalname = "#{userprincipalname}"
$username = "#{username}"      
$password = "#{password}"
az ad user create --display-name $username --password $password --user-principal-name $userprincipalname
az ad user list --filter "displayname eq 'atomicredteam'"
```

### Cleanup

```powershell
az ad user delete --id "#{userprincipalname}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.003/T1136.003.yaml)
