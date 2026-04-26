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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may interact with the Windows Registry as part of a variety of other techniques to aid in defense evasion, persistence, and execution.

Access to specific areas of the Registry depends on account permissions, with some keys requiring administrator-level access. The built-in Windows command-line utility [[reg|Reg (S0075)]] may be used for local or remote Registry modification.(Citation: Microsoft Reg) Other tools, such as remote access tools, may also contain functionality to interact with the Registry through the Windows API.

The Registry may be modified in order to hide configuration information or malicious payloads via [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]].(Citation: Unit42 BabyShark Feb 2019)(Citation: Avaddon Ransomware 2021)(Citation: Microsoft BlackCat Jun 2022)(Citation: CISA Russian Gov Critical Infra 2018) The Registry may also be modified to [[T1562-impair_defenses|T1562: Impair Defenses]], such as by enabling macros for all Microsoft Office products, allowing privilege escalation without alerting the user, increasing the maximum number of allowed outbound requests, and/or modifying systems to store plaintext credentials in memory.(Citation: CISA LockBit 2023)(Citation: Unit42 BabyShark Feb 2019)

The Registry of a remote system may be modified to aid in execution of files as part of lateral movement. It requires the remote Registry service to be running on the target system.(Citation: Microsoft Remote) Often [[T1078-valid_accounts|T1078: Valid Accounts]] are required, along with access to the remote system's [[T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]] for RPC communication.

Finally, Registry modifications may also include actions to hide keys, such as prepending key names with a null character, which will cause an error and/or be ignored when read via [[reg|Reg (S0075)]] or other utilities using the Win32 API.(Citation: Microsoft Reghide NOV 2006) Adversaries may abuse these pseudo-hidden keys to conceal payloads/commands used to maintain persistence.(Citation: TrendMicro POWELIKS AUG 2014)(Citation: SpectorOps Hiding Reg Jul 2017)

## Workspace

- [[workspaces/attack/techniques/T1112-modify_registry-note|Open workspace note]]

![[workspaces/attack/techniques/T1112-modify_registry-note]]

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

