---
atomic_guid: "837d609b-845e-4519-90ce-edc3b4b0e138"
title: "Discover System Language with locale"
framework: "atomic"
generated: "true"
attack_technique_id: "T1614.001"
attack_technique_name: "System Location Discovery: System Language Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614.001/T1614.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "837d609b-845e-4519-90ce-edc3b4b0e138"
  - "Discover System Language with locale"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Identify System language with the `locale` command.

Upon successful execution, the output will contain the environment variables that indicate
the 5 character locale that can be looked up to correlate the language and territory.

## ATT&CK Mapping

- [[kb/attack/techniques/T1614-system_location_discovery#^t1614001-system-language-discovery|T1614.001: System Language Discovery]]

## Executor

- name: sh

### Command

```bash
locale
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614.001/T1614.001.yaml)
