---
atomic_guid: "0fd48ef7-d890-4e93-a533-f7dedd5191d3"
title: "WMI Reconnaissance List Remote Services"
framework: "atomic"
generated: "true"
attack_technique_id: "T1047"
attack_technique_name: "Windows Management Instrumentation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1047/T1047.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "0fd48ef7-d890-4e93-a533-f7dedd5191d3"
  - "WMI Reconnaissance List Remote Services"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adversary might use WMI to check if a certain Remote Service is running on a remote device. 
When the test completes, a service information will be displayed on the screen if it exists.
A common feedback message is that "No instance(s) Available" if the service queried is not running.
A common error message is "Node - (provided IP or default)  ERROR Description =The RPC server is unavailable" 
if the provided remote host is unreachable

## ATT&CK Mapping

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]

## Input Arguments

### node

- description: Ip Address
- type: string
- default: 127.0.0.1

### service_search_string

- description: Name Of Service
- type: string
- default: Spooler

## Executor

- name: command_prompt

### Command

```cmd
wmic /node:"#{node}" service where (caption like "%#{service_search_string}%")
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1047/T1047.yaml)
