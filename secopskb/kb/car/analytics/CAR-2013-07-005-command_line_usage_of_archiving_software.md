---
car_id: "CAR-2013-07-005"
title: "Command Line Usage of Archiving Software"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2013-07-005/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-07-005.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2013-07-005"
  - "Command Line Usage of Archiving Software"
attack_technique_ids:
  - "T1560"
  - "T1560.001"
platforms:
  - "Windows"
  - "Linux"
  - "macOS"
implementation_types:
  - "pseudocode"
  - "DNIF"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

# CAR-2013-07-005: Command Line Usage of Archiving Software

## Metadata

- CAR ID: CAR-2013-07-005
- Submission Date: 2013/07/31
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows, Linux, macOS
- Data Subtypes: Process
- Contributors: MITRE

## Description

Before [exfiltrating data](https://attack.mitre.org/tactics/TA0010) that an adversary has [collected](https://attack.mitre.org/tactics/TA0009), it is very likely that a [compressed archive](https://attack.mitre.org/techniques/T1560) will be created, so that transfer times are minimized and fewer files are transmitted. There is variety between the tools used to compress data, but the command line usage and context of archiving tools, such as ZIP, RAR, and 7ZIP, should be monitored.

In addition to looking for RAR or 7z program names, command line usage of 7Zip or RAR can be detected with the flag usage of "`\* a \*`". This is helpful, as adversaries may change program names.

## ATT&CK Coverage

- [[kb/attack/techniques/T1560-archive_collected_data|T1560]] (coverage: Moderate; tactics: TA0010)
  - [[kb/attack/techniques/T1560-archive_collected_data|T1560.001]]

## Implementations

### pseudocode

This analytic looks for the command line argument `a`, which is used by RAR. However, there may be other programs that have this as a legitimate argument and may need to be filtered out.

```pseudocode
processes = search Process:Create
rar_argument = filter processes where (command_line == "* a *")
output rar_argument
```

### DNIF

DNIF version of the above pseudocode.

- Data Model: Sysmon native

```dnif
_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 AND $Process=regex(.* a .*)i limit 100
```

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 command="* a *"
```

## Data Model References

- process/create/command_line

## Unit Tests

Download 7zip or other archiving software you plan to monitor. Create an innocuous text file for testing, or substitute an existing file.

- Configurations: Windows 7

```text
7z.exe a test.zip test.txt
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2013-07-005/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-07-005.yaml)
