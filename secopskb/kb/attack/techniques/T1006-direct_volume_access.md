---
mitre_id: "T1006"
mitre_name: "Direct Volume Access"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--0c8ab3eb-df48-4b9c-ace7-beacaac81cc5"
mitre_created: "2017-05-31T21:30:20.934Z"
mitre_modified: "2025-10-24T17:48:23.015Z"
mitre_version: "2.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1006/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 14:47:22"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Network Devices"
  - "Windows"
mitre_tactic_ids:
  - "TA0005"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Adversaries may directly access a volume to bypass file access controls and file system monitoring. Windows allows programs to have direct access to logical volumes. Programs with direct access may read and write files directly from the drive by analyzing file system data structures. This technique may bypass Windows file access controls as well as file system monitoring tools. (Citation: Hakobyan 2009)

Utilities, such as `NinjaCopy`, exist to perform these actions in PowerShell.(Citation: Github PowerSploit Ninjacopy) Adversaries may also use built-in or third-party utilities (such as `vssadmin`, `wbadmin`, and [[esentutl|esentutl]]) to create shadow copies or backups of data from system volumes.(Citation: LOLBAS Esentutl)

## Workspace

- [[notes/attack/techniques/T1006-direct_volume_access-note|Open workspace note]]

![[notes/attack/techniques/T1006-direct_volume_access-note]]

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1040-behavior_prevention_on_endpoint|M1040: Behavior Prevention on Endpoint]]

## Tools

- [[esentutl|esentutl]]

## Platforms

- Network Devices
- Windows

