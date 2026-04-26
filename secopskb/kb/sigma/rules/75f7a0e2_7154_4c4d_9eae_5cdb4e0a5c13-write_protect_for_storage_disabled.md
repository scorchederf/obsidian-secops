---
sigma_id: "75f7a0e2-7154-4c4d-9eae-5cdb4e0a5c13"
title: "Write Protect For Storage Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_write_protect_for_storage_disabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_write_protect_for_storage_disabled.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "75f7a0e2-7154-4c4d-9eae-5cdb4e0a5c13"
  - "Write Protect For Storage Disabled"
attack_technique_ids:
  - "T1562"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Write Protect For Storage Disabled

Detects applications trying to modify the registry in order to disable any write-protect property for storage devices.
This could be a precursor to a ransomware attack and has been an observed technique used by cypherpunk group.

## Metadata

- Rule ID: 75f7a0e2-7154-4c4d-9eae-5cdb4e0a5c13
- Status: test
- Level: medium
- Author: Sreeman
- Date: 2021-06-11
- Modified: 2024-01-18
- Source Path: rules/windows/process_creation/proc_creation_win_reg_write_protect_for_storage_disabled.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - \System\CurrentControlSet\Control
  - Write Protection
  - '0'
  - storage
condition: selection
```

## False Positives

- Unknown

## References

- https://www.manageengine.com/products/desktop-central/os-imaging-deployment/media-is-write-protected.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_write_protect_for_storage_disabled.yml)
