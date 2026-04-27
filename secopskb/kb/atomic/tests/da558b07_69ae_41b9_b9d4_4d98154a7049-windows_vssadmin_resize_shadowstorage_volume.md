---
atomic_guid: "da558b07-69ae-41b9-b9d4-4d98154a7049"
title: "Windows - vssadmin Resize Shadowstorage Volume"
framework: "atomic"
generated: "true"
attack_technique_id: "T1490"
attack_technique_name: "Inhibit System Recovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "da558b07-69ae-41b9-b9d4-4d98154a7049"
  - "Windows - vssadmin Resize Shadowstorage Volume"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Adversaries generally try to Resize Shadowstorage Volume using vssadmin.exe to avoid the shadow volumes being made again. This technique is typically found used by adversaries during a ransomware event and a precursor to deleting the shadowstorage.

## ATT&CK Mapping

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490: Inhibit System Recovery]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
vssadmin resize shadowstorage /For=C: /On=C: /MaxSize=20%
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml)
