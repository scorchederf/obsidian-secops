---
id: T1222
name: File and Directory Permissions Modification
created: 2018-10-17 00:14:20.652000+00:00
modified: 2025-10-24 17:48:52.570000+00:00
type: attack-pattern
x_mitre_version: 2.3
x_mitre_domains: enterprise-attack
---

## Tactic

- [[defense_evasion|Defense Evasion]]

Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access protected files.(Citation: Hybrid Analysis Icacls1 June 2018)(Citation: Hybrid Analysis Icacls2 May 2018) File and directory permissions are commonly managed by ACLs configured by the file or directory owner, or users with the appropriate permissions. File and directory ACL implementations vary by platform, but generally explicitly designate which users or groups can perform which actions (read, write, execute, etc.).

Modifications may include changing specific access rights, which may require taking ownership of a file or directory and/or elevated permissions depending on the file or directory’s existing permissions. This may enable malicious activity such as modifying, replacing, or deleting specific files or directories. Specific file and directory modifications may be a required step for many techniques, such as establishing Persistence via [Accessibility Features](https://attack.mitre.org/techniques/T1546/008), [Boot or Logon Initialization Scripts](https://attack.mitre.org/techniques/T1037), [Unix Shell Configuration Modification](https://attack.mitre.org/techniques/T1546/004), or tainting/hijacking other instrumental binary/configuration files via [Hijack Execution Flow](https://attack.mitre.org/techniques/T1574).

Adversaries may also change permissions of symbolic links. For example, malware (particularly ransomware) may modify symbolic links and associated settings to enable access to files from local shortcuts with remote paths.(Citation: new_rust_based_ransomware)(Citation: bad_luck_blackcat)(Citation: falconoverwatch_blackcat_attack)(Citation: blackmatter_blackcat)(Citation: fsutil_behavior) 

## Properties

- id: T1222
- name: File and Directory Permissions Modification
- created: 2018-10-17 00:14:20.652000+00:00
- modified: 2025-10-24 17:48:52.570000+00:00
- type: attack-pattern
- x_mitre_version: 2.3
- x_mitre_domains: enterprise-attack

## Subtechniques

### T1222.001: Windows File and Directory Permissions Modification

^t1222001-windows-file-and-directory-permissions-modification

**Parent Technique**
- [[T1222-file_and_directory_permissions_modification|T1222: File and Directory Permissions Modification]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access protected files.(Citation: Hybrid Analysis Icacls1 June 2018)(Citation: Hybrid Analysis Icacls2 May 2018) File and directory permissions are commonly managed by ACLs configured by the file or directory owner, or users with the appropriate permissions. File and directory ACL implementations vary by platform, but generally explicitly designate which users or groups can perform which actions (read, write, execute, etc.).

Windows implements file and directory ACLs as Discretionary Access Control Lists (DACLs).(Citation: Microsoft DACL May 2018) Similar to a standard ACL, DACLs identifies the accounts that are allowed or denied access to a securable object. When an attempt is made to access a securable object, the system checks the access control entries in the DACL in order. If a matching entry is found, access to the object is granted. Otherwise, access is denied.(Citation: Microsoft Access Control Lists May 2018)

Adversaries can interact with the DACLs using built-in Windows commands, such as `icacls`, `cacls`, `takeown`, and `attrib`, which can grant adversaries higher permissions on specific files and folders. Further, [PowerShell](https://attack.mitre.org/techniques/T1059/001) provides cmdlets that can be used to retrieve or modify file and directory DACLs. Specific file and directory modifications may be a required step for many techniques, such as establishing Persistence via [Accessibility Features](https://attack.mitre.org/techniques/T1546/008), [Boot or Logon Initialization Scripts](https://attack.mitre.org/techniques/T1037), or tainting/hijacking other instrumental binary/configuration files via [Hijack Execution Flow](https://attack.mitre.org/techniques/T1574).

#### Properties

- id: T1222.001
- name: Windows File and Directory Permissions Modification
- created: 2020-02-04 19:17:41.767000+00:00
- modified: 2025-10-24 17:48:37.826000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1222.002: Linux and Mac File and Directory Permissions Modification

^t1222002-linux-and-mac-file-and-directory-permissions-modification

**Parent Technique**
- [[T1222-file_and_directory_permissions_modification|T1222: File and Directory Permissions Modification]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access protected files.(Citation: Hybrid Analysis Icacls1 June 2018)(Citation: Hybrid Analysis Icacls2 May 2018) File and directory permissions are commonly managed by ACLs configured by the file or directory owner, or users with the appropriate permissions. File and directory ACL implementations vary by platform, but generally explicitly designate which users or groups can perform which actions (read, write, execute, etc.).

Most Linux and Linux-based platforms provide a standard set of permission groups (user, group, and other) and a standard set of permissions (read, write, and execute) that are applied to each group. While nuances of each platform’s permissions implementation may vary, most of the platforms provide two primary commands used to manipulate file and directory ACLs: <code>chown</code> (short for change owner), and <code>chmod</code> (short for change mode).

Adversarial may use these commands to make themselves the owner of files and directories or change the mode if current permissions allow it. They could subsequently lock others out of the file. Specific file and directory modifications may be a required step for many techniques, such as establishing Persistence via [Unix Shell Configuration Modification](https://attack.mitre.org/techniques/T1546/004) or tainting/hijacking other instrumental binary/configuration files via [Hijack Execution Flow](https://attack.mitre.org/techniques/T1574).(Citation: 20 macOS Common Tools and Techniques) 

#### Properties

- id: T1222.002
- name: Linux and Mac File and Directory Permissions Modification
- created: 2020-02-04 19:24:27.774000+00:00
- modified: 2025-10-24 17:48:21.839000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1022-restrict_file_and_directory_permissions|M1022: Restrict File and Directory Permissions]]
- [[M1026-privileged_account_management|M1026: Privileged Account Management]]

## Platforms

- ESXi
- Linux
- macOS
- Windows

## Tools


