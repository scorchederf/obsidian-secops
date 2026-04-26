---
sigma_id: "e78c408a-e2ea-43cd-b5ea-51975cf358c0"
title: "Disable Windows Firewall by Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_disable_windows_firewall.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_windows_firewall.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "e78c408a-e2ea-43cd-b5ea-51975cf358c0"
  - "Disable Windows Firewall by Registry"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Disable Windows Firewall by Registry

Detect set EnableFirewall to 0 to disable the Windows firewall

## Metadata

- Rule ID: e78c408a-e2ea-43cd-b5ea-51975cf358c0
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-08-19
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_disable_windows_firewall.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Detection

```yaml
selection:
  TargetObject|endswith:
  - \SOFTWARE\Policies\Microsoft\WindowsFirewall\StandardProfile\EnableFirewall
  - \SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile\EnableFirewall
  Details: DWORD (0x00000000)
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/40b77d63808dd4f4eafb83949805636735a1fd15/atomics/T1562.004/T1562.004.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_windows_firewall.yml)
