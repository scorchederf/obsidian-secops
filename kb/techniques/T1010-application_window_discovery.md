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
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "Windows"
  - "macOS"
mitre_tactic_ids:
  - "TA0007"
---

# T1010: Application Window Discovery

Adversaries may attempt to get a listing of open application windows. Window listings could convey information about how the system is used.(Citation: Prevailion DarkWatchman 2021) For example, information about application windows could be used identify potential data to collect as well as identifying security tooling ([[T1518-software_discovery#^t1518001-security-software-discovery|T1518.001: Security Software Discovery]]) to evade.(Citation: ESET Grandoreiro April 2020)

Adversaries typically abuse system features for this type of enumeration. For example, they may gather information through native system features such as [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]] commands and [[T1106-native_api|T1106: Native API]] functions.

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Tools

- [[silenttrinity|SILENTTRINITY]]

## Platforms

- Linux
- Windows
- macOS

