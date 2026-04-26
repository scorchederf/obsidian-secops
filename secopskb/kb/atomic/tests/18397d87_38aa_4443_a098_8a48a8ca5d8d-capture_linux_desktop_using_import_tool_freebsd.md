---
atomic_guid: "18397d87-38aa-4443-a098-8a48a8ca5d8d"
title: "Capture Linux Desktop using Import Tool (freebsd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1113"
attack_technique_name: "Screen Capture"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1113/T1113.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "18397d87-38aa-4443-a098-8a48a8ca5d8d"
  - "Capture Linux Desktop using Import Tool (freebsd)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Capture Linux Desktop using Import Tool (freebsd)

Use import command from ImageMagick to collect a full desktop screenshot

## Metadata

- Atomic GUID: 18397d87-38aa-4443-a098-8a48a8ca5d8d
- Technique: T1113: Screen Capture
- Platforms: linux
- Executor: sh
- Source Path: atomics/T1113/T1113.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1113-screen_capture|T1113]]

## Input Arguments

### output_file

- description: Output file path
- type: path
- default: /tmp/T1113_desktop.png

## Dependencies

ImageMagick must be installed

### Prerequisite Check

```untitled
if import -help > /dev/null 2>&1; then exit 0; else exit 1; fi
```

### Get Prerequisite

```untitled
pkg install -y ImageMagick7
```

## Executor

- name: sh

### Command

```bash
import -window root #{output_file}
```

### Cleanup

```bash
rm #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1113/T1113.yaml)
