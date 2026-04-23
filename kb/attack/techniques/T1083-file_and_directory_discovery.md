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
build_date: "2026-04-23 22:40:56"
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

# T1083: File and Directory Discovery

Adversaries may enumerate files and directories or may search in specific locations of a host or network share for certain information within a file system. Adversaries may use the information from [[T1083-file_and_directory_discovery|T1083: File and Directory Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Many command shell utilities can be used to obtain this information. Examples include `dir`, `tree`, `ls`, `find`, and `locate`.(Citation: Windows Commands JPCERT) Custom tools may also be used to gather file and directory information and interact with the [[T1106-native_api|T1106: Native API]]. Adversaries may also leverage a [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] on network devices to gather file and directory information (e.g. `dir`, `show flash`, and/or `nvram`).(Citation: US-CERT-TA18-106A)

Some files and directories may require elevated or specific user permissions to access.

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

- [[cmd|cmd]]
- [[pupy|Pupy]]
- [[forfiles|Forfiles]]
- [[koadic|Koadic]]
- [[remcos|Remcos]]
- [[empire|Empire]]
- [[poshc2|PoshC2]]
- [[imminent_monitor|Imminent Monitor]]
- [[crackmapexec|CrackMapExec]]
- [[remoteutilities|RemoteUtilities]]
- [[sliver|Sliver]]
- [[silenttrinity|SILENTTRINITY]]
- [[rclone|Rclone]]

## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

## Workspace

- [[kb/notes/attack/techniques/t1083-notes|Open workspace note]]

