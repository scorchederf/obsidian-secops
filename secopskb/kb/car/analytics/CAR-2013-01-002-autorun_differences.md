---
car_id: "CAR-2013-01-002"
title: "Autorun Differences"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2013-01-002/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-01-002.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2013-01-002"
  - "Autorun Differences"
attack_technique_ids:
  - "T1543"
  - "T1543.003"
  - "T1053"
  - "T1053.005"
  - "T1547"
  - "T1547.001"
  - "T1547.010"
  - "T1547.004"
  - "T1574"
  - "T1574.007"
  - "T1574.008"
  - "T1574.009"
  - "T1574.010"
  - "T1574.011"
  - "T1546"
  - "T1546.001"
  - "T1546.003"
  - "T1546.008"
  - "T1546.010"
  - "T1112"
  - "T1037"
  - "T1037.001"
platforms:
  - "Windows"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# CAR-2013-01-002: Autorun Differences

## Metadata

- CAR ID: CAR-2013-01-002
- Submission Date: 2013/01/25
- Information Domain: Analytic, Host
- Analytic Type: Situational Awareness, TTP
- Platforms: Windows
- Data Subtypes: Registry
- Contributors: MITRE

## Description

The Sysinternals tool [Autoruns](../sensors/autoruns) checks the registry and file system for known identify persistence mechanisms. It will output any tools identified, including built-in or added-on Microsoft functionality and third party software. Many of these locations are known by adversaries and used to obtain [Persistence](https://attack.mitre.org/tactics/TA0003). Running Autoruns periodically in an environment makes it possible to collect and monitor its output for differences, which may include the removal or addition of persistent tools. Depending on the persistence mechanism and location, legitimate software may be more likely to make changes than an adversary tool. Thus, this analytic may result in significant noise in a highly dynamic environment. While Autoruns is a convenient method to scan for programs using persistence mechanisms its scanning nature does not conform well to streaming based analytics. This analytic could be replaced with one that draws from sensors that collect registry and file information if streaming analytics are desired.

Utilizes the Sysinternals autoruns tool (ignoring validated Microsoft entries). Primarily not a detection analytic by itself but through analysis of results by an analyst can be used for such. Building another analytic on top of this one identifying unusual entries would likely be a beneficial alternative.

## ATT&CK Coverage

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543]] (coverage: Moderate; tactics: TA0003)
  - [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]
- [[kb/attack/techniques/T1053-scheduled_task_job|T1053]] (coverage: Moderate; tactics: TA0003)
  - [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]
- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547]] (coverage: Moderate; tactics: TA0003)
  - [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]
  - [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.010]]
  - [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.004]]
- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574]] (coverage: Moderate; tactics: TA0003, TA0004)
  - [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.007]]
  - [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.008]]
  - [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.009]]
  - [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.010]]
  - [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.011]]
- [[kb/attack/techniques/T1546-event_triggered_execution|T1546]] (coverage: Moderate; tactics: TA0004, TA0003)
  - [[kb/attack/techniques/T1546-event_triggered_execution|T1546.001]]
  - [[kb/attack/techniques/T1546-event_triggered_execution|T1546.003]]
  - [[kb/attack/techniques/T1546-event_triggered_execution|T1546.008]]
  - [[kb/attack/techniques/T1546-event_triggered_execution|T1546.010]]
- [[kb/attack/techniques/T1112-modify_registry|T1112]] (coverage: Moderate; tactics: TA0003, TA0002)
- [[kb/attack/techniques/T1037-boot_or_logon_initialization_scripts|T1037]] (coverage: Moderate; tactics: TA0003)
  - [[kb/attack/techniques/T1037-boot_or_logon_initialization_scripts|T1037.001]]

## D3FEND Mappings

- [[kb/defend/techniques/D3-SICA-system_init_config_analysis|D3-SICA: System Init Config Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2013-01-002/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-01-002.yaml)
