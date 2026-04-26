---
mitre_id: "T1222"
mitre_name: "File and Directory Permissions Modification"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--65917ae0-b854-4139-83fe-bf2441cf0196"
mitre_created: "2018-10-17T00:14:20.652Z"
mitre_modified: "2025-10-24T17:48:52.570Z"
mitre_version: "2.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1222/"
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
  - "Windows"
mitre_tactic_ids:
  - "TA0005"
d3fend_ids:
  - "D3-AM"
  - "D3-CI"
  - "D3-NTPM"
  - "D3-RC"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access protected files.(Citation: Hybrid Analysis Icacls1 June 2018)(Citation: Hybrid Analysis Icacls2 May 2018) File and directory permissions are commonly managed by ACLs configured by the file or directory owner, or users with the appropriate permissions. File and directory ACL implementations vary by platform, but generally explicitly designate which users or groups can perform which actions (read, write, execute, etc.).

Modifications may include changing specific access rights, which may require taking ownership of a file or directory and/or elevated permissions depending on the file or directory’s existing permissions. This may enable malicious activity such as modifying, replacing, or deleting specific files or directories. Specific file and directory modifications may be a required step for many techniques, such as establishing Persistence via [[T1546-event_triggered_execution#^t1546008-accessibility-features|T1546.008: Accessibility Features]], [[T1037-boot_or_logon_initialization_scripts|T1037: Boot or Logon Initialization Scripts]], [[T1546-event_triggered_execution#^t1546004-unix-shell-configuration-modification|T1546.004: Unix Shell Configuration Modification]], or tainting/hijacking other instrumental binary/configuration files via [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]].

Adversaries may also change permissions of symbolic links. For example, malware (particularly ransomware) may modify symbolic links and associated settings to enable access to files from local shortcuts with remote paths.(Citation: new_rust_based_ransomware)(Citation: bad_luck_blackcat)(Citation: falconoverwatch_blackcat_attack)(Citation: blackmatter_blackcat)(Citation: fsutil_behavior) 

## Workspace

- [[workspaces/attack/techniques/T1222-file_and_directory_permissions_modification-note|Open workspace note]]

![[workspaces/attack/techniques/T1222-file_and_directory_permissions_modification-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2019-07-001-access_permission_modification|CAR-2019-07-001: Access Permission Modification]]

### Sigma Rules

- [[kb/sigma/rules/028c7842_4243_41cd_be6f_12f3cf1a26c7-ad_object_writedac_access|AD Object WriteDAC Access (critical; windows / security)]]
- [[kb/sigma/rules/3bf1d859_3a7e_44cb_8809_a99e066d3478-powershell_set_acl_on_windows_folder_psscript|PowerShell Set-Acl On Windows Folder - PsScript (high; windows / ps_script)]]

### Atomic Tests

- [[kb/atomic/tests/0451125c_b5f6_488f_993b_5a32b09f7d8f-chmod_change_file_or_folder_mode_symbolic_mode_recursively|chmod - Change file or folder mode (symbolic mode) recursively (bash; linux, macos)]]
- [[kb/atomic/tests/18592ba1_5f88_4e3c_abc8_ab1c6042e389-chown_through_c_script|Chown through c script (sh; macos, linux)]]
- [[kb/atomic/tests/32b979da_7b68_42c9_9a99_0e39900fc36c-attrib_hide_file|attrib - hide file (command_prompt; windows)]]
- [[kb/atomic/tests/34ca1464_de9d_40c6_8c77_690adf36a135-chmod_change_file_or_folder_mode_numeric_mode|chmod - Change file or folder mode (numeric mode) (sh; linux, macos)]]
- [[kb/atomic/tests/3b015515_b3d8_44e9_b8cd_6fa84faf30b2-chown_change_file_or_folder_ownership_recursively|chown - Change file or folder ownership recursively (bash; macos, linux)]]
- [[kb/atomic/tests/60eee3ea_2ebd_453b_a666_c52ce08d2709-chflags_remove_immutable_file_attribute|chflags - Remove immutable file attribute (sh; linux)]]
- [[kb/atomic/tests/6c4ac96f_d4fa_44f4_83ca_56d8f4a55c02-enable_local_and_remote_symbolic_links_via_fsutil|Enable Local and Remote Symbolic Links via fsutil (command_prompt; windows)]]
- [[kb/atomic/tests/6cd715aa_20ac_4be1_a8f1_dda7bae160bd-enable_local_and_remote_symbolic_links_via_powershell|Enable Local and Remote Symbolic Links via Powershell (powershell; windows)]]
- [[kb/atomic/tests/78bef0d4_57fb_417d_a67a_b75ae02ea3ab-enable_local_and_remote_symbolic_links_via_reg_exe|Enable Local and Remote Symbolic Links via reg.exe (command_prompt; windows)]]
- [[kb/atomic/tests/967ba79d_f184_4e0e_8d09_6362b3162e99-chown_change_file_or_folder_mode_ownership_only|chown - Change file or folder mode ownership only (sh; linux, macos)]]
- 13 more in the generated source index

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## D3FEND

- [[D3-AM-access_modeling|D3-AM: Access Modeling]]
- [[D3-CI-configuration_inventory|D3-CI: Configuration Inventory]]
- [[D3-NTPM-network_traffic_policy_mapping|D3-NTPM: Network Traffic Policy Mapping]]
- [[D3-RC-restore_configuration|D3-RC: Restore Configuration]]

## Subtechniques

### T1222.001: Windows File and Directory Permissions Modification

^t1222001-windows-file-and-directory-permissions-modification

Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access protected files.(Citation: Hybrid Analysis Icacls1 June 2018)(Citation: Hybrid Analysis Icacls2 May 2018) File and directory permissions are commonly managed by ACLs configured by the file or directory owner, or users with the appropriate permissions. File and directory ACL implementations vary by platform, but generally explicitly designate which users or groups can perform which actions (read, write, execute, etc.).

Windows implements file and directory ACLs as Discretionary Access Control Lists (DACLs).(Citation: Microsoft DACL May 2018) Similar to a standard ACL, DACLs identifies the accounts that are allowed or denied access to a securable object. When an attempt is made to access a securable object, the system checks the access control entries in the DACL in order. If a matching entry is found, access to the object is granted. Otherwise, access is denied.(Citation: Microsoft Access Control Lists May 2018)

Adversaries can interact with the DACLs using built-in Windows commands, such as `icacls`, `cacls`, `takeown`, and `attrib`, which can grant adversaries higher permissions on specific files and folders. Further, [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]] provides cmdlets that can be used to retrieve or modify file and directory DACLs. Specific file and directory modifications may be a required step for many techniques, such as establishing Persistence via [[T1546-event_triggered_execution#^t1546008-accessibility-features|T1546.008: Accessibility Features]], [[T1037-boot_or_logon_initialization_scripts|T1037: Boot or Logon Initialization Scripts]], or tainting/hijacking other instrumental binary/configuration files via [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]].

### T1222.002: Linux and Mac File and Directory Permissions Modification

^t1222002-linux-and-mac-file-and-directory-permissions-modification

Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access protected files.(Citation: Hybrid Analysis Icacls1 June 2018)(Citation: Hybrid Analysis Icacls2 May 2018) File and directory permissions are commonly managed by ACLs configured by the file or directory owner, or users with the appropriate permissions. File and directory ACL implementations vary by platform, but generally explicitly designate which users or groups can perform which actions (read, write, execute, etc.).

Most Linux and Linux-based platforms provide a standard set of permission groups (user, group, and other) and a standard set of permissions (read, write, and execute) that are applied to each group. While nuances of each platform’s permissions implementation may vary, most of the platforms provide two primary commands used to manipulate file and directory ACLs: `chown` (short for change owner), and `chmod` (short for change mode).

Adversarial may use these commands to make themselves the owner of files and directories or change the mode if current permissions allow it. They could subsequently lock others out of the file. Specific file and directory modifications may be a required step for many techniques, such as establishing Persistence via [[T1546-event_triggered_execution#^t1546004-unix-shell-configuration-modification|T1546.004: Unix Shell Configuration Modification]] or tainting/hijacking other instrumental binary/configuration files via [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]].(Citation: 20 macOS Common Tools and Techniques) 

## Mitigations

- [[M1022-restrict_file_and_directory_permissions|M1022: Restrict File and Directory Permissions]]
- [[M1026-privileged_account_management|M1026: Privileged Account Management]]

## Platforms

- ESXi
- Linux
- macOS
- Windows

