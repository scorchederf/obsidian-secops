---
car_id: "CAR-2021-05-009"
title: "CertUtil With Decode Argument"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-05-009/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-05-009.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2021-05-009"
  - "CertUtil With Decode Argument"
attack_technique_ids:
  - "T1140"
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

# CAR-2021-05-009: CertUtil With Decode Argument

## Metadata

- CAR ID: CAR-2021-05-009
- Submission Date: 2021/05/11
- Information Domain: Analytic
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Splunk Threat Research <research@splunk.com>

## Description

CertUtil.exe may be used to `encode` and `decode` a file, including PE and script code. Encoding will convert a file to base64 with `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` tags. Malicious usage will include decoding a encoded file that was downloaded. Once decoded, it will be loaded by a parallel process. Note that there are two additional command switches that may be used - `encodehex` and `decodehex`. Similarly, the file will be encoded in HEX and later decoded for further execution. During triage, identify the source of the file being decoded. Review its contents or execution behavior for further analysis.

## ATT&CK Coverage

- [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140]] (coverage: Moderate; tactics: TA0005)

## Implementations

### Pseudocode

Pseudocode implementation of the Splunk search below

- Data Model: CAR native

```pseudocode
processes = search Process:Create
certutil_downloads = filter processes where (
  exe =”C:\Windows\System32\certutil.exe” AND command_line = *decode* )
output certutil_downloads
```

### Splunk

To successfully implement this search you need to be ingesting information on process that include the name of the process responsible for the changes from your endpoints into the `Endpoint` datamodel in the `Processes` node.

- Data Model: Endpoint

```splunk
| tstats count min(_time) as firstTime max(_time) as lastTime from datamodel=Endpoint.Processes where Processes.process_name=certutil.exe Processes.process=*decode* by Processes.dest Processes.user Processes.parent_process Processes.process_name Processes.process Processes.process_id Processes.parent_process_id
```

## Data Model References

- process/create/exe
- process/create/command_line

## Unit Tests

Replay the detection [dataset](https://media.githubusercontent.com/media/splunk/attack_data/master/datasets/attack_techniques/T1140/atomic_red_team/windows-sysmon.log) using the Splunk attack range with the commands below

- Configurations: Using Splunk [Attack Range](https://github.com/splunk/attack_range)

```text
python attack_range.py replay -dn data_dump [--dump NAME_OF_DUMP]
```

execute the atomic test [T1140](https://github.com/redcanaryco/atomic-red-team/tree/master/atomics/T1140) against a Windows target.

- Configurations: Using [Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam)

```text
Invoke-AtomicTest T1140
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2021-05-009/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-05-009.yaml)
