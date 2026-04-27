---
atomic_guid: "5db21e1d-dd9c-4a50-b885-b1e748912767"
title: "Testing usage of uncommonly used port"
framework: "atomic"
generated: "true"
attack_technique_id: "T1571"
attack_technique_name: "Non-Standard Port"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1571/T1571.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "5db21e1d-dd9c-4a50-b885-b1e748912767"
  - "Testing usage of uncommonly used port"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Testing uncommonly used port utilizing telnet.

## ATT&CK Mapping

- [[kb/attack/techniques/T1571-non-standard_port|T1571: Non-Standard Port]]

## Input Arguments

### domain

- description: Specify target hostname
- type: string
- default: google.com

### port

- description: Specify uncommon port number
- type: string
- default: 8081

## Dependencies

Requires telnet

### Prerequisite Check

```bash
which telnet
```

### Get Prerequisite

```bash
echo "please install telnet to run this test"; exit 1
```

## Executor

- name: sh

### Command

```bash
echo quit | telnet #{domain} #{port}
exit 0
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1571/T1571.yaml)
