---
car_id: "CAR-2020-11-001"
title: "Boot or Logon Initialization Scripts"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2020-11-001/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-11-001.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2020-11-001"
  - "Boot or Logon Initialization Scripts"
attack_technique_ids:
  - "T1037"
  - "T1037.001"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CAR-2020-11-001: Boot or Logon Initialization Scripts

## Metadata

- CAR ID: CAR-2020-11-001
- Submission Date: 2020/11/30
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Registry, Process
- Contributors: Olaf Hartong

## Description

Adversaries may schedule software to run whenever a user logs into the system; this is done to establish persistence and sometimes for lateral movement. This trigger is established through the registry key HKEY_CURRENT_USER\Environment*UserInitMprLogonScript*. This signature looks edits to existing keys or creation of new keys in that path. Users purposefully adding benign scripts to this path will result in false positives; that case is rare, however. There are other ways of running a script at startup or login that are not covered in this signature. Note that this signature overlaps with the Windows Sysinternals Autoruns tool, which would also show changes to this registry path.

## ATT&CK Coverage

- [[kb/attack/techniques/T1037-boot_or_logon_initialization_scripts|T1037]] (coverage: Moderate; tactics: TA0003, TA0008)
  - [[kb/attack/techniques/T1037-boot_or_logon_initialization_scripts|T1037.001]]

## Implementations

### Pseudocode

This is a pseudocode representation of the below splunk search.

- Data Model: CAR native

```pseudocode
processes = search Process:Create
logon_script_key_processes = filter processes where (
  command_line = "*reg*add*\Environment*UserInitMprLogonScript")
registry = search (Registry:Add OR Registry:Edit)
registry_logon_key_events = filter registry where (
  key = "*\Environment*UserInitMprLogonScript")
output (logon_script_key_processes, registry_logon_key_events)
```

### Splunk

Look for commands for adding a logon script as a registry value, as well as direct registry events for the same thing.

- Data Model: Sysmon native

```splunk
(index=__your_sysmon_index__ EventCode=1 Image="C:\\Windows\\System32\\reg.exe" CommandLine="*add*\\Environment*UserInitMprLogonScript") OR (index=__your_sysmon_index__ (EventCode=12 OR EventCode=14 OR EventCode=13) TargetObject="*\\Environment*UserInitMprLogonScript")
```

### LogPoint

Look for commands for adding a logon script as a registry value, as well as direct registry events for the same thing.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon ((event_id=1 image="C:\Windows\System32\reg.exe" command="*add*\Environment*UserInitMprLogonScript") OR (event_id IN [12, 13, 14] target_object="*\Environment*UserInitMprLogonScript"))
```

## Data Model References

- process/create/command_line
- process/create/exe
- registry/add/key
- registry/edit/key

## D3FEND Mappings

- [[kb/defend/techniques/D3-SICA-system_init_config_analysis|D3-SICA: System Init Config Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2020-11-001/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-11-001.yaml)
