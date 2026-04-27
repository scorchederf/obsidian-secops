---
car_id: "CAR-2021-05-012"
title: "Create Service In Suspicious File Path"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-05-012/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-05-012.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2021-05-012"
  - "Create Service In Suspicious File Path"
attack_technique_ids:
  - "T1569"
  - "T1569.001"
  - "T1569.002"
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

# CAR-2021-05-012: Create Service In Suspicious File Path

## Metadata

- CAR ID: CAR-2021-05-012
- Submission Date: 2021/05/11
- Update Date: 2021/04/05
- Information Domain: Analytic
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Splunk Threat Research <research@splunk.com>

## Description

This detection is to identify a creation of "user mode service" where the service file path is located in non-common service folder in windows.

## ATT&CK Coverage

- [[kb/attack/techniques/T1569-system_services|T1569]] (coverage: Moderate; tactics: TA0002)
  - [[kb/attack/techniques/T1569-system_services|T1569.001]]
  - [[kb/attack/techniques/T1569-system_services|T1569.002]]

## Implementations

### Pseudocode

Pseudocode implementation of the Splunk search below.

- Data Model: CAR native

```pseudocode
services = search Service:create
suspicious_services = filter services where image_path = "*\.exe" AND image_path does not contain ["C:\\Windows\\*", "%windir%\\*", "C:\\Program File*", "C:\\Programdata\\*", "%systemroot%\\*"] )
output suspicious_services
```

### Splunk

To successfully implement this search, you need to be ingesting logs with the Service name, Service File Name Service Start type, and Service Type from your endpoints.

- Data Model: Endpoint

```splunk
 `wineventlog_system` EventCode=7045  Service_File_Name = "*\.exe" NOT (Service_File_Name IN ("C:\\Windows\\*", "%windir%\\*", "C:\\Program File*", "C:\\Programdata\\*", "%systemroot%\\*")) Service_Type = "user mode service" | stats count min(_time) as firstTime max(_time) as lastTime by EventCode Service_File_Name Service_Name Service_Start_Type Service_Type
```

## Data Model References

- service/create/image_path

## Unit Tests

Replay the detection [dataset](https://media.githubusercontent.com/media/splunk/attack_data/master/datasets/malware/clop/clop_a/windows-system.log) using the Splunk attack range with the commands below

- Configurations: Using Splunk [Attack Range](https://github.com/splunk/attack_range)

```text
python attack_range.py replay -dn data_dump [--dump NAME_OF_DUMP]
```

execute the atomic test [T1569.001](https://github.com/redcanaryco/atomic-red-team/tree/master/atomics/T1569.001) against a Windows target.

- Configurations: Using [Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam)

```text
Invoke-AtomicTest T1569.001
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2021-05-012/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-05-012.yaml)
