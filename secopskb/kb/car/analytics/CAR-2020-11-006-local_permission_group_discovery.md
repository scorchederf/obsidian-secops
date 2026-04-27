---
car_id: "CAR-2020-11-006"
title: "Local Permission Group Discovery"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2020-11-006/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-11-006.yaml"
build_date: "2026-04-27 19:03:49"
aliases:
  - "CAR-2020-11-006"
  - "Local Permission Group Discovery"
attack_technique_ids:
  - "T1069"
  - "T1069.001"
  - "T1069.002"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Cyber actors frequently enumerate local or domain permissions groups. The net utility is usually used for this purpose. This analytic looks for any instances of net.exe, which is not normally used for benign purposes, although system administrator actions may trigger false positives.

## ATT&CK Coverage

- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069: Permission Groups Discovery]] (coverage: Moderate; tactics: TA0007)
  - [[kb/attack/techniques/T1069-permission_groups_discovery#^t1069001-local-groups|T1069.001: Local Groups]]
  - [[kb/attack/techniques/T1069-permission_groups_discovery#^t1069002-domain-groups|T1069.002: Domain Groups]]

## Implementations

### Pseudocode

This is a pseudocode representation of the below splunk search.

- Data Model: CAR native

```pseudocode
processes = search Process:Create
net_processes = filter processes where (
  exe = "net.exe" AND (
  command_line="*net* user*" OR
  command_line="*net* group*" OR
  command_line="*net* localgroup*" OR
  command_line="*get-localgroup*" OR
  command_line="*get-ADPrincipalGroupMembership*" )
output net_processes
```

### Splunk

Look for instances of net.exe

- Data Model: Sysmon native

```splunk
(index=__your_sysmon_index__ EventCode=1) Image="C:\\Windows\\System32\\net.exe" AND (CommandLine="* user*" OR CommandLine="* group*" OR CommandLine="* localgroup*" OR CommandLine="*get-localgroup*" OR CommandLine="*get-ADPrincipalGroupMembership*")
```

### LogPoint

Look for instances of net.exe

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 image="C:\Windows\System32\net.exe" (command="* user*" OR command="* group*" OR command="* localgroup*" OR command="*get-localgroup*" OR command="*get-ADPrincipalGroupMembership*")
```

## Data Model References

- process/create/exe
- process/create/command_line

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2020-11-006/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-11-006.yaml)
