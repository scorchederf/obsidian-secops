---
id: T1006
name: Direct Volume Access
created: 2017-05-31 21:30:20.934000+00:00
modified: 2025-10-24 17:48:23.015000+00:00
type: attack-pattern
x_mitre_version: 2.3
x_mitre_domains: enterprise-attack
---

## Tactic

- [[defense_evasion|Defense Evasion]]

Adversaries may directly access a volume to bypass file access controls and file system monitoring. Windows allows programs to have direct access to logical volumes. Programs with direct access may read and write files directly from the drive by analyzing file system data structures. This technique may bypass Windows file access controls as well as file system monitoring tools. (Citation: Hakobyan 2009)

Utilities, such as `NinjaCopy`, exist to perform these actions in PowerShell.(Citation: Github PowerSploit Ninjacopy) Adversaries may also use built-in or third-party utilities (such as `vssadmin`, `wbadmin`, and [esentutl](https://attack.mitre.org/software/S0404)) to create shadow copies or backups of data from system volumes.(Citation: LOLBAS Esentutl)

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1040-behavior_prevention_on_endpoint|M1040: Behavior Prevention on Endpoint]]

## Platforms

- Network Devices
- Windows

