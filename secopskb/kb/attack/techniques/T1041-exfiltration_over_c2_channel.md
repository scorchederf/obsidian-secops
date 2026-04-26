---
mitre_id: "T1041"
mitre_name: "Exfiltration Over C2 Channel"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--92d7da27-2d91-488e-a00c-059dc162766d"
mitre_created: "2017-05-31T21:30:41.804Z"
mitre_modified: "2025-10-24T17:49:06.675Z"
mitre_version: "2.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1041/"
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
  - "TA0010"
d3fend_ids:
  - "D3-APCA"
  - "D3-CA"
  - "D3-CF"
  - "D3-CM"
  - "D3-CQ"
  - "D3-CSPP"
  - "D3-DF"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-LFP"
  - "D3-NTCD"
  - "D3-NTF"
  - "D3-NTSA"
  - "D3-PHDURA"
  - "D3-PMAD"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-RTSD"
  - "D3-UGLPA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may steal data by exfiltrating it over an existing command and control channel. Stolen data is encoded into the normal communications channel using the same protocol as command and control communications.

## Workspace

- [[workspaces/attack/techniques/T1041-exfiltration_over_c2_channel-note|Open workspace note]]

![[workspaces/attack/techniques/T1041-exfiltration_over_c2_channel-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/b4e6b016_a2ac_4759_ad85_8000b300d61e-opencanary_tftp_request|OpenCanary - TFTP Request (high; opencanary / application)]]

### Atomic Tests

- [[kb/atomic/tests/c9207f3e_213d_4cc7_ad2a_7697a7237df9-text_based_data_exfiltration_using_dns_subdomains|Text Based Data Exfiltration using DNS subdomains (powershell; windows)]]
- [[kb/atomic/tests/d1253f6e_c29b_49dc_b466_2147a6191932-c2_data_exfiltration|C2 Data Exfiltration (powershell; windows)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0010-exfiltration|TA0010: Exfiltration]]

## D3FEND

- [[D3-APCA-application_protocol_command_analysis|D3-APCA: Application Protocol Command Analysis]]
- [[D3-CA-certificate_analysis|D3-CA: Certificate Analysis]]
- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-CSPP-client-server_payload_profiling|D3-CSPP: Client-server Payload Profiling]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-NTCD-network_traffic_community_deviation|D3-NTCD: Network Traffic Community Deviation]]
- [[D3-NTF-network_traffic_filtering|D3-NTF: Network Traffic Filtering]]
- [[D3-NTSA-network_traffic_signature_analysis|D3-NTSA: Network Traffic Signature Analysis]]
- [[D3-PHDURA-per_host_download-upload_ratio_analysis|D3-PHDURA: Per Host Download-Upload Ratio Analysis]]
- [[D3-PMAD-protocol_metadata_anomaly_detection|D3-PMAD: Protocol Metadata Anomaly Detection]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-RTSD-remote_terminal_session_detection|D3-RTSD: Remote Terminal Session Detection]]
- [[D3-UGLPA-user_geolocation_logon_pattern_analysis|D3-UGLPA: User Geolocation Logon Pattern Analysis]]

## Mitigations

- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1057-data_loss_prevention|M1057: Data Loss Prevention]]

## Tools
- [[empire|Empire (S0363)]]
- [[imminent_monitor|Imminent Monitor (S0434)]]
- [[pcshare|PcShare (S1050)]]
- [[pupy|Pupy (S0192)]]
- [[shimratreporter|ShimRatReporter (S0445)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]
- [[sliver|Sliver (S0633)]]


## Platforms

- ESXi
- Linux
- macOS
- Windows

