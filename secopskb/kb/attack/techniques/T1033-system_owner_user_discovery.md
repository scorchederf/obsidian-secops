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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Adversaries may attempt to identify the primary user, currently logged in user, set of users that commonly uses a system, or whether a user is actively using the system. They may do this, for example, by retrieving account usernames or by using [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]. The information may be collected in a number of different ways using other Discovery techniques, because user and username details are prevalent throughout a system and include running process ownership, file/directory ownership, session information, and system logs. Adversaries may use the information from [[T1033-system_owner_user_discovery|T1033: System Owner/User Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Various utilities and commands may acquire this information, including `whoami`. In macOS and Linux, the currently logged in user can be identified with `w` and `who`. On macOS the `dscl . list /Users | grep -v '_'` command can also be used to enumerate user accounts. Environment variables, such as `%USERNAME%` and `$USER`, may also be used to access this information.

On network devices, [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] commands such as `show users` and `show ssh` can be used to display users currently logged into the device.(Citation: show_ssh_users_cmd_cisco)(Citation: US-CERT TA18-106A Network Infrastructure Devices 2018)

## Workspace

- [[workspaces/attack/techniques/T1033-system_owner_user_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1033-system_owner_user_discovery-note]]

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

