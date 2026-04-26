---
sigma_id: "0877ed01-da46-4c49-8476-d49cdd80dfa7"
title: "Screen Capture - macOS"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_screencapture.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_screencapture.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "low"
logsource: "macos / process_creation"
aliases:
  - "0877ed01-da46-4c49-8476-d49cdd80dfa7"
  - "Screen Capture - macOS"
attack_technique_ids:
  - "T1113"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Screen Capture - macOS

Detects attempts to use screencapture to collect macOS screenshots

## Metadata

- Rule ID: 0877ed01-da46-4c49-8476-d49cdd80dfa7
- Status: test
- Level: low
- Author: remotephone, oscd.community
- Date: 2020-10-13
- Modified: 2021-11-27
- Source Path: rules/macos/process_creation/proc_creation_macos_screencapture.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1113-screen_capture|T1113]]

## Detection

```yaml
selection:
  Image: /usr/sbin/screencapture
condition: selection
```

## False Positives

- Legitimate user activity taking screenshots

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1113/T1113.md
- https://github.com/EmpireProject/Empire/blob/08cbd274bef78243d7a8ed6443b8364acd1fc48b/lib/modules/python/collection/osx/screenshot.py

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_screencapture.yml)
