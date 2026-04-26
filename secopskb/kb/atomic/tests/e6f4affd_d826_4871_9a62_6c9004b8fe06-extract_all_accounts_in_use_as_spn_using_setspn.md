---
atomic_guid: "e6f4affd-d826-4871-9a62-6c9004b8fe06"
title: "Extract all accounts in use as SPN using setspn"
framework: "atomic"
generated: "true"
attack_technique_id: "T1558.003"
attack_technique_name: "Steal or Forge Kerberos Tickets: Kerberoasting"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1558.003/T1558.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "e6f4affd-d826-4871-9a62-6c9004b8fe06"
  - "Extract all accounts in use as SPN using setspn"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Extract all accounts in use as SPN using setspn

The following test will utilize setspn to extract the Service Principal Names. This behavior is typically used during a kerberos or silver ticket attack. 
A successful execution will output all the SPNs for the related domain.

## Metadata

- Atomic GUID: e6f4affd-d826-4871-9a62-6c9004b8fe06
- Technique: T1558.003: Steal or Forge Kerberos Tickets: Kerberoasting
- Platforms: windows
- Executor: command_prompt
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

- name: command_prompt

### Command

```cmd
setspn -T #{domain_name} -Q */*
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1558.003/T1558.003.yaml)
