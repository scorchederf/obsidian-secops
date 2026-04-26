---
sigma_id: "6597be7b-ac61-4ac8-bef4-d3ec88174853"
title: "UAC Bypass Abusing Winsat Path Parsing - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_uac_bypass_winsat.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_uac_bypass_winsat.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "6597be7b-ac61-4ac8-bef4-d3ec88174853"
  - "UAC Bypass Abusing Winsat Path Parsing - Registry"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# UAC Bypass Abusing Winsat Path Parsing - Registry

Detects the pattern of UAC Bypass using a path parsing issue in winsat.exe (UACMe 52)

## Metadata

- Rule ID: 6597be7b-ac61-4ac8-bef4-d3ec88174853
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-08-30
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_uac_bypass_winsat.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  TargetObject|contains: \Root\InventoryApplicationFile\winsat.exe|
  TargetObject|endswith: \LowerCaseLongPath
  Details|startswith: c:\users\
  Details|endswith: \appdata\local\temp\system32\winsat.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/hfiref0x/UACME

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_uac_bypass_winsat.yml)
