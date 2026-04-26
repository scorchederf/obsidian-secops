---
car_id: "CAR-2021-01-003"
title: "Clearing Windows Logs with Wevtutil"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-01-003/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-01-003.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2021-01-003"
  - "Clearing Windows Logs with Wevtutil"
attack_technique_ids:
  - "T1070"
  - "T1070.001"
platforms:
  - "Windows"
implementation_types:
  - "Splunk"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CAR-2021-01-003: Clearing Windows Logs with Wevtutil

## Metadata

- CAR ID: CAR-2021-01-003
- Submission Date: 2020/12/02
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Cyware Labs

## Description

In an attempt to clear traces after compromising a machine, threat actors often try to clear Windows Event logs. This is often done using “wevtutil”, a legitimate tool provided by Microsoft. This action interferes with event collection and notification, and may lead to a security event going undetected, thereby potentially leading to further compromise of the network.

## ATT&CK Coverage

- [[kb/attack/techniques/T1070-indicator_removal|T1070]] (coverage: Low; tactics: TA0005)
  - [[kb/attack/techniques/T1070-indicator_removal|T1070.001]]

## Implementations

### Splunk

This search query looks for an instance where wevtutil is invoked along with a command that may cause the system to remove Windows Event logs.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_index__ sourcetype= __your__windows__sysmon__sourcetype EventCode=1 Image=*wevtutil* CommandLine=*cl* (CommandLine=*System* OR CommandLine=*Security* OR CommandLine=*Setup* OR CommandLine=*Application*)
```

## Data Model References

- process/create/command_line

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2021-01-003/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-01-003.yaml)
