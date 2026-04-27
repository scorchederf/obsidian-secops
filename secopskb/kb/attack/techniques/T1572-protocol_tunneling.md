---
mitre_id: "T1572"
mitre_name: "Protocol Tunneling"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--4fe28b27-b13c-453e-a386-c2ef362a573b"
mitre_created: "2020-03-15T16:03:39.082Z"
mitre_modified: "2025-10-24T17:48:45.888Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1572/"
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
  - "TA0011"
d3fend_ids:
  - "D3-APCA"
  - "D3-CSPP"
  - "D3-NTCD"
  - "D3-NTF"
  - "D3-NTSA"
  - "D3-OTF"
  - "D3-PHDURA"
  - "D3-PMAD"
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

Adversaries may tunnel network communications to and from a victim system within a separate protocol to avoid detection/network filtering and/or enable access to otherwise unreachable systems. Tunneling involves explicitly encapsulating a protocol within another. This behavior may conceal malicious traffic by blending in with existing traffic and/or provide an outer layer of encryption (similar to a VPN). Tunneling could also enable routing of network packets that would otherwise not reach their intended destination, such as SMB, RDP, or other traffic that would be filtered by network appliances or not routed over the Internet. 

There are various means to encapsulate a protocol within another protocol. For example, adversaries may perform SSH tunneling (also known as SSH port forwarding), which involves forwarding arbitrary data over an encrypted SSH tunnel.(Citation: SSH Tunneling)(Citation: Sygnia Abyss Locker 2025) 

[[T1572-protocol_tunneling|T1572: Protocol Tunneling]] may also be abused by adversaries during [[T1568-dynamic_resolution|T1568: Dynamic Resolution]]. Known as DNS over HTTPS (DoH), queries to resolve C2 infrastructure may be encapsulated within encrypted HTTPS packets.(Citation: BleepingComp Godlua JUL19) 

