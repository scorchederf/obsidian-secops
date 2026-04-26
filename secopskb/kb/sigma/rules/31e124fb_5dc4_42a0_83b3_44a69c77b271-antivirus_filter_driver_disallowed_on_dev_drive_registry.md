---
sigma_id: "31e124fb-5dc4-42a0-83b3-44a69c77b271"
title: "Antivirus Filter Driver Disallowed On Dev Drive - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_devdrv_disallow_antivirus_filter.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_devdrv_disallow_antivirus_filter.yml"
build_date: "2026-04-26 15:01:43"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Antivirus Filter Driver Disallowed On Dev Drive - Registry

Detects activity that indicates a user disabling the ability for Antivirus mini filter to inspect a "Dev Drive".

## Metadata

- Rule ID: 31e124fb-5dc4-42a0-83b3-44a69c77b271
- Status: test
- Level: high
- Author: @kostastsale, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-11-05
- Modified: 2024-08-16
- Source Path: rules/windows/registry/registry_set/registry_set_devdrv_disallow_antivirus_filter.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

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
