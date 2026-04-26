---
car_id: "CAR-2021-05-006"
title: "CertUtil Download With URLCache and Split Arguments"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-05-006/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-05-006.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2021-05-006"
  - "CertUtil Download With URLCache and Split Arguments"
attack_technique_ids:
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CAR-2021-05-006: CertUtil Download With URLCache and Split Arguments

## Metadata

- CAR ID: CAR-2021-05-006
- Submission Date: 2021/05/11
- Information Domain: Analytic
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Splunk Threat Research <research@splunk.com>

## Description

Certutil.exe may download a file from a remote destination using `-urlcache`. This behavior does require a URL to be passed on the command-line. In addition, `-f` (force) and `-split` (Split embedded ASN.1 elements, and save to files) will be used. It is not entirely common for `certutil.exe` to contact public IP space. However, it is uncommon for `certutil.exe` to write files to world writeable paths.\ During triage, capture any files on disk and review. Review the reputation of the remote IP or domain in question.

## ATT&CK Coverage

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]] (coverage: Moderate; tactics: TA0011)

## Implementations

### Pseudocode

Pseudocode implementation of the Splunk search below

- Data Model: CAR native

```pseudocode
processes = search Process:Create
certutil_downloads = filter processes where (
  exe ="C:\Windows\System32\certutil.exe" AND command_line = *urlcache* AND command_line = *split*)
output certutil_downloads
```

### Splunk

To successfully implement this search you need to be ingesting information on process that include the name of the process responsible for the changes from your endpoints into the `Endpoint` datamodel in the `Processes` node.

- Data Model: Endpoint

```splunk
| tstats count min(_time) as firstTime max(_time) as lastTime from datamodel=Endpoint.Processes where Processes.process_name=certutil.exe Processes.process=*urlcache* Processes.process=*split* by Processes.dest Processes.user Processes.parent_process Processes.process_name Processes.process Processes.process_id Processes.parent_process_id
```

## Data Model References

- process/create/exe
- process/create/command_line

## Unit Tests

Replay the detection [dataset](https://media.githubusercontent.com/media/splunk/attack_data/master/datasets/attack_techniques/T1105/atomic_red_team/windows-sysmon.log)  using the Splunk attack range with the commands below

- Configurations: Using Splunk [Attack Range](https://github.com/splunk/attack_range)

```text
python attack_range.py replay -dn data_dump [--dump NAME_OF_DUMP]
```

execute the atomic test [T1105](https://github.com/redcanaryco/atomic-red-team/tree/master/atomics/T1105) against a Windows target.

- Configurations: Using [Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam)

```text
Invoke-AtomicTest T1105
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2021-05-006/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-05-006.yaml)
