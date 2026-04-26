---
sigma_id: "5f9db380-ea57-4d1e-beab-8a2d33397e93"
title: "UAC Bypass Using Windows Media Player - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_uac_bypass_wmp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_uac_bypass_wmp.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "5f9db380-ea57-4d1e-beab-8a2d33397e93"
  - "UAC Bypass Using Windows Media Player - Registry"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# UAC Bypass Using Windows Media Player - Registry

Detects the pattern of UAC Bypass using Windows Media Player osksupport.dll (UACMe 32)

## Metadata

- Rule ID: 5f9db380-ea57-4d1e-beab-8a2d33397e93
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-08-23
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_uac_bypass_wmp.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  TargetObject|endswith: \SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Compatibility
    Assistant\Store\C:\Program Files\Windows Media Player\osk.exe
  Details: Binary Data
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/hfiref0x/UACME

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_uac_bypass_wmp.yml)
