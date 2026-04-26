---
sigma_id: "1547e27c-3974-43e2-a7d7-7f484fb928ec"
title: "Registry Persistence via Service in Safe Mode"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_add_load_service_in_safe_mode.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_add_load_service_in_safe_mode.yml"
build_date: "2026-04-26 15:01:50"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "1547e27c-3974-43e2-a7d7-7f484fb928ec"
  - "Registry Persistence via Service in Safe Mode"
attack_technique_ids:
  - "T1564.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Registry Persistence via Service in Safe Mode

Detects the modification of the registry to allow a driver or service to persist in Safe Mode.

## Metadata

- Rule ID: 1547e27c-3974-43e2-a7d7-7f484fb928ec
- Status: test
- Level: high
- Author: frack113
- Date: 2022-04-04
- Modified: 2025-10-22
- Source Path: rules/windows/registry/registry_set/registry_set_add_load_service_in_safe_mode.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.001]]

## Detection

```yaml
selection:
  TargetObject|contains:
  - \Control\SafeBoot\Minimal\
  - \Control\SafeBoot\Network\
  TargetObject|endswith: \(Default)
  Details: Service
filter_optional_sophos:
  Image: C:\WINDOWS\system32\msiexec.exe
  TargetObject|endswith:
  - \Control\SafeBoot\Minimal\SAVService\(Default)
  - \Control\SafeBoot\Network\SAVService\(Default)
filter_optional_mbamservice:
  Image|endswith: \MBAMInstallerService.exe
  TargetObject|endswith: \MBAMService\(Default)
  Details: Service
filter_optional_hexnode:
  Image: C:\Hexnode\Hexnode Agent\Current\HexnodeAgent.exe
  TargetObject|endswith:
  - \Control\SafeBoot\Minimal\Hexnode Updater\(Default)
  - \Control\SafeBoot\Network\Hexnode Updater\(Default)
  - \Control\SafeBoot\Minimal\Hexnode Agent\(Default)
  - \Control\SafeBoot\Network\Hexnode Agent\(Default)
  Details: Service
condition: selection and not 1 of filter_optional_*
```

## False Positives

- Unknown

## Simulation

### Windows Add Registry Value to Load Service in Safe Mode without Network

- Atomic Test: [[kb/atomic/tests/1dd59fb3_1cb3_4828_805d_cf80b4c3bbb5-windows_add_registry_value_to_load_service_in_safe_mode_without_network|1dd59fb3-1cb3-4828-805d-cf80b4c3bbb5]]
- atomic_guid: 1dd59fb3-1cb3-4828-805d-cf80b4c3bbb5
- name: Windows Add Registry Value to Load Service in Safe Mode without Network
- technique: T1112
- type: atomic-red-team

### Windows Add Registry Value to Load Service in Safe Mode with Network

- Atomic Test: [[kb/atomic/tests/c173c948_65e5_499c_afbe_433722ed5bd4-windows_add_registry_value_to_load_service_in_safe_mode_with_network|c173c948-65e5-499c-afbe-433722ed5bd4]]
- atomic_guid: c173c948-65e5-499c-afbe-433722ed5bd4
- name: Windows Add Registry Value to Load Service in Safe Mode with Network
- technique: T1112
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1112/T1112.md#atomic-test-33---windows-add-registry-value-to-load-service-in-safe-mode-without-network
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1112/T1112.md#atomic-test-34---windows-add-registry-value-to-load-service-in-safe-mode-with-network

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_add_load_service_in_safe_mode.yml)
