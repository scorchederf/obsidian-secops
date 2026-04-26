---
sigma_id: "df4dc653-1029-47ba-8231-3c44238cc0ae"
title: "Potential Persistence Using DebugPath"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_appx_debugger.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_appx_debugger.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "df4dc653-1029-47ba-8231-3c44238cc0ae"
  - "Potential Persistence Using DebugPath"
attack_technique_ids:
  - "T1546.015"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Persistence Using DebugPath

Detects potential persistence using Appx DebugPath

## Metadata

- Rule ID: df4dc653-1029-47ba-8231-3c44238cc0ae
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-07-27
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_appx_debugger.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.015]]

## Detection

```yaml
selection_debug:
  TargetObject|contains: Classes\ActivatableClasses\Package\Microsoft.
  TargetObject|endswith: \DebugPath
selection_default:
  TargetObject|contains: \Software\Microsoft\Windows\CurrentVersion\PackagedAppXDebug\Microsoft.
  TargetObject|endswith: \(Default)
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://oddvar.moe/2018/09/06/persistence-using-universal-windows-platform-apps-appx/
- https://github.com/rootm0s/WinPwnage

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_appx_debugger.yml)
