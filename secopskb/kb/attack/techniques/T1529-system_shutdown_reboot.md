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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may shutdown/reboot systems to interrupt access to, or aid in the destruction of, those systems. Operating systems may contain commands to initiate a shutdown/reboot of a machine or network device. In some cases, these commands may also be used to initiate a shutdown/reboot of a remote computer or network device via [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] (e.g. `reload`).(Citation: Microsoft Shutdown Oct 2017)(Citation: alert_TA18_106A) They may also include shutdown/reboot of a virtual machine via hypervisor / cloud consoles or command line tools.

Shutting down or rebooting systems may disrupt access to computer resources for legitimate users while also impeding incident response/recovery.

Adversaries may also use Windows API functions, such as `InitializeSystemShutdownExW` or `ExitWindowsEx`, to force a system to shut down or reboot.(Citation: CrowdStrike Blog)(Citation: Unit42 Agrius 2023) Alternatively, the `NtRaiseHardError`or `ZwRaiseHardError` Windows API functions with the `ResponseOption` parameter set to `OptionShutdownSystem` may deliver a “blue screen of death” (BSOD) to a system.(Citation: SonicWall)(Citation: NtRaiseHardError)(Citation: NotMe-BSOD) In order to leverage these API functions, an adversary may need to acquire `SeShutdownPrivilege` (e.g., via [[T1134-access_token_manipulation|T1134: Access Token Manipulation]]).(Citation: Unit42 Agrius 2023)
 In some cases, the system may not be able to boot again. 

Adversaries may attempt to shutdown/reboot a system after impacting it in other ways, such as [[T1561-disk_wipe#^t1561002-disk-structure-wipe|T1561.002: Disk Structure Wipe]] or [[T1490-inhibit_system_recovery|T1490: Inhibit System Recovery]], to hasten the intended effects on system availability.(Citation: Talos Nyetya June 2017)(Citation: Talos Olympic Destroyer 2018)

## Workspace

- [[workspaces/attack/techniques/T1529-system_shutdown_reboot-note|Open workspace note]]

![[workspaces/attack/techniques/T1529-system_shutdown_reboot-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/3ceb2083_a27f_449a_be33_14ec1b7cc973-silence_eda_detection|Silence.EDA Detection (critical; windows / ps_script)]]

### Atomic Tests

- [[kb/atomic/tests/189f7d6e_9442_4160_9bc3_5e4104d93ece-esxi_avoslocker_enumerates_vms_and_forcefully_kills_vms|ESXi - Avoslocker enumerates VMs and forcefully kills VMs (command_prompt; windows)]]
- [[kb/atomic/tests/3d8c25b5_7ff5_4c9d_b21f_85ebd06654a4-logoff_system_windows|Logoff System - Windows (command_prompt; windows)]]
- [[kb/atomic/tests/47d0b042_a918_40ab_8cf9_150ffe919027-restart_system_via_reboot_freebsd_macos_linux|Restart System via `reboot` - FreeBSD/macOS/Linux (sh; linux, macos)]]
- [[kb/atomic/tests/4963a81e_a3ad_4f02_adda_812343b351de-shutdown_system_via_shutdown_freebsd_macos_linux|Shutdown System via `shutdown` - FreeBSD/macOS/Linux (sh; linux, macos)]]
- [[kb/atomic/tests/5a282e50_86ff_438d_8cef_8ae01c9e62e1-reboot_system_via_poweroff_freebsd|Reboot System via `poweroff` - FreeBSD (sh; linux)]]
- [[kb/atomic/tests/61303105_ff60_427b_999e_efb90b314e41-reboot_system_via_poweroff_linux|Reboot System via `poweroff` - Linux (bash; linux)]]
- [[kb/atomic/tests/622cc1a0_45e7_428c_aed7_c96dd605fbe6-esxi_vim_cmd_used_to_power_off_vms|ESXi - vim-cmd Used to Power Off VMs (command_prompt; windows)]]
- [[kb/atomic/tests/6326dbc4_444b_4c04_88f4_27e94d0327cb-restart_system_via_shutdown_freebsd_macos_linux|Restart System via `shutdown` - FreeBSD/macOS/Linux (sh; linux, macos)]]
- [[kb/atomic/tests/73a90cd2_48a2_4ac5_8594_2af35fa909fa-shutdown_system_via_poweroff_freebsd_linux|Shutdown System via `poweroff` - FreeBSD/Linux (sh; linux)]]
- [[kb/atomic/tests/78f92e14_f1e9_4446_b3e9_f1b921f2459e-reboot_system_via_halt_linux|Reboot System via `halt` - Linux (bash; linux)]]
- 6 more in the generated source index

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0040-impact|TA0040: Impact]]

## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

