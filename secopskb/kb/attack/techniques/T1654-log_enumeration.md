---
mitre_id: "T1654"
mitre_name: "Log Enumeration"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--866d0d6d-02c6-42bd-aa2f-02907fdc0969"
mitre_created: "2023-07-10T16:50:57.587Z"
mitre_modified: "2025-04-15T19:58:48.705Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1654/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 14:47:22"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "IaaS"
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Adversaries may enumerate system and service logs to find useful data. These logs may highlight various types of valuable insights for an adversary, such as user authentication records ([[T1087-account_discovery|T1087: Account Discovery]]), security or vulnerable software ([[T1518-software_discovery|T1518: Software Discovery]]), or hosts within a compromised network ([[T1018-remote_system_discovery|T1018: Remote System Discovery]]).

Host binaries may be leveraged to collect system logs. Examples include using `wevtutil.exe` or [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]] on Windows to access and/or export security event information.(Citation: WithSecure Lazarus-NoPineapple Threat Intel Report 2023)(Citation: Cadet Blizzard emerges as novel threat actor) In cloud environments, adversaries may leverage utilities such as the Azure VM Agent’s `CollectGuestLogs.exe` to collect security logs from cloud hosted infrastructure.(Citation: SIM Swapping and Abuse of the Microsoft Azure Serial Console)

Adversaries may also target centralized logging infrastructure such as SIEMs. Logs may also be bulk exported and sent to adversary-controlled infrastructure for offline analysis.

In addition to gaining a better understanding of the environment, adversaries may also monitor logs in real time to track incident response procedures. This may allow them to adjust their techniques in order to maintain persistence or evade defenses.(Citation: Permiso GUI-Vil 2023)

## Workspace

- [[notes/attack/techniques/T1654-log_enumeration-note|Open workspace note]]

![[notes/attack/techniques/T1654-log_enumeration-note]]

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]

## Tools

- [[pacu|Pacu]]

## Platforms

- ESXi
- IaaS
- Linux
- macOS
- Windows

