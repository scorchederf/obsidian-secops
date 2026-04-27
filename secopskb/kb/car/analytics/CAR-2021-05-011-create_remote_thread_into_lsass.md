---
car_id: "CAR-2021-05-011"
title: "Create Remote Thread into LSASS"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-05-011/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-05-011.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2021-05-011"
  - "Create Remote Thread into LSASS"
attack_technique_ids:
  - "T1003"
  - "T1003.001"
platforms:
  - "Windows"
implementation_types:
  - "Pseudocode"
  - "Splunk"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CAR-2021-05-011: Create Remote Thread into LSASS

## Metadata

- CAR ID: CAR-2021-05-011
- Submission Date: 2021/05/11
- Information Domain: Analytic
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Splunk Threat Research <research@splunk.com>

## Description

Actors may create a remote thread into the LSASS service as part of a workflow to dump credentials.

## ATT&CK Coverage

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]] (coverage: Moderate; tactics: TA0006)
  - [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Implementations

### Pseudocode

Pseudocode implementation of the Splunk search below. The CAR data model does not currently contain a Target Image field, for remote thread creation, so this code Is somewhat inexact. See the Splunk implementation for a more precise search for the lsass image target.

- Data Model: CAR native

```pseudocode
remote_threads = search Thread:remote_create
lsass_remote_create = filter remote_threads where "lsass" in raw event
output lsass_remote_create
```

### Splunk

This search needs Sysmon Logs with a Sysmon configuration, which includes EventCode 8 with lsass.exe. This search uses an input macro named `sysmon`. We strongly recommend that you specify your environment-specific configurations (index, source, sourcetype, etc.) for Windows Sysmon logs. Replace the macro definition with configurations for your Splunk environment. The search also uses a post-filter macro designed to filter out known false positives.

```splunk
`sysmon` EventID=8 TargetImage=*lsass.exe | stats count min(_time) as firstTime max(_time) as lastTime by Computer, EventCode, TargetImage, TargetProcessId | rename Computer as dest
```

## Data Model References

- thread/remote_create

## Unit Tests

Replay the detection [dataset](https://media.githubusercontent.com/media/splunk/attack_data/master/datasets/attack_techniques/T1003.001/atomic_red_team/windows-sysmon.log) using the Splunk attack range with the commands below

- Configurations: Using Splunk [Attack Range](https://github.com/splunk/attack_range)

```text
python attack_range.py replay -dn data_dump [--dump NAME_OF_DUMP]
```

execute the atomic test [T1003.001](https://github.com/redcanaryco/atomic-red-team/tree/master/atomics/T1003.001) against a Windows target.

- Configurations: Using [Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam)

```text
Invoke-AtomicTest T1003.001
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2021-05-011/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-05-011.yaml)
