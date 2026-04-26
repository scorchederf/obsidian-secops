---
atomic_guid: "bcf05343-ef1d-4052-8a27-b00c9be42b9f"
title: "System Network Connections Discovery via ss or lsof (Linux/MacOS)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1049"
attack_technique_name: "System Network Connections Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1049/T1049.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "bcf05343-ef1d-4052-8a27-b00c9be42b9f"
  - "System Network Connections Discovery via ss or lsof (Linux/MacOS)"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# System Network Connections Discovery via ss or lsof (Linux/MacOS)

List active TCP/UDP network connections using ss, with lsof as a fallback
when ss is unavailable. Serves as an alternative to the netstat-based test.

## Metadata

- Atomic GUID: bcf05343-ef1d-4052-8a27-b00c9be42b9f
- Technique: T1049: System Network Connections Discovery
- Platforms: linux, macos
- Executor: bash
- Source Path: atomics/T1049/T1049.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1049-system_network_connections_discovery|T1049]]

## Executor

- name: bash

### Command

```bash
if command -v ss >/dev/null 2>&1; then ss -antp 2>/dev/null || ss -ant; ss -aunp 2>/dev/null || true; else lsof -i -nP 2>/dev/null || true; fi
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1049/T1049.yaml)
