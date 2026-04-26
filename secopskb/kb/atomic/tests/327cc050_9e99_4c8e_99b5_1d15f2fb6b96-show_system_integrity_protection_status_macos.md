---
atomic_guid: "327cc050-9e99-4c8e-99b5-1d15f2fb6b96"
title: "Show System Integrity Protection status (MacOS)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "327cc050-9e99-4c8e-99b5-1d15f2fb6b96"
  - "Show System Integrity Protection status (MacOS)"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Show System Integrity Protection status (MacOS)

Read and Display System Intergrety Protection status. csrutil is commonly used by malware and post-exploitation tools to determine whether certain files and directories on the system are writable or not.

## Metadata

- Atomic GUID: 327cc050-9e99-4c8e-99b5-1d15f2fb6b96
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
csrutil status
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
