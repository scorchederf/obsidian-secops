---
atomic_guid: "edff98ec-0f73-4f63-9890-6b117092aff6"
title: "System Information Discovery"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "edff98ec-0f73-4f63-9890-6b117092aff6"
  - "System Information Discovery"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# System Information Discovery

Identify System Info

## Metadata

- Atomic GUID: edff98ec-0f73-4f63-9890-6b117092aff6
- Technique: T1082: System Information Discovery
- Platforms: macos
- Executor: sh
- Source Path: atomics/T1082/T1082.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Executor

- name: sh

### Command

```sh
system_profiler
ls -al /Applications
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
