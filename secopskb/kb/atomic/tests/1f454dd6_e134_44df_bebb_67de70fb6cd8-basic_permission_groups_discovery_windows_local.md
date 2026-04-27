---
atomic_guid: "1f454dd6-e134-44df-bebb-67de70fb6cd8"
title: "Basic Permission Groups Discovery Windows (Local)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1069.001"
attack_technique_name: "Permission Groups Discovery: Local Groups"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.001/T1069.001.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "1f454dd6-e134-44df-bebb-67de70fb6cd8"
  - "Basic Permission Groups Discovery Windows (Local)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Basic Permission Groups Discovery for Windows. This test will display some errors if run on a computer not connected to a domain. Upon execution, domain
information will be displayed.

## ATT&CK Mapping

- [[kb/attack/techniques/T1069-permission_groups_discovery#^t1069001-local-groups|T1069.001: Local Groups]]

## Executor

- name: command_prompt

### Command

```cmd
net localgroup
net localgroup "Administrators"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.001/T1069.001.yaml)
