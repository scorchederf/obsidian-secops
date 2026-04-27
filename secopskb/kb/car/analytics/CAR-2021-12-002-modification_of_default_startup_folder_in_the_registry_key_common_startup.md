---
car_id: "CAR-2021-12-002"
title: "Modification of Default Startup Folder in the Registry Key 'Common Startup'"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-12-002/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-12-002.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2021-12-002"
  - "Modification of Default Startup Folder in the Registry Key 'Common Startup'"
attack_technique_ids:
  - "T1547"
  - "T1547.001"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CAR-2021-12-002: Modification of Default Startup Folder in the Registry Key 'Common Startup'

## Metadata

- CAR ID: CAR-2021-12-002
- Submission Date: 2021/12/06
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process, Registry
- Contributors: Lucas Heiligenstein

## Description

Detection of the modification of the registry key `Common Startup` located in `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders\` and `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders\`. When a user logs on, any files located in the Startup Folder are launched. Attackers may modify these folders with other files in order to evade detection set on these default folders. This detection focuses on EventIDs 4688 and 1 for process creation and EventID 4657 for the modification of the Registry Keys.

## ATT&CK Coverage

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547]] (coverage: Medium; tactics: TA0003, TA0004)
  - [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]
- [[kb/attack/techniques/T1112-modify_registry|T1112]] (coverage: Medium; tactics: TA0005)

## Implementations

### Pseudocode

This detects modification of the `Common Startup` registry key value, either via a new process (command line) or direct registry manipulation.

- Data Model: CAR native

```pseudocode
processes = search Process:create
logon_reg_processes = filter processes where (command_line CONTAINS("*reg*") AND command_line CONTAINS("*add*") AND command_line CONTAINS("*/d*") OR (command_line CONTAINS("*Set-ItemProperty*") AND command_line CONTAINS("*-value*")) AND command_line CONTAINS("*Common Startup*"))
reg_keys = search Registry:value_edit
logon_reg_keys = filter reg_keys where value="Common Startup"
output logon_reg_processes, logon_reg_keys
```

### Splunk

This is a Splunk representation of the above pseudocode search.

```splunk
(((EventCode="4688" OR EventCode="1") (CommandLine="*reg*" AND CommandLine="*add*" AND CommandLine="*/d*") OR (CommandLine="*Set-ItemProperty*" AND CommandLine="*-value*") CommandLine="*Common Startup*") OR ((EventCode="4657" ObjectValueName="Common Startup") OR (EventCode="13" TargetObject="*Common Startup")))
```

### Elastic

This is an ElasticSeearech representation of the above pseudocode search.

```elastic
((EventLog:"Security" AND (winlog.event_id:"4688" OR winlog.event_id:"1") AND ((process.command_line:*reg* AND process.command_line:*add* AND process.command_line:*\/d*) OR (process.command_line:*Set\-ItemProperty* AND process.command_line:*\-value*)) AND process.command_line:*Common\ Startup*) OR (winlog.event_id:"4657" AND winlog.event_data.ObjectValueName:"Common\ Startup") OR (winlog.event_id:"13" AND winlog.event_data.TargetObject:"*Common Startup"))
```

### LogPoint

This is a LogPoint representation of the above pseudocode search.

```logpoint
((EventLog="Security" (event_id="4688" OR event_id="1") ((CommandLine="*reg*" CommandLine="*add*" CommandLine="*/d*") OR (CommandLine="*Set-ItemProperty*" CommandLine="*-value*")) CommandLine="*Common Startup*") OR (event_id="4657" ObjectValueName="Common Startup") OR (event_id="13" TargetObject="*Common Startup"))
```

## Data Model References

- process/create/command_line
- registry/add/key

## Unit Tests

Modification on Registry Key with cmd. Files in new_malicious_startup_folder will be launched when user logon

```text
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders" /v "Common Startup" /d "C:\Users\Lucas\Documents\new_malicious_startup_folder" /f
```

Modification on Registry Key with Powershell. Files in new_malicious_startup_folder will be launched when user logon

```text
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders" -Name "Common Startup" -Value C:\Users\Lucas\Documents\new_malicious_startup_folder
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2021-12-002/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-12-002.yaml)
