---
sigma_id: "39f919f3-980b-4e6f-a975-8af7e507ef2b"
title: "Critical Hive In Suspicious Location Access Bits Cleared"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/microsoft_windows_kernel_general/win_system_susp_critical_hive_location_access_bits_cleared.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_kernel_general/win_system_susp_critical_hive_location_access_bits_cleared.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "39f919f3-980b-4e6f-a975-8af7e507ef2b"
  - "Critical Hive In Suspicious Location Access Bits Cleared"
attack_technique_ids:
  - "T1003.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Critical Hive In Suspicious Location Access Bits Cleared

Detects events from the Kernel-General ETW indicating that the access bits of a hive with a system like hive name located in the temp directory have been reset.
This occurs when an application tries to access a hive and the hive has not be recognized since the last 7 days (by default).
Registry hive dumping utilities such as QuarksPwDump were seen emitting this behavior.

## Metadata

- Rule ID: 39f919f3-980b-4e6f-a975-8af7e507ef2b
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2017-05-15
- Modified: 2024-01-18
- Source Path: rules/windows/builtin/system/microsoft_windows_kernel_general/win_system_susp_critical_hive_location_access_bits_cleared.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]

## Detection

```yaml
selection:
  EventID: 16
  Provider_Name: Microsoft-Windows-Kernel-General
  HiveName|contains:
  - \Temp\SAM
  - \Temp\SECURITY
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/nasbench/Misc-Research/blob/b20da2336de0f342d31ef4794959d28c8d3ba5ba/ETW/Microsoft-Windows-Kernel-General.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_kernel_general/win_system_susp_critical_hive_location_access_bits_cleared.yml)
