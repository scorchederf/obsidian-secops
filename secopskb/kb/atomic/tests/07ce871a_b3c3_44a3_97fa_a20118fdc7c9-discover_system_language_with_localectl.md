---
atomic_guid: "07ce871a-b3c3-44a3-97fa-a20118fdc7c9"
title: "Discover System Language with localectl"
framework: "atomic"
generated: "true"
attack_technique_id: "T1614.001"
attack_technique_name: "System Location Discovery: System Language Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614.001/T1614.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "07ce871a-b3c3-44a3-97fa-a20118fdc7c9"
  - "Discover System Language with localectl"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Discover System Language with localectl

Identify System language with the `localectl` command.

Upon successful execution, the key `System Locale` from the output will contain the
`LANG` environment variable that has the 5 character locale result that can be looked
up to correlate the language and territory.

## Metadata

- Atomic GUID: 07ce871a-b3c3-44a3-97fa-a20118fdc7c9
- Technique: T1614.001: System Location Discovery: System Language Discovery
- Platforms: linux
- Executor: sh
- Source Path: atomics/T1614.001/T1614.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1614-system_location_discovery|T1614.001]]

## Executor

- name: sh

### Command

```bash
localectl status
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614.001/T1614.001.yaml)
