---
mitre_id: "T1135"
mitre_name: "Network Share Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--3489cfc5-640f-4bb3-a103-9137b97de79f"
mitre_created: "2017-12-14T16:46:06.044Z"
mitre_modified: "2025-10-24T17:48:37.475Z"
mitre_version: "3.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1135/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may look for folders and drives shared on remote systems as a means of identifying sources of information to gather as a precursor for Collection and to identify potential systems of interest for Lateral Movement. Networks often contain shared network drives and folders that enable users to access file directories on various systems across a network. 

File sharing over a Windows network occurs over the SMB protocol. (Citation: Wikipedia Shared Resource) (Citation: TechNet Shared Folder) [[net|Net (S0039)]] can be used to query a remote system for available shared drives using the `net view \\\\remotesystem` command. It can also be used to query shared drives on the local system using `net share`. For macOS, the `sharing -l` command lists all shared points used for smb services.

## Workspace

- [[workspaces/attack/techniques/T1135-network_share_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1135-network_share_discovery-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/b2317cfa_4a47_4ead_b3ff_297438c0bc2d-hacktool_sharpview_execution|HackTool - SharpView Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/c3d76afc_93df_461e_8e67_9b2bad3f2ac4-file_explorer_folder_opened_using_explorer_folder_shortcut_via_shell|File Explorer Folder Opened Using Explorer Folder Shortcut Via Shell (high; windows / process_creation)]]

### Atomic Tests

- [[kb/atomic/tests/13daa2cf_195a_43df_a8bd_7dd5ffb607b5-network_share_discovery_via_dir_command|Network Share Discovery via dir command (command_prompt; windows)]]
- [[kb/atomic/tests/1b0814d1_bb24_402d_9615_1b20c50733fb-network_share_discovery_powershell|Network Share Discovery PowerShell (powershell; windows)]]
- [[kb/atomic/tests/20f1097d_81c1_405c_8380_32174d493bbb-network_share_discovery_command_prompt|Network Share Discovery command prompt (command_prompt; windows)]]
- [[kb/atomic/tests/77e468a6_3e5c_45a1_9948_c4b5603747cb-network_share_discovery_freebsd|Network Share Discovery - FreeBSD (sh; linux)]]
- [[kb/atomic/tests/875805bc_9e86_4e87_be86_3a5527315cae-network_share_discovery_linux|Network Share Discovery - linux (bash; linux)]]
- [[kb/atomic/tests/987901d1_5b87_4558_a6d9_cffcabc638b8-winpwn_shareenumeration|WinPwn - shareenumeration (powershell; windows)]]
- [[kb/atomic/tests/ab39a04f_0c93_4540_9ff2_83f862c385ae-view_available_share_drives|View available share drives (command_prompt; windows)]]
- [[kb/atomic/tests/b1636f0a_ba82_435c_b699_0d78794d8bfd-share_discovery_with_powerview|Share Discovery with PowerView (powershell; windows)]]
- [[kb/atomic/tests/b19d74b7_5e72_450a_8499_82e49e379d1a-enumerate_all_network_shares_with_snaffler|Enumerate All Network Shares with Snaffler (powershell; windows)]]
- [[kb/atomic/tests/d07e4cc1_98ae_447e_9d31_36cb430d28c4-powerview_sharefinder|PowerView ShareFinder (powershell; windows)]]
- 2 more in the generated source index

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Mitigations

- [[M1028-operating_system_configuration|M1028: Operating System Configuration]]

## Tools
- [[crackmapexec|CrackMapExec (S0488)]]
- [[empire|Empire (S0363)]]
- [[koadic|Koadic (S0250)]]
- [[net|Net (S0039)]]
- [[pupy|Pupy (S0192)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]


## Platforms

- Linux
- macOS
- Windows

