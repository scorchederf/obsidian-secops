---
sigma_id: "91c49341-e2ef-40c0-ac45-49ec5c3fe26c"
title: "RTCore Suspicious Service Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_susp_rtcore64_service_install.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_susp_rtcore64_service_install.yml"
build_date: "2026-04-26 15:01:50"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "91c49341-e2ef-40c0-ac45-49ec5c3fe26c"
  - "RTCore Suspicious Service Installation"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# RTCore Suspicious Service Installation

Detects the installation of RTCore service. Which could be an indication of Micro-Star MSI Afterburner vulnerable driver abuse

## Metadata

- Rule ID: 91c49341-e2ef-40c0-ac45-49ec5c3fe26c
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-30
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_susp_rtcore64_service_install.yml

## Logsource

- product: windows
- service: system

## Detection

```yaml
selection:
  Provider_Name: Service Control Manager
  EventID: 7045
  ServiceName: RTCore64
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/br-sn/CheekyBlinder/blob/e1764a8a0e7cda8a3716aefa35799f560686e01c/CheekyBlinder/CheekyBlinder.cpp

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_susp_rtcore64_service_install.yml)
