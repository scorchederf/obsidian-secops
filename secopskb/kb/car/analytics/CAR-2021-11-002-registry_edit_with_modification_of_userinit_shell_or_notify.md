---
car_id: "CAR-2021-11-002"
title: "Registry Edit with Modification of Userinit, Shell or Notify"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-11-002/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-11-002.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2021-11-002"
  - "Registry Edit with Modification of Userinit, Shell or Notify"
attack_technique_ids:
  - "T1547"
  - "T1547.004"
  - "T1112"
platforms:
  - "Windows"
implementation_types:
  - "Pseudocode"
  - "Splunk"
  - "Elastic"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CAR-2021-11-002: Registry Edit with Modification of Userinit, Shell or Notify

## Metadata

- CAR ID: CAR-2021-11-002
- Submission Date: 2021/11/28
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process, Registry
- Contributors: Lucas Heiligenstein

## Description

Detection of modification of the registry key values of `Notify`, `Userinit`, and `Shell` located in `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\` and `HKEY_LOCAL_USER\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\`. When a user logs on, the Registry key values of `Notify`, `Userinit` and `Shell` are used to load dedicated Windows component. Attackers may insert malicious payload following the legitimate value to launch a malicious payload.

## ATT&CK Coverage

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547]] (coverage: Medium; tactics: TA0003, TA0004)
  - [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.004]]
- [[kb/attack/techniques/T1112-modify_registry|T1112]] (coverage: Medium; tactics: TA0005)

## Implementations

### Pseudocode

This detects logon registry key modification, either via a new process (command line) or direct registry manipulation.

- Data Model: CAR native

```pseudocode
processes = search Process:create
logon_reg_processes = filter processes where command_line CONTAINS("*\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon*") AND (command_line CONTAINS("*Userinit*") OR command_line CONTAINS("*Shell*") OR command_line CONTAINS("*Notify*")) AND (((command_line CONTAINS("*reg*") OR command_line CONTAINS("*add*") OR command_line CONTAINS("*/d*")) OR (command_line CONTAINS("*Set-ItemProperty*") OR command_line CONTAINS("*New-ItemProperty*") OR command_line CONTAINS("*-value*"))))
reg_keys = search Registry:value_edit
logon_reg_keys = filter reg_keys where (value="Userinit" OR value="Shell" OR value="Notify")
output logon_reg_processes, logon_reg_keys
```

### Splunk

This is a Splunk representation of the above pseudocode.

```splunk
(((((EventCode="4688" OR EventCode="1") ((CommandLine="*reg*" CommandLine="*add*" CommandLine="*/d*") OR ((CommandLine="*Set-ItemProperty*" OR CommandLine="*New-ItemProperty*") CommandLine="*-value*")) CommandLine="*\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon*" (CommandLine="*Userinit*" OR CommandLine="*Shell*" OR CommandLine="*Notify*")) OR ((EventCode="4657") (ObjectValueName="Userinit" OR ObjectValueName="Shell" OR ObjectValueName="Notify"))) OR ((EventCode="13") (TargetObject="*Userinit" OR TargetObject="*Shell" OR TargetObject="*Notify"))))
```

### Elastic

This is an ElasticSearch representation of the above pseudocode.

```elastic
(((EventCode:("4688" OR "1") AND ((process.command_line:*reg* AND process.command_line:*add* AND process.command_line:*\/d*) OR (process.command_line:(*Set\-ItemProperty* OR *New\-ItemProperty*) AND process.command_line:*\-value*)) AND process.command_line:*\\Microsoft\\Windows\ NT\\CurrentVersion\\Winlogon* AND process.command_line:(*Userinit* OR *Shell* OR *Notify*)) OR (EventCode:"4657" AND winlog.event_data.ObjectValueName:("Userinit" OR "Shell" OR "Notify"))) OR (EventCode:"13" AND winlog.event_data.TargetObject:(*Userinit OR *Shell OR *Notify)))
```

### LogPoint

This is a LogPoint representation of the above pseudocode.

```logpoint
(((EventCode IN ["4688", "1"] ((CommandLine="*reg*" CommandLine="*add*" CommandLine="*/d*") OR (CommandLine IN ["*Set-ItemProperty*", "*New-ItemProperty*"] CommandLine="*-value*")) CommandLine="*\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon*" CommandLine IN ["*Userinit*", "*Shell*", "*Notify*"]) OR (EventCode IN "4657" ObjectValueName IN ["Userinit", "Shell", "Notify"])) OR (EventCode IN "13" TargetObject IN ["*Userinit", "*Shell", "*Notify"]))
```

## Data Model References

- process/create/command_line
- registry/add/key

## Unit Tests

Modification on Registry Key with cmd. Calc.exe will be launched when user will login

```text
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Userinit /d C:\Windows\system32\userinit.exe,C:\Windows\system32\calc.exe
```

Modification on Registry Key with Powershell. Calc.exe will be launched when user will login

```text
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name Userinit -Value C:\Windows\system32\userinit.exe,C:\Windows\system32\calc.exe
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2021-11-002/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-11-002.yaml)
