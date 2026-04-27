---
atomic_guid: "c5806a4f-62b8-4900-980b-c7ec004e9908"
title: "Process Discovery - tasklist"
framework: "atomic"
generated: "true"
attack_technique_id: "T1057"
attack_technique_name: "Process Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1057/T1057.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "c5806a4f-62b8-4900-980b-c7ec004e9908"
  - "Process Discovery - tasklist"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Utilize tasklist to identify processes.

Upon successful execution, cmd.exe will execute tasklist.exe to list processes. Output will be via stdout.

## ATT&CK Mapping

- [[kb/attack/techniques/T1057-process_discovery|T1057: Process Discovery]]

## Executor

- name: command_prompt

### Command

```cmd
tasklist
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1057/T1057.yaml)
