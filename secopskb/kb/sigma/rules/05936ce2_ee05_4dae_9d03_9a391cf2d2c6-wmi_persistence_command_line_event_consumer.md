---
sigma_id: "05936ce2-ee05-4dae-9d03-9a391cf2d2c6"
title: "WMI Persistence - Command Line Event Consumer"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_wmi_persistence_commandline_event_consumer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_wmi_persistence_commandline_event_consumer.yml"
build_date: "2026-04-26 14:14:39"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "05936ce2-ee05-4dae-9d03-9a391cf2d2c6"
  - "WMI Persistence - Command Line Event Consumer"
attack_technique_ids:
  - "T1546.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# WMI Persistence - Command Line Event Consumer

Detects WMI command line event consumers

## Metadata

- Rule ID: 05936ce2-ee05-4dae-9d03-9a391cf2d2c6
- Status: test
- Level: high
- Author: Thomas Patzke
- Date: 2018-03-07
- Modified: 2021-11-27
- Source Path: rules/windows/image_load/image_load_wmi_persistence_commandline_event_consumer.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.003]]

## Detection

```yaml
selection:
  Image: C:\Windows\System32\wbem\WmiPrvSE.exe
  ImageLoaded|endswith: \wbemcons.dll
condition: selection
```

## False Positives

- Unknown (data set is too small; further testing needed)

## References

- https://www.eideon.com/2018-03-02-THL03-WMIBackdoors/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_wmi_persistence_commandline_event_consumer.yml)
