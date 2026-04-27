---
mitre_id: "T1048"
mitre_name: "Exfiltration Over Alternative Protocol"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--a19e86f8-1c0a-4fea-8407-23b73d615776"
mitre_created: "2017-05-31T21:30:44.720Z"
mitre_modified: "2025-10-24T17:49:10.460Z"
mitre_version: "1.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1048/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "IaaS"
  - "Linux"
  - "macOS"
  - "Network Devices"
  - "Office Suite"
  - "SaaS"
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
  - "D3-OTF"
  - "D3-PHDURA"
  - "D3-PMAD"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-RPA"
  - "D3-RTSD"
  - "D3-UGLPA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may steal data by exfiltrating it over a different protocol than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server.  

Alternate protocols include FTP, SMTP, HTTP/S, DNS, SMB, or any other network protocol not being used as the main command and control channel. Adversaries may also opt to encrypt and/or obfuscate these alternate channels. 

[[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]] can be done using various common operating system utilities such as [[net|Net (S0039)]]/SMB or FTP.(Citation: Palo Alto OilRig Oct 2016) On macOS and Linux `curl` may be used to invoke protocols such as HTTP/S or FTP/S to exfiltrate data from a system.(Citation: 20 macOS Common Tools and Techniques)

Many IaaS and SaaS platforms (such as Microsoft Exchange, Microsoft SharePoint, GitHub, and AWS S3) support the direct download of files, emails, source code, and other sensitive information via the web console or [[T1059-command_and_scripting_interpreter#^t1059009-cloud-api|T1059.009: Cloud API]].

## Workspace

- [[workspaces/attack/techniques/T1048-exfiltration_over_alternative_protocol-note|Open workspace note]]

![[workspaces/attack/techniques/T1048-exfiltration_over_alternative_protocol-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/6ddff2e8_ea1a_45d0_8938_93dfc1d67ae7-pua_restic_backup_tool_execution|PUA - Restic Backup Tool Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/982e9f2d_1a85_4d5b_aea4_31f5e97c6555-suspicious_webdav_client_execution_via_rundll32_exe|Suspicious WebDav Client Execution Via Rundll32.EXE (high; windows / process_creation)]]
- [[kb/sigma/rules/98a96a5a_64a0_4c42_92c5_489da3866cb0-dns_exfiltration_and_tunneling_tools_execution|DNS Exfiltration and Tunneling Tools Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/ab9e3b40_0c85_4ba1_aede_455d226fd124-suspicious_redirection_to_local_admin_share|Suspicious Redirection to Local Admin Share (high; windows / process_creation)]]
- [[kb/sigma/rules/d59d7842_9a21_4bc6_ba98_64bfe0091355-powershell_dnsexfiltration|Powershell DNSExfiltration (high; windows / ps_script)]]

### Atomic Tests

- [[kb/atomic/tests/1cdf2fb0_51b6_4fd8_96af_77020d5f1bf0-exfiltrate_data_https_using_curl_windows|Exfiltrate data HTTPS using curl windows (command_prompt; windows)]]
- [[kb/atomic/tests/1d1abbd6_a3d3_4b2e_bef5_c59293f46eff-exfiltration_over_alternative_protocol_http|Exfiltration Over Alternative Protocol - HTTP (manual; macos, linux)]]
- [[kb/atomic/tests/3ea1f938_f80a_4305_9aa8_431bc4867313-python3_http_server|Python3 http.server (sh; linux)]]
- [[kb/atomic/tests/4a4f31e2_46ea_4c26_ad89_f09ad1d5fe01-exfiltrate_data_https_using_curl_freebsd_linux_or_macos|Exfiltrate data HTTPS using curl freebsd,linux or macos (bash; macos, linux)]]
- [[kb/atomic/tests/57799bc2_ad1e_4130_a793_fb0c385130ba-maze_ftp_upload|MAZE FTP Upload (powershell; windows)]]
- [[kb/atomic/tests/6aa58451_1121_4490_a8e9_1dada3f1c68c-exfiltration_over_alternative_protocol_http|Exfiltration Over Alternative Protocol - HTTP (powershell; windows)]]
- [[kb/atomic/tests/7c3cb337_35ae_4d06_bf03_3032ed2ec268-exfiltration_over_alternative_protocol_ssh|Exfiltration Over Alternative Protocol - SSH (sh; macos, linux)]]
- [[kb/atomic/tests/7ccdfcfa_6707_46bc_b812_007ab6ff951c-exfiltrate_data_in_a_file_over_https_using_wget|Exfiltrate data in a file over HTTPS using wget (sh; linux)]]
- [[kb/atomic/tests/8bec51da_7a6d_4346_b941_51eca448c4b0-exfiltrate_data_as_text_over_https_using_wget|Exfiltrate data as text over HTTPS using wget (sh; linux)]]
- [[kb/atomic/tests/a27916da_05f2_4316_a3ee_feec67a437be-exfiltrate_data_using_dns_queries_via_dig|Exfiltrate Data using DNS Queries via dig (bash; macos, linux)]]
- 6 more in the generated source index

### LOLBAS Entries

- [[kb/lolbas/entries/osbinaries-cmd_exe|Cmd.exe (ADS, Download, Upload)]]
- [[kb/lolbas/entries/othermsbinaries-testwindowremoteagent_exe|TestWindowRemoteAgent.exe (Upload)]]

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
- [[D3-OTF-outbound_traffic_filtering|D3-OTF: Outbound Traffic Filtering]]
- [[D3-PHDURA-per_host_download-upload_ratio_analysis|D3-PHDURA: Per Host Download-Upload Ratio Analysis]]
- [[D3-PMAD-protocol_metadata_anomaly_detection|D3-PMAD: Protocol Metadata Anomaly Detection]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-RPA-relay_pattern_analysis|D3-RPA: Relay Pattern Analysis]]
- [[D3-RTSD-remote_terminal_session_detection|D3-RTSD: Remote Terminal Session Detection]]
- [[D3-UGLPA-user_geolocation_logon_pattern_analysis|D3-UGLPA: User Geolocation Logon Pattern Analysis]]

## Subtechniques

### T1048.001: Exfiltration Over Symmetric Encrypted Non-C2 Protocol

^t1048001-exfiltration-over-symmetric-encrypted-non-c2-protocol

Adversaries may steal data by exfiltrating it over a symmetrically encrypted network protocol other than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server. 

Symmetric encryption algorithms are those that use shared or the same keys/secrets on each end of the channel. This requires an exchange or pre-arranged agreement/possession of the value used to encrypt and decrypt data. 

Network protocols that use asymmetric encryption often utilize symmetric encryption once keys are exchanged, but adversaries may opt to manually share keys and implement symmetric cryptographic algorithms (ex: RC4, AES) vice using mechanisms that are baked into a protocol. This may result in multiple layers of encryption (in protocols that are natively encrypted such as HTTPS) or encryption in protocols that not typically encrypted (such as HTTP or FTP). 

### T1048.002: Exfiltration Over Asymmetric Encrypted Non-C2 Protocol

^t1048002-exfiltration-over-asymmetric-encrypted-non-c2-protocol

Adversaries may steal data by exfiltrating it over an asymmetrically encrypted network protocol other than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server. 

Asymmetric encryption algorithms are those that use different keys on each end of the channel. Also known as public-key cryptography, this requires pairs of cryptographic keys that can encrypt/decrypt data from the corresponding key. Each end of the communication channels requires a private key (only in the procession of that entity) and the public key of the other entity. The public keys of each entity are exchanged before encrypted communications begin. 

Network protocols that use asymmetric encryption (such as HTTPS/TLS/SSL) often utilize symmetric encryption once keys are exchanged. Adversaries may opt to use these encrypted mechanisms that are baked into a protocol. 

### T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol

^t1048003-exfiltration-over-unencrypted-non-c2-protocol

Adversaries may steal data by exfiltrating it over an un-encrypted network protocol other than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server.(Citation: copy_cmd_cisco)

Adversaries may opt to obfuscate this data, without the use of encryption, within network protocols that are natively unencrypted (such as HTTP, FTP, or DNS). This may include custom or publicly available encoding/compression algorithms (such as base64) as well as embedding data within protocol headers and fields. 

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1022-restrict_file_and_directory_permissions|M1022: Restrict File and Directory Permissions]]
- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]
- [[M1057-data_loss_prevention|M1057: Data Loss Prevention]]

## Tools

- [[aadinternals|AADInternals (S0677)]]

## Platforms

- ESXi
- IaaS
- Linux
- macOS
- Network Devices
- Office Suite
- SaaS
- Windows

