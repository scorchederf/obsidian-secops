---
mitre_id: "T1124"
mitre_name: "System Time Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--f3c544dc-673c-4ef3-accb-53229f1ae077"
mitre_created: "2017-05-31T21:31:37.450Z"
mitre_modified: "2025-10-24T17:49:36.399Z"
mitre_version: "1.5"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1124/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "Linux"
  - "macOS"
  - "Network Devices"
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
---

# T1124: System Time Discovery

An adversary may gather the system time and/or time zone settings from a local or remote system. The system time is set and stored by services, such as the Windows Time Service on Windows or `systemsetup` on macOS.(Citation: MSDN System Time)(Citation: Technet Windows Time Service)(Citation: systemsetup mac time) These time settings may also be synchronized between systems and services in an enterprise network, typically accomplished with a network time server within a domain.(Citation: Mac Time Sync)(Citation: linux system time)

System time information may be gathered in a number of ways, such as with [[net|Net]] on Windows by performing `net time \\hostname` to gather the system time on a remote system. The victim's time zone may also be inferred from the current system time or gathered by using `w32tm /tz`.(Citation: Technet Windows Time Service) In addition, adversaries can discover device uptime through functions such as `GetTickCount()` to determine how long it has been since the system booted up.(Citation: Virtualization/Sandbox Evasion)

On network devices, [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] commands such as `show clock detail` can be used to see the current time configuration.(Citation: show_clock_detail_cisco_cmd) On ESXi servers, `esxcli system clock get` can be used for the same purpose.

In addition, system calls – such as `time()` – have been used to collect the current time on Linux devices.(Citation: MAGNET GOBLIN) On macOS systems, adversaries may use commands such as `systemsetup -gettimezone` or `timeIntervalSinceNow` to gather current time zone information or current date and time.(Citation: System Information Discovery Technique)(Citation: ESET DazzleSpy Jan 2022)

This information could be useful for performing other techniques, such as executing a file with a [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]](Citation: RSA EU12 They're Inside), or to discover locality information based on time zone to assist in victim targeting (i.e. [[T1614-system_location_discovery|T1614: System Location Discovery]]). Adversaries may also use knowledge of system time as part of a time bomb, or delaying execution until a specified date/time.(Citation: AnyRun TimeBomb)

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Tools

- [[net|Net]]
- [[silenttrinity|SILENTTRINITY]]

## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

