---
atomic_guid: "562f3bc2-74e8-46c5-95c7-0e01f9ccc65c"
title: "X Windows Capture (freebsd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1113"
attack_technique_name: "Screen Capture"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1113/T1113.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "562f3bc2-74e8-46c5-95c7-0e01f9ccc65c"
  - "X Windows Capture (freebsd)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# X Windows Capture (freebsd)

Use xwd command to collect a full desktop screenshot and review file with xwud

## Metadata

- Atomic GUID: 562f3bc2-74e8-46c5-95c7-0e01f9ccc65c
- Technique: T1113: Screen Capture
- Platforms: linux
- Executor: sh
- Dependency Executor: sh
- Source Path: atomics/T1113/T1113.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1113-screen_capture|T1113]]

## Input Arguments

### output_file

- description: Output file path
- type: path
- default: /tmp/T1113_desktop.xwd

## Dependencies

Package with XWD and XWUD must exist on device

### Prerequisite Check

```text
if [ -x "$(command -v xwd)" ]; then exit 0; else exit 1; fi
if [ -x "$(command -v xwud)" ]; then exit 0; else exit 1; fi
```

### Get Prerequisite

```text
pkg install -y xwd xwud
```

## Executor

- name: sh

### Command

```sh
xwd -root -out #{output_file}
xwud -in #{output_file}
```

### Cleanup

```sh
rm #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1113/T1113.yaml)
