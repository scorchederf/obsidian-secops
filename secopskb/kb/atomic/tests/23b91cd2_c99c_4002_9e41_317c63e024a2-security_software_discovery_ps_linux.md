---
atomic_guid: "23b91cd2-c99c-4002-9e41-317c63e024a2"
title: "Security Software Discovery - ps (Linux)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1518.001"
attack_technique_name: "Software Discovery: Security Software Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518.001/T1518.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "23b91cd2-c99c-4002-9e41-317c63e024a2"
  - "Security Software Discovery - ps (Linux)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Security Software Discovery - ps (Linux)

Methods to identify Security Software on an endpoint
when sucessfully executed, command shell  is going to display AV/Security software it is running.

## Metadata

- Atomic GUID: 23b91cd2-c99c-4002-9e41-317c63e024a2
- Technique: T1518.001: Software Discovery: Security Software Discovery
- Platforms: linux
- Executor: sh
- Source Path: atomics/T1518.001/T1518.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1518-software_discovery|T1518.001]]

## Executor

- name: sh

### Command

```bash
ps aux | egrep 'falcond|nessusd|cbagentd|td-agent|packetbeat|filebeat|auditbeat|osqueryd'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518.001/T1518.001.yaml)
