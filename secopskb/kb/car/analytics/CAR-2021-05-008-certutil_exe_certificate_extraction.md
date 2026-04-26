---
car_id: "CAR-2021-05-008"
title: "Certutil exe certificate extraction"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-05-008/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-05-008.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2021-05-008"
  - "Certutil exe certificate extraction"
attack_technique_ids:
  - "T1606"
  - "T1606.002"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CAR-2021-05-008: Certutil exe certificate extraction

## Metadata

- CAR ID: CAR-2021-05-008
- Submission Date: 2021/05/11
- Information Domain: Analytic
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Splunk Threat Research <research@splunk.com>

## Description

This search looks for arguments to certutil.exe indicating the manipulation or extraction of Certificate. This certificate can then be used to sign new authentication tokens specially inside Federated environments such as Windows ADFS.

## ATT&CK Coverage

- [[kb/attack/techniques/T1606-forge_web_credentials|T1606]] (coverage: Moderate; tactics: TA0006)
  - [[kb/attack/techniques/T1606-forge_web_credentials|T1606.002]]

## Implementations

### Pseudocode

Pseudocode implementation of the Splunk search below

- Data Model: CAR native

```pseudocode
processes = search Process:Create
certutil_downloads = filter processes where (
  exe =”C:\Windows\System32\certutil.exe” AND command_line = * -exportPFX * )
output certutil_downloads
```

### Splunk

Splunk implementation

- Data Model: Endpoint

```splunk
| tstats count min(_time) as firstTime values(Processes.process) as process max(_time) as lastTime from datamodel=Endpoint.Processes where Processes.process_name=certutil.exe Processes.process = "* -exportPFX *" by Processes.parent_process Processes.process_name Processes.process Processes.user
```

## Data Model References

- process/create/exe
- process/create/command_line

## Unit Tests

Replay the detection [dataset](https://media.githubusercontent.com/media/splunk/attack_data/master/datasets/suspicious_behaviour/certutil_exe_certificate_extraction/windows-sysmon.log) using the Splunk attack range with the commands below

- Configurations: Using Splunk [Attack Range](https://github.com/splunk/attack_range)

```text
python attack_range.py replay -dn data_dump [--dump NAME_OF_DUMP]
```

Execute the atomic test [T1606.002](https://github.com/redcanaryco/atomic-red-team/tree/master/atomics/T1606.002) against a Windows target.

- Configurations: Using [Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam)

```text
Invoke-AtomicTest T1606.002
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2021-05-008/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-05-008.yaml)
