---
sigma_id: "160d2780-31f7-4922-8b3a-efce30e63e96"
title: "Potential AMSI COM Server Hijacking"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_amsi_com_hijack.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_amsi_com_hijack.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "160d2780-31f7-4922-8b3a-efce30e63e96"
  - "Potential AMSI COM Server Hijacking"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential AMSI COM Server Hijacking

Detects changes to the AMSI come server registry key in order disable AMSI scanning functionalities. When AMSI attempts to starts its COM component, it will query its registered CLSID and return a non-existent COM server. This causes a load failure and prevents any scanning methods from being accessed, ultimately rendering AMSI useless

## Metadata

- Rule ID: 160d2780-31f7-4922-8b3a-efce30e63e96
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-04
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_amsi_com_hijack.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  TargetObject|endswith: \CLSID\{fdb00e52-a214-4aa1-8fba-4357bb0072ec}\InProcServer32\(Default)
filter:
  Details: '%windir%\system32\amsi.dll'
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://enigma0x3.net/2017/07/19/bypassing-amsi-via-com-server-hijacking/
- https://github.com/r00t-3xp10it/hacking-material-books/blob/43cb1e1932c16ff1f58b755bc9ab6b096046853f/obfuscation/simple_obfuscation.md#amsi-comreg-bypass

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_amsi_com_hijack.yml)
