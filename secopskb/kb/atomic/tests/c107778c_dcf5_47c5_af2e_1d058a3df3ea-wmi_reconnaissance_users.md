---
atomic_guid: "c107778c-dcf5-47c5-af2e-1d058a3df3ea"
title: "WMI Reconnaissance Users"
framework: "atomic"
generated: "true"
attack_technique_id: "T1047"
attack_technique_name: "Windows Management Instrumentation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1047/T1047.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "c107778c-dcf5-47c5-af2e-1d058a3df3ea"
  - "WMI Reconnaissance Users"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adversary might use WMI to list all local User Accounts. 
When the test completes , there should be local user accounts information displayed on the command line.

## ATT&CK Mapping

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]

## Executor

- name: command_prompt

### Command

```cmd
wmic useraccount get /ALL /format:csv
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1047/T1047.yaml)
