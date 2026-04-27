---
sigma_id: "b110ebaf-697f-4da1-afd5-b536fa27a2c1"
title: "Potential Signing Bypass Via Windows Developer Features - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_turn_on_dev_features.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_turn_on_dev_features.yml"
build_date: "2026-04-27 19:13:54"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when the enablement of developer features such as "Developer Mode" or "Application Sideloading". Which allows the user to install untrusted packages.

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
