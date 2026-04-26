---
car_id: "CAR-2013-02-003"
title: "Processes Spawning cmd.exe"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2013-02-003/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-02-003.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2013-02-003"
  - "Processes Spawning cmd.exe"
attack_technique_ids:
  - "T1059"
  - "T1059.003"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

# CAR-2013-02-003: Processes Spawning cmd.exe

## Metadata

- CAR ID: CAR-2013-02-003
- Submission Date: 2013/02/05
- Information Domain: Host
- Analytic Type: Situational Awareness
- Platforms: Windows
- Data Subtypes: Process
- Contributors: MITRE

## Description

The Windows [Command Prompt](https://en.wikipedia.org/wiki/cmd.exe) (`cmd.exe`) is a utility that provides a command line interface to Windows operating systems. It provides the ability to run additional programs and also has several built-in commands such as `dir`, `copy`, `mkdir`, and `type`, as well as batch scripts (`.bat`). Typically, when a user runs a command prompt, the parent process is `explorer.exe` or another instance of the prompt. There may be automated programs, logon scripts, or administrative tools that launch instances of the command prompt in order to run scripts or other built-in commands. Spawning the process `cmd.exe` from certain parents may be more indicative of malice. For example, if Adobe Reader or Outlook launches a command shell, this may suggest that a malicious document has been loaded and should be investigated. Thus, by looking for abnormal parent processes of `cmd.exe`, it may be possible to detect adversaries.

## ATT&CK Coverage

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]] (coverage: Moderate; tactics: TA0002)
  - [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]

## Implementations

### pseudocode

```pseudocode
process = search Process:Create
cmd = filter process where (exe == "cmd.exe")
output cmd
```

### DNIF

DNIF version of the above pseudocode.

- Data Model: Sysmon native

```dnif
_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 AND $Process=regex(.*cmd\.exe.*)i limit 100
```

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 image="*\cmd.exe"
```

## Data Model References

- process/create/exe
- process/create/parent_exe

## Unit Tests

Within a command prompt or powershell, run cmd.exe

- Configurations: Windows 7

## D3FEND Mappings

- [[kb/defend/techniques/D3-PLA-process_lineage_analysis|D3-PLA: Process Lineage Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2013-02-003/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-02-003.yaml)
