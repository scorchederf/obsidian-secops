---
sigma_id: "67a6c006-3fbe-46a7-9074-2ba3b82c3000"
title: "Path To Screensaver Binary Modified"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_modify_screensaver_binary_path.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_modify_screensaver_binary_path.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / registry_event"
aliases:
  - "67a6c006-3fbe-46a7-9074-2ba3b82c3000"
  - "Path To Screensaver Binary Modified"
attack_technique_ids:
  - "T1546.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Path To Screensaver Binary Modified

Detects value modification of registry key containing path to binary used as screensaver.

## Metadata

- Rule ID: 67a6c006-3fbe-46a7-9074-2ba3b82c3000
- Status: test
- Level: medium
- Author: Bartlomiej Czyz @bczyz1, oscd.community
- Date: 2020-10-11
- Modified: 2021-11-27
- Source Path: rules/windows/registry/registry_event/registry_event_modify_screensaver_binary_path.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.002]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Control Panel\Desktop\SCRNSAVE.EXE
filter:
  Image|endswith:
  - \rundll32.exe
  - \explorer.exe
condition: selection and not filter
```

## False Positives

- Legitimate modification of screensaver

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1546.002/T1546.002.md
- https://www.welivesecurity.com/wp-content/uploads/2017/08/eset-gazer.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_modify_screensaver_binary_path.yml)
