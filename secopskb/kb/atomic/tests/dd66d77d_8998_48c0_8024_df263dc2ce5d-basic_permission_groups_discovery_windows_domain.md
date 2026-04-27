---
atomic_guid: "dd66d77d-8998-48c0-8024-df263dc2ce5d"
title: "Basic Permission Groups Discovery Windows (Domain)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1069.002"
attack_technique_name: "Permission Groups Discovery: Domain Groups"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.002/T1069.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "dd66d77d-8998-48c0-8024-df263dc2ce5d"
  - "Basic Permission Groups Discovery Windows (Domain)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Basic Permission Groups Discovery Windows (Domain)

Basic Permission Groups Discovery for Windows. This test will display some errors if run on a computer not connected to a domain. Upon execution, domain
information will be displayed.

## Metadata

- Atomic GUID: dd66d77d-8998-48c0-8024-df263dc2ce5d
- Technique: T1069.002: Permission Groups Discovery: Domain Groups
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1069.002/T1069.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.002]]

## Executor

- name: command_prompt

### Command

```cmd
net localgroup
net group /domain
net group "enterprise admins" /domain
net group "domain admins" /domain
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.002/T1069.002.yaml)
