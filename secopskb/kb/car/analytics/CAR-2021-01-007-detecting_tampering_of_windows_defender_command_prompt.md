---
car_id: "CAR-2021-01-007"
title: "Detecting Tampering of Windows Defender Command Prompt"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-01-007/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-01-007.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2021-01-007"
  - "Detecting Tampering of Windows Defender Command Prompt"
attack_technique_ids:
  - "T1562"
  - "T1562.001"
platforms:
  - "Windows"
implementation_types:
  - "Splunk"
  - "pseudocode"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CAR-2021-01-007: Detecting Tampering of Windows Defender Command Prompt

## Metadata

- CAR ID: CAR-2021-01-007
- Submission Date: 2020/12/11
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Cyware Labs

## Description

In an attempt to avoid detection after compromising a machine, threat actors often try to disable Windows Defender. This is often done using “sc” [service control], a legitimate tool provided by Microsoft for managing services. This action interferes with event detection and may lead to a security event going undetected, thereby potentially leading to further compromise of the network.

## ATT&CK Coverage

- [[kb/attack/techniques/T1562-impair_defenses|T1562]] (coverage: Medium; tactics: TA0005)
  - [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Implementations

### Splunk

This query looks for the specific use of service control for querying or trying to stop Windows Defender.

- Data Model: Sysmon native

```splunk
index= __your_sysmon__index__ EventCode=1 Image = "C:\\Windows\\System32\\sc.exe"  | regex CommandLine="^sc\s*(config|stop|query)\sWinDefend$"
```

### pseudocode

This query looks for the specific use of service control for querying or trying to stop Windows Defender.

```pseudocode
processes = search Process:Create
target_processes = filter processes where (
                   (exe="C:\\Windows\\System32\\sc.exe") AND (command_line="sc *config*" OR command_line="sc *stop*" OR command_line="sc *query*")
                   )
output target_processes
```

## Data Model References

- process/create/command_line

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2021-01-007/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-01-007.yaml)
