---
mitre_id: "T1092"
mitre_name: "Communication Through Removable Media"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--64196062-5210-42c3-9a02-563a0d1797ef"
mitre_created: "2017-05-31T21:31:09.379Z"
mitre_modified: "2025-10-24T17:48:52.106Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1092/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0011"
---

# T1092: Communication Through Removable Media

Adversaries can perform command and control between compromised hosts on potentially disconnected networks using removable media to transfer commands from system to system.(Citation: ESET Sednit USBStealer 2014) Both systems would need to be compromised, with the likelihood that an Internet-connected system was compromised first and the second through lateral movement by [[T1091-replication_through_removable_media|T1091: Replication Through Removable Media]]. Commands and files would be relayed from the disconnected system to the Internet-connected system to which the adversary has direct access.

## Tactics

- [[TA0011-command_and_control|TA0011: Command and Control]]

## Mitigations

- [[M1028-operating_system_configuration|M1028: Operating System Configuration]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]

## Platforms

- Linux
- macOS
- Windows

