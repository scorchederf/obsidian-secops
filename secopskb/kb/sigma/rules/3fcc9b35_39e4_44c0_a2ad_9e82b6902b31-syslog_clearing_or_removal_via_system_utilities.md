---
sigma_id: "3fcc9b35-39e4-44c0-a2ad-9e82b6902b31"
title: "Syslog Clearing or Removal Via System Utilities"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_clear_syslog.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_clear_syslog.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "3fcc9b35-39e4-44c0-a2ad-9e82b6902b31"
  - "Syslog Clearing or Removal Via System Utilities"
attack_technique_ids:
  - "T1070.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Syslog Clearing or Removal Via System Utilities

Detects specific commands commonly used to remove or empty the syslog. Which is a technique often used by attacker as a method to hide their tracks

## Metadata

- Rule ID: 3fcc9b35-39e4-44c0-a2ad-9e82b6902b31
- Status: test
- Level: high
- Author: Max Altgelt (Nextron Systems), Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research), MSTIC
- Date: 2021-10-15
- Modified: 2025-10-15
- Source Path: rules/linux/process_creation/proc_creation_lnx_clear_syslog.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.002]]

## Detection

```yaml
selection_file:
  CommandLine|contains: /var/log/syslog
selection_command_rm:
  Image|endswith: /rm
  CommandLine|contains:
  - ' -r '
  - ' -f '
  - ' -rf '
  - /var/log/syslog
selection_command_unlink:
  Image|endswith: /unlink
selection_command_mv:
  Image|endswith: /mv
selection_command_truncate:
  Image|endswith: /truncate
  CommandLine|contains|all:
  - '0 '
  - /var/log/syslog
  CommandLine|contains:
  - '-s '
  - '-c '
  - --size
selection_command_ln:
  Image|endswith: /ln
  CommandLine|contains|all:
  - '/dev/null '
  - /var/log/syslog
  CommandLine|contains:
  - '-sf '
  - '-sfn '
  - '-sfT '
selection_command_cp:
  Image|endswith: /cp
  CommandLine|contains: /dev/null
selection_command_shred:
  Image|endswith: /shred
  CommandLine|contains: '-u '
selection_unique_other:
  CommandLine|contains:
  - ' > /var/log/syslog'
  - ' >/var/log/syslog'
  - ' >| /var/log/syslog'
  - ': > /var/log/syslog'
  - :> /var/log/syslog
  - :>/var/log/syslog
  - '>|/var/log/syslog'
selection_unique_journalctl:
  CommandLine|contains:
  - journalctl --vacuum
  - journalctl --rotate
condition: (selection_file and 1 of selection_command_*) or 1 of selection_unique_*
```

## False Positives

- Log rotation.
- Maintenance.

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1070.002/T1070.002.md
- https://www.virustotal.com/gui/file/54d60fd58d7fa3475fa123985bfc1594df26da25c1f5fbc7dfdba15876dd8ac5/behavior

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_clear_syslog.yml)
