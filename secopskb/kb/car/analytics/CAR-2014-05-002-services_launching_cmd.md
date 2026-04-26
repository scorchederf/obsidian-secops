---
car_id: "CAR-2014-05-002"
title: "Services launching Cmd"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2014-05-002/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-05-002.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2014-05-002"
  - "Services launching Cmd"
attack_technique_ids:
  - "T1543"
  - "T1543.003"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
  - "Splunk"
  - "EQL"
  - "DNIF"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# CAR-2014-05-002: Services launching Cmd

## Metadata

- CAR ID: CAR-2014-05-002
- Submission Date: 2014/05/05
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: MITRE

## Description

Windows runs the [Service Control Manager](https://en.wikipedia.org/wiki/Service_Control_Manager) (SCM) within the process `services.exe`. Windows launches services as independent processes or DLL loads within a [svchost.exe](https://en.wikipedia.org/wiki/svchost.exe) group. To be a legitimate service, a process (or DLL) must have the appropriate service entry point [SvcMain](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687414.aspx). If an application does not have the entry point, then it will timeout (default is 30 seconds) and the process will be killed.

To survive the timeout, [adversaries and red teams](https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-RAT-and-Staging-Report.pdf) can create services that direct to `cmd.exe` with the flag `/c`, followed by the desired command. The `/c` flag causes the command shell to run a command and immediately exit. As a result, the desired program will remain running and it will report an error starting the service. This analytic will catch that command prompt instance that is used to launch the actual malicious executable. Additionally, the children and descendants of services.exe will run as a SYSTEM user by default. Thus, services are a convenient way for an adversary to gain [Persistence](https://attack.mitre.org/tactics/TA0003) and [Privilege Escalation](https://attack.mitre.org/tactics/TA0004).

## ATT&CK Coverage

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543]] (coverage: Moderate; tactics: TA0003, TA0004)
  - [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Implementations

### pseudocode

Returns all processes named `cmd.exe` that have `services.exe` as a parent process. Because this should never happen, the `/c` flag is redundant in the search.

```pseudocode
process = search Process:Create
cmd = filter process where (exe == "cmd.exe" and parent_exe == "services.exe")
output cmd
```

### Splunk

The Splunk version of the above pseudocode.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_index__ EventCode=1 Image="C:\\Windows\\*\\cmd.exe" ParentImage="C:\\Windows\\*\\services.exe"
```

### EQL

EQL version of the above pseudocode.

- Data Model: EQL native

```eql
process where subtype.create and
  (process_name == "cmd.exe" and parent_process_name == "services.exe")
```

### DNIF

DNIF version of the above pseudocode.

- Data Model: Sysmon native

```dnif
_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 AND $App=cmd.exe AND $ParentProcess=regex(.*services.exe.*)i limit 30
```

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 image="C:\Windows\System32\cmd.exe" parent_image="C:\Windows\System32\services.exe"
```

## Data Model References

- process/create/exe
- process/create/parent_exe

## D3FEND Mappings

- [[kb/defend/techniques/D3-PLA-process_lineage_analysis|D3-PLA: Process Lineage Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2014-05-002/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-05-002.yaml)
