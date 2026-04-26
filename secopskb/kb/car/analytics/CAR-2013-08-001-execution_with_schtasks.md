---
car_id: "CAR-2013-08-001"
title: "Execution with schtasks"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2013-08-001/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-08-001.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2013-08-001"
  - "Execution with schtasks"
attack_technique_ids:
  - "T1053"
  - "T1053.005"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
  - "DNIF"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CAR-2013-08-001: Execution with schtasks

## Metadata

- CAR ID: CAR-2013-08-001
- Submission Date: 2013/08/07
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: MITRE

## Description

The Windows built-in tool `schtasks.exe` provides the creation, modification, and running of [scheduled tasks](https://attack.mitre.org/techniques/T1053) on a local or remote computer. It is provided as a more flexible alternative to `at.exe`, described in [[kb/car/analytics/CAR-2013-05-004-execution_with_at|CAR-2013-05-004]]. Although used by adversaries, the tool is also legitimately used by administrators, scripts, and software configurations. The scheduled tasks tool can be used to gain [Persistence](https://attack.mitre.org/tactics/TA0003) and can be used in combination with a [Lateral Movement](https://attack.mitre.org/tactics/TA0008) technique to remotely gain [execution](https://attack.mitre.org/tactics/TA0002). Additionally, the command has parameters to specify the user and password responsible for creating the task, as well as the user and password combination that the task will run as. The `/s` flag specifies the remote system on which the task should be scheduled, usually indicating [Lateral Movement](https://attack.mitre.org/tactics/TA0008).

## ATT&CK Coverage

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053]] (coverage: Moderate; tactics: TA0003)
  - [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Implementations

### pseudocode

Look for instances of `schtasks.exe` running as processes. The `command_line` field is necessary to disambiguate between types of schtasks commands. These include the flags `/create`, `/run`, `/query`, `/delete`, `/change`, and `/end`.

```pseudocode
process = search Process:Create
schtasks = filter process where (exe == "schtasks.exe")
output schtasks
```

### DNIF

DNIF version of the above pseudocode.

- Data Model: Sysmon native

```dnif
_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 AND $App=schtasks.exe AND $Process=regex(.*(\/create|\/run|\/query|\/delete|\/change|\/end).*)i limit 100
```

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 image="*\schtasks.exe" command IN ["*/create*", "*/run*", "*/query*", "*/delete*", "*/change*", "*/end*"]
```

## Data Model References

- process/create/exe
- process/create/command_line

## Unit Tests

Create a new scheduled task with schtasks.exe and verify the analytic fires when the task executes.
* From an admin account, open Windows command prompt (right click, run as administrator)
* Execute `schtasks /Create /SC ONCE /ST 19:00 /TR C:\Windows\System32\calc.exe /TN calctask`, substituting a time in the near future for 19:00
* The program should respond with “SUCCESS: The scheduled task “calctask” has successfully been created.”
* The program should execute at the time specified. This is what the analytic should fire on.
* To remove the scheduled task, execute `schtasks /Delete /TN calctask`.
* The program should respond with “SUCCESS: The scheduled task “calctask” was successfully deleted.”

- Configurations: Windows 7

```text
schtasks /Create /SC ONCE /ST 19:00 /TR C:\Windows\System32\calc.exe /TN calctask
schtasks /Delete /TN calctask
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-SJA-scheduled_job_analysis|D3-SJA: Scheduled Job Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2013-08-001/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-08-001.yaml)
