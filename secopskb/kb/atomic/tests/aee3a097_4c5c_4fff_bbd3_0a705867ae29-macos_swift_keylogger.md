---
atomic_guid: "aee3a097-4c5c-4fff-bbd3-0a705867ae29"
title: "MacOS Swift Keylogger"
framework: "atomic"
generated: "true"
attack_technique_id: "T1056.001"
attack_technique_name: "Input Capture: Keylogging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.001/T1056.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "aee3a097-4c5c-4fff-bbd3-0a705867ae29"
  - "MacOS Swift Keylogger"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# MacOS Swift Keylogger

Utilizes a swift script to log keys to sout. It runs for 5 seconds then dumps the output to standard. Input Monitoring is required.
Input Monitoring can be enabled in System Preferences > Security & Privacy > Privacy > Input Monitoring.
Referece: https://cedowens.medium.com/taking-esf-for-a-nother-spin-6e1e6acd1b74

## Metadata

- Atomic GUID: aee3a097-4c5c-4fff-bbd3-0a705867ae29
- Technique: T1056.001: Input Capture: Keylogging
- Platforms: macos
- Executor: bash
- Elevation Required: False
- Dependency Executor: bash
- Source Path: atomics/T1056.001/T1056.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1056-input_capture|T1056.001]]

## Input Arguments

### swift_src

- description: Location of swift script
- type: path
- default: PathToAtomicsFolder/T1056.001/src/MacOSKeylogger.swift

## Dependencies

swift script must exist at #{swift_src}, and the terminal must have input monitoring permissions.

### Prerequisite Check

```bash
if [ -f #{swift_src} ]; then chmod +x #{swift_src}; else exit 1; fi
```

### Get Prerequisite

```bash
echo ""
```

## Executor

- elevation_required: False
- name: bash

### Command

```bash
swift #{swift_src} -keylog
```

### Cleanup

```bash
kill `pgrep swift-frontend`
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.001/T1056.001.yaml)
