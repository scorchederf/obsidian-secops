---
sigma_id: "3ae1a046-f7db-439d-b7ce-b8b366b81fa6"
title: "Disable Windows Security Center Notifications"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_disable_security_center_notifications.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_security_center_notifications.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "3ae1a046-f7db-439d-b7ce-b8b366b81fa6"
  - "Disable Windows Security Center Notifications"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Disable Windows Security Center Notifications

Detect set UseActionCenterExperience to 0 to disable the Windows security center notification

## Metadata

- Rule ID: 3ae1a046-f7db-439d-b7ce-b8b366b81fa6
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-08-19
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_disable_security_center_notifications.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  TargetObject|endswith: Windows\CurrentVersion\ImmersiveShell\UseActionCenterExperience
  Details: DWORD (0x00000000)
condition: selection
```

## False Positives

- Unknown

## Simulation

### Disable Windows Security Center Notifications

- atomic_guid: 45914594-8df6-4ea9-b3cc-7eb9321a807e
- name: Disable Windows Security Center Notifications
- technique: T1112
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/40b77d63808dd4f4eafb83949805636735a1fd15/atomics/T1112/T1112.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_security_center_notifications.yml)
