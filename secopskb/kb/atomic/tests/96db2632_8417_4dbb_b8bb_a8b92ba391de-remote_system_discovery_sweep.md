---
atomic_guid: "96db2632-8417-4dbb-b8bb-a8b92ba391de"
title: "Remote System Discovery - sweep"
framework: "atomic"
generated: "true"
attack_technique_id: "T1018"
attack_technique_name: "Remote System Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "96db2632-8417-4dbb-b8bb-a8b92ba391de"
  - "Remote System Discovery - sweep"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Remote System Discovery - sweep

Identify remote systems via ping sweep.

Upon successful execution, sh will perform a ping sweep on the 192.168.1.1/24 and echo via stdout if an IP is active.

## Metadata

- Atomic GUID: 96db2632-8417-4dbb-b8bb-a8b92ba391de
- Technique: T1018: Remote System Discovery
- Platforms: linux, macos
- Executor: sh
- Source Path: atomics/T1018/T1018.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018]]

## Input Arguments

### start_host

- description: Subnet used for ping sweep.
- type: string
- default: 1

### stop_host

- description: Subnet used for ping sweep.
- type: string
- default: 254

### subnet

- description: Subnet used for ping sweep.
- type: string
- default: 192.168.1

## Executor

- name: sh

### Command

```sh
for ip in $(seq #{start_host} #{stop_host}); do ping -c 1 #{subnet}.$ip; [ $? -eq 0 ] && echo "#{subnet}.$ip UP" || : ; done
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml)
