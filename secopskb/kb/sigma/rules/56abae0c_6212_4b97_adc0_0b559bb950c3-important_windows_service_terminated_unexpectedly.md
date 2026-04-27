---
sigma_id: "56abae0c-6212-4b97-adc0-0b559bb950c3"
title: "Important Windows Service Terminated Unexpectedly"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_service_terminated_unexpectedly.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_terminated_unexpectedly.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "56abae0c-6212-4b97-adc0-0b559bb950c3"
  - "Important Windows Service Terminated Unexpectedly"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Important Windows Service Terminated Unexpectedly

Detects important or interesting Windows services that got terminated unexpectedly.

## Metadata

- Rule ID: 56abae0c-6212-4b97-adc0-0b559bb950c3
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-04-14
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_service_terminated_unexpectedly.yml

## Logsource

- product: windows
- service: system

## Detection

```yaml
selection_eid:
  Provider_Name: Service Control Manager
  EventID: 7034
selection_name:
- param1|contains: Message Queuing
- Binary|contains:
  - 4d0053004d005100
  - 6d0073006d007100
condition: all of selection_*
```

## False Positives

- Rare false positives could occur since service termination could happen due to multiple reasons

## References

- https://www.randori.com/blog/vulnerability-analysis-queuejumper-cve-2023-21554/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_terminated_unexpectedly.yml)
