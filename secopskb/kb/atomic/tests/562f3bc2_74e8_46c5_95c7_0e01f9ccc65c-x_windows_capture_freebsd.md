---
atomic_guid: "562f3bc2-74e8-46c5-95c7-0e01f9ccc65c"
title: "X Windows Capture (freebsd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1113"
attack_technique_name: "Screen Capture"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1113/T1113.yaml"
build_date: "2026-04-27 19:12:27"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Use xwd command to collect a full desktop screenshot and review file with xwud

## ATT&CK Mapping

- [[kb/attack/techniques/T1113-screen_capture|T1113: Screen Capture]]

## Input Arguments

### output_file

- description: Output file path
- type: path
- default: /tmp/T1113_desktop.xwd

## Dependencies

Package with XWD and XWUD must exist on device

### Prerequisite Check

```bash
if [ -x "$(command -v xwd)" ]; then exit 0; else exit 1; fi
if [ -x "$(command -v xwud)" ]; then exit 0; else exit 1; fi
```

### Get Prerequisite

```bash
pkg install -y xwd xwud
```

## Executor

- name: sh

### Command

```bash
xwd -root -out #{output_file}
xwud -in #{output_file}
```

### Cleanup

```bash
rm #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1113/T1113.yaml)
