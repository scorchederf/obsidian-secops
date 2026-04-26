---
sigma_id: "919f2ef0-be2d-4a7a-b635-eb2b41fde044"
title: "Disable Security Events Logging Adding Reg Key MiniNt"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_disable_security_events_logging_adding_reg_key_minint.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_disable_security_events_logging_adding_reg_key_minint.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / registry_event"
aliases:
  - "919f2ef0-be2d-4a7a-b635-eb2b41fde044"
  - "Disable Security Events Logging Adding Reg Key MiniNt"
attack_technique_ids:
  - "T1562.002"
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable Security Events Logging Adding Reg Key MiniNt

Detects the addition of a key 'MiniNt' to the registry. Upon a reboot, Windows Event Log service will stop writing events.

## Metadata

- Rule ID: 919f2ef0-be2d-4a7a-b635-eb2b41fde044
- Status: test
- Level: high
- Author: Ilyas Ochkov, oscd.community
- Date: 2019-10-25
- Modified: 2021-11-27
- Source Path: rules/windows/registry/registry_event/registry_event_disable_security_events_logging_adding_reg_key_minint.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.002]]
- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
- TargetObject: HKLM\SYSTEM\CurrentControlSet\Control\MiniNt
  EventType: CreateKey
- NewName: HKLM\SYSTEM\CurrentControlSet\Control\MiniNt
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/0gtweet/status/1182516740955226112
- https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_disable_security_events_logging_adding_reg_key_minint.yml)
