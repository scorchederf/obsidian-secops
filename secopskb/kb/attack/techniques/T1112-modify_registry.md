---
mitre_id: "T1112"
mitre_name: "Modify Registry"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--57340c81-c025-4189-8fa0-fc7ede51bae4"
mitre_created: "2017-05-31T21:31:23.587Z"
mitre_modified: "2025-10-24T17:48:49.294Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1112/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
mitre_tactic_ids:
  - "TA0005"
  - "TA0003"
d3fend_ids:
  - "D3-DI"
  - "D3-RD"
  - "D3-SCP"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may interact with the Windows Registry as part of a variety of other techniques to aid in defense evasion, persistence, and execution.

Access to specific areas of the Registry depends on account permissions, with some keys requiring administrator-level access. The built-in Windows command-line utility [[reg|Reg (S0075)]] may be used for local or remote Registry modification.(Citation: Microsoft Reg) Other tools, such as remote access tools, may also contain functionality to interact with the Registry through the Windows API.

The Registry may be modified in order to hide configuration information or malicious payloads via [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]].(Citation: Unit42 BabyShark Feb 2019)(Citation: Avaddon Ransomware 2021)(Citation: Microsoft BlackCat Jun 2022)(Citation: CISA Russian Gov Critical Infra 2018) The Registry may also be modified to [[T1562-impair_defenses|T1562: Impair Defenses]], such as by enabling macros for all Microsoft Office products, allowing privilege escalation without alerting the user, increasing the maximum number of allowed outbound requests, and/or modifying systems to store plaintext credentials in memory.(Citation: CISA LockBit 2023)(Citation: Unit42 BabyShark Feb 2019)

The Registry of a remote system may be modified to aid in execution of files as part of lateral movement. It requires the remote Registry service to be running on the target system.(Citation: Microsoft Remote) Often [[T1078-valid_accounts|T1078: Valid Accounts]] are required, along with access to the remote system's [[T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]] for RPC communication.

Finally, Registry modifications may also include actions to hide keys, such as prepending key names with a null character, which will cause an error and/or be ignored when read via [[reg|Reg (S0075)]] or other utilities using the Win32 API.(Citation: Microsoft Reghide NOV 2006) Adversaries may abuse these pseudo-hidden keys to conceal payloads/commands used to maintain persistence.(Citation: TrendMicro POWELIKS AUG 2014)(Citation: SpectorOps Hiding Reg Jul 2017)

## Workspace

- [[workspaces/attack/techniques/T1112-modify_registry-note|Open workspace note]]

![[workspaces/attack/techniques/T1112-modify_registry-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]
- [[kb/car/analytics/CAR-2013-03-001-reg_exe_called_from_command_shell|CAR-2013-03-001: Reg.exe called from Command Shell]]
- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2014-11-005-remote_registry|CAR-2014-11-005: Remote Registry]]
- [[kb/car/analytics/CAR-2020-05-003-rare_lolbas_command_lines|CAR-2020-05-003: Rare LolBAS Command Lines]]
- [[kb/car/analytics/CAR-2021-11-001-registry_edit_with_creation_of_safedllsearchmode_key_set_to_0|CAR-2021-11-001: Registry Edit with Creation of SafeDllSearchMode Key Set to 0]]
- [[kb/car/analytics/CAR-2021-11-002-registry_edit_with_modification_of_userinit_shell_or_notify|CAR-2021-11-002: Registry Edit with Modification of Userinit, Shell or Notify]]
- [[kb/car/analytics/CAR-2021-12-002-modification_of_default_startup_folder_in_the_registry_key_common_startup|CAR-2021-12-002: Modification of Default Startup Folder in the Registry Key 'Common Startup']]

### Sigma Rules

