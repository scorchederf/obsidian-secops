---
car_id: "CAR-2021-05-005"
title: "BITSAdmin Download File"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-05-005/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-05-005.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2021-05-005"
  - "BITSAdmin Download File"
attack_technique_ids:
  - "T1197"
  - "T1105"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# CAR-2021-05-005: BITSAdmin Download File

## Metadata

- CAR ID: CAR-2021-05-005
- Submission Date: 2021/05/11
- Information Domain: Analytic
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Splunk Threat Research <research@splunk.com>

## Description

The following query identifies Microsoft Background Intelligent Transfer Service utility `bitsadmin.exe` using the `transfer` parameter to download a remote object. In addition, look for `download` or `upload` on the command-line, the switches are not required to perform a transfer. Capture any files downloaded. Review the reputation of the IP or domain used. Typically once executed, a follow on command will be used to execute the dropped file. Note that the network connection or file modification events related will not spawn or create from `bitsadmin.exe`, but the artifacts will appear in a parallel process of `svchost.exe` with a command-line similar to `svchost.exe -k netsvcs -s BITS`. It's important to review all parallel and child processes to capture any behaviors and artifacts. In some suspicious and malicious instances, BITS jobs will be created. You can use `bitsadmin /list /verbose` to list out the jobs during investigation.

## ATT&CK Coverage

- [[kb/attack/techniques/T1197-bits_jobs|T1197]] (coverage: Moderate; tactics: TA0005, TA0003)
- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]] (coverage: Moderate; tactics: TA0011)

## Implementations

### Pseudocode

Pseudocode implementation of the Splunk search below

- Data Model: CAR native

```pseudocode
processes = search Process:Create
bitsadmin_commands = filter processes where (
  exe ="C:\Windows\System32\bitsadmin.exe" AND command_line = *transfer*)
output bitsadmin_commands
```

### Splunk

To successfully implement this search you need to be ingesting information on process that include the name of the process responsible for the changes from your endpoints into the `Endpoint` datamodel in the `Processes` node.

- Data Model: Endpoint

```splunk
| tstats count min(_time) as firstTime max(_time) as lastTime from datamodel=Endpoint.Processes where Processes.process_name=bitsadmin.exe Processes.process=*transfer* by Processes.dest Processes.user Processes.parent_process Processes.process_name Processes.process Processes.process_id Processes.parent_process_id
```

## Data Model References

- process/create/exe
- process/create/command_line

## Unit Tests

Replay the detection [dataset](https://media.githubusercontent.com/media/splunk/attack_data/master/datasets/attack_techniques/T1197/atomic_red_team/windows-sysmon.log) using the Splunk attack range with the commands below

- Configurations: Using Splunk [Attack Range](https://github.com/splunk/attack_range)

```text
python attack_range.py replay -dn data_dump [--dump NAME_OF_DUMP]
```

execute the atomic test [T1197](https://github.com/redcanaryco/atomic-red-team/tree/master/atomics/T1197) against a Windows target.

- Configurations: Using [Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam)

```text
Invoke-AtomicTest T1197
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2021-05-005/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-05-005.yaml)
