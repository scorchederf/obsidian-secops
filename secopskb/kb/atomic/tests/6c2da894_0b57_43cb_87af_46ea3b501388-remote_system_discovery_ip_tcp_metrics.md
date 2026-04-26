---
atomic_guid: "6c2da894-0b57-43cb-87af-46ea3b501388"
title: "Remote System Discovery - ip tcp_metrics"
framework: "atomic"
generated: "true"
attack_technique_id: "T1018"
attack_technique_name: "Remote System Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "6c2da894-0b57-43cb-87af-46ea3b501388"
  - "Remote System Discovery - ip tcp_metrics"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Remote System Discovery - ip tcp_metrics

Use the ip tcp_metrics command to display the recent cached entries for IPv4 and IPv6 source and destination addresses.

## Metadata

- Atomic GUID: 6c2da894-0b57-43cb-87af-46ea3b501388
- Technique: T1018: Remote System Discovery
- Platforms: linux
- Executor: sh
- Dependency Executor: sh
- Source Path: atomics/T1018/T1018.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018]]

## Dependencies

Check if ip command exists on the machine

### Prerequisite Check

```text
if [ -x "$(command -v ip)" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```text
apt-get install iproute2 -y
```

## Executor

- name: sh

### Command

```sh
ip tcp_metrics show |grep --invert-match "^127\."
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml)
