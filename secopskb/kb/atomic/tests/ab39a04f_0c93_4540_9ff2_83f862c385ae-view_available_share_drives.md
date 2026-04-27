---
atomic_guid: "ab39a04f-0c93-4540-9ff2-83f862c385ae"
title: "View available share drives"
framework: "atomic"
generated: "true"
attack_technique_id: "T1135"
attack_technique_name: "Network Share Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "ab39a04f-0c93-4540-9ff2-83f862c385ae"
  - "View available share drives"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

View information about all of the resources that are shared on the local computer Upon execution, available share drives will be displayed in the powershell session

## ATT&CK Mapping

- [[kb/attack/techniques/T1135-network_share_discovery|T1135: Network Share Discovery]]

## Executor

- name: command_prompt

### Command

```cmd
net share
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml)
