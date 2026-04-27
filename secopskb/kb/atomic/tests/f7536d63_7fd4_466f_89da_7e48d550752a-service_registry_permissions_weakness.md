---
atomic_guid: "f7536d63-7fd4-466f-89da-7e48d550752a"
title: "Service Registry Permissions Weakness"
framework: "atomic"
generated: "true"
attack_technique_id: "T1574.011"
attack_technique_name: "Hijack Execution Flow: Services Registry Permissions Weakness"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.011/T1574.011.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "f7536d63-7fd4-466f-89da-7e48d550752a"
  - "Service Registry Permissions Weakness"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Service registry permissions weakness check and then which can lead to privilege escalation with ImagePath. eg.
reg add "HKLM\SYSTEM\CurrentControlSet\Services\#{weak_service_name}" /f /v ImagePath /d "C:\temp\AtomicRedteam.exe"

## ATT&CK Mapping

- [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574011-services-registry-permissions-weakness|T1574.011: Services Registry Permissions Weakness]]

## Input Arguments

### weak_service_name

- description: weak service check
- type: string
- default: weakservicename

## Executor

- name: powershell

### Command

```powershell
get-acl REGISTRY::HKLM\SYSTEM\CurrentControlSet\Services\* |FL
get-acl REGISTRY::HKLM\SYSTEM\CurrentControlSet\Services\#{weak_service_name} |FL
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.011/T1574.011.yaml)
