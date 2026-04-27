---
sigma_id: "6a5f68d1-c4b5-46b9-94ee-5324892ea939"
title: "Uninstall Sysinternals Sysmon"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sysinternals_sysmon_uninstall.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_sysmon_uninstall.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "6a5f68d1-c4b5-46b9-94ee-5324892ea939"
  - "Uninstall Sysinternals Sysmon"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Uninstall Sysinternals Sysmon

Detects the removal of Sysmon, which could be a potential attempt at defense evasion

## Metadata

- Rule ID: 6a5f68d1-c4b5-46b9-94ee-5324892ea939
- Status: test
- Level: high
- Author: frack113
- Date: 2022-01-12
- Modified: 2024-03-13
- Source Path: rules/windows/process_creation/proc_creation_win_sysinternals_sysmon_uninstall.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_pe:
- Image|endswith:
  - \Sysmon64.exe
  - \Sysmon.exe
- Description: System activity monitor
selection_cli:
  CommandLine|contains|windash: -u
condition: all of selection_*
```

## False Positives

- Legitimate administrators might use this command to remove Sysmon for debugging purposes

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/T1562.001.md#atomic-test-11---uninstall-sysmon

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_sysmon_uninstall.yml)
