---
atomic_guid: "f4b26bce-4c2c-46c0-bcc5-fce062d38bef"
title: "System Service Discovery - systemctl/service"
framework: "atomic"
generated: "true"
attack_technique_id: "T1007"
attack_technique_name: "System Service Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1007/T1007.yaml"
build_date: "2026-04-27 19:12:25"
executor: "bash"
aliases:
  - "f4b26bce-4c2c-46c0-bcc5-fce062d38bef"
  - "System Service Discovery - systemctl/service"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Enumerates system service using systemctl/service

## ATT&CK Mapping

- [[kb/attack/techniques/T1007-system_service_discovery|T1007: System Service Discovery]]

## Executor

- name: bash

### Command

```bash
if [ "$(uname)" = 'FreeBSD' ]; then service -e; else systemctl --type=service; fi;
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1007/T1007.yaml)
