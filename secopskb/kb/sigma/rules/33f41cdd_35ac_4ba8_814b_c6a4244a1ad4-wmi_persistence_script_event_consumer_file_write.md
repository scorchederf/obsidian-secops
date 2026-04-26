---
sigma_id: "33f41cdd-35ac-4ba8-814b-c6a4244a1ad4"
title: "WMI Persistence - Script Event Consumer File Write"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_wmi_persistence_script_event_consumer_write.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_wmi_persistence_script_event_consumer_write.yml"
build_date: "2026-04-26 15:01:54"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "33f41cdd-35ac-4ba8-814b-c6a4244a1ad4"
  - "WMI Persistence - Script Event Consumer File Write"
attack_technique_ids:
  - "T1546.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WMI Persistence - Script Event Consumer File Write

Detects file writes of WMI script event consumer

## Metadata

- Rule ID: 33f41cdd-35ac-4ba8-814b-c6a4244a1ad4
- Status: test
- Level: high
- Author: Thomas Patzke
- Date: 2018-03-07
- Modified: 2021-11-27
- Source Path: rules/windows/file/file_event/file_event_win_wmi_persistence_script_event_consumer_write.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.003]]

## Detection

```yaml
selection:
  Image: C:\WINDOWS\system32\wbem\scrcons.exe
condition: selection
```

## False Positives

- Dell Power Manager (C:\Program Files\Dell\PowerManager\DpmPowerPlanSetup.exe)

## References

- https://www.eideon.com/2018-03-02-THL03-WMIBackdoors/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_wmi_persistence_script_event_consumer_write.yml)
