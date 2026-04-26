---
sigma_id: "60f1ce20-484e-41bd-85f4-ac4afec2c541"
title: "GUI Input Capture - macOS"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_gui_input_capture.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_gui_input_capture.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "low"
logsource: "macos / process_creation"
aliases:
  - "60f1ce20-484e-41bd-85f4-ac4afec2c541"
  - "GUI Input Capture - macOS"
attack_technique_ids:
  - "T1056.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# GUI Input Capture - macOS

Detects attempts to use system dialog prompts to capture user credentials

## Metadata

- Rule ID: 60f1ce20-484e-41bd-85f4-ac4afec2c541
- Status: test
- Level: low
- Author: remotephone, oscd.community
- Date: 2020-10-13
- Modified: 2025-12-05
- Source Path: rules/macos/process_creation/proc_creation_macos_gui_input_capture.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1056-input_capture|T1056.002]]

## Detection

```yaml
selection_img:
  Image|endswith: /osascript
selection_cli_1:
  CommandLine|contains|all:
  - -e
  - display
  - dialog
  - answer
selection_cli_2:
  CommandLine|contains:
  - admin
  - administrator
  - authenticate
  - authentication
  - credentials
  - pass
  - password
  - unlock
condition: all of selection_*
```

## False Positives

- Legitimate administration tools and activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1056.002/T1056.002.md
- https://scriptingosx.com/2018/08/user-interaction-from-bash-scripts/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_gui_input_capture.yml)
