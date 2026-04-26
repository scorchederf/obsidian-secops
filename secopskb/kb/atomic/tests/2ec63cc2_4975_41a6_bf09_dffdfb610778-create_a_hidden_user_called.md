---
atomic_guid: "2ec63cc2-4975-41a6-bf09-dffdfb610778"
title: "Create a Hidden User Called \"$\""
framework: "atomic"
generated: "true"
attack_technique_id: "T1564"
attack_technique_name: "Hide Artifacts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564/T1564.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "2ec63cc2-4975-41a6-bf09-dffdfb610778"
  - "Create a Hidden User Called \"$\""
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Create a Hidden User Called "$"

Creating a user with a username containing "$"

## Metadata

- Atomic GUID: 2ec63cc2-4975-41a6-bf09-dffdfb610778
- Technique: T1564: Hide Artifacts
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1564/T1564.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts|T1564]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
net user $ ATOMIC123! /add /active:yes
```

### Cleanup

```cmd
net user $ /DELETE 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564/T1564.yaml)
