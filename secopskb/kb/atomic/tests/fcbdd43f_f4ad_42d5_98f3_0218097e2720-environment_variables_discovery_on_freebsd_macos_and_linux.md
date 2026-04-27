---
atomic_guid: "fcbdd43f-f4ad-42d5-98f3-0218097e2720"
title: "Environment variables discovery on freebsd, macos and linux"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "fcbdd43f-f4ad-42d5-98f3-0218097e2720"
  - "Environment variables discovery on freebsd, macos and linux"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Environment variables discovery on freebsd, macos and linux

Identify all environment variables. Upon execution, environments variables and your path info will be displayed.

## Metadata

- Atomic GUID: fcbdd43f-f4ad-42d5-98f3-0218097e2720
- Technique: T1082: System Information Discovery
- Platforms: linux, macos
- Executor: sh
- Source Path: atomics/T1082/T1082.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Executor

- name: sh

### Command

```bash
env
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
