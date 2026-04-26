---
atomic_guid: "9cd1cccb-91e4-4550-9139-e20a586fcea1"
title: "Capture Linux Desktop using Import Tool"
framework: "atomic"
generated: "true"
attack_technique_id: "T1113"
attack_technique_name: "Screen Capture"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1113/T1113.yaml"
build_date: "2026-04-26 14:38:40"
executor: "bash"
aliases:
  - "9cd1cccb-91e4-4550-9139-e20a586fcea1"
  - "Capture Linux Desktop using Import Tool"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Capture Linux Desktop using Import Tool

Use import command from ImageMagick to collect a full desktop screenshot

## Metadata

- Atomic GUID: 9cd1cccb-91e4-4550-9139-e20a586fcea1
- Technique: T1113: Screen Capture
- Platforms: linux
- Executor: bash
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

```text
if import -help > /dev/null 2>&1; then exit 0; else exit 1; fi
```

### Get Prerequisite

```text
sudo apt install graphicsmagick-imagemagick-compat
```

## Executor

- name: bash

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
