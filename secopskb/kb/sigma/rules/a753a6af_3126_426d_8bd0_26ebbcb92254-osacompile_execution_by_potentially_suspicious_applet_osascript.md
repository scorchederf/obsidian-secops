---
sigma_id: "a753a6af-3126-426d-8bd0-26ebbcb92254"
title: "Osacompile Execution By Potentially Suspicious Applet/Osascript"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_suspicious_applet_behaviour.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_suspicious_applet_behaviour.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "a753a6af-3126-426d-8bd0-26ebbcb92254"
  - "Osacompile Execution By Potentially Suspicious Applet/Osascript"
attack_technique_ids:
  - "T1059.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Osacompile Execution By Potentially Suspicious Applet/Osascript

Detects potential suspicious applet or osascript executing "osacompile".

## Metadata

- Rule ID: a753a6af-3126-426d-8bd0-26ebbcb92254
- Status: test
- Level: medium
- Author: Sohan G (D4rkCiph3r), Red Canary (Idea)
- Date: 2023-04-03
- Source Path: rules/macos/process_creation/proc_creation_macos_suspicious_applet_behaviour.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.002]]

## Detection

```yaml
selection:
  ParentImage|endswith:
  - /applet
  - /osascript
  CommandLine|contains: osacompile
condition: selection
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/mac-application-bundles/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_suspicious_applet_behaviour.yml)
