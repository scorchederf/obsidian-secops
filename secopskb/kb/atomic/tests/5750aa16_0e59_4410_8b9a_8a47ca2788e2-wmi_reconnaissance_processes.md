---
atomic_guid: "5750aa16-0e59-4410-8b9a-8a47ca2788e2"
title: "WMI Reconnaissance Processes"
framework: "atomic"
generated: "true"
attack_technique_id: "T1047"
attack_technique_name: "Windows Management Instrumentation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1047/T1047.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "5750aa16-0e59-4410-8b9a-8a47ca2788e2"
  - "WMI Reconnaissance Processes"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adversary might use WMI to list Processes running on the compromised host.
When the test completes , there should be running processes listed on the command line.

## ATT&CK Mapping

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]

## Executor

- name: command_prompt

### Command

```cmd
wmic process get caption,executablepath,commandline /format:csv
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1047/T1047.yaml)
