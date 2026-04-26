---
sigma_id: "1a4bd6e3-4c6e-405d-a9a3-53a116e341d4"
title: "USB Device Plugged"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/driverframeworks/win_usb_device_plugged.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/driverframeworks/win_usb_device_plugged.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "low"
logsource: "windows / driver-framework"
aliases:
  - "1a4bd6e3-4c6e-405d-a9a3-53a116e341d4"
  - "USB Device Plugged"
attack_technique_ids:
  - "T1200"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# USB Device Plugged

Detects plugged/unplugged USB devices

## Metadata

- Rule ID: 1a4bd6e3-4c6e-405d-a9a3-53a116e341d4
- Status: test
- Level: low
- Author: Florian Roth (Nextron Systems)
- Date: 2017-11-09
- Modified: 2021-11-30
- Source Path: rules/windows/builtin/driverframeworks/win_usb_device_plugged.yml

## Logsource

- definition: Requires enabling and collection of the Microsoft-Windows-DriverFrameworks-UserMode/Operational eventlog
- product: windows
- service: driver-framework

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1200-hardware_additions|T1200]]

## Detection

```yaml
selection:
  EventID:
  - 2003
  - 2100
  - 2102
condition: selection
```

## False Positives

- Legitimate administrative activity

## References

- https://df-stream.com/2014/01/the-windows-7-event-log-and-usb-device/
- https://www.techrepublic.com/article/how-to-track-down-usb-flash-drive-usage-in-windows-10s-event-viewer/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/driverframeworks/win_usb_device_plugged.yml)
