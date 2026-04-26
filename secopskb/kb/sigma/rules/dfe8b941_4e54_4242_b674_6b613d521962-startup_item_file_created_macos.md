---
sigma_id: "dfe8b941-4e54-4242-b674-6b613d521962"
title: "Startup Item File Created - MacOS"
framework: "sigma"
generated: "true"
source_path: "rules/macos/file_event/file_event_macos_susp_startup_item_created.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/file_event/file_event_macos_susp_startup_item_created.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "low"
logsource: "macos / file_event"
aliases:
  - "dfe8b941-4e54-4242-b674-6b613d521962"
  - "Startup Item File Created - MacOS"
attack_technique_ids:
  - "T1037.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Startup Item File Created - MacOS

Detects the creation of a startup item plist file, that automatically get executed at boot initialization to establish persistence.
Adversaries may use startup items automatically executed at boot initialization to establish persistence.
Startup items execute during the final phase of the boot process and contain shell scripts or other executable files along with configuration information used by the system to determine the execution order for all startup items.

## Metadata

- Rule ID: dfe8b941-4e54-4242-b674-6b613d521962
- Status: test
- Level: low
- Author: Alejandro Ortuno, oscd.community
- Date: 2020-10-14
- Modified: 2024-08-11
- Source Path: rules/macos/file_event/file_event_macos_susp_startup_item_created.yml

## Logsource

- category: file_event
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1037-boot_or_logon_initialization_scripts|T1037.005]]

## Detection

```yaml
selection:
  TargetFilename|startswith:
  - /Library/StartupItems/
  - /System/Library/StartupItems
  TargetFilename|endswith: .plist
condition: selection
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1037.005/T1037.005.md
- https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/StartupItems.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/file_event/file_event_macos_susp_startup_item_created.yml)
