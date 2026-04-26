---
car_id: "CAR-2021-05-002"
title: "Batch File Write to System32"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-05-002/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-05-002.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2021-05-002"
  - "Batch File Write to System32"
attack_technique_ids:
  - "T1204"
  - "T1204.002"
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

# CAR-2021-05-002: Batch File Write to System32

## Metadata

- CAR ID: CAR-2021-05-002
- Submission Date: 2021/05/11
- Information Domain: Analytic
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Splunk Threat Research <research@splunk.com>

## Description

While batch files are not inherently malicious, it is uncommon to see them created after OS installation, especially in the Windows directory. This analytic looks for the suspicious activity of a batch file being created within the C:\Windows\System32 directory tree. There will be only occasional false positives due to administrator actions.

## ATT&CK Coverage

- [[kb/attack/techniques/T1204-user_execution|T1204]] (coverage: Moderate; tactics: TA0002)
  - [[kb/attack/techniques/T1204-user_execution|T1204.002]]

## Implementations

### Pseudocode

Pseudocode implementation of the Splunk search below

- Data Model: CAR native

```pseudocode
files = search File:create
batch_files = filter files where (
  extension =".bat" AND file_path = "C:\Windows\system32*" )
output batch_files
```

### Splunk

You must be ingesting data that records the file-system activity from your hosts to populate the Endpoint file-system data-model node. If you are using Sysmon, you will need a Splunk Universal Forwarder on each endpoint from which you want to collect data.

- Data Model: Endpoint

```splunk
| tstats count min(_time) as firstTime max(_time) as lastTime values(Filesystem.dest) as dest values(Filesystem.file_name) as file_name values(Filesystem.user) as user from datamodel=Endpoint.Filesystem by Filesystem.file_path   | rex field=file_name "(?<file_extension>\.[^\.]+)$" | search file_path=*system32* AND file_extension=.bat
```

## Data Model References

- file/create/extension
- file/create/file_path

## Unit Tests

Replay the detection [dataset](https://media.githubusercontent.com/media/splunk/attack_data/master/datasets/attack_techniques/T1204.002/batch_file_in_system32/windows-sysmon.log) using the Splunk attack range with the commands below

- Configurations: Using Splunk [Attack Range](https://github.com/splunk/attack_range)

```text
python attack_range.py replay -dn data_dump [--dump NAME_OF_DUMP]
```

execute the atomic test [T1204.002](https://github.com/redcanaryco/atomic-red-team/tree/master/atomics/T1204.002) against a Windows target.

- Configurations: Using [Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam)

```text
Invoke-AtomicTest T1204.002
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2021-05-002/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-05-002.yaml)
