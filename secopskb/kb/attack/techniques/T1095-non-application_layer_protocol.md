---
mitre_id: "T1095"
mitre_name: "Non-Application Layer Protocol"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--c21d5a77-d422-4a69-acd7-2c53c1faa34b"
mitre_created: "2017-05-31T21:31:10.728Z"
mitre_modified: "2025-10-24T17:49:20.136Z"
mitre_version: "2.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1095/"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may use an OSI non-application layer protocol for communication between host and C2 server or among infected hosts within a network. The list of possible protocols is extensive.(Citation: Wikipedia OSI) Specific examples include use of network layer protocols, such as the Internet Control Message Protocol (ICMP), transport layer protocols, such as the User Datagram Protocol (UDP), session layer protocols, such as Socket Secure (SOCKS), as well as redirected/tunneled protocols, such as Serial over LAN (SOL).

ICMP communication between hosts is one example.(Citation: Cisco Synful Knock Evolution) Because ICMP is part of the Internet Protocol Suite, it is required to be implemented by all IP-compatible hosts.(Citation: Microsoft ICMP) However, it is not as commonly monitored as other Internet Protocols such as TCP or UDP and may be used by adversaries to hide communications.

In ESXi environments, adversaries may leverage the Virtual Machine Communication Interface (VMCI) for communication between guest virtual machines and the ESXi host. This traffic is similar to client-server communications on traditional network sockets but is localized to the physical machine running the ESXi host, meaning it does not traverse external networks (routers, switches). This results in communications that are invisible to external monitoring and standard networking tools like tcpdump, netstat, nmap, and Wireshark. By adding a VMCI backdoor to a compromised ESXi host, adversaries may persistently regain access from any guest VM to the compromised ESXi host’s backdoor, regardless of network segmentation or firewall rules in place.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023)

## Workspace

- [[workspaces/attack/techniques/T1095-non-application_layer_protocol-note|Open workspace note]]

![[workspaces/attack/techniques/T1095-non-application_layer_protocol-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/e31033fc_33f0_4020_9a16_faf9b31cbf08-pua_netcat_suspicious_execution|PUA - Netcat Suspicious Execution (high; windows / process_creation)]]

### Atomic Tests

- [[kb/atomic/tests/0268e63c_e244_42db_bef7_72a9e59fc1fc-icmp_c2|ICMP C2 (powershell; windows)]]
- [[kb/atomic/tests/3e0e0e7f_6aa2_4a61_b61d_526c2cc9330e-powercat_c2|Powercat C2 (powershell; windows)]]
- [[kb/atomic/tests/8e139e1f_1f3a_4be7_901d_afae9738c064-linux_icmp_reverse_shell_using_icmp_cnc|Linux ICMP Reverse Shell using icmp-cnc (manual; linux)]]
- [[kb/atomic/tests/bcf0d1c1_3f6a_4847_b1c9_7ed4ea321f37-netcat_c2|Netcat C2 (powershell; windows)]]

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

- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]
- [[M1047-audit|M1047: Audit]]

## Tools
- [[brute_ratel_c4|Brute Ratel C4 (S1063)]]
- [[frp|FRP (S1144)]]
- [[mythic|Mythic (S0699)]]
- [[quasarrat|QuasarRAT (S0262)]]


## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

