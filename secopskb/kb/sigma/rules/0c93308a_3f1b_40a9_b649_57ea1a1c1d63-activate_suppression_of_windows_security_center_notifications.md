---
sigma_id: "0c93308a-3f1b-40a9-b649-57ea1a1c1d63"
title: "Activate Suppression of Windows Security Center Notifications"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_suppress_defender_notifications.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_suppress_defender_notifications.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "0c93308a-3f1b-40a9-b649-57ea1a1c1d63"
  - "Activate Suppression of Windows Security Center Notifications"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Activate Suppression of Windows Security Center Notifications

Detect set Notification_Suppress to 1 to disable the Windows security center notification

## Metadata

- Rule ID: 0c93308a-3f1b-40a9-b649-57ea1a1c1d63
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-08-19
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_suppress_defender_notifications.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  TargetObject|endswith: SOFTWARE\Policies\Microsoft\Windows Defender\UX Configuration\Notification_Suppress
  Details: DWORD (0x00000001)
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/40b77d63808dd4f4eafb83949805636735a1fd15/atomics/T1112/T1112.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_suppress_defender_notifications.yml)
