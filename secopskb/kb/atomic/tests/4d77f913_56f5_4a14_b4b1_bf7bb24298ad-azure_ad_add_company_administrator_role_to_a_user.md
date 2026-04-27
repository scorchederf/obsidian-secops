---
atomic_guid: "4d77f913-56f5-4a14-b4b1-bf7bb24298ad"
title: "Azure AD - Add Company Administrator Role to a user"
framework: "atomic"
generated: "true"
attack_technique_id: "T1098.003"
attack_technique_name: "Account Manipulation: Additional Cloud Roles"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098.003/T1098.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "4d77f913-56f5-4a14-b4b1-bf7bb24298ad"
  - "Azure AD - Add Company Administrator Role to a user"
platforms:
  - "azure-ad"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Azure AD - Add Company Administrator Role to a user

Add an existing Azure user account the Company Administrator Role.

## Metadata

- Atomic GUID: 4d77f913-56f5-4a14-b4b1-bf7bb24298ad
- Technique: T1098.003: Account Manipulation: Additional Cloud Roles
- Platforms: azure-ad
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1098.003/T1098.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1098-account_manipulation|T1098.003]]

## Input Arguments

### password

- description: Azure AD password
- type: string
- default: p4sswd

### target_user

- description: Name of the user who will be assigned the Company Admin role
- type: string
- default: default

### username

- description: Azure AD username
- type: string
- default: jonh@contoso.com

## Dependencies

MSOnline module must be installed.

### Prerequisite Check

```powershell
try {if (Get-InstalledModule -Name MSOnline -ErrorAction SilentlyContinue) {exit 0} else {exit 1}} catch {exit 1}
```

### Get Prerequisite

```powershell
Install-Module -Name MSOnline -Force
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
Import-Module MSOnline
$Password = ConvertTo-SecureString -String "#{password}" -AsPlainText -Force
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "#{username}", $Password
Connect-MsolService -Credential $Credential
Add-MsolRoleMember -RoleName "Company Administrator" -RoleMemberEmailAddress "#{target_user}"
```

### Cleanup

```powershell
Remove-MsolRoleMember -RoleName "Company Administrator" -RoleMemberType User -RoleMemberEmailAddress "#{target_user}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098.003/T1098.003.yaml)
