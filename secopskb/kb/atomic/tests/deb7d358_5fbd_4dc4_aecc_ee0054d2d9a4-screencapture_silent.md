---
atomic_guid: "deb7d358-5fbd-4dc4-aecc-ee0054d2d9a4"
title: "Screencapture (silent)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1113"
attack_technique_name: "Screen Capture"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1113/T1113.yaml"
build_date: "2026-04-26 14:38:40"
executor: "bash"
aliases:
  - "deb7d358-5fbd-4dc4-aecc-ee0054d2d9a4"
  - "Screencapture (silent)"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Screencapture (silent)

Use screencapture command to collect a full desktop screenshot

## Metadata

- Atomic GUID: deb7d358-5fbd-4dc4-aecc-ee0054d2d9a4
- Technique: T1113: Screen Capture
- Platforms: macos
- Executor: bash
- Source Path: atomics/T1113/T1113.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1113-screen_capture|T1113]]

## Input Arguments

### output_file

- description: Output file path
- type: path
- default: /tmp/T1113_desktop.png

## Executor

- name: bash

### Command

```bash
screencapture -x #{output_file}
```

### Cleanup

```bash
rm #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1113/T1113.yaml)
