---
sigma_id: "9b0f8a61-91b2-464f-aceb-0527e0a45020"
title: "Potential COM Object Hijacking Via TreatAs Subkey - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_com_key_linking.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_com_key_linking.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "9b0f8a61-91b2-464f-aceb-0527e0a45020"
  - "Potential COM Object Hijacking Via TreatAs Subkey - Registry"
attack_technique_ids:
  - "T1546.015"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential COM Object Hijacking Via TreatAs Subkey - Registry

Detects COM object hijacking via TreatAs subkey

## Metadata

- Rule ID: 9b0f8a61-91b2-464f-aceb-0527e0a45020
- Status: test
- Level: medium
- Author: Kutepov Anton, oscd.community
- Date: 2019-10-23
- Modified: 2025-10-26
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_com_key_linking.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.015]]

## Detection

```yaml
selection:
  TargetObject|contains|all:
  - HKU\
  - Classes\CLSID\
  - \TreatAs
filter_main_svchost:
  Image: C:\WINDOWS\system32\svchost.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Maybe some system utilities in rare cases use linking keys for backward compatibility

## Simulation

### COM hijacking via TreatAs

- atomic_guid: 33eacead-f117-4863-8eb0-5c6304fbfaa9
- name: COM hijacking via TreatAs
- technique: T1546.015
- type: atomic-red-team

## References

- https://bohops.com/2018/08/18/abusing-the-com-registry-structure-part-2-loading-techniques-for-evasion-and-persistence/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_com_key_linking.yml)
