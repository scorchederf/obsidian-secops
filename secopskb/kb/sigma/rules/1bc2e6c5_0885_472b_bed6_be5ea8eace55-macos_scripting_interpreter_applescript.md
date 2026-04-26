---
sigma_id: "1bc2e6c5-0885-472b-bed6-be5ea8eace55"
title: "MacOS Scripting Interpreter AppleScript"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_applescript.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_applescript.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "1bc2e6c5-0885-472b-bed6-be5ea8eace55"
  - "MacOS Scripting Interpreter AppleScript"
attack_technique_ids:
  - "T1059.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# MacOS Scripting Interpreter AppleScript

Detects execution of AppleScript of the macOS scripting language AppleScript.

## Metadata

- Rule ID: 1bc2e6c5-0885-472b-bed6-be5ea8eace55
- Status: test
- Level: medium
- Author: Alejandro Ortuno, oscd.community
- Date: 2020-10-21
- Modified: 2023-02-01
- Source Path: rules/macos/process_creation/proc_creation_macos_applescript.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.002]]

## Detection

```yaml
selection:
  Image|endswith: /osascript
  CommandLine|contains:
  - ' -e '
  - .scpt
  - .js
condition: selection
```

## False Positives

- Application installers might contain scripts as part of the installation process.

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1059.002/T1059.002.md
- https://redcanary.com/blog/applescript/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_applescript.yml)
