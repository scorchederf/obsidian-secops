---
mitre_id: "T1005"
mitre_name: "Data from Local System"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--3c4a2599-71ee-4405-ba1e-0e28414b4bc5"
mitre_created: "2017-05-31T21:30:20.537Z"
mitre_modified: "2025-10-24T17:48:40.839Z"
mitre_version: "1.8"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1005/"
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
  - "TA0009"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may search local system sources, such as file systems, configuration files, local databases, virtual machine files, or process memory, to find files of interest and sensitive data prior to Exfiltration.

Adversaries may do this using a [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]], such as [[cmd|cmd (S0106)]] as well as a [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]], which have functionality to interact with the file system to gather information.(Citation: show_run_config_cmd_cisco) Adversaries may also use [[T1119-automated_collection|T1119: Automated Collection]] on the local system.


## Workspace

- [[workspaces/attack/techniques/T1005-data_from_local_system-note|Open workspace note]]

![[workspaces/attack/techniques/T1005-data_from_local_system-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/0f60b28c_64dd_4e2c_9a63_5334d3e3a6e6-script_interpreter_spawning_credential_scanner_windows|Script Interpreter Spawning Credential Scanner - Windows (high; windows / process_creation)]]
- [[kb/sigma/rules/22777c9e_873a_4b49_855f_6072ab861a52-opencanary_smb_file_open_request|OpenCanary - SMB File Open Request (high; opencanary / application)]]
- [[kb/sigma/rules/24c77512_782b_448a_8950_eddb0785fc71-sqlite_chromium_profile_data_db_access|SQLite Chromium Profile Data DB Access (high; windows / process_creation)]]
- [[kb/sigma/rules/4833155a_4053_4c9c_a997_777fcea0baa7-sqlite_firefox_profile_data_db_access|SQLite Firefox Profile Data DB Access (high; windows / process_creation)]]
- [[kb/sigma/rules/b57ba453_b384_4ab9_9f40_1038086b4e53-veeambackup_database_credentials_dump_via_sqlcmd_exe|VeeamBackup Database Credentials Dump Via Sqlcmd.EXE (high; windows / process_creation)]]
- [[kb/sigma/rules/f0025a69_e1b7_4dda_a53c_db21fa2d4071-script_interpreter_spawning_credential_scanner_linux|Script Interpreter Spawning Credential Scanner - Linux (high; linux / process_creation)]]

### Atomic Tests

- [[kb/atomic/tests/00cbb875_7ae4_4cf1_b638_e543fd825300-find_and_dump_sqlite_databases_linux|Find and dump sqlite databases (Linux) (bash; linux)]]
- [[kb/atomic/tests/cfb6d400_a269_4c06_a347_6d88d584d5f7-copy_apple_notes_database_files_using_applescript|Copy Apple Notes database files using AppleScript (sh; macos)]]
- [[kb/atomic/tests/d3d9af44_b8ad_4375_8b0a_4bff4b7e419c-search_files_of_interest_and_save_them_to_a_single_zip_file_windows|Search files of interest and save them to a single zip file (Windows) (powershell; windows)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0009-collection|TA0009: Collection]]

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

## Mitigations

- [[M1057-data_loss_prevention|M1057: Data Loss Prevention]]

## Tools
- [[brute_ratel_c4|Brute Ratel C4 (S1063)]]
- [[esentutl|esentutl (S0404)]]
- [[forfiles|Forfiles (S0193)]]
- [[koadic|Koadic (S0250)]]
- [[mcmd|MCMD (S0500)]]
- [[nppspy|NPPSPY (S1131)]]
- [[out1|Out1 (S0594)]]
- [[pcshare|PcShare (S1050)]]
- [[powersploit|PowerSploit (S0194)]]
- [[quasarrat|QuasarRAT (S0262)]]
- [[wevtutil|Wevtutil (S0645)]]


## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

