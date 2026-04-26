---
sigma_id: "fe20dda1-6f37-4379-bbe0-a98d400cae90"
title: "Potential Persistence Via Scrobj.dll COM Hijacking"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_scrobj_dll.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_scrobj_dll.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "fe20dda1-6f37-4379-bbe0-a98d400cae90"
  - "Potential Persistence Via Scrobj.dll COM Hijacking"
attack_technique_ids:
  - "T1546.015"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Persistence Via Scrobj.dll COM Hijacking

Detect use of scrobj.dll as this DLL looks for the ScriptletURL key to get the location of the script to execute

## Metadata

- Rule ID: fe20dda1-6f37-4379-bbe0-a98d400cae90
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-08-20
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_scrobj_dll.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.015]]

## Detection

```yaml
selection:
  TargetObject|endswith: InprocServer32\(Default)
  Details: C:\WINDOWS\system32\scrobj.dll
condition: selection
```

## False Positives

- Legitimate use of the dll.

## References

- https://github.com/redcanaryco/atomic-red-team/blob/40b77d63808dd4f4eafb83949805636735a1fd15/atomics/T1546.015/T1546.015.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_scrobj_dll.yml)
