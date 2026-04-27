---
atomic_guid: "a55a22e9-a3d3-42ce-bd48-2653adb8f7a9"
title: "Domain Account and Group Manipulate"
framework: "atomic"
generated: "true"
attack_technique_id: "T1098"
attack_technique_name: "Account Manipulation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098/T1098.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "a55a22e9-a3d3-42ce-bd48-2653adb8f7a9"
  - "Domain Account and Group Manipulate"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Domain Account and Group Manipulate

Create a random atr-nnnnnnnn account and add it to a domain group (by default, Domain Admins). 

The quickest way to run it is against a domain controller, using `-Session` of `Invoke-AtomicTest`. Alternatively,
you need to install PS Module ActiveDirectory (in prereqs) and run the script with appropriare AD privileges to 
create the user and alter the group. Automatic installation of the dependency requires an elevated session, 
and is unlikely to work with Powershell Core (untested).

If you consider running this test against a production Active Directory, the good practise is to create a dedicated
service account whose delegation is given onto a dedicated OU for user creation and deletion, as well as delegated
as group manager of the target group.

Example: `Invoke-AtomicTest -Session $session 'T1098' -TestNames "Domain Account and Group Manipulate" -InputArgs @{"group" = "DNSAdmins" }`

## Metadata

- Atomic GUID: a55a22e9-a3d3-42ce-bd48-2653adb8f7a9
- Technique: T1098: Account Manipulation
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1098/T1098.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Input Arguments

### account_prefix

- description: Prefix string of the random username (by default, atr-). Because the cleanup deletes such account based on
a match `(&(samaccountname=#{account_prefix}-*)(givenName=Test))`, if you are to change it, be careful.

- type: string
- default: atr-

### create_args

- description: Additional string appended to New-ADUser call
- type: string

### group

- description: Name of the group to alter
- type: string
- default: Domain Admins

## Dependencies

PS Module ActiveDirectory

### Prerequisite Check

```untitled
Try {
    Import-Module ActiveDirectory -ErrorAction Stop | Out-Null
    exit 0
} 
Catch {
    exit 1
}
```

### Get Prerequisite

```untitled
if((Get-CimInstance -ClassName Win32_OperatingSystem).ProductType -eq 1) {
  Add-WindowsCapability -Name (Get-WindowsCapability -Name RSAT.ActiveDirectory.DS* -Online).Name -Online
} else {
  Install-WindowsFeature RSAT-AD-PowerShell
}
```

## Executor

- name: powershell

### Command

```powershell
$x = Get-Random -Minimum 2 -Maximum 99
$y = Get-Random -Minimum 2 -Maximum 99
$z = Get-Random -Minimum 2 -Maximum 99
$w = Get-Random -Minimum 2 -Maximum 99

Import-Module ActiveDirectory
$account = "#{account_prefix}-$x$y$z"
New-ADUser -Name $account -GivenName "Test" -DisplayName $account -SamAccountName $account -Surname $account -Enabled:$False #{create_args}
Add-ADGroupMember "#{group}" $account
```

### Cleanup

```powershell
Get-ADUser -LDAPFilter "(&(samaccountname=#{account_prefix}-*)(givenName=Test))" | Remove-ADUser -Confirm:$False
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098/T1098.yaml)
