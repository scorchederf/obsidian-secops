---
atomic_guid: "812c3ab8-94b0-4698-a9bf-9420af23ce24"
title: "Execute a process from a directory masquerading as the current parent directory"
framework: "atomic"
generated: "true"
attack_technique_id: "T1036.005"
attack_technique_name: "Masquerading: Match Legitimate Name or Location"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.005/T1036.005.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "812c3ab8-94b0-4698-a9bf-9420af23ce24"
  - "Execute a process from a directory masquerading as the current parent directory"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Execute a process from a directory masquerading as the current parent directory

Create and execute a process from a directory masquerading as the current parent directory (`...` instead of normal `..`)

## Metadata

- Atomic GUID: 812c3ab8-94b0-4698-a9bf-9420af23ce24
- Technique: T1036.005: Masquerading: Match Legitimate Name or Location
- Platforms: macos, linux
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1036.005/T1036.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1036-masquerading|T1036.005]]

## Input Arguments

### test_message

- description: Test message to echo out to the screen
- type: string
- default: Hello from the Atomic Red Team test T1036.005#1

## Executor

- elevation_required: False
- name: sh

### Command

```bash
mkdir $HOME/...
cp $(which sh) $HOME/...
$HOME/.../sh -c "echo #{test_message}"
```

### Cleanup

```bash
rm -f $HOME/.../sh
rmdir $HOME/.../
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.005/T1036.005.yaml)
