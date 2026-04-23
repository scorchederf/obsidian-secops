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
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0005"
---

# T1222: File and Directory Permissions Modification

Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access protected files.(Citation: Hybrid Analysis Icacls1 June 2018)(Citation: Hybrid Analysis Icacls2 May 2018) File and directory permissions are commonly managed by ACLs configured by the file or directory owner, or users with the appropriate permissions. File and directory ACL implementations vary by platform, but generally explicitly designate which users or groups can perform which actions (read, write, execute, etc.).

Modifications may include changing specific access rights, which may require taking ownership of a file or directory and/or elevated permissions depending on the file or directory’s existing permissions. This may enable malicious activity such as modifying, replacing, or deleting specific files or directories. Specific file and directory modifications may be a required step for many techniques, such as establishing Persistence via [[T1546-event_triggered_execution#^t1546008-accessibility-features|T1546.008: Accessibility Features]], [[T1037-boot_or_logon_initialization_scripts|T1037: Boot or Logon Initialization Scripts]], [[T1546-event_triggered_execution#^t1546004-unix-shell-configuration-modification|T1546.004: Unix Shell Configuration Modification]], or tainting/hijacking other instrumental binary/configuration files via [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]].

Adversaries may also change permissions of symbolic links. For example, malware (particularly ransomware) may modify symbolic links and associated settings to enable access to files from local shortcuts with remote paths.(Citation: new_rust_based_ransomware)(Citation: bad_luck_blackcat)(Citation: falconoverwatch_blackcat_attack)(Citation: blackmatter_blackcat)(Citation: fsutil_behavior) 

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

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

