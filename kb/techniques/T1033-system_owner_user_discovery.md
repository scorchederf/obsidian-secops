---
mitre_id: "T1033"
mitre_name: "System Owner/User Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--03d7999c-1f4c-42cc-8373-e7690d318104"
mitre_created: "2017-05-31T21:30:35.733Z"
mitre_modified: "2025-10-24T17:48:20.366Z"
mitre_version: "1.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1033/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Network Devices"
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
---

# T1033: System Owner/User Discovery

Adversaries may attempt to identify the primary user, currently logged in user, set of users that commonly uses a system, or whether a user is actively using the system. They may do this, for example, by retrieving account usernames or by using [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]. The information may be collected in a number of different ways using other Discovery techniques, because user and username details are prevalent throughout a system and include running process ownership, file/directory ownership, session information, and system logs. Adversaries may use the information from [[T1033-system_owner_user_discovery|T1033: System Owner/User Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Various utilities and commands may acquire this information, including `whoami`. In macOS and Linux, the currently logged in user can be identified with `w` and `who`. On macOS the `dscl . list /Users | grep -v '_'` command can also be used to enumerate user accounts. Environment variables, such as `%USERNAME%` and `$USER`, may also be used to access this information.

On network devices, [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] commands such as `show users` and `show ssh` can be used to display users currently logged into the device.(Citation: show_ssh_users_cmd_cisco)(Citation: US-CERT TA18-106A Network Infrastructure Devices 2018)

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Tools

- [[pupy|Pupy]]
- [[koadic|Koadic]]
- [[quasarrat|QuasarRAT]]
- [[empire|Empire]]
- [[bloodhound|BloodHound]]
- [[nbtscan|NBTscan]]
- [[silenttrinity|SILENTTRINITY]]
- [[asyncrat|AsyncRAT]]

## Platforms

- Linux
- macOS
- Network Devices
- Windows

