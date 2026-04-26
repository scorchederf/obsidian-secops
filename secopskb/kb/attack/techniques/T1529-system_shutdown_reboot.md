---
mitre_id: "T1529"
mitre_name: "System Shutdown/Reboot"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--ff73aa03-0090-4464-83ac-f89e233c02bc"
mitre_created: "2019-10-04T20:42:28.541Z"
mitre_modified: "2025-10-24T17:49:40.145Z"
mitre_version: "1.5"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1529/"
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
  - "TA0040"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may shutdown/reboot systems to interrupt access to, or aid in the destruction of, those systems. Operating systems may contain commands to initiate a shutdown/reboot of a machine or network device. In some cases, these commands may also be used to initiate a shutdown/reboot of a remote computer or network device via [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] (e.g. `reload`).(Citation: Microsoft Shutdown Oct 2017)(Citation: alert_TA18_106A) They may also include shutdown/reboot of a virtual machine via hypervisor / cloud consoles or command line tools.

Shutting down or rebooting systems may disrupt access to computer resources for legitimate users while also impeding incident response/recovery.

Adversaries may also use Windows API functions, such as `InitializeSystemShutdownExW` or `ExitWindowsEx`, to force a system to shut down or reboot.(Citation: CrowdStrike Blog)(Citation: Unit42 Agrius 2023) Alternatively, the `NtRaiseHardError`or `ZwRaiseHardError` Windows API functions with the `ResponseOption` parameter set to `OptionShutdownSystem` may deliver a “blue screen of death” (BSOD) to a system.(Citation: SonicWall)(Citation: NtRaiseHardError)(Citation: NotMe-BSOD) In order to leverage these API functions, an adversary may need to acquire `SeShutdownPrivilege` (e.g., via [[T1134-access_token_manipulation|T1134: Access Token Manipulation]]).(Citation: Unit42 Agrius 2023)
 In some cases, the system may not be able to boot again. 

Adversaries may attempt to shutdown/reboot a system after impacting it in other ways, such as [[T1561-disk_wipe#^t1561002-disk-structure-wipe|T1561.002: Disk Structure Wipe]] or [[T1490-inhibit_system_recovery|T1490: Inhibit System Recovery]], to hasten the intended effects on system availability.(Citation: Talos Nyetya June 2017)(Citation: Talos Olympic Destroyer 2018)

## Workspace

- [[workspaces/attack/techniques/T1529-system_shutdown_reboot-note|Open workspace note]]

![[workspaces/attack/techniques/T1529-system_shutdown_reboot-note]]

## Tactics

- [[TA0040-impact|TA0040: Impact]]

## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

