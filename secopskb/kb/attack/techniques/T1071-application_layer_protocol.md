---
mitre_id: "T1071"
mitre_name: "Application Layer Protocol"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--355be19c-ffc9-46d5-8d50-d6a036c675b6"
mitre_created: "2017-05-31T21:30:56.776Z"
mitre_modified: "2025-10-24T17:48:38.368Z"
mitre_version: "2.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1071/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
  - "Network Devices"
  - "ESXi"
mitre_tactic_ids:
  - "TA0011"
d3fend_ids:
  - "D3-APCA"
  - "D3-CA"
  - "D3-CF"
  - "D3-CM"
  - "D3-CQ"
  - "D3-CSPP"
  - "D3-DF"
  - "D3-DNSAL"
  - "D3-DNSDL"
  - "D3-DNSTA"
  - "D3-FA"
  - "D3-FC"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-FRDDL"
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
  - "D3-RRID"
  - "D3-RTSD"
  - "D3-UGLPA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may communicate using OSI application layer protocols to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server. 

Adversaries may utilize many different protocols, including those used for web browsing, transferring files, electronic mail, DNS, or publishing/subscribing. For connections that occur internally within an enclave (such as those between a proxy or pivot node and other nodes), commonly used protocols are SMB, SSH, or RDP.(Citation: Mandiant APT29 Eye Spy Email Nov 22) 

## Workspace

- [[workspaces/attack/techniques/T1071-application_layer_protocol-note|Open workspace note]]

![[workspaces/attack/techniques/T1071-application_layer_protocol-note]]

## Tactics

- [[TA0011-command_and_control|TA0011: Command and Control]]

## D3FEND

- [[D3-APCA-application_protocol_command_analysis|D3-APCA: Application Protocol Command Analysis]]
- [[D3-CA-certificate_analysis|D3-CA: Certificate Analysis]]
- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-CSPP-client-server_payload_profiling|D3-CSPP: Client-server Payload Profiling]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-DNSAL-dns_allowlisting|D3-DNSAL: DNS Allowlisting]]
- [[D3-DNSDL-dns_denylisting|D3-DNSDL: DNS Denylisting]]
- [[D3-DNSTA-dns_traffic_analysis|D3-DNSTA: DNS Traffic Analysis]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FC-file_carving|D3-FC: File Carving]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-FRDDL-forward_resolution_domain_denylisting|D3-FRDDL: Forward Resolution Domain Denylisting]]
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
- [[D3-RRID-reverse_resolution_ip_denylisting|D3-RRID: Reverse Resolution IP Denylisting]]
- [[D3-RTSD-remote_terminal_session_detection|D3-RTSD: Remote Terminal Session Detection]]
- [[D3-UGLPA-user_geolocation_logon_pattern_analysis|D3-UGLPA: User Geolocation Logon Pattern Analysis]]

## Subtechniques

### T1071.001: Web Protocols

^t1071001-web-protocols

Adversaries may communicate using application layer protocols associated with web traffic to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server. 

Protocols such as HTTP/S(Citation: CrowdStrike Putter Panda) and WebSocket(Citation: Brazking-Websockets) that carry web traffic may be very common in environments. HTTP/S packets have many fields and headers in which data can be concealed. An adversary may abuse these protocols to communicate with systems under their control within a victim network while also mimicking normal, expected traffic. 

### T1071.002: File Transfer Protocols

^t1071002-file-transfer-protocols

Adversaries may communicate using application layer protocols associated with transferring files to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server. 

Protocols such as SMB(Citation: US-CERT TA18-074A), FTP(Citation: ESET Machete July 2019), FTPS, and TFTP that transfer files may be very common in environments.  Packets produced from these protocols may have many fields and headers in which data can be concealed. Data could also be concealed within the transferred files. An adversary may abuse these protocols to communicate with systems under their control within a victim network while also mimicking normal, expected traffic. 

### T1071.003: Mail Protocols

^t1071003-mail-protocols

Adversaries may communicate using application layer protocols associated with electronic mail delivery to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server. 

Protocols such as SMTP/S, POP3/S, and IMAP that carry electronic mail may be very common in environments.  Packets produced from these protocols may have many fields and headers in which data can be concealed. Data could also be concealed within the email messages themselves. An adversary may abuse these protocols to communicate with systems under their control within a victim network while also mimicking normal, expected traffic.(Citation: FireEye APT28) 

### T1071.004: DNS

^t1071004-dns

Adversaries may communicate using the Domain Name System (DNS) application layer protocol to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server. 

The DNS protocol serves an administrative function in computer networking and thus may be very common in environments. DNS traffic may also be allowed even before network authentication is completed. DNS packets contain many fields and headers in which data can be concealed. Often known as DNS tunneling, adversaries may abuse DNS to communicate with systems under their control within a victim network while also mimicking normal, expected traffic.(Citation: PAN DNS Tunneling)(Citation: Medium DnsTunneling)

DNS beaconing may be used to send commands to remote systems via DNS queries. A DNS beacon is created by tunneling DNS traffic (i.e. [[T1572-protocol_tunneling|T1572: Protocol Tunneling]]). The commands may be embedded into different DNS records, for example, TXT or A records.(Citation: OilRig Uses Updated BONDUPDATER to Target Middle Eastern Government) DNS beacons may be difficult to detect because the beacons infrequently communicate with infected devices.(Citation: DNS Beacons) Infrequent communication conceals the malicious DNS traffic with normal DNS traffic. 

### T1071.005: Publish/Subscribe Protocols

^t1071005-publish-subscribe-protocols

Adversaries may communicate using publish/subscribe (pub/sub) application layer protocols to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server. 

Protocols such as `MQTT`, `XMPP`, `AMQP`, and `STOMP` use a publish/subscribe design, with message distribution managed by a centralized broker.(Citation: wailing crab sub/pub)(Citation: Mandiant APT1 Appendix) Publishers categorize their messages by topics, while subscribers receive messages according to their subscribed topics.(Citation: wailing crab sub/pub) An adversary may abuse publish/subscribe protocols to communicate with systems under their control from behind a message broker while also mimicking normal, expected traffic.

## Mitigations

- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]

## Tools

- [[sliver|Sliver (S0633)]]

## Platforms

- Linux
- macOS
- Windows
- Network Devices
- ESXi

