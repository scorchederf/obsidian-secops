---
sigma_id: "1a4bd6af-99ac-4466-b5b2-7b72b4a05462"
title: "Security Event Logging Disabled via MiniNt Registry Key - Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_event_logging_disable_via_key_minint.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_event_logging_disable_via_key_minint.yml"
build_date: "2026-04-26 17:03:22"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "1a4bd6af-99ac-4466-b5b2-7b72b4a05462"
  - "Security Event Logging Disabled via MiniNt Registry Key - Process"
attack_technique_ids:
  - "T1562.002"
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Security Event Logging Disabled via MiniNt Registry Key - Process

Detects attempts to disable security event logging by adding the `MiniNt` registry key.
This key is used to disable the Windows Event Log service, which collects and stores event logs from the operating system and applications.
Adversaries may want to disable this service to prevent logging of security events that could be used to detect their activities.

## Metadata

- Rule ID: 1a4bd6af-99ac-4466-b5b2-7b72b4a05462
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-04-09
- Source Path: rules/windows/process_creation/proc_creation_win_event_logging_disable_via_key_minint.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.002]]
- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection_reg_img:
- Image|endswith: \reg.exe
- OriginalFileName: reg.exe
selection_reg_cmd:
  CommandLine|contains|all:
  - ' add '
  - \SYSTEM\CurrentControlSet\Control\MiniNt
selection_powershell_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  - \powershell_ise.exe
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
selection_powershell_cmd1:
  CommandLine|contains:
  - 'New-Item '
  - 'ni '
selection_powershell_cmd2:
  CommandLine|contains: \SYSTEM\CurrentControlSet\Control\MiniNt
condition: all of selection_reg_* or all of selection_powershell_*
```

## False Positives

- Highly Unlikely

## References

- https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_event_logging_disable_via_key_minint.yml)
