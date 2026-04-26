---
sigma_id: "b110ebaf-697f-4da1-afd5-b536fa27a2c1"
title: "Potential Signing Bypass Via Windows Developer Features - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_turn_on_dev_features.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_turn_on_dev_features.yml"
build_date: "2026-04-26 15:01:49"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "b110ebaf-697f-4da1-afd5-b536fa27a2c1"
  - "Potential Signing Bypass Via Windows Developer Features - Registry"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Signing Bypass Via Windows Developer Features - Registry

Detects when the enablement of developer features such as "Developer Mode" or "Application Sideloading". Which allows the user to install untrusted packages.

## Metadata

- Rule ID: b110ebaf-697f-4da1-afd5-b536fa27a2c1
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-12
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_turn_on_dev_features.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection:
  TargetObject|contains:
  - \Microsoft\Windows\CurrentVersion\AppModelUnlock
  - \Policies\Microsoft\Windows\Appx\
  TargetObject|endswith:
  - \AllowAllTrustedApps
  - \AllowDevelopmentWithoutDevLicense
  Details: DWORD (0x00000001)
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/malmoeb/status/1560536653709598721
- https://www.sentinelone.com/labs/inside-malicious-windows-apps-for-malware-deployment/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_turn_on_dev_features.yml)
