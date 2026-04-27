---
atomic_guid: "43f71395-6c37-498e-ab17-897d814a0947"
title: "Remove Account From Domain Admin Group"
framework: "atomic"
generated: "true"
attack_technique_id: "T1531"
attack_technique_name: "Account Access Removal"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1531/T1531.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "43f71395-6c37-498e-ab17-897d814a0947"
  - "Remove Account From Domain Admin Group"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test will remove an account from the domain admins group

## ATT&CK Mapping

- [[kb/attack/techniques/T1531-account_access_removal|T1531: Account Access Removal]]

## Input Arguments

### remove_user

- description: Account to remove from domain admins.
- type: string
- default: remove_user

### super_pass

- description: super_user account password.
- type: string
- default: password

### super_user

- description: Account used to run the execution command (must include domain).
- type: string
- default: domain\super_user

## Dependencies

Requires the Active Directory module for powershell to be installed.

### Prerequisite Check

```powershell
if(Get-Module -ListAvailable -Name ActiveDirectory) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Add-WindowsCapability -Online -Name "Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0"
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$PWord = ConvertTo-SecureString -String #{super_pass} -AsPlainText -Force
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList #{super_user}, $PWord
if((Get-ADUser #{remove_user} -Properties memberof).memberof -like "CN=Domain Admins*"){
  Remove-ADGroupMember -Identity "Domain Admins" -Members #{remove_user} -Credential $Credential -Confirm:$False
} else{
    write-host "Error - Make sure #{remove_user} is in the domain admins group" -foregroundcolor Red
}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1531/T1531.yaml)
