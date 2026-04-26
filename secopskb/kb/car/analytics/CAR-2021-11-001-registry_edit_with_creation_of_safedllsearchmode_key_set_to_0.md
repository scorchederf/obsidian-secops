---
car_id: "CAR-2021-11-001"
title: "Registry Edit with Creation of SafeDllSearchMode Key Set to 0"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-11-001/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-11-001.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2021-11-001"
  - "Registry Edit with Creation of SafeDllSearchMode Key Set to 0"
attack_technique_ids:
  - "T1574"
  - "T1574.001"
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

# CAR-2021-11-001: Registry Edit with Creation of SafeDllSearchMode Key Set to 0

## Metadata

- CAR ID: CAR-2021-11-001
- Submission Date: 2021/11/24
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process, Registry
- Contributors: Lucas Heiligenstein

## Description

Detection of creation of registry key HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\SafeDllSearchMode. The key SafeDllSearchMode, if set to 0, will block the Windows mechanism for the search DLL order and adversaries may execute their own malicious dll.

## ATT&CK Coverage

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574]] (coverage: Medium; tactics: TA0003, TA0004, TA0005)
  - [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]
- [[kb/attack/techniques/T1112-modify_registry|T1112]] (coverage: Medium; tactics: TA0005)

## Implementations

### Pseudocode

This detects SafeDllSearchMode creation, either via a new process (command line) or direct registry manipulation.

- Data Model: CAR native

```pseudocode
processes = search Process:create
safe_dll_search_processes = filter processes where command_line CONTAINS("*SafeDllSearchMode*") AND ((command_line CONTAINS("*reg*") AND command_line CONTAINS("*add*") AND command_line CONTAINS("*/d*")) OR (command_line CONTAINS("*Set-ItemProperty*") AND command_line CONTAINS(*-value*)) OR ((command_line CONTAINS("*00000000*") AND command_line CONTAINS(*0*)))
reg_keys = search Registry:value_edit
safe_dll_reg_keys = filter reg_keys where value="SafeDllSearchMode" AND value_data="0"
output safe_dll_search_processes, safe_dll_reg_keys
```

### Splunk

This is a Splunk representation of the above pseudocode.

- Data Model: Win. Eventlog/Sysmon native

```splunk
(source="WinEventLog:*" ((((EventCode="4688" OR EventCode="1") ((CommandLine="*reg*" CommandLine="*add*" CommandLine="*/d*") OR (CommandLine="*Set-ItemProperty*" CommandLine="*-value*")) (CommandLine="*00000000*" OR CommandLine="*0*") CommandLine="*SafeDllSearchMode*") OR ((EventCode="4657") ObjectValueName="SafeDllSearchMode" value="0")) OR ((EventCode="13") EventType="SetValue" TargetObject="*SafeDllSearchMode" Details="DWORD (0x00000000)")))
```

### Elastic

This is an Elastic representation of the above pseudocode.

- Data Model: Win. Eventlog/Sysmon native

```elastic
(((EventCode:("4688" OR "1") AND ((process.command_line:*reg* AND process.command_line:*add* AND process.command_line:*\/d*) OR (process.command_line:*Set\-ItemProperty* AND process.command_line:*\-value*)) AND process.command_line:(*00000000* OR *0*) AND process.command_line:*SafeDllSearchMode*) OR (EventCode:"4657" AND winlog.event_data.ObjectValueName:"SafeDllSearchMode" AND value:"0")) OR (EventCode:"13" AND winlog.event_data.EventType:"SetValue" AND winlog.event_data.TargetObject:*SafeDllSearchMode AND winlog.event_data.Details:"DWORD\ \(0x00000000\)"))
```

### LogPoint

This is a LogPoint representation of the above pseudocode.

- Data Model: Win. Eventlog/Sysmon native

```logpoint
(((EventCode IN ["4688", "1"] ((CommandLine="*reg*" CommandLine="*add*" CommandLine="*/d*") OR (CommandLine="*Set-ItemProperty*" CommandLine="*-value*")) CommandLine IN ["*00000000*", "*0*"] CommandLine="*SafeDllSearchMode*") OR (EventCode IN "4657" ObjectValueName="SafeDllSearchMode" value="0")) OR (EventCode IN "13" EventType="SetValue" TargetObject="*SafeDllSearchMode" Details="DWORD (0x00000000)"))
```

## Data Model References

- process/create/command_line
- registry/add/key

## Unit Tests

Execute command with cmd

```text
reg add "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager" /v SafeDllSearchMode /d 0
```

Execute command with powershell

```text
Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Session Manager" -Name SafeDllSearchMode -Value 0
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2021-11-001/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-11-001.yaml)
