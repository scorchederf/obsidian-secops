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
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Network Devices"
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
d3fend_ids:
  - "D3-ABPI"
  - "D3-CF"
  - "D3-CM"
  - "D3-CQ"
  - "D3-DF"
  - "D3-DI"
  - "D3-DTP"
  - "D3-EAL"
  - "D3-EDL"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-HBPI"
  - "D3-HR"
  - "D3-HS"
  - "D3-KBPI"
  - "D3-LFP"
  - "D3-PLA"
  - "D3-PS"
  - "D3-PSA"
  - "D3-PSEP"
  - "D3-PSMD"
  - "D3-PT"
  - "D3-RD"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-SAOR"
  - "D3-SCA"
  - "D3-SCF"
  - "D3-WSAM"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may attempt to identify the primary user, currently logged in user, set of users that commonly uses a system, or whether a user is actively using the system. They may do this, for example, by retrieving account usernames or by using [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]. The information may be collected in a number of different ways using other Discovery techniques, because user and username details are prevalent throughout a system and include running process ownership, file/directory ownership, session information, and system logs. Adversaries may use the information from [[T1033-system_owner_user_discovery|T1033: System Owner/User Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Various utilities and commands may acquire this information, including `whoami`. In macOS and Linux, the currently logged in user can be identified with `w` and `who`. On macOS the `dscl . list /Users | grep -v '_'` command can also be used to enumerate user accounts. Environment variables, such as `%USERNAME%` and `$USER`, may also be used to access this information.

On network devices, [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] commands such as `show users` and `show ssh` can be used to display users currently logged into the device.(Citation: show_ssh_users_cmd_cisco)(Citation: US-CERT TA18-106A Network Infrastructure Devices 2018)

## Workspace

- [[workspaces/attack/techniques/T1033-system_owner_user_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1033-system_owner_user_discovery-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2016-03-001-host_discovery_commands|CAR-2016-03-001: Host Discovery Commands]]

### Sigma Rules

- [[kb/sigma/rules/4ebc877f_4612_45cb_b3a5_8e3834db36c9-webshell_hacking_activity_patterns|Webshell Hacking Activity Patterns (high; windows / process_creation)]]
- [[kb/sigma/rules/56fda488_113e_4ce9_8076_afc2457922c3-possible_dcsync_attack|Possible DCSync Attack (high; rpc_firewall / application)]]
- [[kb/sigma/rules/6d580420_ff3f_4e0e_b6b0_41b90c787e28-sharphound_recon_sessions|SharpHound Recon Sessions (high; rpc_firewall / application)]]
- [[kb/sigma/rules/79ce34ca_af29_4d0e_b832_fc1b377020db-whoami_exe_execution_from_privileged_process|Whoami.EXE Execution From Privileged Process (high; windows / process_creation)]]
- [[kb/sigma/rules/97a80ec7_0e2f_4d05_9ef4_65760e634f6b-security_privileges_enumeration_via_whoami_exe|Security Privileges Enumeration Via Whoami.EXE (high; windows / process_creation)]]
- [[kb/sigma/rules/b2317cfa_4a47_4ead_b3ff_297438c0bc2d-hacktool_sharpview_execution|HackTool - SharpView Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/bed2a484_9348_4143_8a8a_b801c979301c-webshell_detection_with_command_line_keywords|Webshell Detection With Command Line Keywords (high; windows / process_creation)]]
- [[kb/sigma/rules/d9367cbb_c2e0_47ce_bdc0_128cb6da898d-hacktool_sharpldapwhoami_execution|HackTool - SharpLdapWhoami Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/e9142d84_fbe0_401d_ac50_3e519fb00c89-whoami_as_parameter|WhoAmI as Parameter (high; windows / process_creation)]]
- [[kb/sigma/rules/f1086bf7_a0c4_4a37_9102_01e573caf4a0-renamed_whoami_execution|Renamed Whoami Execution (critical; windows / process_creation)]]
- 1 more in the generated source index

### Atomic Tests

- [[kb/atomic/tests/1392bd0f_5d5a_429e_81d9_eb9d4d4d5b3b-getcurrent_user_with_powershell_script|GetCurrent User with PowerShell Script (powershell; windows)]]
- [[kb/atomic/tests/29857f27_a36f_4f7e_8084_4557cd6207ca-find_computers_where_user_has_session_stealth_mode_powerview|Find computers where user has session - Stealth mode (PowerView) (powershell; windows)]]
- [[kb/atomic/tests/2a9b677d_a230_44f4_ad86_782df1ef108c-system_owner_user_discovery|System Owner/User Discovery (sh; linux, macos)]]
- [[kb/atomic/tests/3d257a03_eb80_41c5_b744_bb37ac7f65c7-system_discovery_socgholish_whoami|System Discovery - SocGholish whoami (powershell; windows)]]
- [[kb/atomic/tests/4c4959bf_addf_4b4a_be86_8d09cc1857aa-system_owner_user_discovery|System Owner/User Discovery (command_prompt; windows)]]
- [[kb/atomic/tests/ba38e193_37a6_4c41_b214_61b33277fe36-system_owner_user_discovery_using_command_prompt|System Owner/User Discovery Using Command Prompt (command_prompt; windows)]]
- [[kb/atomic/tests/dcb6cdee_1fb0_4087_8bf8_88cfd136ba51-user_discovery_with_env_vars_powershell_script|User Discovery With Env Vars PowerShell Script (powershell; windows)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## D3FEND

- [[D3-ABPI-application-based_process_isolation|D3-ABPI: Application-based Process Isolation]]
- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-DI-data_inventory|D3-DI: Data Inventory]]
- [[D3-DTP-domain_trust_policy|D3-DTP: Domain Trust Policy]]
- [[D3-EAL-executable_allowlisting|D3-EAL: Executable Allowlisting]]
- [[D3-EDL-executable_denylisting|D3-EDL: Executable Denylisting]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-HBPI-hardware-based_process_isolation|D3-HBPI: Hardware-based Process Isolation]]
- [[D3-HR-host_reboot|D3-HR: Host Reboot]]
- [[D3-HS-host_shutdown|D3-HS: Host Shutdown]]
- [[D3-KBPI-kernel-based_process_isolation|D3-KBPI: Kernel-based Process Isolation]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-PLA-process_lineage_analysis|D3-PLA: Process Lineage Analysis]]
- [[D3-PS-process_suspension|D3-PS: Process Suspension]]
- [[D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]
- [[D3-PSEP-process_segment_execution_prevention|D3-PSEP: Process Segment Execution Prevention]]
- [[D3-PSMD-process_self-modification_detection|D3-PSMD: Process Self-Modification Detection]]
- [[D3-PT-process_termination|D3-PT: Process Termination]]
- [[D3-RD-restore_database|D3-RD: Restore Database]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-SAOR-segment_address_offset_randomization|D3-SAOR: Segment Address Offset Randomization]]
- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]
- [[D3-WSAM-web_session_access_mediation|D3-WSAM: Web Session Access Mediation]]

## Tools
- [[asyncrat|AsyncRAT (S1087)]]
- [[bloodhound|BloodHound (S0521)]]
- [[empire|Empire (S0363)]]
- [[koadic|Koadic (S0250)]]
- [[nbtscan|NBTscan (S0590)]]
- [[pupy|Pupy (S0192)]]
- [[quasarrat|QuasarRAT (S0262)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]


## Platforms

- Linux
- macOS
- Network Devices
- Windows

