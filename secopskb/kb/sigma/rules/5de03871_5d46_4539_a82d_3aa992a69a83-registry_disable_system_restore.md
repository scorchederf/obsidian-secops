---
sigma_id: "5de03871-5d46-4539-a82d-3aa992a69a83"
title: "Registry Disable System Restore"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_disable_system_restore.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_system_restore.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "5de03871-5d46-4539-a82d-3aa992a69a83"
  - "Registry Disable System Restore"
attack_technique_ids:
  - "T1490"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Registry Disable System Restore

Detects the modification of the registry to disable a system restore on the computer

## Metadata

- Rule ID: 5de03871-5d46-4539-a82d-3aa992a69a83
- Status: test
- Level: high
- Author: frack113
- Date: 2022-04-04
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_disable_system_restore.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]]

## Detection

```yaml
selection:
  TargetObject|contains:
  - \Policies\Microsoft\Windows NT\SystemRestore
  - \Microsoft\Windows NT\CurrentVersion\SystemRestore
  TargetObject|endswith:
  - DisableConfig
  - DisableSR
  Details: DWORD (0x00000001)
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1490/T1490.md#atomic-test-9---disable-system-restore-through-registry

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_system_restore.yml)
