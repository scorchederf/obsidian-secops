---
car_id: "CAR-2021-05-010"
title: "Create local admin accounts using net exe"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-05-010/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-05-010.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2021-05-010"
  - "Create local admin accounts using net exe"
attack_technique_ids:
  - "T1136"
  - "T1136.001"
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

# CAR-2021-05-010: Create local admin accounts using net exe

## Metadata

- CAR ID: CAR-2021-05-010
- Submission Date: 2021/05/11
- Information Domain: Analytic
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Splunk Threat Research <research@splunk.com>

## Description

This search looks for the creation of local administrator accounts using net.exe.

## ATT&CK Coverage

- [[kb/attack/techniques/T1136-create_account|T1136]] (coverage: Moderate; tactics: TA0003)
  - [[kb/attack/techniques/T1136-create_account|T1136.001]]

## Implementations

### Pseudocode

Pseudocode implementation of the Splunk search below

- Data Model: CAR native

```pseudocode
processes = search Process:Create
certutil_downloads = filter processes where (
  (exe = C:\Windows\System32\net.exe OR exe = C:\Windows\System32\net1.exe ) AND (command_line = *localgroup* OR command_line = */add* OR command_line = *user* ))
output certutil_downloads
```

### Splunk

You must be ingesting data that records process activity from your hosts to populate the Endpoint data model in the Processes node. You must also be ingesting logs with both the process name and command line from your endpoints. The command-line arguments are mapped to the "process" field in the Endpoint data model.

- Data Model: Endpoint

```splunk
| tstats count values(Processes.user) as user values(Processes.parent_process) as parent_process min(_time) as firstTime max(_time) as lastTime from datamodel=Endpoint.Processes where (Processes.process_name=net.exe OR Processes.process_name=net1.exe) AND (Processes.process=*localgroup* OR Processes.process=*/add* OR Processes.process=*user*) by Processes.process Processes.process_name Processes.dest   |`create_local_admin_accounts_using_net_exe_filter`
```

## Data Model References

- process/create/exe
- process/create/command_line

## Unit Tests

Replay the detection [dataset](https://media.githubusercontent.com/media/splunk/attack_data/master/datasets/attack_techniques/T1136.001/atomic_red_team/windows-security.log)  using the Splunk attack range with the commands below

- Configurations: Using Splunk [Attack Range](https://github.com/splunk/attack_range)

```text
python attack_range.py replay -dn data_dump [--dump NAME_OF_DUMP]
```

execute the atomic test [T1136.001](https://github.com/redcanaryco/atomic-red-team/tree/master/atomics/T1136.001) against a Windows target.

- Configurations: Using [Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam)

```text
Invoke-AtomicTest T1136.001
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2021-05-010/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-05-010.yaml)
