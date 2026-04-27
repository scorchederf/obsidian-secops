---
atomic_guid: "8a7f56ee-10e7-444c-a139-0109438288eb"
title: "Rundll32 execute payload by calling RouteTheCall"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.011"
attack_technique_name: "Signed Binary Proxy Execution: Rundll32"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.011/T1218.011.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "8a7f56ee-10e7-444c-a139-0109438288eb"
  - "Rundll32 execute payload by calling RouteTheCall"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Launch an executable payload by calling RouteTheCall. Test execution of a command using rundll32.exe to execute a payload{calc.exe} by calling RouteTheCall. Upon execution, calc.exe will be launched.
Reference: https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Zipfldr.yml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

## Input Arguments

### exe_to_launch

- description: Path of the executable to launch
- type: path
- default: '%windir%\System32\calc.exe'

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
rundll32.exe zipfldr.dll,RouteTheCall "#{exe_to_launch}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.011/T1218.011.yaml)
