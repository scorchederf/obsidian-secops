---
sigma_id: "4d431012-2ab5-4db7-a84e-b29809da2172"
title: "Enable Remote Connection Between Anonymous Computer - AllowAnonymousCallback"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_set_enable_anonymous_connection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_set_enable_anonymous_connection.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "4d431012-2ab5-4db7-a84e-b29809da2172"
  - "Enable Remote Connection Between Anonymous Computer - AllowAnonymousCallback"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Enable Remote Connection Between Anonymous Computer - AllowAnonymousCallback

Detects enabling of the "AllowAnonymousCallback" registry value, which allows a remote connection between computers that do not have a trust relationship.

## Metadata

- Rule ID: 4d431012-2ab5-4db7-a84e-b29809da2172
- Status: test
- Level: medium
- Author: X__Junior (Nextron Systems)
- Date: 2023-11-03
- Source Path: rules/windows/registry/registry_event/registry_set_enable_anonymous_connection.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  TargetObject|contains: \Microsoft\WBEM\CIMOM\AllowAnonymousCallback
  Details: DWORD (0x00000001)
condition: selection
```

## False Positives

- Administrative activity

## References

- https://learn.microsoft.com/en-us/windows/win32/wmisdk/connecting-to-wmi-remotely-starting-with-vista

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_set_enable_anonymous_connection.yml)
