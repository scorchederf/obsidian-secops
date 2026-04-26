---
sigma_id: "5a93eb65-dffa-4543-b761-94aa60098fb6"
title: "Registry Hide Function from User"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_hide_function_user.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_hide_function_user.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "5a93eb65-dffa-4543-b761-94aa60098fb6"
  - "Registry Hide Function from User"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Registry Hide Function from User

Detects registry modifications that hide internal tools or functions from the user (malware like Agent Tesla, Hermetic Wiper uses this technique)

## Metadata

- Rule ID: 5a93eb65-dffa-4543-b761-94aa60098fb6
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-03-18
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_hide_function_user.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection_set_1:
  TargetObject|endswith:
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\HideClock
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\HideSCAHealth
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\HideSCANetwork
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\HideSCAPower
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\HideSCAVolume
  Details: DWORD (0x00000001)
selection_set_0:
  TargetObject|endswith:
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced\ShowInfoTip
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced\ShowCompColor
  Details: DWORD (0x00000000)
condition: 1 of selection_set_*
```

## False Positives

- Legitimate admin script

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1564.001/T1564.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_hide_function_user.yml)
