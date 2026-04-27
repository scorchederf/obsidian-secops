---
atomic_guid: "7816c252-b728-4ea6-a683-bd9441ca0b71"
title: "System Binary Proxy Execution - Wlrmdr Lolbin"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218"
attack_technique_name: "Signed Binary Proxy Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "7816c252-b728-4ea6-a683-bd9441ca0b71"
  - "System Binary Proxy Execution - Wlrmdr Lolbin"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Use wlrmdr(Windows Logon Reminder executable) as a proxy binary to evade defensive countermeasures

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Input Arguments

### payload_path

- description: Path to the executable
- type: String
- default: C:\Windows\System32\calc.exe

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
wlrmdr.exe -s 3600 -f 0 -t _ -m _ -a 11 -u "#{payload_path}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml)
