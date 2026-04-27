---
atomic_guid: "f1bf6c8f-9016-4edf-aff9-80b65f5d711f"
title: "Remote System Discovery - net group Domain Computers"
framework: "atomic"
generated: "true"
attack_technique_id: "T1018"
attack_technique_name: "Remote System Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml"
build_date: "2026-04-27 19:12:25"
executor: "command_prompt"
aliases:
  - "f1bf6c8f-9016-4edf-aff9-80b65f5d711f"
  - "Remote System Discovery - net group Domain Computers"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Identify remote systems with net.exe querying the Active Directory Domain Computers group.

Upon successful execution, cmd.exe will execute cmd.exe against Active Directory to list the "Domain Computers" group. Output will be via stdout.

## ATT&CK Mapping

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018: Remote System Discovery]]

## Executor

- name: command_prompt

### Command

```cmd
net group "Domain Computers" /domain
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml)
