---
sigma_id: "b86852fb-4c77-48f9-8519-eb1b2c308b59"
title: "Potential Persistence Via AppCompat RegisterAppRestart Layer"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_app_cpmpat_layer_registerapprestart.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_app_cpmpat_layer_registerapprestart.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "b86852fb-4c77-48f9-8519-eb1b2c308b59"
  - "Potential Persistence Via AppCompat RegisterAppRestart Layer"
attack_technique_ids:
  - "T1546.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Persistence Via AppCompat RegisterAppRestart Layer

Detects the setting of the REGISTERAPPRESTART compatibility layer on an application.
This compatibility layer allows an application to register for restart using the "RegisterApplicationRestart" API.
This can be potentially abused as a persistence mechanism.

## Metadata

- Rule ID: b86852fb-4c77-48f9-8519-eb1b2c308b59
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2024-01-01
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_app_cpmpat_layer_registerapprestart.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.011]]

## Detection

```yaml
selection:
  TargetObject|contains: \SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers\
  Details|contains: REGISTERAPPRESTART
condition: selection
```

## False Positives

- Legitimate applications making use of this feature for compatibility reasons

## References

- https://github.com/nasbench/Misc-Research/blob/d114d6a5e0a437d3818e492ef9864367152543e7/Other/Persistence-Via-RegisterAppRestart-Shim.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_app_cpmpat_layer_registerapprestart.yml)
