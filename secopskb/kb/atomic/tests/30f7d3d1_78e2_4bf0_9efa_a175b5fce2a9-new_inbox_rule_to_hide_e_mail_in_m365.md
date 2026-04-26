---
atomic_guid: "30f7d3d1-78e2-4bf0-9efa-a175b5fce2a9"
title: "New-Inbox Rule to Hide E-mail in M365"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564.008"
attack_technique_name: "Hide Artifacts: Email Hiding Rules"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.008/T1564.008.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "30f7d3d1-78e2-4bf0-9efa-a175b5fce2a9"
  - "New-Inbox Rule to Hide E-mail in M365"
platforms:
  - "office-365"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# New-Inbox Rule to Hide E-mail in M365

This test simulates a user adding an inbox rule in M365 to delete emails with specific keywords in email subject or body.
 Reference: https://www.mandiant.com/sites/default/files/2021-09/rpt-fin4.pdf

## Metadata

- Atomic GUID: 30f7d3d1-78e2-4bf0-9efa-a175b5fce2a9
- Technique: T1564.008: Hide Artifacts: Email Hiding Rules
- Platforms: office-365
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1564.008/T1564.008.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.008]]

## Input Arguments

### auth_password

- description: M365 Password
- type: string
- default: p4sswd

### auth_username

- description: M365 Username
- type: string
- default: john@contoso.com

### mail_rulename

- description: Name of the inbox rule.
- type: string
- default: default

### target_mailbox

- description: Mailbox you are creating the rule in
- type: string
- default: jane@contoso.com

## Dependencies

ExchangeOnlineManagement module must be installed.

### Prerequisite Check

```text
try {if (Get-InstalledModule -Name ExchangeOnlineManagement -ErrorAction SilentlyContinue) {exit 0} else {exit 1}} catch {exit 1}
```

### Get Prerequisite

```text
Install-Module -Name ExchangeOnlineManagement -Force
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
Import-Module ExchangeOnlineManagement
$password = ConvertTo-SecureString -String "#{auth_password}" -AsPlainText -Force
$credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "#{auth_username}", $password
Connect-ExchangeOnline -Credential $credential -ErrorAction:SilentlyContinue
New-InboxRule -Mailbox #{target_mailbox} -Name #{mail_rulename} -SubjectOrBodyContainsWords ("phish","malware","hacked") -Confirm:$false -DeleteMessage:$true
```

### Cleanup

```powershell
Import-Module ExchangeOnlineManagement
$password = ConvertTo-SecureString -String "#{auth_password}" -AsPlainText -Force
$credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "#{auth_username}", $password
Connect-ExchangeOnline -Credential $credential
Remove-InboxRule -Mailbox #{target_mailbox} -Identity #{mail_rulename} -Confirm:$false
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.008/T1564.008.yaml)
