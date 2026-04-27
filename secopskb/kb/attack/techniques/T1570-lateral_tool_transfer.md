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
  - "TA0008"
d3fend_ids:
  - "D3-APCA"
  - "D3-CAA"
  - "D3-CSPP"
  - "D3-FC"
  - "D3-NTCD"
  - "D3-NTF"
  - "D3-NTSA"
  - "D3-PHDURA"
  - "D3-PMAD"
  - "D3-RTSD"
  - "D3-UGLPA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may transfer tools or other files between systems in a compromised environment. Once brought into the victim environment (i.e., [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]) files may then be copied from one system to another to stage adversary tools or other files over the course of an operation.

Adversaries may copy files between internal victim systems to support lateral movement using inherent file sharing protocols such as file sharing over [[T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]] to connected network shares or with authenticated connections via [[T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]].(Citation: Unit42 LockerGoga 2019)

Files can also be transferred using native or otherwise present tools on the victim system, such as scp, rsync, curl, sftp, and [[ftp|ftp (S0095)]]. In some cases, adversaries may be able to leverage [[T1102-web_service|T1102: Web Service]]s such as Dropbox or OneDrive to copy files from one machine to another via shared, automatically synced folders.(Citation: Dropbox Malware Sync)

## Workspace

- [[workspaces/attack/techniques/T1570-lateral_tool_transfer-note|Open workspace note]]

![[workspaces/attack/techniques/T1570-lateral_tool_transfer-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2013-05-003-smb_write_request|CAR-2013-05-003: SMB Write Request]]
- [[kb/car/analytics/CAR-2013-05-005-smb_copy_and_execution|CAR-2013-05-005: SMB Copy and Execution]]
- [[kb/car/analytics/CAR-2014-03-001-smb_write_request_namedpipes|CAR-2014-03-001: SMB Write Request - NamedPipes]]

### Sigma Rules

- [[kb/sigma/rules/304afd73_55a5_4bb9_8c21_0b1fc84ea9e4-psexec_remote_execution_file_artefact|PSEXEC Remote Execution File Artefact (high; windows / file_event)]]
- [[kb/sigma/rules/5bb68627_3198_40ca_b458_49f973db8752-rundll32_execution_without_parameters|Rundll32 Execution Without Parameters (high; windows / process_creation)]]
- [[kb/sigma/rules/6fb63b40_e02a_403e_9ffd_3bcc1d749442-metasploit_or_impacket_service_installation_via_smb_psexec|Metasploit Or Impacket Service Installation Via SMB PsExec (high; windows / security)]]

### Atomic Tests

- [[kb/atomic/tests/183235ca_8e6c_422c_88c2_3aa28c4825d9-exfiltration_over_smb_over_quic_net_use|Exfiltration Over SMB over QUIC (NET USE) (powershell; windows)]]
- [[kb/atomic/tests/d8d13303_159e_4f33_89f4_9f07812d016f-exfiltration_over_smb_over_quic_new_smbmapping|Exfiltration Over SMB over QUIC (New-SmbMapping) (powershell; windows)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0008-lateral_movement|TA0008: Lateral Movement]]

## D3FEND

- [[D3-APCA-application_protocol_command_analysis|D3-APCA: Application Protocol Command Analysis]]
- [[D3-CAA-connection_attempt_analysis|D3-CAA: Connection Attempt Analysis]]
- [[D3-CSPP-client-server_payload_profiling|D3-CSPP: Client-server Payload Profiling]]
- [[D3-FC-file_carving|D3-FC: File Carving]]
- [[D3-NTCD-network_traffic_community_deviation|D3-NTCD: Network Traffic Community Deviation]]
- [[D3-NTF-network_traffic_filtering|D3-NTF: Network Traffic Filtering]]
- [[D3-NTSA-network_traffic_signature_analysis|D3-NTSA: Network Traffic Signature Analysis]]
- [[D3-PHDURA-per_host_download-upload_ratio_analysis|D3-PHDURA: Per Host Download-Upload Ratio Analysis]]
- [[D3-PMAD-protocol_metadata_anomaly_detection|D3-PMAD: Protocol Metadata Anomaly Detection]]
- [[D3-RTSD-remote_terminal_session_detection|D3-RTSD: Remote Terminal Session Detection]]
- [[D3-UGLPA-user_geolocation_logon_pattern_analysis|D3-UGLPA: User Geolocation Logon Pattern Analysis]]

## Mitigations

- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]

## Tools
- [[bitsadmin|BITSAdmin (S0190)]]
- [[cmd|cmd (S0106)]]
- [[esentutl|esentutl (S0404)]]
- [[expand|Expand (S0361)]]
- [[ftp|ftp (S0095)]]
- [[impacket|Impacket (S0357)]]
- [[psexec|PsExec (S0029)]]


## Platforms

- ESXi
- Linux
- macOS
- Windows

