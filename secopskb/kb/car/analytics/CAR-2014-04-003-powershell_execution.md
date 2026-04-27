---
car_id: "CAR-2014-04-003"
title: "Powershell Execution"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2014-04-003/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-04-003.yaml"
build_date: "2026-04-27 19:03:49"
aliases:
  - "CAR-2014-04-003"
  - "Powershell Execution"
attack_technique_ids:
  - "T1059"
  - "T1059.001"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

[PowerShell](https://attack.mitre.org/techniques/T1059/001/) is a scripting environment included with Windows that is used by both attackers and administrators. Execution of PowerShell scripts in most Windows versions is opaque and not typically secured by antivirus which makes using PowerShell an easy way to circumvent security measures. This analytic detects execution of PowerShell scripts.

Powershell can be used to hide monitored command line execution such as:
-   `net use`
-   `sc start`

## ATT&CK Coverage

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]] (coverage: High; tactics: TA0002)
  - [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]] (coverage: Moderate; tactics: TA0005)
  - [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

## Implementations

### pseudocode

Look for versions of `PowerShell` that were not launched interactively.

```pseudocode
process = search Process:Create
powershell = filter process where (exe == "powershell.exe" AND parent_exe != "explorer.exe" )
output powershell
```

### Splunk

Splunk version of the above pseudocode.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_index__ EventCode=1 Image="C:\\Windows\\*\\powershell.exe" ParentImage!="C:\\Windows\\explorer.exe"|stats values(CommandLine) as "Command Lines" values(ParentImage) as "Parent Images" by ComputerName
```

### EQL

EQL version of the above pseudocode.

- Data Model: EQL native

```eql
process where subtype.create and
  (process_name == "powershell.exe" and parent_process_name != "explorer.exe")
```

### DNIF

DNIF version of the above pseudocode.

- Data Model: Sysmon native

```dnif
_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 AND $App=powershell.exe NOT $ParentProcess=regex(.*explorer.exe.*)i limit 30
```

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 image="*\powershell.exe" -parent_image="C:\Windows\explorer.exe"
```

## Data Model References

- process/create/exe
- process/create/parent_exe

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2014-04-003/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-04-003.yaml)
