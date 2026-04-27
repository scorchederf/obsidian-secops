---
car_id: "CAR-2021-05-004"
title: "BITS Job Persistence"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-05-004/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-05-004.yaml"
build_date: "2026-04-27 19:03:49"
aliases:
  - "CAR-2021-05-004"
  - "BITS Job Persistence"
attack_technique_ids:
  - "T1197"
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

The following query identifies Microsoft Background Intelligent Transfer Service utility `bitsadmin.exe` scheduling a BITS job to persist on an endpoint. The query identifies the parameters used to create, resume or add a file to a BITS job. Typically seen combined in a oneliner or ran in sequence. If identified, review the BITS job created and capture any files written to disk. It is possible for BITS to be used to upload files and this may require further network data analysis to identify. You can use `bitsadmin /list /verbose` to list out the jobs during investigation.

## ATT&CK Coverage

- [[kb/attack/techniques/T1197-bits_jobs|T1197: BITS Jobs]] (coverage: Moderate; tactics: TA0005, TA0003)

## Implementations

### Pseudocode

Pseudocode implementation of the splunk search below

- Data Model: CAR native

```pseudocode
processes = search Process:Create
bitsadmin_commands = filter processes where (
  exe ="C:\Windows\System32\bitsadmin.exe" AND command_line includes one of [*create*, *addfile*, *setnotifyflags*, *setnotifycmdline*, *setminretrydelay*, *setcustomheaders*,*resume*])
output bitsadmin_commands
```

### Splunk

To successfully implement this search you need to be ingesting information on process that include the name of the process responsible for the changes from your endpoints into the `Endpoint` datamodel in the `Processes` node.

- Data Model: Endpoint

```splunk
| tstats count min(_time) as firstTime max(_time) as lastTime from datamodel=Endpoint.Processes where Processes.process_name=bitsadmin.exe Processes.process IN (*create*, *addfile*, *setnotifyflags*, *setnotifycmdline*, *setminretrydelay*, *setcustomheaders*, *resume* ) by Processes.dest Processes.user Processes.parent_process Processes.process_name Processes.process Processes.process_id Processes.parent_process_id
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

- [CAR website](https://car.mitre.org/analytics/CAR-2021-05-004/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-05-004.yaml)
