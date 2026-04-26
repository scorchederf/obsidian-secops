---
car_id: "CAR-2016-03-001"
title: "Host Discovery Commands"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2016-03-001/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2016-03-001.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2016-03-001"
  - "Host Discovery Commands"
attack_technique_ids:
  - "T1087"
  - "T1087.001"
  - "T1087.002"
  - "T1069"
  - "T1069.001"
  - "T1069.002"
  - "T1016"
  - "T1082"
  - "T1033"
  - "T1057"
  - "T1007"
platforms:
  - "Windows"
  - "Linux"
  - "macOS"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

# CAR-2016-03-001: Host Discovery Commands

## Metadata

- CAR ID: CAR-2016-03-001
- Submission Date: 2016/03/24
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows, Linux, macOS
- Data Subtypes: Process
- Contributors: MITRE

## Description

When entering on a host for the first time, an adversary may try to [discover](https://attack.mitre.org/tactics/TA0007) information about the host. There are several built-in Windows commands that can be used to learn about the software configurations, active users, administrators, and networking configuration. These commands should be monitored to identify when an adversary is learning information about the system and environment. The information returned may impact choices an adversary can make when [establishing persistence](https://attack.mitre.org/tactics/TA0003), [escalating privileges](https://attack.mitre.org/tactics/TA0004), or [moving laterally](https://attack.mitre.org/tactics/TA0008).

Because these commands are built in, they may be run frequently by power users or even by normal users. Thus, an analytic looking at this information should have well-defined white- or blacklists, and should consider looking at an anomaly detection approach, so that this information can be learned dynamically.

Within the built-in Windows Commands:

-   `hostname`
-   `ipconfig`
-   `net`
-   `quser`
-   `qwinsta`
-   `sc` with flags `query`, `queryex`, `qc`
-   `systeminfo`
-   `tasklist`
-   `dsquery`
-   `whoami`

**Note** `dsquery` is only pre-existing on Windows servers.

## ATT&CK Coverage

- [[kb/attack/techniques/T1087-account_discovery|T1087]] (coverage: Moderate; tactics: TA0007)
  - [[kb/attack/techniques/T1087-account_discovery|T1087.001]]
  - [[kb/attack/techniques/T1087-account_discovery|T1087.002]]
- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069]] (coverage: Moderate; tactics: TA0007)
  - [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.001]]
  - [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.002]]
- [[kb/attack/techniques/T1016-system_network_configuration_discovery|T1016]] (coverage: Moderate; tactics: TA0007)
- [[kb/attack/techniques/T1082-system_information_discovery|T1082]] (coverage: Moderate; tactics: TA0007)
- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]] (coverage: Moderate; tactics: TA0007)
- [[kb/attack/techniques/T1057-process_discovery|T1057]] (coverage: Moderate; tactics: TA0007)
- [[kb/attack/techniques/T1007-system_service_discovery|T1007]] (coverage: Moderate; tactics: TA0007)

## Implementations

### pseudocode

To be effective in deciphering malicious and benign activity, the full command line is essential. Similarly, having information about the parent process can help with making decisions and tuning to an environment.

```pseudocode
process = search Process:Create
info_command = filter process where (
 exe == "hostname.exe" or
 exe == "ipconfig.exe" or
 exe == "net.exe" or
 exe == "quser.exe" or
 exe == "qwinsta.exe" or
 exe == "sc" and (command_line match " query" or command_line match " qc")) or
 exe == "systeminfo.exe" or
 exe == "tasklist.exe" or
 exe == "whoami.exe"
)
output info_command
```

### Splunk

Splunk version of the above pseudocode search.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_index__ EventCode=1 (Image="C:\\Windows\\*\\hostname.exe" OR Image="C:\\Windows\\*\\ipconfig.exe" OR Image="C:\\Windows\\*\\net.exe" OR Image="C:\\Windows\\*\\quser.exe" OR Image="C:\\Windows\\*\\qwinsta.exe" OR (Image="C:\\Windows\\*\\sc.exe" AND (CommandLine="* query *" OR CommandLine="* qc *")) OR Image="C:\\Windows\\*\\systeminfo.exe" OR Image="C:\\Windows\\*\\tasklist.exe" OR Image="C:\\Windows\\*\\whoami.exe")|stats values(Image) as "Images" values(CommandLine) as "Command Lines" by ComputerName
```

### EQL

EQL version of the above pseudocode search.

- Data Model: EQL native

```eql
process where subtype.create and
  (process_name == "hostname.exe" or process_name == "ipconfig.exe" or process_name == "net.exe" or process_name == "quser.exe" process_name == "qwinsta.exe" or process_name == "systeminfo.exe" or process_name == "tasklist.exe" or process_name == "whoami.exe" or (process_name == "sc.exe" and (command_line == "* query *" or command_line == "* qc *")))
```

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 (image in ["*\hostname.exe", "*\ipconfig.exe", "*\net.exe", "*\quser.exe", "*\qwinsta.exe", "*\systeminfo.exe", "*\tasklist.exe", "*\whoami.exe"] OR (image="*\sc.exe" command IN ["* query *", "* qc *"))
```

## Data Model References

- process/create/command_line
- process/create/exe

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2016-03-001/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2016-03-001.yaml)
