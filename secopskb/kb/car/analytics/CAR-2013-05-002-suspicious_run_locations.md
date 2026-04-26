---
car_id: "CAR-2013-05-002"
title: "Suspicious Run Locations"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2013-05-002/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-05-002.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2013-05-002"
  - "Suspicious Run Locations"
attack_technique_ids:
  - "T1036"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
  - "DNIF"
  - "Sigma"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

# CAR-2013-05-002: Suspicious Run Locations

## Metadata

- CAR ID: CAR-2013-05-002
- Submission Date: 2013/05/07
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: MITRE

## Description

In Windows, files should never execute out of certain directory locations. Any of these locations may exist for a variety of reasons, and executables may be present in the directory but should not execute. As a result, some defenders make the mistake of ignoring these directories and assuming that a process will never run from one. There are known TTPs that have taken advantage of this fact to go undetected. This fact should inform defenders to monitor these directories more closely, knowing that they should never contain running processes.

Monitors the directories

-   `*:\RECYCLER`
-   `*:\SystemVolumeInformation`
-   `%systemroot%\Tasks`
-   `%systemroot%\debug`

## ATT&CK Coverage

- [[kb/attack/techniques/T1036-masquerading|T1036]] (coverage: Low; tactics: TA0005)

## Implementations

### pseudocode

The RECYCLER and SystemVolumeInformation directories will be present on every drive. Replace %systemroot% and %windir% with the actual paths as configured by the endpoints.

```pseudocode
processes = search Process:Create
suspicious_locations = filter process where (
 image_path == "*:\RECYCLER\*" or
 image_path == "*:\SystemVolumeInformation\*" or
 image_path == "%windir%\Tasks\*" or
 image_path == "%systemroot%\debug\*"
)
output suspicious_locations
```

### DNIF

DNIF version of the above pseudocode.

- Data Model: Sysmon native

```dnif
_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 AND $Process=regex(.*(\:\\recycler\\|\:\\systemvolumeinformation\\|\%windir\%\\tasks\\|\%systemroot\%\\debug\\).*)i group count_unique $App limit 100
```

### Sigma

[Sigma version](https://github.com/Neo23x0/sigma/blob/master/rules/windows/process_creation/win_susp_run_locations.yml) of the above pseudocode, with some modifications.

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 image IN ["*:\RECYCLER\*", "*:\SystemVolumeInformation\*", "C:\Windows\Tasks\*", "C:\Windows\System32\debug\*"]
```

## Data Model References

- process/create/image_path

## Unit Tests

-   Typically %systemroot% is C:\\Windows but you can check this by running "echo %systemdrive%" at the command line.
-   Copy C:\\Windows\\system32\\notepad to C:\\Windows\\Tasks.
-   Run notepad. The analytic should fire.
-   Delete the executable to clean up from the test.

- Configurations: Windows 7

```text
copy C:\windows\system32\notepad.exe C:\windows\tasks
start C:\windows\tasks\notepad.exe
del C:\windows\tasks\notepad.exe
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2013-05-002/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-05-002.yaml)
