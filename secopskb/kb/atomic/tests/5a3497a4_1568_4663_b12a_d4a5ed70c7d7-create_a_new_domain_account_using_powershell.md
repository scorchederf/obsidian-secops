---
atomic_guid: "5a3497a4-1568-4663-b12a-d4a5ed70c7d7"
title: "Create a new Domain Account using PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1136.002"
attack_technique_name: "Create Account: Domain Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.002/T1136.002.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "5a3497a4-1568-4663-b12a-d4a5ed70c7d7"
  - "Create a new Domain Account using PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Create a new Domain Account using PowerShell

Creates a new Domain User using the credentials of the Current User

## Metadata

- Atomic GUID: 5a3497a4-1568-4663-b12a-d4a5ed70c7d7
- Technique: T1136.002: Create Account: Domain Account
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1136.002/T1136.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1136-create_account|T1136.002]]

## Input Arguments

### password

- description: Password of the Account to be created
- type: string
- default: T1136_pass123!

### username

- description: Name of the Account to be created
- type: string
- default: T1136.002_Admin

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$SamAccountName = '#{username}'
$AccountPassword = ConvertTo-SecureString '#{password}' -AsPlainText -Force
Add-Type -AssemblyName System.DirectoryServices.AccountManagement
$Context = New-Object -TypeName System.DirectoryServices.AccountManagement.PrincipalContext -ArgumentList ([System.DirectoryServices.AccountManagement.ContextType]::Domain)
$User = New-Object -TypeName System.DirectoryServices.AccountManagement.UserPrincipal -ArgumentList ($Context)
$User.SamAccountName = $SamAccountName
$TempCred = New-Object System.Management.Automation.PSCredential('a', $AccountPassword)
$User.SetPassword($TempCred.GetNetworkCredential().Password)
$User.Enabled = $True
$User.PasswordNotRequired = $False
$User.DisplayName = $SamAccountName
$User.Save()
$User
```

### Cleanup

```powershell
cmd /c "net user #{username} /del >nul 2>&1"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.002/T1136.002.yaml)
