---
sigma_id: "0cf2e1c6-8d10-4273-8059-738778f981ad"
title: "Potential WerFault ReflectDebugger Registry Value Abuse"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_reflectdebugger.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_reflectdebugger.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "0cf2e1c6-8d10-4273-8059-738778f981ad"
  - "Potential WerFault ReflectDebugger Registry Value Abuse"
attack_technique_ids:
  - "T1036.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects potential WerFault "ReflectDebugger" registry value abuse for persistence.

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading#^t1036003-rename-legitimate-utilities|T1036.003: Rename Legitimate Utilities]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Microsoft\Windows\Windows Error Reporting\Hangs\ReflectDebugger
condition: selection
```

## False Positives

- Unknown

## References

- https://cocomelonc.github.io/malware/2022/11/02/malware-pers-18.html
- https://www.hexacorn.com/blog/2018/08/31/beyond-good-ol-run-key-part-85/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_reflectdebugger.yml)
