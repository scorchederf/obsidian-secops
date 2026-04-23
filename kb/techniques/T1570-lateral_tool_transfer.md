---
mitre_id: "T1570"
mitre_name: "Lateral Tool Transfer"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--bf90d72c-c00b-45e3-b3aa-68560560d4c5"
mitre_created: "2020-03-11T21:01:00.959Z"
mitre_modified: "2025-10-24T17:49:19.137Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1570/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0008"
---

# T1570: Lateral Tool Transfer

Adversaries may transfer tools or other files between systems in a compromised environment. Once brought into the victim environment (i.e., [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]) files may then be copied from one system to another to stage adversary tools or other files over the course of an operation.

Adversaries may copy files between internal victim systems to support lateral movement using inherent file sharing protocols such as file sharing over [[T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]] to connected network shares or with authenticated connections via [[T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]].(Citation: Unit42 LockerGoga 2019)

Files can also be transferred using native or otherwise present tools on the victim system, such as scp, rsync, curl, sftp, and [[ftp|ftp]]. In some cases, adversaries may be able to leverage [[T1102-web_service|T1102: Web Service]]s such as Dropbox or OneDrive to copy files from one machine to another via shared, automatically synced folders.(Citation: Dropbox Malware Sync)

## Tactics

- [[TA0008-lateral_movement|TA0008: Lateral Movement]]

## Mitigations

- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]

## Tools

- [[psexec|PsExec]]
- [[ftp|ftp]]
- [[cmd|cmd]]
- [[bitsadmin|BITSAdmin]]
- [[impacket|Impacket]]
- [[expand|Expand]]
- [[esentutl|esentutl]]

## Platforms

- ESXi
- Linux
- macOS
- Windows

