---
sigma_id: "c7dcacd0-cc59-4004-b0a4-1d6cdebe6f3e"
title: "Disable Administrative Share Creation at Startup"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_disable_administrative_share.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_administrative_share.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "c7dcacd0-cc59-4004-b0a4-1d6cdebe6f3e"
  - "Disable Administrative Share Creation at Startup"
attack_technique_ids:
  - "T1070.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Disable Administrative Share Creation at Startup

Administrative shares are hidden network shares created by Microsoft Windows NT operating systems that grant system administrators remote access to every disk volume on a network-connected system

## Metadata

- Rule ID: c7dcacd0-cc59-4004-b0a4-1d6cdebe6f3e
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-16
- Modified: 2024-03-25
- Source Path: rules/windows/registry/registry_set/registry_set_disable_administrative_share.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.005]]

## Detection

```yaml
selection:
  TargetObject|contains: \Services\LanmanServer\Parameters\
  TargetObject|endswith:
  - \AutoShareWks
  - \AutoShareServer
  Details: DWORD (0x00000000)
condition: selection
```

## False Positives

- Unknown

## Simulation

### Disable Administrative Share Creation at Startup

- atomic_guid: 99c657aa-ebeb-4179-a665-69288fdd12b8
- name: Disable Administrative Share Creation at Startup
- technique: T1070.005
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1070.005/T1070.005.md#atomic-test-4---disable-administrative-share-creation-at-startup

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_administrative_share.yml)
