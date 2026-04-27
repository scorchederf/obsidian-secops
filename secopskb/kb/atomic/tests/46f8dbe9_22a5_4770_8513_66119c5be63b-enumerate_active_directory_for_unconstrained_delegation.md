---
atomic_guid: "46f8dbe9-22a5-4770-8513-66119c5be63b"
title: "Enumerate Active Directory for Unconstrained Delegation"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.002"
attack_technique_name: "Account Discovery: Domain Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "46f8dbe9-22a5-4770-8513-66119c5be63b"
  - "Enumerate Active Directory for Unconstrained Delegation"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Attackers may attempt to query for computer objects with the UserAccountControl property
'TRUSTED_FOR_DELEGATION' (0x80000;524288) set
More Information - https://shenaniganslabs.io/2019/01/28/Wagging-the-Dog.html#when-the-stars-align-unconstrained-delegation-leads-to-rce
Prerequisite: AD RSAT PowerShell module is needed and it must run under a domain user

## ATT&CK Mapping

- [[kb/attack/techniques/T1087-account_discovery#^t1087002-domain-account|T1087.002: Domain Account]]

## Input Arguments

### domain

- description: Domain FQDN
- type: string
- default: $env:UserDnsDomain

### uac_prop

- description: UAC Property to search
- type: integer
- default: 524288

## Dependencies

PowerShell ActiveDirectory Module must be installed

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

- elevation_required: False
- name: powershell

### Command

```powershell
Get-ADObject -LDAPFilter '(UserAccountControl:1.2.840.113556.1.4.803:=#{uac_prop})' -Server #{domain}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml)
