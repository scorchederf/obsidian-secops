---
atomic_guid: "68981660-6670-47ee-a5fa-7e74806420a4"
title: "Find and Display Internet Explorer Browser Version"
framework: "atomic"
generated: "true"
attack_technique_id: "T1518"
attack_technique_name: "Software Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518/T1518.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "68981660-6670-47ee-a5fa-7e74806420a4"
  - "Find and Display Internet Explorer Browser Version"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Query the registry to determine the version of internet explorer installed on the system.
Upon execution, version information about internet explorer will be displayed.

## ATT&CK Mapping

- [[kb/attack/techniques/T1518-software_discovery|T1518: Software Discovery]]

## Executor

- name: command_prompt

### Command

```cmd
reg query "HKEY_LOCAL_MACHINE\Software\Microsoft\Internet Explorer" /v svcVersion
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518/T1518.yaml)
