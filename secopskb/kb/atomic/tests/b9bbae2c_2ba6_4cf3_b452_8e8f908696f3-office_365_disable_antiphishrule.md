---
atomic_guid: "b9bbae2c-2ba6-4cf3-b452-8e8f908696f3"
title: "office-365-Disable-AntiPhishRule"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "b9bbae2c-2ba6-4cf3-b452-8e8f908696f3"
  - "office-365-Disable-AntiPhishRule"
platforms:
  - "office-365"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Using the Disable-AntiPhishRule cmdlet to disable antiphish rules in your office-365 organization.

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

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
$test = Get-AntiPhishRule
Disable-AntiPhishRule -Identity $test.Name -Confirm:$false
Get-AntiPhishRule
```

### Cleanup

```powershell
if("#{password}" -ne "") {
$secure_pwd = ("#{password}" + "") | ConvertTo-SecureString -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential -ArgumentList "#{username}", $secure_pwd
Connect-ExchangeOnline -Credential $creds
$test = Get-AntiPhishRule
Enable-AntiPhishRule -Identity $test.Name -Confirm:$false
Get-AntiPhishRule
}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
