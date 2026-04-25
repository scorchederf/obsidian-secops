---
mitre_id: "T1614"
mitre_name: "System Location Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--c877e33f-1df6-40d6-b1e7-ce70f16f4979"
mitre_created: "2021-04-01T16:42:08.735Z"
mitre_modified: "2025-10-24T17:49:22.536Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1614/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "IaaS"
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
d3fend_ids:
  - "D3-CI"
  - "D3-DI"
  - "D3-RC"
  - "D3-RD"
  - "D3-SCP"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---


Adversaries may gather information in an attempt to calculate the geographical location of a victim host. Adversaries may use the information from [[T1614-system_location_discovery|T1614: System Location Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Adversaries may attempt to infer the location of a system using various system checks, such as time zone, keyboard layout, and/or language settings.(Citation: FBI Ragnar Locker 2020)(Citation: Sophos Geolocation 2016)(Citation: Bleepingcomputer RAT malware 2020) Windows API functions such as `GetLocaleInfoW` can also be used to determine the locale of the host.(Citation: FBI Ragnar Locker 2020) In cloud environments, an instance's availability zone may also be discovered by accessing the instance metadata service from the instance.(Citation: AWS Instance Identity Documents)(Citation: Microsoft Azure Instance Metadata 2021)

Adversaries may also attempt to infer the location of a victim host using IP addressing, such as via online geolocation IP-lookup services.(Citation: Securelist Trasparent Tribe 2020)(Citation: Sophos Geolocation 2016)

## Workspace

- [[workspaces/attack/techniques/T1614-system_location_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1614-system_location_discovery-note]]

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## D3FEND

- [[D3-CI-configuration_inventory|D3-CI: Configuration Inventory]]
- [[D3-DI-data_inventory|D3-DI: Data Inventory]]
- [[D3-RC-restore_configuration|D3-RC: Restore Configuration]]
- [[D3-RD-restore_database|D3-RD: Restore Database]]
- [[D3-SCP-system_configuration_permissions|D3-SCP: System Configuration Permissions]]

## Subtechniques

### T1614.001: System Language Discovery

^t1614001-system-language-discovery

Adversaries may attempt to gather information about the system language of a victim in order to infer the geographical location of that host. This information may be used to shape follow-on behaviors, including whether the adversary infects the target and/or attempts specific actions. This decision may be employed by malware developers and operators to reduce their risk of attracting the attention of specific law enforcement agencies or prosecution/scrutiny from other entities.(Citation: Malware System Language Check)

There are various sources of data an adversary could use to infer system language, such as system defaults and keyboard layouts. Specific checks will vary based on the target and/or adversary, but may involve behaviors such as [[T1012-query_registry|T1012: Query Registry]] and calls to [[T1106-native_api|T1106: Native API]] functions.(Citation: CrowdStrike Ryuk January 2019) 

For example, on a Windows system adversaries may attempt to infer the language of a system by querying the registry key `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Nls\Language` or parsing the outputs of Windows API functions `GetUserDefaultUILanguage`, `GetSystemDefaultUILanguage`, `GetKeyboardLayoutList` and `GetUserDefaultLangID`.(Citation: Darkside Ransomware Cybereason)(Citation: Securelist JSWorm)(Citation: SecureList SynAck Doppelgänging May 2018)

On a macOS or Linux system, adversaries may query `locale` to retrieve the value of the `$LANG` environment variable.

## Tools

- [[quasarrat|QuasarRAT (S0262)]]

## Platforms

- IaaS
- Linux
- macOS
- Windows

