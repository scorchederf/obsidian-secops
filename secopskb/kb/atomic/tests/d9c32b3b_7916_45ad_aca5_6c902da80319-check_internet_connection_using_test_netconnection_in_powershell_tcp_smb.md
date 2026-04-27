---
atomic_guid: "d9c32b3b-7916-45ad-aca5-6c902da80319"
title: "Check internet connection using Test-NetConnection in PowerShell (TCP-SMB)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1016.001"
attack_technique_name: "System Network Configuration Discovery: Internet Connection Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016.001/T1016.001.yaml"
build_date: "2026-04-27 19:12:25"
executor: "powershell"
aliases:
  - "d9c32b3b-7916-45ad-aca5-6c902da80319"
  - "Check internet connection using Test-NetConnection in PowerShell (TCP-SMB)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Check internet connection using PowerShell's Test-NetConnection cmdlet and the TCP protocol to check for outbound SMB (Port 445) access. The default target is 8.8.8.8.

## ATT&CK Mapping

- [[kb/attack/techniques/T1016-system_network_configuration_discovery#^t1016001-internet-connection-discovery|T1016.001: Internet Connection Discovery]]

## Input Arguments

### target

- description: target of the request
- type: string
- default: 8.8.8.8

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
Test-NetConnection -CommonTCPPort SMB -ComputerName #{target}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016.001/T1016.001.yaml)
