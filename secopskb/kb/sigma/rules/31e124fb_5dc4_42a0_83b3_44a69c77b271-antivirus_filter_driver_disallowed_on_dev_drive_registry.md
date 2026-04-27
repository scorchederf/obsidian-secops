---
sigma_id: "31e124fb-5dc4-42a0-83b3-44a69c77b271"
title: "Antivirus Filter Driver Disallowed On Dev Drive - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_devdrv_disallow_antivirus_filter.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_devdrv_disallow_antivirus_filter.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "31e124fb-5dc4-42a0-83b3-44a69c77b271"
  - "Antivirus Filter Driver Disallowed On Dev Drive - Registry"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects activity that indicates a user disabling the ability for Antivirus mini filter to inspect a "Dev Drive".

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Detection

```yaml
selection:
  TargetObject|endswith: \FilterManager\FltmgrDevDriveAllowAntivirusFilter
  Details: DWORD (0x00000000)
condition: selection
```

## False Positives

- Unlikely

## References

- https://twitter.com/0gtweet/status/1720419490519752955

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_devdrv_disallow_antivirus_filter.yml)
