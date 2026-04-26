---
car_id: "CAR-2020-11-005"
title: "Clear Powershell Console Command History"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2020-11-005/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-11-005.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2020-11-005"
  - "Clear Powershell Console Command History"
attack_technique_ids:
  - "T1070"
  - "T1070.003"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

# CAR-2020-11-005: Clear Powershell Console Command History

## Metadata

- CAR ID: CAR-2020-11-005
- Submission Date: 2020/11/30
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Olaf Hartong

## Description

Adversaries may attempt to conceal their tracks by deleting the history of commands run within the Powershell console, or turning off history saving to begin with. This analytic looks for several commands that would do this. This does not capture the event if it is done within the console itself; only commandline-based commands are detected. Note that the command to remove the history file directly may very a bit if the history file is not saved in the default path on a particular system.

## ATT&CK Coverage

- [[kb/attack/techniques/T1070-indicator_removal|T1070]] (coverage: Low; tactics: TA0005)
  - [[kb/attack/techniques/T1070-indicator_removal|T1070.003]]

## Implementations

### Pseudocode

This is a pseudocode representation of the below splunk search.

- Data Model: CAR native

```pseudocode
processes = search Process:Create
clear_commands = filter processes where (
  command_line ="*rm (Get-PSReadlineOption).HistorySavePath*" OR command_line="*del (Get-PSReadlineOption).HistorySavePath*" OR command_line="*Set-PSReadlineOption –HistorySaveStyle SaveNothing*" OR command_line="*Remove-Item (Get-PSReadlineOption).HistorySavePath*")  OR command_linee="del*Microsoft\Windows\Powershell\PSReadline\ConsoleHost_history.txt")
output clear_commands
```

### Splunk

Look for powershell commands that would clear command history

- Data Model: Sysmon native

```splunk
(index=__your_sysmon_index__ EventCode=1) (CommandLine="*rm (Get-PSReadlineOption).HistorySavePath*" OR CommandLine="*del (Get-PSReadlineOption).HistorySavePath*" OR CommandLine="*Set-PSReadlineOption –HistorySaveStyle SaveNothing*" OR CommandLine="*Remove-Item (Get-PSReadlineOption).HistorySavePath*" OR CommandLine="del*Microsoft\\Windows\\Powershell\\PSReadline\\ConsoleHost_history.txt")
```

### LogPoint

Look for powershell commands that would clear command history

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 (command="*rm (Get-PSReadlineOption).HistorySavePath*" OR command="*del (Get-PSReadlineOption).HistorySavePath*" OR command="*Set-PSReadlineOption –HistorySaveStyle SaveNothing*" OR command="*Remove-Item (Get-PSReadlineOption).HistorySavePath*" OR command="del*Microsoft\Windows\Powershell\PSReadline\ConsoleHost_history.txt")
```

## Data Model References

- process/create/exe
- process/create/command_line

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2020-11-005/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-11-005.yaml)
