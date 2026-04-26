---
atomic_guid: "d2791d72-b67f-4615-814f-ec824a91f514"
title: "Remote System Discovery - netstat"
framework: "atomic"
generated: "true"
attack_technique_id: "T1018"
attack_technique_name: "Remote System Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "d2791d72-b67f-4615-814f-ec824a91f514"
  - "Remote System Discovery - netstat"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Remote System Discovery - netstat

Use the netstat command to display the kernels routing tables.

## Metadata

- Atomic GUID: d2791d72-b67f-4615-814f-ec824a91f514
- Technique: T1018: Remote System Discovery
- Platforms: linux
- Executor: sh
- Source Path: atomics/T1018/T1018.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018]]

## Executor

- name: sh

### Command

```bash
netstat -r | grep default
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml)
