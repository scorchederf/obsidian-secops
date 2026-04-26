---
sigma_id: "0f06a3a5-6a09-413f-8743-e6cf35561297"
title: "WMI Event Subscription"
framework: "sigma"
generated: "true"
source_path: "rules/windows/wmi_event/sysmon_wmi_event_subscription.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/wmi_event/sysmon_wmi_event_subscription.yml"
build_date: "2026-04-26 14:14:39"
status: "test"
level: "medium"
logsource: "windows / wmi_event"
aliases:
  - "0f06a3a5-6a09-413f-8743-e6cf35561297"
  - "WMI Event Subscription"
attack_technique_ids:
  - "T1546.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# WMI Event Subscription

Detects creation of WMI event subscription persistence method

## Metadata

- Rule ID: 0f06a3a5-6a09-413f-8743-e6cf35561297
- Status: test
- Level: medium
- Author: Tom Ueltschi (@c_APT_ure)
- Date: 2019-01-12
- Modified: 2021-11-27
- Source Path: rules/windows/wmi_event/sysmon_wmi_event_subscription.yml

## Logsource

- category: wmi_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.003]]

## Detection

```yaml
selection:
  EventID:
  - 19
  - 20
  - 21
condition: selection
```

## False Positives

- Exclude legitimate (vetted) use of WMI event subscription in your network

## References

- https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-19-wmievent-wmieventfilter-activity-detected
- https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-20-wmievent-wmieventconsumer-activity-detected
- https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-21-wmievent-wmieventconsumertofilter-activity-detected

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/wmi_event/sysmon_wmi_event_subscription.yml)
