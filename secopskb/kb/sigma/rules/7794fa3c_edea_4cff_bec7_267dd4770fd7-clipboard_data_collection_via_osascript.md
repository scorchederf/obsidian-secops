---
sigma_id: "7794fa3c-edea-4cff-bec7-267dd4770fd7"
title: "Clipboard Data Collection Via OSAScript"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_clipboard_data_via_osascript.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_clipboard_data_via_osascript.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "high"
logsource: "macos / process_creation"
aliases:
  - "7794fa3c-edea-4cff-bec7-267dd4770fd7"
  - "Clipboard Data Collection Via OSAScript"
attack_technique_ids:
  - "T1115"
  - "T1059.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Clipboard Data Collection Via OSAScript

Detects possible collection of data from the clipboard via execution of the osascript binary

## Metadata

- Rule ID: 7794fa3c-edea-4cff-bec7-267dd4770fd7
- Status: test
- Level: high
- Author: Sohan G (D4rkCiph3r)
- Date: 2023-01-31
- Source Path: rules/macos/process_creation/proc_creation_macos_clipboard_data_via_osascript.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1115-clipboard_data|T1115]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.002]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - osascript
  - ' -e '
  - clipboard
condition: selection
```

## False Positives

- Unlikely

## References

- https://www.sentinelone.com/blog/how-offensive-actors-use-applescript-for-attacking-macos/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_clipboard_data_via_osascript.yml)
