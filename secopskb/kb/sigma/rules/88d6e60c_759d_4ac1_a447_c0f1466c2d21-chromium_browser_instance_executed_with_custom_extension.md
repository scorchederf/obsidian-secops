---
sigma_id: "88d6e60c-759d-4ac1-a447-c0f1466c2d21"
title: "Chromium Browser Instance Executed With Custom Extension"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_browsers_chromium_load_extension.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_browsers_chromium_load_extension.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "88d6e60c-759d-4ac1-a447-c0f1466c2d21"
  - "Chromium Browser Instance Executed With Custom Extension"
attack_technique_ids:
  - "T1176.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Chromium Browser Instance Executed With Custom Extension

Detects a Chromium based browser process with the 'load-extension' flag to start a instance with a custom extension

## Metadata

- Rule ID: 88d6e60c-759d-4ac1-a447-c0f1466c2d21
- Status: test
- Level: medium
- Author: Aedan Russell, frack113, X__Junior (Nextron Systems)
- Date: 2022-06-19
- Modified: 2023-11-28
- Source Path: rules/windows/process_creation/proc_creation_win_browsers_chromium_load_extension.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1176-software_extensions|T1176.001]]

## Detection

```yaml
selection:
  Image|endswith:
  - \brave.exe
  - \chrome.exe
  - \msedge.exe
  - \opera.exe
  - \vivaldi.exe
  CommandLine|contains: --load-extension=
condition: selection
```

## False Positives

- Usage of Chrome Extensions in testing tools such as BurpSuite will trigger this alert

## References

- https://redcanary.com/blog/chromeloader/
- https://emkc.org/s/RJjuLa
- https://www.mandiant.com/resources/blog/lnk-between-browsers

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_browsers_chromium_load_extension.yml)
