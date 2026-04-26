---
sigma_id: "6e4dcdd1-e48b-42f7-b2d8-3b413fc58cb4"
title: "Suspicious Execution via macOS Script Editor"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_susp_execution_macos_script_editor.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_susp_execution_macos_script_editor.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "6e4dcdd1-e48b-42f7-b2d8-3b413fc58cb4"
  - "Suspicious Execution via macOS Script Editor"
attack_technique_ids:
  - "T1566"
  - "T1566.002"
  - "T1059"
  - "T1059.002"
  - "T1204"
  - "T1204.001"
  - "T1553"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Execution via macOS Script Editor

Detects when the macOS Script Editor utility spawns an unusual child process.

## Metadata

- Rule ID: 6e4dcdd1-e48b-42f7-b2d8-3b413fc58cb4
- Status: test
- Level: medium
- Author: Tim Rauch (rule), Elastic (idea)
- Date: 2022-10-21
- Modified: 2022-12-28
- Source Path: rules/macos/process_creation/proc_creation_macos_susp_execution_macos_script_editor.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1566-phishing|T1566]]
- [[kb/attack/techniques/T1566-phishing|T1566.002]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.002]]
- [[kb/attack/techniques/T1204-user_execution|T1204]]
- [[kb/attack/techniques/T1204-user_execution|T1204.001]]
- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith: /Script Editor
selection_img:
- Image|endswith:
  - /curl
  - /bash
  - /sh
  - /zsh
  - /dash
  - /fish
  - /osascript
  - /mktemp
  - /chmod
  - /php
  - /nohup
  - /openssl
  - /plutil
  - /PlistBuddy
  - /xattr
  - /sqlite
  - /funzip
  - /popen
- Image|contains:
  - python
  - perl
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/elastic/protections-artifacts/commit/746086721fd385d9f5c6647cada1788db4aea95f#diff-7f541fbc4a4a28a92970e8bf53effea5bd934604429112c920affb457f5b2685
- https://wojciechregula.blog/post/macos-red-teaming-initial-access-via-applescript-url/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_susp_execution_macos_script_editor.yml)
