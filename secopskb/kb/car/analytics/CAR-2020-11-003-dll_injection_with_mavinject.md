---
car_id: "CAR-2020-11-003"
title: "DLL Injection with Mavinject"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2020-11-003/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-11-003.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2020-11-003"
  - "DLL Injection with Mavinject"
attack_technique_ids:
  - "T1055"
  - "T1055.001"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CAR-2020-11-003: DLL Injection with Mavinject

## Metadata

- CAR ID: CAR-2020-11-003
- Submission Date: 2020/11/30
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Olaf Hartong

## Description

Injecting a malicious DLL into a process is a common adversary TTP. Although the ways of doing this are numerous, mavinject.exe is a commonly used tool for doing so because it roles up many of the necessary steps into one, and is available within Windows. Attackers may rename the executable, so we also use the common argument "INJECTRUNNING" as a related signature here. Whitelisting certain applications may be necessary to reduce noise for this analytic.

## ATT&CK Coverage

- [[kb/attack/techniques/T1055-process_injection|T1055]] (coverage: Low; tactics: TA0004, TA0005)
  - [[kb/attack/techniques/T1055-process_injection|T1055.001]]

## Implementations

### Pseudocode

This is a pseudocode representation of the below splunk search.

- Data Model: CAR native

```pseudocode
processes = search Process:Create
mavinject_processes = filter processes where (
  exe = "C:\\Windows\\SysWOW64\\mavinject.exe" OR Image="C:\\Windows\\System32\\mavinject.exe" OR command_line = "*/INJECTRUNNING*"
output mavinject_processes
```

### Splunk

Search for instances of mavinject.exe or mavinject32.exe

- Data Model: Sysmon native

```splunk
(index=__your_sysmon_index__ EventCode=1) (Image="C:\\Windows\\SysWOW64\\mavinject.exe" OR Image="C:\\Windows\\System32\\mavinject.exe" OR CommandLine="*\INJECTRUNNING*")
```

### LogPoint

Search for instances of mavinject.exe or mavinject32.exe

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 (image="C:\Windows\SysWOW64\mavinject.exe" OR image="C:\Windows\System32\mavinject.exe" OR command="*\INJECTRUNNING*")
```

## Data Model References

- process/create/exe
- process/create/command_line

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2020-11-003/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-11-003.yaml)