- [[kb/sigma/rules/07bdd2f5_9c58_4f38_aec8_e101bb79ef8d-terminal_server_client_connection_history_cleared_registry|Terminal Server Client Connection History Cleared - Registry (high; windows / registry_delete)]]
- [[kb/sigma/rules/0b80ade5_6997_4b1d_99a1_71701778ea61-imports_registry_key_from_an_ads|Imports Registry Key From an ADS (high; windows / process_creation)]]
- [[kb/sigma/rules/0d5675be_bc88_4172_86d3_1e96a4476536-potential_tampering_with_rdp_related_registry_keys_via_reg_exe|Potential Tampering With RDP Related Registry Keys Via Reg.EXE (high; windows / process_creation)]]
- [[kb/sigma/rules/18beca67_ab3e_4ee3_ba7a_a46ca8d7d0cc-sysmon_channel_reference_deletion|Sysmon Channel Reference Deletion (high; windows / security)]]
- [[kb/sigma/rules/1a2d6c47_75b0_45bd_b133_2c0be75349fd-wdigest_credguard_registry_modification|Wdigest CredGuard Registry Modification (high; windows / registry_event)]]
- [[kb/sigma/rules/1a4bd6af_99ac_4466_b5b2_7b72b4a05462-security_event_logging_disabled_via_minint_registry_key_process|Security Event Logging Disabled via MiniNt Registry Key - Process (high; windows / process_creation)]]
- [[kb/sigma/rules/1a5c46e9_f32f_42f7_b2bc_6e9084db7fbf-trust_access_disable_for_vbapplications|Trust Access Disable For VBApplications (high; windows / registry_set)]]
- [[kb/sigma/rules/1c8e96cd_2bed_487d_9de0_b46c90cade56-potential_qakbot_registry_activity|Potential Qakbot Registry Activity (high; windows / registry_event)]]
- [[kb/sigma/rules/28036918_04d3_423d_91c0_55ecf99fb892-net_ngenassemblyusagelog_registry_key_tamper|NET NGenAssemblyUsageLog Registry Key Tamper (high; windows / registry_set)]]
- [[kb/sigma/rules/28ac00d6_22d9_4a3c_927f_bbd770104573-restrictedadminmode_registry_value_tampering_proccreation|RestrictedAdminMode Registry Value Tampering - ProcCreation (high; windows / process_creation)]]
- 34 more in the generated source index

### Atomic Tests

- [[kb/atomic/tests/003f466a_6010_4b15_803a_cbb478a314d7-disable_windows_toast_notifications|Disable Windows Toast Notifications (command_prompt; windows)]]
- [[kb/atomic/tests/01b20ca8_c7a3_4d86_af59_059f15ed5474-disable_windows_os_auto_update|Disable Windows OS Auto Update (command_prompt; windows)]]
- [[kb/atomic/tests/02d8b9f7_1a51_4011_8901_2d55cca667f9-modify_usetpmkeypin_registry_entry|Modify UseTPMKeyPIN Registry entry (command_prompt; windows)]]
- [[kb/atomic/tests/09147b61_40f6_4b2a_b6fb_9e73a3437c96-disabling_showui_settings_of_windows_error_reporting_wer|Disabling ShowUI Settings of Windows Error Reporting (WER) (command_prompt; windows)]]
- [[kb/atomic/tests/0b79c06f_c788_44a2_8630_d69051f1123d-blackbyte_ransomware_registry_changes_powershell|BlackByte Ransomware Registry Changes - Powershell (powershell; windows)]]
- [[kb/atomic/tests/10b33fb0_c58b_44cd_8599_b6da5ad6384c-modify_usetpmpin_registry_entry|Modify UseTPMPIN Registry entry (command_prompt; windows)]]
- [[kb/atomic/tests/12e03af7_79f9_4f95_af48_d3f12f28a260-disable_win_defender_notification|Disable Win Defender Notification (command_prompt; windows)]]
- [[kb/atomic/tests/12f50e15_dbc6_478b_a801_a746e8ba1723-activate_windows_noclose_group_policy_feature|Activate Windows NoClose Group Policy Feature (command_prompt; windows)]]
- [[kb/atomic/tests/1324796b_d0f6_455a_b4ae_21ffee6aa6b9-modify_registry_of_current_user_profile_cmd|Modify Registry of Current User Profile - cmd (command_prompt; windows)]]
- [[kb/atomic/tests/15f44ea9_4571_4837_be9e_802431a7bfae-javascript_in_registry|Javascript in registry (powershell; windows)]]
- 80 more in the generated source index

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]
- [[TA0003-persistence|TA0003: Persistence]]

## D3FEND

- [[D3-DI-data_inventory|D3-DI: Data Inventory]]
- [[D3-RD-restore_database|D3-RD: Restore Database]]
- [[D3-SCP-system_configuration_permissions|D3-SCP: System Configuration Permissions]]

## Mitigations

- [[M1024-restrict_registry_permissions|M1024: Restrict Registry Permissions]]

## Tools
- [[aadinternals|AADInternals (S0677)]]
- [[crackmapexec|CrackMapExec (S0488)]]
- [[cspy_downloader|CSPY Downloader (S0527)]]
- [[nppspy|NPPSPY (S1131)]]
- [[pcshare|PcShare (S1050)]]
- [[quasarrat|QuasarRAT (S0262)]]
- [[reg|Reg (S0075)]]
- [[remcos|Remcos (S0332)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]


## Platforms

- Windows

