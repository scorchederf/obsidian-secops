---
car_id: "CAR-2021-01-002"
title: "Unusually Long Command Line Strings"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-01-002/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-01-002.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2021-01-002"
  - "Unusually Long Command Line Strings"
attack_technique_ids:
  - "T1059"
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

# CAR-2021-01-002: Unusually Long Command Line Strings

## Metadata

- CAR ID: CAR-2021-01-002
- Submission Date: 2020/11/27
- Information Domain: Host
- Analytic Type: Anomaly
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Cyware Labs

## Description

Often, after a threat actor gains access to a system, they will attempt to run some kind of malware to further infect the victim machine. These malware often have long command line strings, which could be a possible indicator of attack. Here, we use sysmon and Splunk to first find the average command string length and search for command strings that stretch over multiple lines, thus identifying anomalies and possibly malicious commands.

## ATT&CK Coverage

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]] (coverage: Low; tactics: TA0002)

## Implementations

### Splunk

This is a Splunk query that determines the average length of a command per user and searches for a command string that is multiple times longer than the average length

- Data Model: Sysmon native

```splunk
index=* sourcetype="xmlwineventlog" EventCode=4688  |eval cmd_len=len(CommandLine) | eventstats avg(cmd_len) as avg by host| stats max(cmd_len) as maxlen, values(avg) as avgperhost by host, CommandLine | where maxlen > 10*avgperhost
```

## Data Model References

- process/create/command_line

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2021-01-002/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-01-002.yaml)
