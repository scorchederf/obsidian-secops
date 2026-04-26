---
atomic_guid: "9b378962-a75e-4856-b117-2503d6dcebba"
title: "System Service Discovery - macOS launchctl"
framework: "atomic"
generated: "true"
attack_technique_id: "T1007"
attack_technique_name: "System Service Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1007/T1007.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "9b378962-a75e-4856-b117-2503d6dcebba"
  - "System Service Discovery - macOS launchctl"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# System Service Discovery - macOS launchctl

Enumerates services on macOS using launchctl. Used by adversaries for
identifying daemons, background services, and persistence mechanisms.

## Metadata

- Atomic GUID: 9b378962-a75e-4856-b117-2503d6dcebba
- Technique: T1007: System Service Discovery
- Platforms: macos
- Executor: sh
- Source Path: atomics/T1007/T1007.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1007-system_service_discovery|T1007]]

## Executor

- name: sh

### Command

```sh
launchctl list
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1007/T1007.yaml)
