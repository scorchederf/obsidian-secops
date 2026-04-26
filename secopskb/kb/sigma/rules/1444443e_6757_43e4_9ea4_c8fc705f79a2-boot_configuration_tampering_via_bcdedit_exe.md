---
sigma_id: "1444443e-6757-43e4-9ea4-c8fc705f79a2"
title: "Boot Configuration Tampering Via Bcdedit.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_bcdedit_boot_conf_tamper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bcdedit_boot_conf_tamper.yml"
build_date: "2026-04-26 14:14:21"
status: "stable"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "1444443e-6757-43e4-9ea4-c8fc705f79a2"
  - "Boot Configuration Tampering Via Bcdedit.EXE"
attack_technique_ids:
  - "T1490"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Boot Configuration Tampering Via Bcdedit.EXE

Detects the use of the bcdedit command to tamper with the boot configuration data. This technique is often times used by malware or attackers as a destructive way before launching ransomware.

## Metadata

- Rule ID: 1444443e-6757-43e4-9ea4-c8fc705f79a2
- Status: stable
- Level: high
- Author: E.M. Anhaus (originally from Atomic Blue Detections, Endgame), oscd.community
- Date: 2019-10-24
- Modified: 2023-02-15
- Source Path: rules/windows/process_creation/proc_creation_win_bcdedit_boot_conf_tamper.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]]

## Detection

```yaml
selection_img:
- Image|endswith: \bcdedit.exe
- OriginalFileName: bcdedit.exe
selection_set:
  CommandLine|contains: set
selection_cli:
- CommandLine|contains|all:
  - bootstatuspolicy
  - ignoreallfailures
- CommandLine|contains|all:
  - recoveryenabled
  - 'no'
condition: all of selection_*
```

## False Positives

- Unlikely

## Simulation

### Windows - Disable Windows Recovery Console Repair

- atomic_guid: cf21060a-80b3-4238-a595-22525de4ab81
- name: Windows - Disable Windows Recovery Console Repair
- technique: T1490
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1490/T1490.md
- https://eqllib.readthedocs.io/en/latest/analytics/c4732632-9c1d-4980-9fa8-1d98c93f918e.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bcdedit_boot_conf_tamper.yml)
