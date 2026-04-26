---
sigma_id: "f033f3f3-fd24-4995-97d8-a3bb17550a88"
title: "WMI Persistence - Security"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_wmi_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_wmi_persistence.yml"
build_date: "2026-04-26 14:14:39"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "f033f3f3-fd24-4995-97d8-a3bb17550a88"
  - "WMI Persistence - Security"
attack_technique_ids:
  - "T1546.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# WMI Persistence - Security

Detects suspicious WMI event filter and command line event consumer based on WMI and Security Logs.

## Metadata

- Rule ID: f033f3f3-fd24-4995-97d8-a3bb17550a88
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Gleb Sukhodolskiy, Timur Zinniatullin oscd.community
- Date: 2017-08-22
- Modified: 2022-11-29
- Source Path: rules/windows/builtin/security/win_security_wmi_persistence.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.003]]

## Detection

```yaml
selection:
  EventID: 4662
  ObjectType: WMI Namespace
  ObjectName|contains: subscription
condition: selection
```

## False Positives

- Unknown (data set is too small; further testing needed)

## References

- https://twitter.com/mattifestation/status/899646620148539397
- https://www.eideon.com/2018-03-02-THL03-WMIBackdoors/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_wmi_persistence.yml)
