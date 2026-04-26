---
sigma_id: "f69a87ea-955e-4fb4-adb2-bb9fd6685632"
title: "External Disk Drive Or USB Storage Device Was Recognized By The System"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_external_device.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_external_device.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "low"
logsource: "windows / security"
aliases:
  - "f69a87ea-955e-4fb4-adb2-bb9fd6685632"
  - "External Disk Drive Or USB Storage Device Was Recognized By The System"
attack_technique_ids:
  - "T1091"
  - "T1200"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# External Disk Drive Or USB Storage Device Was Recognized By The System

Detects external disk drives or plugged-in USB devices.

## Metadata

- Rule ID: f69a87ea-955e-4fb4-adb2-bb9fd6685632
- Status: test
- Level: low
- Author: Keith Wright
- Date: 2019-11-20
- Modified: 2024-02-09
- Source Path: rules/windows/builtin/security/win_security_external_device.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1091-replication_through_removable_media|T1091]]
- [[kb/attack/techniques/T1200-hardware_additions|T1200]]

## Detection

```yaml
selection_eid:
  EventID: 6416
selection_field:
- ClassName: DiskDrive
- DeviceDescription: USB Mass Storage Device
condition: all of selection_*
```

## False Positives

- Likely

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-6416

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_external_device.yml)
