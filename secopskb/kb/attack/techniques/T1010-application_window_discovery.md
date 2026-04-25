---
mitre_id: "T1010"
mitre_name: "Application Window Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--4ae4f953-fe58-4cc8-a327-33257e30a830"
mitre_created: "2017-05-31T21:30:24.512Z"
mitre_modified: "2025-10-24T17:48:44.488Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1010/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 14:47:22"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "Windows"
  - "macOS"
mitre_tactic_ids:
  - "TA0007"
d3fend_ids:
  - "D3-EAL"
  - "D3-EDL"
  - "D3-HBPI"
  - "D3-PSA"
  - "D3-SCA"
  - "D3-SCF"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Adversaries may attempt to get a listing of open application windows. Window listings could convey information about how the system is used.(Citation: Prevailion DarkWatchman 2021) For example, information about application windows could be used identify potential data to collect as well as identifying security tooling ([[T1518-software_discovery#^t1518001-security-software-discovery|T1518.001: Security Software Discovery]]) to evade.(Citation: ESET Grandoreiro April 2020)

Adversaries typically abuse system features for this type of enumeration. For example, they may gather information through native system features such as [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]] commands and [[T1106-native_api|T1106: Native API]] functions.

## Workspace

- [[notes/attack/techniques/T1010-application_window_discovery-note|Open workspace note]]

![[notes/attack/techniques/T1010-application_window_discovery-note]]

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## D3FEND

- [[D3-EAL-executable_allowlisting|D3-EAL: Executable Allowlisting]]
- [[D3-EDL-executable_denylisting|D3-EDL: Executable Denylisting]]
- [[D3-HBPI-hardware-based_process_isolation|D3-HBPI: Hardware-based Process Isolation]]
- [[D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]
- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]

## Tools

- [[silenttrinity|SILENTTRINITY]]

## Platforms

- Linux
- Windows
- macOS

