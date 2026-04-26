---
car_id: "CAR-2014-11-003"
title: "Debuggers for Accessibility Applications"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2014-11-003/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-11-003.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2014-11-003"
  - "Debuggers for Accessibility Applications"
attack_technique_ids:
  - "T1546"
  - "T1546.008"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CAR-2014-11-003: Debuggers for Accessibility Applications

## Metadata

- CAR ID: CAR-2014-11-003
- Submission Date: 2014/11/21
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: MITRE

## Description

The Windows Registry location `HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options` allows for parameters to be set for applications during execution. One feature used by malicious actors is the "Debugger" option. When a key has this value enabled, a Debugging command line can be specified. Windows will launch the Debugging command line, and pass the original command line in as an argument. Adversaries can set a Debugger for [Accessibility Applications](https://attack.mitre.org/techniques/T1546/008). The analytic looks for the original command line as an argument to the Debugger. When the strings "sethc.exe", "utilman.exe", "osk.exe", "narrator.exe", and "Magnify.exe" are detected in the arguments, but not as the main executable, it is very likely that a Debugger is set.

This analytic could depend on the possibility of the known strings used as arguments for other applications used in the day-to-day environment. Although the chance of the string "sethc.exe" being used as an argument for another application is unlikely, it still is a possibility.

## ATT&CK Coverage

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546]] (coverage: Moderate; tactics: TA0004, TA0003)
  - [[kb/attack/techniques/T1546-event_triggered_execution|T1546.008]]

## Implementations

### pseudocode

One simple way to implement this technique is to note that in a default Windows configuration there are no spaces in the path to the `system32` folder. If the accessibility programs are ever run with a Debugger set, then Windows will launch the Debugger process and append the command line to the accessibility program. As a result, a space is inserted in the command line before the path. Looking for any instances of a space in the command line before the name of an accessibility program will help identify when Debuggers are set.

```pseudocode
process = search Process:Create
debuggers = filter process where (command_line match "$.* .*(sethc{{pipe}}utilman{{pipe}}osk{{pipe}}narrator{{pipe}}magnify)\.exe")
output debuggers
```

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 command IN ["$* *sethc.exe", "$* *utilman.exe", "$* *osk.exe", "$* *narrator.exe", "$* *magnify.exe"]
```

## Data Model References

- process/create/command_line
- process/create/exe

## Unit Tests

Although it does not actually utilize the Debugging command line, an easy way to test this analytic to run cmd.exe from a command window, supplying one of the strings as arguments.

- Configurations: Windows 7

```text
cmd.exe Magnify.exe
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PLA-process_lineage_analysis|D3-PLA: Process Lineage Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2014-11-003/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-11-003.yaml)
