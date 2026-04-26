---
sigma_id: "974515da-6cc5-4c95-ae65-f97f9150ec7f"
title: "Disable Microsoft Defender Firewall via Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_disable_defender_firewall.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_defender_firewall.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "974515da-6cc5-4c95-ae65-f97f9150ec7f"
  - "Disable Microsoft Defender Firewall via Registry"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Disable Microsoft Defender Firewall via Registry

Adversaries may disable or modify system firewalls in order to bypass controls limiting network usage

## Metadata

- Rule ID: 974515da-6cc5-4c95-ae65-f97f9150ec7f
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-09
- Modified: 2024-03-25
- Source Path: rules/windows/registry/registry_set/registry_set_disable_defender_firewall.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Detection

```yaml
selection:
  TargetObject|contains: \Services\SharedAccess\Parameters\FirewallPolicy\
  TargetObject|endswith: \EnableFirewall
  Details: DWORD (0x00000000)
condition: selection
```

## False Positives

- Unknown

## Simulation

### Disable Microsoft Defender Firewall via Registry

- atomic_guid: afedc8c4-038c-4d82-b3e5-623a95f8a612
- name: Disable Microsoft Defender Firewall via Registry
- technique: T1562.004
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.004/T1562.004.md#atomic-test-2---disable-microsoft-defender-firewall-via-registry

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_defender_firewall.yml)
