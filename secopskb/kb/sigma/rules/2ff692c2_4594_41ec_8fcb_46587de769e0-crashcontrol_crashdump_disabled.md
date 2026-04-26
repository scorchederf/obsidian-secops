---
sigma_id: "2ff692c2-4594-41ec-8fcb-46587de769e0"
title: "CrashControl CrashDump Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_crashdump_disabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_crashdump_disabled.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "2ff692c2-4594-41ec-8fcb-46587de769e0"
  - "CrashControl CrashDump Disabled"
attack_technique_ids:
  - "T1564"
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CrashControl CrashDump Disabled

Detects disabling the CrashDump per registry (as used by HermeticWiper)

## Metadata

- Rule ID: 2ff692c2-4594-41ec-8fcb-46587de769e0
- Status: test
- Level: medium
- Author: Tobias Michalski (Nextron Systems)
- Date: 2022-02-24
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_crashdump_disabled.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564]]
- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  TargetObject|contains: SYSTEM\CurrentControlSet\Control\CrashControl
  Details: DWORD (0x00000000)
condition: selection
```

## False Positives

- Legitimate disabling of crashdumps

## References

- https://www.sentinelone.com/labs/hermetic-wiper-ukraine-under-attack/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_crashdump_disabled.yml)
