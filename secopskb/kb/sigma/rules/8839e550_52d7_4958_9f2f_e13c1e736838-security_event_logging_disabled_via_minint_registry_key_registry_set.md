---
sigma_id: "8839e550-52d7-4958-9f2f-e13c1e736838"
title: "Security Event Logging Disabled via MiniNt Registry Key - Registry Set"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_create_minint_key.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_create_minint_key.yml"
build_date: "2026-04-27 19:13:56"
status: "experimental"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "8839e550-52d7-4958-9f2f-e13c1e736838"
  - "Security Event Logging Disabled via MiniNt Registry Key - Registry Set"
attack_technique_ids:
  - "T1562.002"
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the addition of the 'MiniNt' key to the registry. Upon a reboot, Windows Event Log service will stop writing events.
Windows Event Log is a service that collects and stores event logs from the operating system and applications. It is an important component of Windows security and auditing.
Adversary may want to disable this service to disable logging of security events which could be used to detect their activities.

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562002-disable-windows-event-logging|T1562.002: Disable Windows Event Logging]]
- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]]

## Detection

```yaml
selection:
  TargetObject: HKLM\System\CurrentControlSet\Control\MiniNt\(Default)
condition: selection
```

## False Positives

- Highly Unlikely

## References

- https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_create_minint_key.yml)
