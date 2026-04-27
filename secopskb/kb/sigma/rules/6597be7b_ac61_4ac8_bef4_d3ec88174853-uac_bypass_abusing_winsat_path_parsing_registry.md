---
sigma_id: "6597be7b-ac61-4ac8-bef4-d3ec88174853"
title: "UAC Bypass Abusing Winsat Path Parsing - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_uac_bypass_winsat.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_uac_bypass_winsat.yml"
build_date: "2026-04-27 19:13:58"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the pattern of UAC Bypass using a path parsing issue in winsat.exe (UACMe 52)

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]

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
