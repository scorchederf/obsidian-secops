---
car_id: "CAR-2016-03-002"
title: "Create Remote Process via WMIC"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2016-03-002/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2016-03-002.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2016-03-002"
  - "Create Remote Process via WMIC"
attack_technique_ids:
  - "T1047"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
  - "Splunk"
  - "EQL"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CAR-2016-03-002: Create Remote Process via WMIC

## Metadata

- CAR ID: CAR-2016-03-002
- Submission Date: 2016/03/28
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: MITRE

## Description

Adversaries may use [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) (WMI) to move laterally, by launching executables remotely.The analytic [[kb/car/analytics/CAR-2014-12-001-remotely_launched_executables_via_wmi|CAR-2014-12-001]] describes how to detect these processes with network traffic monitoring and process monitoring on the target host. However, if the command line utility `wmic.exe` is used on the source host, then it can additionally be detected on an analytic. The command line on the source host is constructed into something like `wmic.exe /node:"\<hostname\>" process call create "\<command line\>"`. It is possible to also connect via IP address, in which case the string `"\<hostname\>"` would instead look like `IP Address`.

Although this analytic was created after [[kb/car/analytics/CAR-2014-12-001-remotely_launched_executables_via_wmi|CAR-2014-12-001]], it is a much simpler (although more limited) approach. Processes can be created remotely via WMI in a few other ways, such as more direct API access or the built-in utility [PowerShell](https://attack.mitre.org/T1059/001).

## ATT&CK Coverage

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]] (coverage: Low; tactics: TA0002)

## Implementations

### pseudocode

Looks for instances of wmic.exe as well as the substrings in the command line:
* `process call create`
* `/node:`

```pseudocode
processes = search Process:Create
wmic = filter processes where (exe == "wmic.exe" and command_line == "* process call create *" and command_line == "* /node:*")
output wmic
```

### Splunk

Splunk version of the above pseudocode.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_index__ EventCode=1 Image="C:\\Windows\\*\\wmic.exe" CommandLine="* process call create *"|search CommandLine="* /node:*"
```

### EQL

EQL version of the above pseudocode.

- Data Model: EQL native

```eql
process where subtype.create and
  (process_name == "wmic.exe" and command_line == "* process call create ")
  |filter command_line == "* /node:*"
```

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 image="C:\\Windows\\*\\wmic.exe" command="* process call create *" command="* /node:*"
```

## Data Model References

- process/create/exe
- process/create/command_line

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2016-03-002/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2016-03-002.yaml)
