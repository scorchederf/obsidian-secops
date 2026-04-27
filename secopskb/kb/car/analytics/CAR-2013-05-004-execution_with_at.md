---
car_id: "CAR-2013-05-004"
title: "Execution with AT"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2013-05-004/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-05-004.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2013-05-004"
  - "Execution with AT"
attack_technique_ids:
  - "T1053"
  - "T1053.002"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
  - "Splunk"
  - "EQL"
  - "DNIF"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CAR-2013-05-004: Execution with AT

## Metadata

- CAR ID: CAR-2013-05-004
- Submission Date: 2013/05/13
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: MITRE

## Description

In order to gain [persistence](https://attack.mitre.org/tactics/TA0003/), [privilege escalation](https://attack.mitre.org/tactics/TA0004/), or [remote execution](https://attack.mitre.org/tactics/TA0002/), an adversary may use the Windows built-in command AT (at.exe) to [schedule a command](https://attack.mitre.org/techniques/T1053/002) to be run at a specified time, date, and even host. This method has been used by adversaries and administrators alike. Its use may lead to detection of compromised hosts and compromised users if it is used to move laterally.
The built-in Windows tool schtasks.exe ([[kb/car/analytics/CAR-2013-08-001-execution_with_schtasks|CAR-2013-08-001]]) offers greater flexibility when creating, modifying, and enumerating tasks. For these reasons, schtasks.exe is more commonly used by administrators, tools/scripts, and power users.

## ATT&CK Coverage

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053]] (coverage: Moderate; tactics: TA0002, TA0003, TA0004)
  - [[kb/attack/techniques/T1053-scheduled_task_job|T1053.002]]

## Implementations

### pseudocode

Instances of the process `at.exe` running imply the querying or creation of tasks. Although the command_line is not essential for the analytic to run, it is critical when identifying the command that was scheduled.

```pseudocode
process = search Process:Create
at = filter process where (exe == "at.exe")
output at
```

### Splunk

Splunk version of the above pseudocode.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_index__ Image="C:\\Windows\\*\\at.exe"|stats values(CommandLine) as "Command Lines" by ComputerName
```

### EQL

EQL version of the above pseudocode.

- Data Model: EQL native

```eql
process where subtype.create and process_name == "at.exe"
```

### DNIF

DNIF version of the above pseudocode.

- Data Model: Sysmon native

```dnif
_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 AND $App=at.exe limit 100
```

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 image="*\at.exe"
```

## Data Model References

- process/create/command_line
- process/create/exe

## Unit Tests

-   From an admin account, open Windows command prompt (right click, run as administrator).
-   Execute "at 10:00 calc.exe," substituting a time in the near future for 10:00.
-   The program should respond with “Added a new job with job ID = 1” where the job ID is dependent on what tasks are scheduled.
-   The program should execute at the time specified. This is what the analytic should fire on.
-   To remove the scheduled task, execute "at 1 /delete" where you replace "1" with the job ID output in step 2a above.

- Configurations: Windows 7

```text
at 10:00 calc.exe // returns a job number X
at X /delete
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-SJA-scheduled_job_analysis|D3-SJA: Scheduled Job Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2013-05-004/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-05-004.yaml)
