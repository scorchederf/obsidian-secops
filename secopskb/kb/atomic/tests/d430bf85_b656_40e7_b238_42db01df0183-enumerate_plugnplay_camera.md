---
atomic_guid: "d430bf85-b656-40e7-b238-42db01df0183"
title: "Enumerate PlugNPlay Camera"
framework: "atomic"
generated: "true"
attack_technique_id: "T1592.001"
attack_technique_name: "Gather Victim Host Information: Hardware"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1592.001/T1592.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "d430bf85-b656-40e7-b238-42db01df0183"
  - "Enumerate PlugNPlay Camera"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Enumerate PlugNPlay Camera using powershell commandlet. this technique was seen in dcrat malware backdoor capabilities where it enumerate the camera info mounted on the compromised host. reference: https://www.mandiant.com/resources/analyzing-dark-crystal-rat-backdoor

## ATT&CK Mapping

- [[kb/attack/techniques/T1592-gather_victim_host_information#^t1592001-hardware|T1592.001: Hardware]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Get-CimInstance -Query "SELECT * FROM Win32_PnPEntity WHERE (PNPClass = 'Image' OR PNPClass = 'Camera')"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1592.001/T1592.001.yaml)
