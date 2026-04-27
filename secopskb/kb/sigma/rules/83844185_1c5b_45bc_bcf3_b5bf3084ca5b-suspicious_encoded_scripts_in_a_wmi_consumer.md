---
sigma_id: "83844185-1c5b-45bc-bcf3-b5bf3084ca5b"
title: "Suspicious Encoded Scripts in a WMI Consumer"
framework: "sigma"
generated: "true"
source_path: "rules/windows/wmi_event/sysmon_wmi_susp_encoded_scripts.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/wmi_event/sysmon_wmi_susp_encoded_scripts.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / wmi_event"
aliases:
  - "83844185-1c5b-45bc-bcf3-b5bf3084ca5b"
  - "Suspicious Encoded Scripts in a WMI Consumer"
attack_technique_ids:
  - "T1047"
  - "T1546.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Encoded Scripts in a WMI Consumer

Detects suspicious encoded payloads in WMI Event Consumers

## Metadata

- Rule ID: 83844185-1c5b-45bc-bcf3-b5bf3084ca5b
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-09-01
- Modified: 2022-10-09
- Source Path: rules/windows/wmi_event/sysmon_wmi_susp_encoded_scripts.yml

## Logsource

- category: wmi_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]
- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.003]]

## Detection

```yaml
selection_destination:
  Destination|base64offset|contains:
  - WriteProcessMemory
  - This program cannot be run in DOS mode
  - This program must be run under Win32
condition: selection_destination
```

## False Positives

- Unknown

## References

- https://github.com/RiccardoAncarani/LiquidSnake

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/wmi_event/sysmon_wmi_susp_encoded_scripts.yml)
