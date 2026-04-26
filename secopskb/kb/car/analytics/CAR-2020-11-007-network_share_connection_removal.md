---
car_id: "CAR-2020-11-007"
title: "Network Share Connection Removal"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2020-11-007/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-11-007.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2020-11-007"
  - "Network Share Connection Removal"
attack_technique_ids:
  - "T1070"
  - "T1070.005"
platforms:
  - "Windows"
implementation_types:
  - "Pseudocode"
  - "Splunk"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# CAR-2020-11-007: Network Share Connection Removal

## Metadata

- CAR ID: CAR-2020-11-007
- Submission Date: 2020/11/30
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Olaf Hartong

## Description

Adversaries may use network shares to exfliltrate date; they will then remove the shares to cover their tracks. This analytic looks for the removal of network shares via commandline, which is otherwise a rare event.

## ATT&CK Coverage

- [[kb/attack/techniques/T1070-indicator_removal|T1070]] (coverage: High; tactics: TA0005)
  - [[kb/attack/techniques/T1070-indicator_removal|T1070.005]]

## Implementations

### Pseudocode

This is a pseudocode representation of the below splunk search.

- Data Model: CAR native

```pseudocode
processes = search Process:Create
target_processes = filter processes where (
  (exe="C:\\Windows\\System32\\net.exe" AND command_line="*delete*") OR
  command_line="*Remove-SmbShare*" OR
  comman_line="*Remove-FileShare*" )
output target_processes
```

### Splunk

looks network shares being deleted from the command line

- Data Model: Sysmon native

```splunk
(index=__your_sysmon_index__ EventCode=1) ((Image="C:\\Windows\\System32\\net.exe" AND CommandLine="*delete*") OR CommandLine="*Remove-SmbShare*" OR CommandLine="*Remove-FileShare*")
```

### LogPoint

looks network shares being deleted from the command line

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 ((image="C:\Windows\System32\net.exe" command="*delete*") OR command="*Remove-SmbShare*" OR command="*Remove-FileShare*")
```

## Data Model References

- process/create/exe
- process/create/command_line

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2020-11-007/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-11-007.yaml)
