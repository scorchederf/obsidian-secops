---
car_id: "CAR-2020-09-003"
title: "Indicator Blocking - Driver Unloaded"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2020-09-003/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-09-003.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2020-09-003"
  - "Indicator Blocking - Driver Unloaded"
attack_technique_ids:
  - "T1562"
  - "T1562.006"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# CAR-2020-09-003: Indicator Blocking - Driver Unloaded

## Metadata

- CAR ID: CAR-2020-09-003
- Submission Date: 2020/09/10
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Olaf Hartong

## Description

Adversaries may attempt to evade system defenses by unloading minifilter drivers used by host-based sensors such as Sysmon through the use of the fltmc command-line utility. Accordingly, this analytic looks for command-line invocations of this utility when used to unload minifilter drivers.

## ATT&CK Coverage

- [[kb/attack/techniques/T1562-impair_defenses|T1562]] (coverage: Low; tactics: TA0005)
  - [[kb/attack/techniques/T1562-impair_defenses|T1562.006]]

## Implementations

### Pseudocode

This is a pseudocode representation of the below splunk search.

- Data Model: CAR native

```pseudocode
processes = search Process:Create
fltmc_processes = filter processes where (
  exe = "fltmc.exe" AND command_line = "*unload*")
output fltmc_processes
```

### Splunk

This Splunk search looks for process create events for the fltmc.exe utility and the specific command line used to unload minifilter drivers.

- Data Model: Sysmon native

```splunk
index=client EventCode=1 CommandLine="*unload*" (Image="C:\\Windows\\SysWOW64\\fltMC.exe" OR Image="C:\\Windows\\System32\\fltMC.exe")
```

### LogPoint

This LogPoint search looks for process create events for the fltmc.exe utility and the specific command line used to unload minifilter drivers.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon command="*unload*" (image="C:\Windows\SysWOW64\fltMC.exe" OR image="C:\Windows\System32\fltMC.exe")
```

## Data Model References

- process/create/exe
- process/create/command_line

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2020-09-003/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-09-003.yaml)
