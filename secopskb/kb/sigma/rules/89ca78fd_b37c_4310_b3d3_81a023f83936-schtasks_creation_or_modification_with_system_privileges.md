---
sigma_id: "89ca78fd-b37c-4310-b3d3-81a023f83936"
title: "Schtasks Creation Or Modification With SYSTEM Privileges"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_system.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_system.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "89ca78fd-b37c-4310-b3d3-81a023f83936"
  - "Schtasks Creation Or Modification With SYSTEM Privileges"
attack_technique_ids:
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Schtasks Creation Or Modification With SYSTEM Privileges

Detects the creation or update of a scheduled task to run with "NT AUTHORITY\SYSTEM" privileges

## Metadata

- Rule ID: 89ca78fd-b37c-4310-b3d3-81a023f83936
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-28
- Modified: 2025-02-15
- Source Path: rules/windows/process_creation/proc_creation_win_schtasks_system.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Detection

```yaml
selection_root:
  Image|endswith: \schtasks.exe
  CommandLine|contains:
  - ' /change '
  - ' /create '
selection_run:
  CommandLine|contains: '/ru '
selection_user:
  CommandLine|contains:
  - NT AUT
  - ' SYSTEM '
filter_optional_teamviewer:
  Image|endswith: \schtasks.exe
  CommandLine|contains|all:
  - /TN TVInstallRestore
  - \TeamViewer_.exe
filter_optional_office:
  CommandLine|contains|all:
  - Subscription Heartbeat
  - \HeartbeatConfig.xml
  - \Microsoft Shared\OFFICE
filter_optional_avira:
  CommandLine|contains:
  - '/Create /F /RU System /SC WEEKLY /TN AviraSystemSpeedupVerify /TR '
  - :\Program Files (x86)\Avira\System Speedup\setup\avira_speedup_setup.exe
  - /VERIFY /VERYSILENT /NOSTART /NODOTNET /NORESTART" /RL HIGHEST
condition: all of selection_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://www.elastic.co/security-labs/exploring-the-qbot-attack-pattern
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_system.yml)
