---
sigma_id: "acfa2210-0d71-4eeb-b477-afab494d596c"
title: "Windows Service Terminated With Error"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_service_terminated_error_generic.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_terminated_error_generic.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "low"
logsource: "windows / system"
aliases:
  - "acfa2210-0d71-4eeb-b477-afab494d596c"
  - "Windows Service Terminated With Error"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Service Terminated With Error

Detects Windows services that got terminated for whatever reason

## Metadata

- Rule ID: acfa2210-0d71-4eeb-b477-afab494d596c
- Status: test
- Level: low
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-04-14
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_service_terminated_error_generic.yml

## Logsource

- product: windows
- service: system

## Detection

```yaml
selection:
  Provider_Name: Service Control Manager
  EventID: 7023
condition: selection
```

## False Positives

- False positives could occur since service termination could happen due to multiple reasons

## References

- https://www.microsoft.com/en-us/security/blog/2023/04/11/guidance-for-investigating-attacks-using-cve-2022-21894-the-blacklotus-campaign/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_terminated_error_generic.yml)
