---
sigma_id: "4916a35e-bfc4-47d0-8e25-a003d7067061"
title: "Sysmon Driver Altitude Change"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_change_sysmon_driver_altitude.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_change_sysmon_driver_altitude.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "4916a35e-bfc4-47d0-8e25-a003d7067061"
  - "Sysmon Driver Altitude Change"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects changes in Sysmon driver altitude value.
If the Sysmon driver is configured to load at an altitude of another registered service, it will fail to load at boot.

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Detection

```yaml
selection:
  TargetObject|contains: \Services\
  TargetObject|endswith: \Instances\Sysmon Instance\Altitude
condition: selection
```

## False Positives

- Legitimate driver altitude change to hide sysmon

## References

- https://posts.specterops.io/shhmon-silencing-sysmon-via-driver-unload-682b5be57650
- https://youtu.be/zSihR3lTf7g

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_change_sysmon_driver_altitude.yml)
