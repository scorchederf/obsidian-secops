---
sigma_id: "ec1d5e28-8f3b-4188-a6f8-6e8df81dc28e"
title: "WMI Persistence - Script Event Consumer"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmi_persistence_script_event_consumer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmi_persistence_script_event_consumer.yml"
build_date: "2026-04-26 14:14:39"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "ec1d5e28-8f3b-4188-a6f8-6e8df81dc28e"
  - "WMI Persistence - Script Event Consumer"
attack_technique_ids:
  - "T1546.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# WMI Persistence - Script Event Consumer

Detects WMI script event consumers

## Metadata

- Rule ID: ec1d5e28-8f3b-4188-a6f8-6e8df81dc28e
- Status: test
- Level: medium
- Author: Thomas Patzke
- Date: 2018-03-07
- Modified: 2022-10-11
- Source Path: rules/windows/process_creation/proc_creation_win_wmi_persistence_script_event_consumer.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.003]]

## Detection

```yaml
selection:
  Image: C:\WINDOWS\system32\wbem\scrcons.exe
  ParentImage: C:\Windows\System32\svchost.exe
condition: selection
```

## False Positives

- Legitimate event consumers
- Dell computers on some versions register an event consumer that is known to cause false positives when brightness is changed by the corresponding keyboard button

## References

- https://www.eideon.com/2018-03-02-THL03-WMIBackdoors/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmi_persistence_script_event_consumer.yml)
