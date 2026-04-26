---
atomic_guid: "52ab5108-3f6f-42fb-8ba3-73bc054f22c8"
title: "Remote System Discovery - nltest"
framework: "atomic"
generated: "true"
attack_technique_id: "T1018"
attack_technique_name: "Remote System Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "52ab5108-3f6f-42fb-8ba3-73bc054f22c8"
  - "Remote System Discovery - nltest"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Remote System Discovery - nltest

Identify domain controllers for specified domain.

Upon successful execution, cmd.exe will execute nltest.exe against a target domain to retrieve a list of domain controllers. Output will be via stdout.

## Metadata

- Atomic GUID: 52ab5108-3f6f-42fb-8ba3-73bc054f22c8
- Technique: T1018: Remote System Discovery
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1018/T1018.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018]]

## Input Arguments

### target_domain

- description: Domain to query for domain controllers
- type: string
- default: %userdnsdomain%

## Executor

- name: command_prompt

### Command

```commandprompt
nltest.exe /dclist:#{target_domain}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml)
