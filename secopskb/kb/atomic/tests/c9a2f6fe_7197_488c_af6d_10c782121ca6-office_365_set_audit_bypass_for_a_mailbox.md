---
atomic_guid: "c9a2f6fe-7197-488c-af6d-10c782121ca6"
title: "Office 365 - Set Audit Bypass For a Mailbox"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.008"
attack_technique_name: "Impair Defenses: Disable Cloud Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.008/T1562.008.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "c9a2f6fe-7197-488c-af6d-10c782121ca6"
  - "Office 365 - Set Audit Bypass For a Mailbox"
platforms:
  - "office-365"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Office 365 - Set Audit Bypass For a Mailbox

Use Exchange Management Shell to Mailbox auditing to bypass. It will prevent any mailbox audit logging entries being generated for the target e-mail box.
https://learn.microsoft.com/en-us/powershell/module/exchange/set-mailboxauditbypassassociation?view=exchange-ps

## Metadata

- Atomic GUID: c9a2f6fe-7197-488c-af6d-10c782121ca6
- Technique: T1562.008: Impair Defenses: Disable Cloud Logs
- Platforms: office-365
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1562.008/T1562.008.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.008]]

## Input Arguments

### password

- description: office-365 password
- type: string
- default: o365_password_test

### target_email

- description: office-365 target_email
- type: string
- default: o365_email_test

### username

- description: office-365 username
- type: string
- default: o365_user_test

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
Set-MailboxAuditBypassAssociation -Identity "#{target_email}" -AuditBypassEnabled $true
```

### Cleanup

```powershell
$secure_pwd = "#{password}" | ConvertTo-SecureString -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential -ArgumentList "#{username}", $secure_pwd
Connect-ExchangeOnline -Credential $creds
Set-MailboxAuditBypassAssociation -Identity "#{target_email}" -AuditBypassEnabled $false
Disconnect-ExchangeOnline -Confirm:$false
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.008/T1562.008.yaml)
