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
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "Linux"
  - "macOS"
  - "Network Devices"
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
d3fend_ids:
  - "D3-EAL"
  - "D3-EDL"
  - "D3-HBPI"
  - "D3-PSA"
  - "D3-SCA"
  - "D3-SCF"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

An adversary may gather the system time and/or time zone settings from a local or remote system. The system time is set and stored by services, such as the Windows Time Service on Windows or `systemsetup` on macOS.(Citation: MSDN System Time)(Citation: Technet Windows Time Service)(Citation: systemsetup mac time) These time settings may also be synchronized between systems and services in an enterprise network, typically accomplished with a network time server within a domain.(Citation: Mac Time Sync)(Citation: linux system time)

System time information may be gathered in a number of ways, such as with [[net|Net (S0039)]] on Windows by performing `net time \\hostname` to gather the system time on a remote system. The victim's time zone may also be inferred from the current system time or gathered by using `w32tm /tz`.(Citation: Technet Windows Time Service) In addition, adversaries can discover device uptime through functions such as `GetTickCount()` to determine how long it has been since the system booted up.(Citation: Virtualization/Sandbox Evasion)

On network devices, [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] commands such as `show clock detail` can be used to see the current time configuration.(Citation: show_clock_detail_cisco_cmd) On ESXi servers, `esxcli system clock get` can be used for the same purpose.

In addition, system calls – such as `time()` – have been used to collect the current time on Linux devices.(Citation: MAGNET GOBLIN) On macOS systems, adversaries may use commands such as `systemsetup -gettimezone` or `timeIntervalSinceNow` to gather current time zone information or current date and time.(Citation: System Information Discovery Technique)(Citation: ESET DazzleSpy Jan 2022)

This information could be useful for performing other techniques, such as executing a file with a [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]](Citation: RSA EU12 They're Inside), or to discover locality information based on time zone to assist in victim targeting (i.e. [[T1614-system_location_discovery|T1614: System Location Discovery]]). Adversaries may also use knowledge of system time as part of a time bomb, or delaying execution until a specified date/time.(Citation: AnyRun TimeBomb)

## Workspace

- [[workspaces/attack/techniques/T1124-system_time_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1124-system_time_discovery-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/6da2c9f5_7c53_401b_aacb_92c040ce1215-use_of_w32tm_as_timer|Use of W32tm as Timer (high; windows / process_creation)]]

### Atomic Tests

- [[kb/atomic/tests/1d5711d6_655c_4a47_ae9c_6503c74fa877-system_time_discovery_powershell|System Time Discovery - PowerShell (powershell; windows)]]
- [[kb/atomic/tests/20aba24b_e61f_4b26_b4ce_4784f763ca20-system_time_discovery|System Time Discovery (command_prompt; windows)]]
- [[kb/atomic/tests/25c5d1f1_a24b_494a_a6c5_5f50a1ae7f47-discover_system_time_zone_via_registry|Discover System Time Zone via Registry (command_prompt; windows)]]
- [[kb/atomic/tests/53ead5db_7098_4111_bb3f_563be390e72e-system_time_with_windows_time_command|System Time with Windows time Command (command_prompt; windows)]]
- [[kb/atomic/tests/d5d5a6b0_0f92_42d8_985d_47aafa2dd4db-system_time_discovery_w32tm_as_a_delay|System Time Discovery W32tm as a Delay (command_prompt; windows)]]
- [[kb/atomic/tests/f449c933_0891_407f_821e_7916a21a1a6f-system_time_discovery_in_freebsd_macos|System Time Discovery in FreeBSD/macOS (sh; linux, macos)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## D3FEND

- [[D3-EAL-executable_allowlisting|D3-EAL: Executable Allowlisting]]
- [[D3-EDL-executable_denylisting|D3-EDL: Executable Denylisting]]
- [[D3-HBPI-hardware-based_process_isolation|D3-HBPI: Hardware-based Process Isolation]]
- [[D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]
- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]

## Tools

- [[net|Net (S0039)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]

## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

