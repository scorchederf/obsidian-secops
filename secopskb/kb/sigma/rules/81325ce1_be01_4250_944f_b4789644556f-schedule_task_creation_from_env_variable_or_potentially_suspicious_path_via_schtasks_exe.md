---
sigma_id: "81325ce1-be01-4250-944f-b4789644556f"
title: "Schedule Task Creation From Env Variable Or Potentially Suspicious Path Via Schtasks.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_env_folder.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_env_folder.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "81325ce1-be01-4250-944f-b4789644556f"
  - "Schedule Task Creation From Env Variable Or Potentially Suspicious Path Via Schtasks.EXE"
attack_technique_ids:
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Schedule Task Creation From Env Variable Or Potentially Suspicious Path Via Schtasks.EXE

Detects Schtask creations that point to a suspicious folder or an environment variable often used by malware

## Metadata

- Rule ID: 81325ce1-be01-4250-944f-b4789644556f
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2022-02-21
- Modified: 2025-10-07
- Source Path: rules/windows/process_creation/proc_creation_win_schtasks_env_folder.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Detection

```yaml
selection_1_create:
  Image|endswith: \schtasks.exe
  CommandLine|contains|windash: ' /create '
selection_1_all_folders:
  CommandLine|contains:
  - :\Perflogs
  - :\Users\All Users\
  - :\Users\Default\
  - :\Users\Public
  - :\Windows\Temp
  - \AppData\Local\
  - \AppData\Roaming\
  - '%AppData%'
  - '%Public%'
selection_2_parent:
  ParentCommandLine|endswith: \svchost.exe -k netsvcs -p -s Schedule
selection_2_some_folders:
  CommandLine|contains:
  - :\Perflogs
  - :\Windows\Temp
  - \Users\Public
  - '%Public%'
filter_optional_other:
- ParentCommandLine|contains: unattended.ini
- CommandLine|contains: update_task.xml
filter_optional_team_viewer:
  CommandLine|contains: /Create /TN TVInstallRestore /TR
filter_optional_avira_install:
  CommandLine|contains|all:
  - '/Create /Xml '
  - \Temp\.CR.
  - \Avira_Security_Installation.xml
filter_optional_avira_other:
  CommandLine|contains|all:
  - /Create /F /TN
  - '/Xml '
  - \Temp\
  - Avira_
  CommandLine|contains:
  - .tmp\UpdateFallbackTask.xml
  - .tmp\WatchdogServiceControlManagerTimeout.xml
  - .tmp\SystrayAutostart.xml
  - .tmp\MaintenanceTask.xml
filter_optional_klite_codec:
  CommandLine|contains|all:
  - \Temp\
  - '/Create /TN "klcp_update" /XML '
  - \klcp_update_task.xml
condition: ( all of selection_1_* or all of selection_2_* ) and not 1 of filter_optional_*
```

## False Positives

- Benign scheduled tasks creations or executions that happen often during software installations
- Software that uses the AppData folder and scheduled tasks to update the software in the AppData folders

## References

- https://www.welivesecurity.com/2022/01/18/donot-go-do-not-respawn/
- https://www.joesandbox.com/analysis/514608/0/html#324415FF7D8324231381BAD48A052F85DF04
- https://blog.talosintelligence.com/gophish-powerrat-dcrat/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_env_folder.yml)
