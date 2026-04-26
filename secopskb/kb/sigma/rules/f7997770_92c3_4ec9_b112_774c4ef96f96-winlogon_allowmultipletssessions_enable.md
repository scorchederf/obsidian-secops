---
sigma_id: "f7997770-92c3-4ec9-b112-774c4ef96f96"
title: "Winlogon AllowMultipleTSSessions Enable"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_winlogon_allow_multiple_tssessions.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_winlogon_allow_multiple_tssessions.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "f7997770-92c3-4ec9-b112-774c4ef96f96"
  - "Winlogon AllowMultipleTSSessions Enable"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Winlogon AllowMultipleTSSessions Enable

Detects when the 'AllowMultipleTSSessions' value is enabled.
Which allows for multiple Remote Desktop connection sessions to be opened at once.
This is often used by attacker as a way to connect to an RDP session without disconnecting the other users

## Metadata

- Rule ID: f7997770-92c3-4ec9-b112-774c4ef96f96
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-09
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_winlogon_allow_multiple_tssessions.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Microsoft\Windows NT\CurrentVersion\Winlogon\AllowMultipleTSSessions
  Details|endswith: DWORD (0x00000001)
condition: selection
```

## False Positives

- Legitimate use of the multi session functionality

## References

- http://blog.talosintelligence.com/2022/09/lazarus-three-rats.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_winlogon_allow_multiple_tssessions.yml)
