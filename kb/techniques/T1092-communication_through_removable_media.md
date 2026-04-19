---
id: T1092
name: Communication Through Removable Media
created: 2017-05-31 21:31:09.379000+00:00
modified: 2025-10-24 17:48:52.106000+00:00
type: attack-pattern
x_mitre_version: 1.0
x_mitre_domains: enterprise-attack
---

## Tactic

- [[command_and_control|Command and Control]]

Adversaries can perform command and control between compromised hosts on potentially disconnected networks using removable media to transfer commands from system to system.(Citation: ESET Sednit USBStealer 2014) Both systems would need to be compromised, with the likelihood that an Internet-connected system was compromised first and the second through lateral movement by [Replication Through Removable Media](https://attack.mitre.org/techniques/T1091). Commands and files would be relayed from the disconnected system to the Internet-connected system to which the adversary has direct access.

## Properties

- id: T1092
- name: Communication Through Removable Media
- created: 2017-05-31 21:31:09.379000+00:00
- modified: 2025-10-24 17:48:52.106000+00:00
- type: attack-pattern
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1028-operating_system_configuration|M1028: Operating System Configuration]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]

## Platforms

- Linux
- macOS
- Windows

## Tools


