---
car_id: "CAR-2014-11-002"
title: "Outlier Parents of Cmd"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2014-11-002/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-11-002.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2014-11-002"
  - "Outlier Parents of Cmd"
attack_technique_ids:
  - "T1059"
  - "T1059.003"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

# CAR-2014-11-002: Outlier Parents of Cmd

## Metadata

- CAR ID: CAR-2014-11-002
- Submission Date: 2014/11/06
- Information Domain: Host
- Analytic Type: Anomaly, TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: MITRE

## Description

Many programs create command prompts as part of their normal operation including malware used by attackers. This analytic attempts to identify suspicious programs spawning `cmd.exe` by looking for programs that do not normally create `cmd.exe`.

While this analytic does not take the user into account, doing so could generate further interesting results.
It is very common for some programs to spawn cmd.exe as a subprocess, for example to run batch files or windows commands. However many process don’t routinely launch a command prompt – for example Microsoft Outlook. A command prompt being launched from a process that normally doesn’t launch command prompts could be the result of malicious code being injected into that process, or of an attacker replacing a legitimate program with a malicious one.


### Output Description

The time and host the new process was started as well as its parent

## ATT&CK Coverage

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]] (coverage: Moderate; tactics: TA0002)
  - [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]

## Implementations

### pseudocode

Create a baseline of parents of `cmd.exe` seen over the last 30 days and a list of parents of `cmd.exe` seen today. Remove parents in the baseline from parents seen today, leaving a list of new parents.

```pseudocode
processes = search Process:Create
cmd = filter processes where (exe == "cmd.exe")
cmd = from cmd select parent_exe
historic_cmd = filter cmd (where timestamp < now - 1 day AND timestamp > now - 1 day)
current_cmd = filter cmd (where timestamp >= now - 1 day)
new_cmd = historic_cmd - current_cmd
output new_cmd
```

## Data Model References

- process/create/exe
- process/create/parent_exe

## D3FEND Mappings

- [[kb/defend/techniques/D3-PLA-process_lineage_analysis|D3-PLA: Process Lineage Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2014-11-002/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-11-002.yaml)
