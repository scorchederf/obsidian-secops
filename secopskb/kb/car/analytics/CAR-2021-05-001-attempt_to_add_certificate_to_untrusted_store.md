---
car_id: "CAR-2021-05-001"
title: "Attempt To Add Certificate To Untrusted Store"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-05-001/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-05-001.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2021-05-001"
  - "Attempt To Add Certificate To Untrusted Store"
attack_technique_ids:
  - "T1553"
  - "T1553.004"
platforms:
  - "Windows"
implementation_types:
  - "Splunk"
  - "Pseudocode"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

# CAR-2021-05-001: Attempt To Add Certificate To Untrusted Store

## Metadata

- CAR ID: CAR-2021-05-001
- Submission Date: 2021/05/11
- Information Domain: Analytic
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Splunk Threat Research <research@splunk.com>

## Description

Adversaries may add their own root certificate to the certificate store, to cause the web browser to trust that certificate and not display a security warning when it encounters the previously unseen certificate. This action may be the precursor to malicious activity.

## ATT&CK Coverage

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553]] (coverage: Moderate; tactics: TA0005)
  - [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.004]]

## Implementations

### Splunk

You must be ingesting data that records process activity from your hosts to populate the Endpoint data model in the Processes node. You must also be ingesting logs with both the process name and command line from your endpoints. The command-line arguments are mapped to the "process" field in the Endpoint data model.

- Data Model: Endpoint

```splunk
| tstats count min(_time) as firstTime values(Processes.process) as process max(_time) as lastTime from datamodel=Endpoint.Processes where Processes.process_name=*certutil* (Processes.process=*-addstore*) by Processes.parent_process Processes.process_name Processes.user
```

### Pseudocode

Pseudocode implementation of the splunk search below

- Data Model: CAR native

```pseudocode
processes = search Process:Create
addstore_commands = filter processes where (
  exe =”C:\Windows\System32\certutil.exe” AND command_line="*-addstore*” )
output addstore_commands
```

## Data Model References

- process/create/exe
- process/create/command_line

## Unit Tests

Replay the detection [dataset](https://media.githubusercontent.com/media/splunk/attack_data/master/datasets/attack_techniques/T1553.004/atomic_red_team/windows-sysmon.log) using the Splunk attack range with the commands below

- Configurations: Using Splunk [Attack Range](https://github.com/splunk/attack_range)

```text
python attack_range.py replay -dn data_dump [--dump NAME_OF_DUMP]
```

execute the atomic test [T1553.004](https://github.com/redcanaryco/atomic-red-team/tree/master/atomics/T1553.004) against a Windows target.

- Configurations: Using [Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam)

```text
Invoke-AtomicTest T1553.004
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2021-05-001/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-05-001.yaml)
