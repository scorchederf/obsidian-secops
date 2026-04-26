---
sigma_id: "f10ed525-97fe-4fed-be7c-2feecca941b1"
title: "Persistence Via Hhctrl.ocx"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_hhctrl_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_hhctrl_persistence.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "f10ed525-97fe-4fed-be7c-2feecca941b1"
  - "Persistence Via Hhctrl.ocx"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Persistence Via Hhctrl.ocx

Detects when an attacker modifies the registry value of the "hhctrl" to point to a custom binary

## Metadata

- Rule ID: f10ed525-97fe-4fed-be7c-2feecca941b1
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-21
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_hhctrl_persistence.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection:
  TargetObject|contains: \CLSID\{52A2AAAE-085D-4187-97EA-8C30DB990436}\InprocServer32\(Default)
filter:
  Details: C:\Windows\System32\hhctrl.ocx
condition: selection and not filter
```

## False Positives

- Unlikely

## References

- https://persistence-info.github.io/Data/hhctrl.html
- https://www.hexacorn.com/blog/2018/04/23/beyond-good-ol-run-key-part-77/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_hhctrl_persistence.yml)
