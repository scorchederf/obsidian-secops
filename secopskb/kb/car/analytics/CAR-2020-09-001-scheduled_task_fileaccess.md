---
car_id: "CAR-2020-09-001"
title: "Scheduled Task - FileAccess"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2020-09-001/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-09-001.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2020-09-001"
  - "Scheduled Task - FileAccess"
attack_technique_ids:
  - "T1053"
  - "T1053.005"
platforms:
  - "Windows"
implementation_types:
  - "Pseudocode"
  - "Splunk"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CAR-2020-09-001: Scheduled Task - FileAccess

## Metadata

- CAR ID: CAR-2020-09-001
- Submission Date: 2020/09/10
- Information Domain: Host
- Analytic Type: Situational Awareness
- Platforms: Windows
- Data Subtypes: File
- Contributors: Olaf Hartong

## Description

In order to gain persistence, privilege escalation, or remote execution, an adversary may use the Windows Task Scheduler to schedule a command to be run at a specified time, date, and even host. Task Scheduler stores tasks as files in two locations - C:\Windows\Tasks (legacy) or C:\Windows\System32\Tasks. Accordingly, this analytic looks for the creation of task files in these two locations.

## ATT&CK Coverage

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053]] (coverage: Low; tactics: TA0002, TA0003, TA0004)
  - [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Implementations

### Pseudocode

This is a pseudocode representation of the below splunk search.

- Data Model: CAR native

```pseudocode
files = search File:Create
task_files = filter files where (
  (file_path = "C:\Windows\System32\Tasks\*" or file_path = "C:\Windows\Tasks\*")  and
  image_path != "C:\WINDOWS\system32\svchost.exe")
output task_files
```

### Splunk

This Splunk search looks for any files created under the Windows tasks directories.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_index__ EventCode=11 Image!="C:\\WINDOWS\\system32\\svchost.exe" (TargetFilename="C:\\Windows\\System32\\Tasks\\
*" OR TargetFilename="C:\\Windows\\Tasks\\*")
```

### LogPoint

This LogPoint search looks for any files created under the Windows tasks directories.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=11 -source_image="C:\WINDOWS\system32\svchost.exe" (path="C:\Windows\System32\Tasks*" OR path="C:\Windows\Tasks*")
```

## Data Model References

- file/create/file_path
- file/create/image_path

## D3FEND Mappings

- [[kb/defend/techniques/D3-FCA-file_creation_analysis|D3-FCA: File Creation Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2020-09-001/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-09-001.yaml)
