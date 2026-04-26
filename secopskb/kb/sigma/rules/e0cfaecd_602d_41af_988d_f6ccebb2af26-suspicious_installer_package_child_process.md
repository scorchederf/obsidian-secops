---
sigma_id: "e0cfaecd-602d-41af-988d-f6ccebb2af26"
title: "Suspicious Installer Package Child Process"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_installer_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_installer_susp_child_process.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "e0cfaecd-602d-41af-988d-f6ccebb2af26"
  - "Suspicious Installer Package Child Process"
attack_technique_ids:
  - "T1059"
  - "T1059.007"
  - "T1071"
  - "T1071.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Installer Package Child Process

Detects the execution of suspicious child processes from macOS installer package parent process. This includes osascript, JXA, curl and wget amongst other interpreters

## Metadata

- Rule ID: e0cfaecd-602d-41af-988d-f6ccebb2af26
- Status: test
- Level: medium
- Author: Sohan G (D4rkCiph3r)
- Date: 2023-02-18
- Source Path: rules/macos/process_creation/proc_creation_macos_installer_susp_child_process.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.007]]
- [[kb/attack/techniques/T1071-application_layer_protocol|T1071]]
- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]

## Detection

```yaml
selection_installer:
  ParentImage|endswith:
  - /package_script_service
  - /installer
  Image|endswith:
  - /sh
  - /bash
  - /dash
  - /python
  - /ruby
  - /perl
  - /php
  - /javascript
  - /osascript
  - /tclsh
  - /curl
  - /wget
  CommandLine|contains:
  - preinstall
  - postinstall
condition: selection_installer
```

## False Positives

- Legitimate software uses the scripts (preinstall, postinstall)

## References

- https://redcanary.com/blog/clipping-silver-sparrows-wings/
- https://github.com/elastic/detection-rules/blob/4312d8c9583be524578a14fe6295c3370b9a9307/rules/macos/execution_installer_package_spawned_network_event.toml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_installer_susp_child_process.yml)
