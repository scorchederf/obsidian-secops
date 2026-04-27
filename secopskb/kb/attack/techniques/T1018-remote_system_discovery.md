---
mitre_id: "T1018"
mitre_name: "Remote System Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--e358d692-23c0-4a31-9eb6-ecc13a8d7735"
mitre_created: "2017-05-31T21:30:28.187Z"
mitre_modified: "2025-10-24T17:49:31.319Z"
mitre_version: "3.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1018/"
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
  - "Network Devices"
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
d3fend_ids:
  - "D3-APCA"
  - "D3-CF"
  - "D3-CM"
  - "D3-CQ"
  - "D3-CSPP"
  - "D3-DF"
  - "D3-EAL"
  - "D3-EDL"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-HBPI"
  - "D3-LFP"
  - "D3-NTCD"
  - "D3-NTF"
  - "D3-NTSA"
  - "D3-PHDURA"
  - "D3-PMAD"
  - "D3-PSA"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-RTSD"
  - "D3-SCA"
  - "D3-SCF"
  - "D3-SFA"
  - "D3-UGLPA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may attempt to get a listing of other systems by IP address, hostname, or other logical identifier on a network that may be used for Lateral Movement from the current system. Functionality could exist within remote access tools to enable this, but utilities available on the operating system could also be used such as  [[ping|Ping (S0097)]], `net view` using [[net|Net (S0039)]], or, on ESXi servers, `esxcli network diag ping`.

Adversaries may also analyze data from local host files (ex: `C:\Windows\System32\Drivers\etc\hosts` or `/etc/hosts`) or other passive means (such as local [[arp|Arp (S0099)]] cache entries) in order to discover the presence of remote systems in an environment.

Adversaries may also target discovery of network infrastructure as well as leverage [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] commands on network devices to gather detailed information about systems within a network (e.g. `show cdp neighbors`, `show arp`).(Citation: US-CERT-TA18-106A)(Citation: CISA AR21-126A FIVEHANDS May 2021)  


## Workspace

- [[workspaces/attack/techniques/T1018-remote_system_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1018-remote_system_discovery-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]

### Sigma Rules

- [[kb/sigma/rules/4ebc877f_4612_45cb_b3a5_8e3834db36c9-webshell_hacking_activity_patterns|Webshell Hacking Activity Patterns (high; windows / process_creation)]]
- [[kb/sigma/rules/7638e5fe_600c_4289_a968_f49dd537ec7d-hacktool_netexec_execution|HackTool - NetExec Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/9a132afa_654e_11eb_ae93_0242ac130002-pua_adfind_suspicious_execution|PUA - AdFind Suspicious Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/bed2a484_9348_4143_8a8a_b801c979301c-webshell_detection_with_command_line_keywords|Webshell Detection With Command Line Keywords (high; windows / process_creation)]]
- [[kb/sigma/rules/df55196f_f105_44d3_a675_e9dfb6cc2f2b-renamed_adfind_execution|Renamed AdFind Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/fa3c117a_bc0d_416e_a31b_0c0e80653efb-chopper_webshell_process_pattern|Chopper Webshell Process Pattern (high; windows / process_creation)]]

### Atomic Tests

- [[kb/atomic/tests/158bd4dd_6359_40ab_b13c_285b9ef6fa25-remote_system_discovery_ip_neighbour|Remote System Discovery - ip neighbour (sh; linux)]]
- [[kb/atomic/tests/1a4ebe70_31d0_417b_ade2_ef4cb3e7d0e1-remote_system_discovery_ip_route|Remote System Discovery - ip route (sh; linux)]]
- [[kb/atomic/tests/2d5a61f5_0447_4be4_944a_1f8530ed6574-remote_system_discovery_arp|Remote System Discovery - arp (command_prompt; windows)]]
- [[kb/atomic/tests/52ab5108_3f6f_42fb_8ba3_73bc054f22c8-remote_system_discovery_nltest|Remote System Discovery - nltest (command_prompt; windows)]]
- [[kb/atomic/tests/5838c31e_a0e2_4b9f_b60a_d79d2cb7995e-adfind_enumerate_active_directory_domain_controller_objects|Adfind - Enumerate Active Directory Domain Controller Objects (command_prompt; windows)]]
- [[kb/atomic/tests/5843529a_5056_4bc1_9c13_a311e2af4ca0-remote_system_discovery_net_group_domain_controller|Remote System Discovery - net group Domain Controller (command_prompt; windows)]]
- [[kb/atomic/tests/64ede6ac_b57a_41c2_a7d1_32c6cd35397d-enumerate_active_directory_computers_with_adsisearcher|Enumerate Active Directory Computers with ADSISearcher (powershell; windows)]]
- [[kb/atomic/tests/6c2da894_0b57_43cb_87af_46ea3b501388-remote_system_discovery_ip_tcp_metrics|Remote System Discovery - ip tcp_metrics (sh; linux)]]
- [[kb/atomic/tests/6db1f57f_d1d5_4223_8a66_55c9c65a9592-remote_system_discovery_ping_sweep|Remote System Discovery - ping sweep (command_prompt; windows)]]
- [[kb/atomic/tests/85321a9c_897f_4a60_9f20_29788e50bccd-remote_system_discovery_net|Remote System Discovery - net (command_prompt; windows)]]
- 12 more in the generated source index

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## D3FEND

- [[D3-APCA-application_protocol_command_analysis|D3-APCA: Application Protocol Command Analysis]]
- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-CSPP-client-server_payload_profiling|D3-CSPP: Client-server Payload Profiling]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-EAL-executable_allowlisting|D3-EAL: Executable Allowlisting]]
- [[D3-EDL-executable_denylisting|D3-EDL: Executable Denylisting]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-HBPI-hardware-based_process_isolation|D3-HBPI: Hardware-based Process Isolation]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-NTCD-network_traffic_community_deviation|D3-NTCD: Network Traffic Community Deviation]]
- [[D3-NTF-network_traffic_filtering|D3-NTF: Network Traffic Filtering]]
- [[D3-NTSA-network_traffic_signature_analysis|D3-NTSA: Network Traffic Signature Analysis]]
- [[D3-PHDURA-per_host_download-upload_ratio_analysis|D3-PHDURA: Per Host Download-Upload Ratio Analysis]]
- [[D3-PMAD-protocol_metadata_anomaly_detection|D3-PMAD: Protocol Metadata Anomaly Detection]]
- [[D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-RTSD-remote_terminal_session_detection|D3-RTSD: Remote Terminal Session Detection]]
- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]
- [[D3-SFA-system_file_analysis|D3-SFA: System File Analysis]]
- [[D3-UGLPA-user_geolocation_logon_pattern_analysis|D3-UGLPA: User Geolocation Logon Pattern Analysis]]

## Tools
- [[adfind|AdFind (S0552)]]
- [[arp|Arp (S0099)]]
- [[bloodhound|BloodHound (S0521)]]
- [[crackmapexec|CrackMapExec (S0488)]]
- [[nbtscan|NBTscan (S0590)]]
- [[net|Net (S0039)]]
- [[nltest|Nltest (S0359)]]
- [[ping|Ping (S0097)]]
- [[roadtools|ROADTools (S0684)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]


## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

