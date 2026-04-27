---
sigma_id: "e1aa95de-610a-427d-b9e7-9b46cfafbe6a"
title: "Windows Defender Service Disabled - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_disable_windows_defender_service.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_windows_defender_service.yml"
build_date: "2026-04-26 17:03:24"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "e1aa95de-610a-427d-b9e7-9b46cfafbe6a"
  - "Windows Defender Service Disabled - Registry"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Windows Defender Service Disabled - Registry

Detects when an attacker or tool disables the  Windows Defender service (WinDefend) via the registry

## Metadata

- Rule ID: e1aa95de-610a-427d-b9e7-9b46cfafbe6a
- Status: test
- Level: high
- Author: Ján Trenčanský, frack113, AlertIQ, Nasreddine Bencherchali
- Date: 2022-08-01
- Modified: 2024-03-25
- Source Path: rules/windows/registry/registry_set/registry_set_disable_windows_defender_service.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Services\WinDefend\Start
  Details: DWORD (0x00000004)
condition: selection
```

## False Positives

- Administrator actions

## References

- https://thedfirreport.com/2021/10/18/icedid-to-xinglocker-ransomware-in-24-hours/
- https://gist.github.com/anadr/7465a9fde63d41341136949f14c21105

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_windows_defender_service.yml)