Adversaries may also leverage [[T1572-protocol_tunneling|T1572: Protocol Tunneling]] in conjunction with [[T1090-proxy|T1090: Proxy]] and/or [[T1001-data_obfuscation#^t1001003-protocol-or-service-impersonation|T1001.003: Protocol or Service Impersonation]] to further conceal C2 communications and infrastructure. 

## Workspace

- [[workspaces/attack/techniques/T1572-protocol_tunneling-note|Open workspace note]]

![[workspaces/attack/techniques/T1572-protocol_tunneling-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/18249279_932f_45e2_b37a_8925f2597670-process_initiated_network_connection_to_ngrok_domain|Process Initiated Network Connection To Ngrok Domain (high; windows / network_connection)]]
- [[kb/sigma/rules/19bf6fdb_7721_4f3d_867f_53467f6a5db6-communication_to_ngrok_tunneling_service_linux|Communication To Ngrok Tunneling Service - Linux (high; linux / network_connection)]]
- [[kb/sigma/rules/1d08ac94_400d_4469_a82f_daee9a908849-communication_to_ngrok_tunneling_service_initiated|Communication To Ngrok Tunneling Service Initiated (high; windows / network_connection)]]
- [[kb/sigma/rules/3ab65069_d82a_4d44_a759_466661a082d1-communication_to_localtonet_tunneling_service_initiated|Communication To LocaltoNet Tunneling Service Initiated (high; windows / network_connection)]]
- [[kb/sigma/rules/3ceb2083_a27f_449a_be33_14ec1b7cc973-silence_eda_detection|Silence.EDA Detection (critical; windows / ps_script)]]
- [[kb/sigma/rules/48a61b29_389f_4032_b317_b30de6b95314-suspicious_plink_port_forwarding|Suspicious Plink Port Forwarding (high; windows / process_creation)]]
- [[kb/sigma/rules/5f699bc5_5446_4a4a_a0b7_5ef2885a3eb4-rdp_over_reverse_ssh_tunnel|RDP Over Reverse SSH Tunnel (high; windows / network_connection)]]
- [[kb/sigma/rules/b1e5da3b_ca8e_4adf_915c_9921f3d85481-rdp_to_http_or_https_target_ports|RDP to HTTP or HTTPS Target Ports (high; windows / network_connection)]]
- [[kb/sigma/rules/c4568f5d_131f_4e78_83d4_45b2da0ec4f1-communication_to_localtonet_tunneling_service_initiated_linux|Communication To LocaltoNet Tunneling Service Initiated - Linux (high; linux / network_connection)]]
- [[kb/sigma/rules/ee37eb7c_a4e7_4cd5_8fa4_efa27f1c3f31-pua_ngrok_execution|PUA - Ngrok Execution (high; windows / process_creation)]]
- 3 more in the generated source index

### Atomic Tests

- [[kb/atomic/tests/0c5f9705_c575_42a6_9609_cbbff4b2fc9b-dns_over_https_regular_beaconing|DNS over HTTPS Regular Beaconing (powershell; windows)]]
- [[kb/atomic/tests/228c336a_2f79_4043_8aef_bfa453a611d5-cloudflare_tunnels_linux_macos|Cloudflare tunnels (Linux/macOS) (sh; linux, macos)]]
- [[kb/atomic/tests/4cdc9fc7_53fb_4894_9f0c_64836943ea60-run_ngrok|run ngrok (powershell; windows)]]
- [[kb/atomic/tests/748a73d5_cea4_4f34_84d8_839da5baa99c-dns_over_https_long_domain_query|DNS over HTTPS Long Domain Query (powershell; windows)]]
- [[kb/atomic/tests/9f94a112_1ce2_464d_a63b_83c1f465f801-microsoft_dev_tunnels_linux_macos|Microsoft Dev tunnels (Linux/macOS) (bash; linux, macos)]]
- [[kb/atomic/tests/ae9ef4b0_d8c1_49d4_8758_06206f19af0a-dns_over_https_large_query_volume|DNS over HTTPS Large Query Volume (powershell; windows)]]
- [[kb/atomic/tests/b877943f_0377_44f4_8477_f79db7f07c4d-vscode_tunnels_linux_macos|VSCode tunnels (Linux/macOS) (sh; linux, macos)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0011-command_and_control|TA0011: Command and Control]]

## D3FEND

- [[D3-APCA-application_protocol_command_analysis|D3-APCA: Application Protocol Command Analysis]]
- [[D3-CSPP-client-server_payload_profiling|D3-CSPP: Client-server Payload Profiling]]
- [[D3-NTCD-network_traffic_community_deviation|D3-NTCD: Network Traffic Community Deviation]]
- [[D3-NTF-network_traffic_filtering|D3-NTF: Network Traffic Filtering]]
- [[D3-NTSA-network_traffic_signature_analysis|D3-NTSA: Network Traffic Signature Analysis]]
- [[D3-OTF-outbound_traffic_filtering|D3-OTF: Outbound Traffic Filtering]]
- [[D3-PHDURA-per_host_download-upload_ratio_analysis|D3-PHDURA: Per Host Download-Upload Ratio Analysis]]
- [[D3-PMAD-protocol_metadata_anomaly_detection|D3-PMAD: Protocol Metadata Anomaly Detection]]
- [[D3-RPA-relay_pattern_analysis|D3-RPA: Relay Pattern Analysis]]
- [[D3-RTSD-remote_terminal_session_detection|D3-RTSD: Remote Terminal Session Detection]]
- [[D3-UGLPA-user_geolocation_logon_pattern_analysis|D3-UGLPA: User Geolocation Logon Pattern Analysis]]

## Mitigations

- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]

## Tools
- [[brute_ratel_c4|Brute Ratel C4 (S1063)]]
- [[frp|FRP (S1144)]]
- [[mythic|Mythic (S0699)]]
- [[ngrok|ngrok (S0508)]]


## Platforms

- ESXi
- Linux
- macOS
- Windows

