---
atomic_guid: "997bb0a6-421e-40c7-b5d2-0f493904ef9b"
title: "System Network Connections Discovery via sockstat (Linux, FreeBSD)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1049"
attack_technique_name: "System Network Connections Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1049/T1049.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "997bb0a6-421e-40c7-b5d2-0f493904ef9b"
  - "System Network Connections Discovery via sockstat (Linux, FreeBSD)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# System Network Connections Discovery via sockstat (Linux, FreeBSD)

Enumerate IPv4/IPv6 network endpoints on FreeBSD using sockstat.

## Metadata

- Atomic GUID: 997bb0a6-421e-40c7-b5d2-0f493904ef9b
- Technique: T1049: System Network Connections Discovery
- Platforms: linux
- Executor: sh
- Source Path: atomics/T1049/T1049.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1049-system_network_connections_discovery|T1049]]

## Executor

- name: sh

### Command

```bash
sockstat -4
sockstat -6 2>/dev/null || true
sockstat -l 2>/dev/null || true
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1049/T1049.yaml)
