---
car_id: "CAR-2021-05-003"
title: "BCDEdit Failure Recovery Modification"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-05-003/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-05-003.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2021-05-003"
  - "BCDEdit Failure Recovery Modification"
attack_technique_ids:
  - "T1490"
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

# CAR-2021-05-003: BCDEdit Failure Recovery Modification

## Metadata

- CAR ID: CAR-2021-05-003
- Submission Date: 2021/05/11
- Information Domain: Analytic
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Splunk Threat Research <research@splunk.com>

## Description

This search looks for flags passed to bcdedit.exe modifications to the built-in Windows error recovery boot configurations. This is typically used by ransomware to prevent recovery.

## ATT&CK Coverage

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]] (coverage: Moderate; tactics: TA0040)

## Implementations

### Pseudocode

Pseudocode implementation of the splunk search below

- Data Model: CAR native

```pseudocode
processes = search Process:Create
bcdedit_commands = filter processes where (
  exe = "C:\Windows\System32\bcdedit.exe" AND command_line="*recoveryenabled*" )
output bcedit_commands
```

### Splunk

You must be ingesting endpoint data that tracks process activity, including parent-child relationships from your endpoints to populate the Endpoint data model in the Processes node. Tune based on parent process names.

- Data Model: Endpoint

```splunk
| tstats count min(_time) as firstTime max(_time) as lastTime from datamodel=Endpoint.Processes where Processes.process_name = bcdedit.exe Processes.process="*recoveryenabled*" (Processes.process="* no*") by Processes.process_name Processes.process Processes.parent_process_name Processes.dest Processes.user
```

## Data Model References

- process/create/exe
- process/create/command_line

## Unit Tests

Replay the detection [dataset](https://media.githubusercontent.com/media/splunk/attack_data/master/datasets/attack_techniques/T1490/atomic_red_team/windows-sysmon.log)  using the Splunk attack range with the commands below

- Configurations: Using Splunk [Attack Range](https://github.com/splunk/attack_range)

```text
python attack_range.py replay -dn data_dump [--dump NAME_OF_DUMP]
```

execute the atomic test [T1490](https://github.com/redcanaryco/atomic-red-team/tree/master/atomics/T1490) against a Windows target.

- Configurations: Using [Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam)

```text
Invoke-AtomicTest T1490
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]
- [[kb/defend/techniques/D3-PLA-process_lineage_analysis|D3-PLA: Process Lineage Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2021-05-003/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-05-003.yaml)
