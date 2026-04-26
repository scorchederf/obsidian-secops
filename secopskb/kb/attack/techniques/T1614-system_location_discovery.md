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
build_date: "2026-04-26 13:08:46"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---


Adversaries may gather information in an attempt to calculate the geographical location of a victim host. Adversaries may use the information from [[T1614-system_location_discovery|T1614: System Location Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Adversaries may attempt to infer the location of a system using various system checks, such as time zone, keyboard layout, and/or language settings.(Citation: FBI Ragnar Locker 2020)(Citation: Sophos Geolocation 2016)(Citation: Bleepingcomputer RAT malware 2020) Windows API functions such as `GetLocaleInfoW` can also be used to determine the locale of the host.(Citation: FBI Ragnar Locker 2020) In cloud environments, an instance's availability zone may also be discovered by accessing the instance metadata service from the instance.(Citation: AWS Instance Identity Documents)(Citation: Microsoft Azure Instance Metadata 2021)

Adversaries may also attempt to infer the location of a victim host using IP addressing, such as via online geolocation IP-lookup services.(Citation: Securelist Trasparent Tribe 2020)(Citation: Sophos Geolocation 2016)

## Workspace

- [[workspaces/attack/techniques/T1614-system_location_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1614-system_location_discovery-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Atomic Tests

- [[kb/atomic/tests/07ce871a_b3c3_44a3_97fa_a20118fdc7c9-discover_system_language_with_localectl|Discover System Language with localectl (sh; linux)]]
- [[kb/atomic/tests/1f23bfe8_36d4_49ce_903a_19a1e8c6631b-discover_system_language_with_powershell|Discover System Language with Powershell (powershell; windows)]]
- [[kb/atomic/tests/4758003d_db14_4959_9c0f_9e87558ac69e-discover_system_language_with_wmic|Discover System Language with WMIC (command_prompt; windows)]]
- [[kb/atomic/tests/552b4db3_8850_412c_abce_ab5cc8a86604-get_geolocation_info_through_ip_lookup_services_using_curl_freebsd_linux_or_macos|Get geolocation info through IP-Lookup services using curl freebsd, linux or macos (bash; macos, linux)]]
- [[kb/atomic/tests/5d7057c9_2c8a_4026_91dd_13b5584daa69-discover_system_language_by_locale_file|Discover System Language by locale file (sh; linux)]]
- [[kb/atomic/tests/631d4cf1_42c9_4209_8fe9_6bd4de9421be-discover_system_language_by_registry_query|Discover System Language by Registry Query (command_prompt; windows)]]
- [[kb/atomic/tests/69f625ba_938f_4900_bdff_82ada3df5d9c-discover_system_language_with_dism_exe|Discover System Language with dism.exe (command_prompt; windows)]]
- [[kb/atomic/tests/837d609b_845e_4519_90ce_edc3b4b0e138-discover_system_language_with_locale|Discover System Language with locale (sh; linux)]]
- [[kb/atomic/tests/cb8f7cdc_36c4_4ed0_befc_7ad7d24dfd7a-discover_system_language_by_environment_variable_query|Discover System Language by Environment Variable Query (sh; linux)]]
- [[kb/atomic/tests/d91473ca_944e_477a_b484_0e80217cd789-discover_system_language_with_chcp|Discover System Language with chcp (command_prompt; windows)]]
- 2 more in the generated source index

<!-- generated-detection-validation-end -->

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

