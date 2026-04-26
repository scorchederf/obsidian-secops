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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may tunnel network communications to and from a victim system within a separate protocol to avoid detection/network filtering and/or enable access to otherwise unreachable systems. Tunneling involves explicitly encapsulating a protocol within another. This behavior may conceal malicious traffic by blending in with existing traffic and/or provide an outer layer of encryption (similar to a VPN). Tunneling could also enable routing of network packets that would otherwise not reach their intended destination, such as SMB, RDP, or other traffic that would be filtered by network appliances or not routed over the Internet. 

There are various means to encapsulate a protocol within another protocol. For example, adversaries may perform SSH tunneling (also known as SSH port forwarding), which involves forwarding arbitrary data over an encrypted SSH tunnel.(Citation: SSH Tunneling)(Citation: Sygnia Abyss Locker 2025) 

[[T1572-protocol_tunneling|T1572: Protocol Tunneling]] may also be abused by adversaries during [[T1568-dynamic_resolution|T1568: Dynamic Resolution]]. Known as DNS over HTTPS (DoH), queries to resolve C2 infrastructure may be encapsulated within encrypted HTTPS packets.(Citation: BleepingComp Godlua JUL19) 

Adversaries may also leverage [[T1572-protocol_tunneling|T1572: Protocol Tunneling]] in conjunction with [[T1090-proxy|T1090: Proxy]] and/or [[T1001-data_obfuscation#^t1001003-protocol-or-service-impersonation|T1001.003: Protocol or Service Impersonation]] to further conceal C2 communications and infrastructure. 

## Workspace

- [[workspaces/attack/techniques/T1572-protocol_tunneling-note|Open workspace note]]

![[workspaces/attack/techniques/T1572-protocol_tunneling-note]]

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

