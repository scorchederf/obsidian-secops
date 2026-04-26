---
sigma_id: "f2c64357-b1d2-41b7-849f-34d2682c0fad"
title: "Suspicious Command Patterns In Scheduled Task Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_susp_pattern.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_susp_pattern.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f2c64357-b1d2-41b7-849f-34d2682c0fad"
  - "Suspicious Command Patterns In Scheduled Task Creation"
attack_technique_ids:
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Command Patterns In Scheduled Task Creation

Detects scheduled task creation using "schtasks" that contain potentially suspicious or uncommon commands

## Metadata

- Rule ID: f2c64357-b1d2-41b7-849f-34d2682c0fad
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-02-23
- Modified: 2024-03-19
- Source Path: rules/windows/process_creation/proc_creation_win_schtasks_susp_pattern.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Detection

```yaml
selection_schtasks:
  Image|endswith: \schtasks.exe
  CommandLine|contains: '/Create '
selection_pattern_1:
  CommandLine|contains:
  - '/sc minute '
  - '/ru system '
selection_pattern_2:
  CommandLine|contains:
  - cmd /c
  - cmd /k
  - cmd /r
  - 'cmd.exe /c '
  - 'cmd.exe /k '
  - 'cmd.exe /r '
selection_uncommon:
  CommandLine|contains:
  - ' -decode '
  - ' -enc '
  - ' -w hidden '
  - ' bypass '
  - ' IEX'
  - .DownloadData
  - .DownloadFile
  - .DownloadString
  - '/c start /min '
  - FromBase64String
  - mshta http
  - mshta.exe http
selection_anomaly_1:
  CommandLine|contains:
  - :\ProgramData\
  - :\Temp\
  - :\Tmp\
  - :\Users\Public\
  - :\Windows\Temp\
  - \AppData\
  - '%AppData%'
  - '%Temp%'
  - '%tmp%'
selection_anomaly_2:
  CommandLine|contains:
  - cscript
  - curl
  - wscript
condition: selection_schtasks and ( all of selection_pattern_* or selection_uncommon
  or all of selection_anomaly_* )
```

## False Positives

- Software installers that run from temporary folders and also install scheduled tasks are expected to generate some false positives

## References

- https://app.any.run/tasks/512c1352-6380-4436-b27d-bb62f0c020d6/
- https://twitter.com/RedDrip7/status/1506480588827467785
- https://www.ncsc.gov.uk/static-assets/documents/malware-analysis-reports/devil-bait/NCSC-MAR-Devil-Bait.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_susp_pattern.yml)
