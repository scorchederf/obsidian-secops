---
atomic_guid: "9c8ef159-c666-472f-9874-90c8d60d136b"
title: "WMI Execute Remote Process"
framework: "atomic"
generated: "true"
attack_technique_id: "T1047"
attack_technique_name: "Windows Management Instrumentation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1047/T1047.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "9c8ef159-c666-472f-9874-90c8d60d136b"
  - "WMI Execute Remote Process"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test uses wmic.exe to execute a process on a remote host. Specify a valid value for remote IP using the node parameter.
To clean up, provide the same node input as the one provided to run the test
A common error message is "Node - (provided IP or default)  ERROR Description =The RPC server is unavailable" if the default or provided IP is unreachable

## ATT&CK Mapping

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]

## Input Arguments

### node

- description: Ip Address
- type: string
- default: 127.0.0.1

### password

- description: Password
- type: string
- default: P@ssw0rd1

### process_to_execute

- description: Name or path of process to execute.
- type: string
- default: notepad.exe

### user_name

- description: Username
- type: string
- default: DOMAIN\Administrator

## Executor

- name: command_prompt

### Command

```cmd
wmic /user:#{user_name} /password:#{password} /node:"#{node}" process call create #{process_to_execute}
```

### Cleanup

```cmd
wmic /user:#{user_name} /password:#{password} /node:"#{node}" process where name='#{process_to_execute}' delete >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1047/T1047.yaml)
