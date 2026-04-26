---
car_id: "CAR-2019-07-002"
title: "Lsass Process Dump via Procdump"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2019-07-002/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2019-07-002.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2019-07-002"
  - "Lsass Process Dump via Procdump"
attack_technique_ids:
  - "T1003"
  - "T1003.001"
platforms:
  - "Windows"
implementation_types:
  - "Pseudocode"
  - "Splunk"
  - "EQL"
  - "Sigma"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

# CAR-2019-07-002: Lsass Process Dump via Procdump

## Metadata

- CAR ID: CAR-2019-07-002
- Submission Date: 2019/07/29
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Kaushal Parikh/Cyware Labs, Tony Lambert/Red Canary, MITRE

## Description

[ProcDump](https://docs.microsoft.com/en-us/sysinternals/downloads/procdump) is a sysinternal command-line utility whose primary purpose is monitoring an application for CPU spikes and generating crash dumps during a spike that an administrator or developer can use to determine the cause of the spike.

ProcDump may be used to dump the memory space of lsass.exe to disk for processing with a credential access tool such as Mimikatz. This is performed by launching procdump.exe as a privileged user with command line options indicating that lsass.exe should be dumped to a file with an arbitrary name.

Note - the CAR data model currently does not support process access actions, so the pseudocode implementation is based around process creates.

## ATT&CK Coverage

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]] (coverage: Low; tactics: TA0006)
  - [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Implementations

### Pseudocode

This base pseudocode looks for process create events where an instance of procdump is executed that references lsass in the command-line.

```pseudocode
processes = search Process:Create
procdump_lsass = filter processes where (
  exe = "procdump*.exe"  and
  command_line = "*lsass*")
output procdump_lsass
```

### Splunk

A Splunk/Sysmon version of the above pseudocode.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_index__ EventCode=1 Image="*\\procdump*.exe" CommandLine="*lsass*"
```

### EQL

An [EQL Version](https://eqllib.readthedocs.io/en/latest/analytics/1e1ef6be-12fc-11e9-8d76-4d6bb837cda4.html) of the above pseudocode.

### Splunk

A related Splunk search, which instead of looking for process create events looks for process access events that target lsass.exe.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_index__ EventCode=10 TargetImage="C:\\WINDOWS\\system32\\lsass.exe" GrantedAccess="0x1FFFFF" ("procdump")
```

### Sigma

A [Sigma Version](https://github.com/Neo23x0/sigma/blob/master/rules/windows/sysmon/sysmon_lsass_memdump.yml) of the above Splunk search, with some more stringent criteria around calltrace.

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 image="*\procdump*.exe" command="*lsass*"
```

## Data Model References

- process/create/exe
- process/create/command_line

## Unit Tests

1. Open a Windows Command Prompt or PowerShell instance.
2. Navigate to folder containing ProcDump.
3. Execute procdump.exe -ma lsass.exe lsass_dump

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2019-07-002/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2019-07-002.yaml)
