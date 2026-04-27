---
sigma_id: "9ac94dc8-9042-493c-ba45-3b5e7c86b980"
title: "Disable Important Scheduled Task"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_disable.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_disable.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "9ac94dc8-9042-493c-ba45-3b5e7c86b980"
  - "Disable Important Scheduled Task"
attack_technique_ids:
  - "T1489"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Disable Important Scheduled Task

Detects when adversaries stop services or processes by disabling their respective scheduled tasks in order to conduct data destructive activities

## Metadata

- Rule ID: 9ac94dc8-9042-493c-ba45-3b5e7c86b980
- Status: test
- Level: high
- Author: frack113, Nasreddine Bencherchali (Nextron Systems), X__Junior
- Date: 2021-12-26
- Modified: 2024-08-25
- Source Path: rules/windows/process_creation/proc_creation_win_schtasks_disable.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1489-service_stop|T1489]]

## Detection

```yaml
selection:
  Image|endswith: \schtasks.exe
  CommandLine|contains|all:
  - /Change
  - /TN
  - /disable
  CommandLine|contains:
  - \Windows\BitLocker
  - \Windows\ExploitGuard
  - \Windows\ExploitGuard\ExploitGuard MDM policy Refresh
  - \Windows\SystemRestore\SR
  - \Windows\UpdateOrchestrator\
  - \Windows\Windows Defender\
  - \Windows\WindowsBackup\
  - \Windows\WindowsUpdate\
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1490/T1490.md#atomic-test-8---windows---disable-the-sr-scheduled-task
- https://twitter.com/MichalKoczwara/status/1553634816016498688
- https://thedfirreport.com/2021/10/18/icedid-to-xinglocker-ransomware-in-24-hours/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_disable.yml)
