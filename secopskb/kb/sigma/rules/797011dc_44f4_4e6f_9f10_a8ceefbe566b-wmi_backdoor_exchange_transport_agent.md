---
sigma_id: "797011dc-44f4-4e6f-9f10-a8ceefbe566b"
title: "WMI Backdoor Exchange Transport Agent"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmi_backdoor_exchange_transport_agent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmi_backdoor_exchange_transport_agent.yml"
build_date: "2026-04-27 19:13:59"
status: "test"
level: "critical"
logsource: "windows / process_creation"
aliases:
  - "797011dc-44f4-4e6f-9f10-a8ceefbe566b"
  - "WMI Backdoor Exchange Transport Agent"
attack_technique_ids:
  - "T1546.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a WMI backdoor in Exchange Transport Agents via WMI event filters

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution#^t1546003-windows-management-instrumentation-event-subscription|T1546.003: Windows Management Instrumentation Event Subscription]]

## Detection

```yaml
selection:
  ParentImage|endswith: \EdgeTransport.exe
filter_conhost:
  Image: C:\Windows\System32\conhost.exe
filter_oleconverter:
  Image|startswith: C:\Program Files\Microsoft\Exchange Server\
  Image|endswith: \Bin\OleConverter.exe
condition: selection and not 1 of filter_*
```

## False Positives

- Unknown

## References

- https://twitter.com/cglyer/status/1182389676876980224
- https://twitter.com/cglyer/status/1182391019633029120

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmi_backdoor_exchange_transport_agent.yml)
