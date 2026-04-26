---
mitre_id: "T1083"
mitre_name: "File and Directory Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--7bc57495-ea59-4380-be31-a64af124ef18"
mitre_created: "2017-05-31T21:31:04.710Z"
mitre_modified: "2025-10-24T17:49:00.036Z"
mitre_version: "1.7"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1083/"
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
  - "D3-CF"
  - "D3-CM"
  - "D3-CQ"
  - "D3-DF"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-LFP"
  - "D3-RF"
  - "D3-RFAM"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may enumerate files and directories or may search in specific locations of a host or network share for certain information within a file system. Adversaries may use the information from [[T1083-file_and_directory_discovery|T1083: File and Directory Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Many command shell utilities can be used to obtain this information. Examples include `dir`, `tree`, `ls`, `find`, and `locate`.(Citation: Windows Commands JPCERT) Custom tools may also be used to gather file and directory information and interact with the [[T1106-native_api|T1106: Native API]]. Adversaries may also leverage a [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] on network devices to gather file and directory information (e.g. `dir`, `show flash`, and/or `nvram`).(Citation: US-CERT-TA18-106A)

Some files and directories may require elevated or specific user permissions to access.

## Workspace

- [[workspaces/attack/techniques/T1083-file_and_directory_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1083-file_and_directory_discovery-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/093d68c7_762a_42f4_9f46_95e79142571a-shell_execution_via_nice_linux|Shell Execution via Nice - Linux (high; linux / process_creation)]]
- [[kb/sigma/rules/38646daa_e78f_4ace_9de0_55547b2d30da-pua_seatbelt_execution|PUA - Seatbelt Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/4b09c71e_4269_4111_9cdd_107d8867f0cc-shell_execution_via_flock_linux|Shell Execution via Flock - Linux (high; linux / process_creation)]]
- [[kb/sigma/rules/6adfbf8f_52be_4444_9bac_81b539624146-shell_execution_via_find_linux|Shell Execution via Find - Linux (high; linux / process_creation)]]
- [[kb/sigma/rules/7ab8f73a_fcff_428b_84aa_6a5ff7877dea-vim_gtfobin_abuse_linux|Vim GTFOBin Abuse - Linux (high; linux / process_creation)]]
- [[kb/sigma/rules/9b5de532_a757_4d70_946c_1f3e44f48b4d-shell_execution_gcc_linux|Shell Execution GCC  - Linux (high; linux / process_creation)]]
- [[kb/sigma/rules/fca949cc_79ca_446e_8064_01aa7e52ece5-hacktool_pchunter_execution|HackTool - PCHunter Execution (high; windows / process_creation)]]

### Atomic Tests

- [[kb/atomic/tests/0e36303b_6762_4500_b003_127743b80ba6-file_and_directory_discovery_cmd_exe|File and Directory Discovery (cmd.exe) (command_prompt; windows)]]
- [[kb/atomic/tests/13c5e1ae_605b_46c4_a79f_db28c77ff24e-nix_file_and_directory_discovery_2|Nix File and Directory Discovery 2 (sh; linux, macos)]]
- [[kb/atomic/tests/2158908e_b7ef_4c21_8a83_3ce4dd05a924-file_and_directory_discovery_powershell|File and Directory Discovery (PowerShell) (powershell; windows)]]
- [[kb/atomic/tests/361fe49d_0c19_46ec_a483_ccb92d38e88e-identifying_network_shares_linux|Identifying Network Shares - Linux (sh; linux)]]
- [[kb/atomic/tests/4a233a40_caf7_4cf1_890a_c6331bbc72cf-esxi_enumerate_vmdks_available_on_an_esxi_host|ESXi - Enumerate VMDKs available on an ESXi Host (command_prompt; windows)]]
- [[kb/atomic/tests/95a21323_770d_434c_80cd_6f6fbf7af432-recursive_enumerate_files_and_directories_by_powershell|Recursive Enumerate Files And Directories By Powershell (powershell; windows)]]
- [[kb/atomic/tests/c5bec457_43c9_4a18_9a24_fe151d8971b7-launch_dirlister_executable|Launch DirLister Executable (powershell; windows)]]
- [[kb/atomic/tests/c6c34f61_1c3e_40fb_8a58_d017d88286d8-simulating_maze_directory_enumeration|Simulating MAZE Directory Enumeration (powershell; windows)]]
- [[kb/atomic/tests/ffc8b249_372a_4b74_adcd_e4c0430842de-nix_file_and_directory_discovery|Nix File and Directory Discovery (sh; linux, macos)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## D3FEND

- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]

## Tools
- [[cmd|cmd (S0106)]]
- [[crackmapexec|CrackMapExec (S0488)]]
- [[empire|Empire (S0363)]]
- [[forfiles|Forfiles (S0193)]]
- [[imminent_monitor|Imminent Monitor (S0434)]]
- [[koadic|Koadic (S0250)]]
- [[poshc2|PoshC2 (S0378)]]
- [[pupy|Pupy (S0192)]]
- [[rclone|Rclone (S1040)]]
- [[remcos|Remcos (S0332)]]
- [[remoteutilities|RemoteUtilities (S0592)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]
- [[sliver|Sliver (S0633)]]


## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

