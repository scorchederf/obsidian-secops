---
atomic_guid: "870ba71e-6858-4f6d-895c-bb6237f6121b"
title: "Enumerate Users Not Requiring Pre Auth (ASRepRoast)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1069.002"
attack_technique_name: "Permission Groups Discovery: Domain Groups"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.002/T1069.002.yaml"
build_date: "2026-04-27 19:12:26"
executor: "powershell"
aliases:
  - "870ba71e-6858-4f6d-895c-bb6237f6121b"
  - "Enumerate Users Not Requiring Pre Auth (ASRepRoast)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

When successful, accounts that do not require kerberos pre-auth will be returned

## ATT&CK Mapping

- [[kb/attack/techniques/T1069-permission_groups_discovery#^t1069002-domain-groups|T1069.002: Domain Groups]]

## Dependencies

Computer must be domain joined.

### Prerequisite Check

```powershell
if((Get-CIMInstance -Class Win32_ComputerSystem).PartOfDomain) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Write-Host Joining this computer to a domain must be done manually.
```

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
get-aduser -f * -pr DoesNotRequirePreAuth | where {$_.DoesNotRequirePreAuth -eq $TRUE}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.002/T1069.002.yaml)
