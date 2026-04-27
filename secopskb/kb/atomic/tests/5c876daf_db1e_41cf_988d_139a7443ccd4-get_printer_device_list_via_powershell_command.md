---
atomic_guid: "5c876daf-db1e-41cf-988d-139a7443ccd4"
title: "Get Printer Device List via PowerShell Command"
framework: "atomic"
generated: "true"
attack_technique_id: "T1120"
attack_technique_name: "Peripheral Device Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1120/T1120.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "5c876daf-db1e-41cf-988d-139a7443ccd4"
  - "Get Printer Device List via PowerShell Command"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test uses PowerShell to list printers on a Windows system, demonstrating a discovery technique attackers might use to 
gather details on connected devices. Using Get-Printer, they can view information on all available printers, identifying 
potential devices for further targeting.

## ATT&CK Mapping

- [[kb/attack/techniques/T1120-peripheral_device_discovery|T1120: Peripheral Device Discovery]]

## Executor

- name: powershell

### Command

```powershell
Get-Printer
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1120/T1120.yaml)
