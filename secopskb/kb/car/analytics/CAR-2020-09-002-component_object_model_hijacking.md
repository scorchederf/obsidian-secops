---
car_id: "CAR-2020-09-002"
title: "Component Object Model Hijacking"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2020-09-002/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-09-002.yaml"
build_date: "2026-04-27 19:03:49"
aliases:
  - "CAR-2020-09-002"
  - "Component Object Model Hijacking"
attack_technique_ids:
  - "T1546"
  - "T1546.015"
platforms:
  - "Windows"
implementation_types:
  - "Pseudocode"
  - "Splunk"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Adversaries may establish persistence or escalate privileges by executing malicious content triggered by hijacked references to Component Object Model (COM) objects. This is typically done by replacing COM object registry entries under the HKEY_CURRENT_USER\Software\Classes\CLSID or HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID keys. Accordingly, this analytic looks for any changes under these keys.

## ATT&CK Coverage

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546: Event Triggered Execution]] (coverage: Moderate; tactics: TA0003, TA0004)
  - [[kb/attack/techniques/T1546-event_triggered_execution#^t1546015-component-object-model-hijacking|T1546.015: Component Object Model Hijacking]]

## Implementations

### Pseudocode

This is a pseudocode representation of the below splunk search.

- Data Model: CAR native

```pseudocode
registry_keys = search (Registry:Create AND Registry:Remove AND Registry:Edit)
clsid_keys = filter registry_keys where (
  key = "*\Software\Classes\CLSID\*")
output clsid_keys
```

### Splunk

This Splunk search looks for any registry keys that were created, deleted, or renamed, as well as any registry values that were set or renamed under the Windows COM Object registry key.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_index__ (EventCode=12 OR EventCode=13 OR EventCode=14) TargetObject="*\\Software\\Classes\\CLSID\\*"
```

### LogPoint

This LogPoint search looks for any registry keys that were created, deleted, or renamed, as well as any registry values that were set or renamed under the Windows COM Object registry key.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id IN [12, 13, 14] target_object="*\Software\Classes\CLSID\*"
```

## Data Model References

- registry/add/key
- registry/remove/key
- registry/edit/key

## D3FEND Mappings

- [[kb/defend/techniques/D3-SICA-system_init_config_analysis|D3-SICA: System Init Config Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2020-09-002/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-09-002.yaml)
