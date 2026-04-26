---
sigma_id: "37b437cf-3fc5-4c8e-9c94-1d7c9aff842b"
title: "Allow RDP Remote Assistance Feature"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_allow_rdp_remote_assistance_feature.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_allow_rdp_remote_assistance_feature.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "37b437cf-3fc5-4c8e-9c94-1d7c9aff842b"
  - "Allow RDP Remote Assistance Feature"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Allow RDP Remote Assistance Feature

Detect enable rdp feature to allow specific user to rdp connect on the targeted machine

## Metadata

- Rule ID: 37b437cf-3fc5-4c8e-9c94-1d7c9aff842b
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-08-19
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_allow_rdp_remote_assistance_feature.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  TargetObject|endswith: System\CurrentControlSet\Control\Terminal Server\fAllowToGetHelp
  Details: DWORD (0x00000001)
condition: selection
```

## False Positives

- Legitimate use of the feature (alerts should be investigated either way)

## Simulation

### Allow RDP Remote Assistance Feature

- atomic_guid: 86677d0e-0b5e-4a2b-b302-454175f9aa9e
- name: Allow RDP Remote Assistance Feature
- technique: T1112
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/40b77d63808dd4f4eafb83949805636735a1fd15/atomics/T1112/T1112.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_allow_rdp_remote_assistance_feature.yml)
