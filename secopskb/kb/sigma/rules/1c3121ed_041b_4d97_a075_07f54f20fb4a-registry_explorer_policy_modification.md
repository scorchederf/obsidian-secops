---
sigma_id: "1c3121ed-041b-4d97-a075-07f54f20fb4a"
title: "Registry Explorer Policy Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_set_nopolicies_user.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_set_nopolicies_user.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "1c3121ed-041b-4d97-a075-07f54f20fb4a"
  - "Registry Explorer Policy Modification"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Registry Explorer Policy Modification

Detects registry modifications that disable internal tools or functions in explorer (malware like Agent Tesla uses this technique)

## Metadata

- Rule ID: 1c3121ed-041b-4d97-a075-07f54f20fb4a
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-03-18
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_set_nopolicies_user.yml

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
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\NoLogOff
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\NoDesktop
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\NoRun
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\NoFind
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\NoControlPanel
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\NoFileMenu
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\NoClose
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\NoSetTaskbar
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\NoPropertiesMyDocuments
  - SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\NoTrayContextMenu
  Details: DWORD (0x00000001)
condition: selection_set_1
```

## False Positives

- Legitimate admin script

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1112/T1112.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_set_nopolicies_user.yml)
