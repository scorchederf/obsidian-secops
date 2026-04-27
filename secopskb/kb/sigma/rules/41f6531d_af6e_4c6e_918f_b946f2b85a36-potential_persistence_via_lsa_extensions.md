---
sigma_id: "41f6531d-af6e-4c6e-918f-b946f2b85a36"
title: "Potential Persistence Via LSA Extensions"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_lsa_extension.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_lsa_extension.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "41f6531d-af6e-4c6e-918f-b946f2b85a36"
  - "Potential Persistence Via LSA Extensions"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Potential Persistence Via LSA Extensions

Detects when an attacker modifies the "REG_MULTI_SZ" value named "Extensions" to include a custom DLL to achieve persistence via lsass.
The "Extensions" list contains filenames of DLLs being automatically loaded by lsass.exe. Each DLL has its InitializeLsaExtension() method called after loading.

## Metadata

- Rule ID: 41f6531d-af6e-4c6e-918f-b946f2b85a36
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-21
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_lsa_extension.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection:
  TargetObject|contains: \SYSTEM\CurrentControlSet\Control\LsaExtensionConfig\LsaSrv\Extensions
condition: selection
```

## False Positives

- Unlikely

## References

- https://persistence-info.github.io/Data/lsaaextension.html
- https://twitter.com/0gtweet/status/1476286368385019906

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_lsa_extension.yml)
