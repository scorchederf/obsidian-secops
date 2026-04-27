---
car_id: "CAR-2019-04-003"
title: "Squiblydoo"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2019-04-003/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2019-04-003.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2019-04-003"
  - "Squiblydoo"
attack_technique_ids:
  - "T1218"
  - "T1218.010"
platforms:
  - "Windows"
implementation_types:
  - "splunk"
  - "EQL"
  - "psuedocode"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CAR-2019-04-003: Squiblydoo

## Metadata

- CAR ID: CAR-2019-04-003
- Submission Date: 2019/04/24
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: MITRE

## Description

Squiblydoo is a specific usage of regsvr32.dll to load a COM scriptlet directly from the internet and execute it in a way that bypasses application whitelisting. It can be seen by looking for regsvr32.exe executions that load the scrobj.dll (which execute the COM scriptlet) or, if that is too noisy, those that also load content directly via HTTP or HTTPS.

Squiblydoo was first written up by Casey Smith at Red Canary, though that blog post is no longer accessible.

## ATT&CK Coverage

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]] (coverage: Moderate; tactics: TA0005)
  - [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.010]]

## Implementations

### splunk

This looks for any and all usage of the scrobj DLL, which is what is used to run COM scriptlets, so it'll detect both loading from network as well as filesystem. This will have almost zero false positives so is suitable for alerting.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_events__ EventCode=1 regsvr32.exe scrobj.dll | search Image="*regsvr32.exe"
```

### EQL

EQL version of the above Splunk search.

- Data Model: EQL native

```eql
process where subtype.create and
  (process_path == "*regsvr32.exe" and command_line == "*scrobj.dll")
```

### psuedocode

Pseudocode version of the above Splunk search.

- Data Model: CAR

```psuedocode
processes = search Process:Create
squiblydoo_processes = filter processes where (
  image_path == "*regsvr32.exe" and command_line == "*scrobj.dll"
  )
output squiblydoo_processes
```

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 image="*\regsvr32.exe" command="*scrobj.dll"
```

## Data Model References

- process/create/exe
- process/create/command_line

## Unit Tests

The [Atomic Red Team test for Squiblydoo](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1117/T1117.md#atomic-test-2---regsvr32-remote-com-scriptlet-execution) is a good test case for this.

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2019-04-003/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2019-04-003.yaml)
