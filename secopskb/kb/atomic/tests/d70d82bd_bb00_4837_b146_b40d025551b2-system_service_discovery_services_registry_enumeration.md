---
atomic_guid: "d70d82bd-bb00-4837-b146-b40d025551b2"
title: "System Service Discovery - Services Registry Enumeration"
framework: "atomic"
generated: "true"
attack_technique_id: "T1007"
attack_technique_name: "System Service Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1007/T1007.yaml"
build_date: "2026-04-27 19:12:25"
executor: "powershell"
aliases:
  - "d70d82bd-bb00-4837-b146-b40d025551b2"
  - "System Service Discovery - Services Registry Enumeration"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Enumerates Windows services by reading the Services registry key
(HKLM\SYSTEM\CurrentControlSet\Services) instead of using Service Control
Manager APIs or CLI tools such as sc.exe or Get-Service.

## ATT&CK Mapping

- [[kb/attack/techniques/T1007-system_service_discovery|T1007: System Service Discovery]]

## Executor

- name: powershell

### Command

```powershell
Get-ChildItem -Path 'HKLM:\SYSTEM\CurrentControlSet\Services' |
  ForEach-Object {
    $p = Get-ItemProperty -Path $_.PSPath -ErrorAction SilentlyContinue
    [PSCustomObject]@{
      Name        = $_.PSChildName
      DisplayName = $p.DisplayName
      ImagePath   = $p.ImagePath
      StartType   = $p.Start
    }
  }
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1007/T1007.yaml)
