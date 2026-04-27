---
mitre_id: "T1102"
mitre_name: "Web Service"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--830c9528-df21-472c-8c14-a036bf17d665"
mitre_created: "2017-05-31T21:31:13.915Z"
mitre_modified: "2025-10-24T17:49:02.831Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1102/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "Linux"
  - "Windows"
  - "macOS"
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

Adversaries may use an existing, legitimate external Web service as a means for relaying data to/from a compromised system. Popular websites, cloud services, and social media acting as a mechanism for C2 may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google, Microsoft, or Twitter, makes it easier for adversaries to hide in expected noise.(Citation: Broadcom BirdyClient Microsoft Graph API 2024) Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection.

Use of Web services may also protect back-end C2 infrastructure from discovery through malware binary analysis while also enabling operational resiliency (since this infrastructure may be dynamically changed).

## Workspace

- [[workspaces/attack/techniques/T1102-web_service-note|Open workspace note]]

![[workspaces/attack/techniques/T1102-web_service-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/18249279_932f_45e2_b37a_8925f2597670-process_initiated_network_connection_to_ngrok_domain|Process Initiated Network Connection To Ngrok Domain (high; windows / network_connection)]]
- [[kb/sigma/rules/19bf6fdb_7721_4f3d_867f_53467f6a5db6-communication_to_ngrok_tunneling_service_linux|Communication To Ngrok Tunneling Service - Linux (high; linux / network_connection)]]
- [[kb/sigma/rules/1d08ac94_400d_4469_a82f_daee9a908849-communication_to_ngrok_tunneling_service_initiated|Communication To Ngrok Tunneling Service Initiated (high; windows / network_connection)]]
- [[kb/sigma/rules/297ae038_edc2_4b2e_bb3e_7c5fc94dd5c7-new_connection_initiated_to_potential_dead_drop_resolver_domain|New Connection Initiated To Potential Dead Drop Resolver Domain (high; windows / network_connection)]]
- [[kb/sigma/rules/2b1ee7e4_89b6_4739_b7bb_b811b6607e5e-pwndrp_access|PwnDrp Access (critical; proxy)]]
- [[kb/sigma/rules/3ab65069_d82a_4d44_a759_466661a082d1-communication_to_localtonet_tunneling_service_initiated|Communication To LocaltoNet Tunneling Service Initiated (high; windows / network_connection)]]
- [[kb/sigma/rules/5468045b_4fcc_4d1a_973c_c9c9578edacb-raw_paste_service_access|Raw Paste Service Access (high; proxy)]]
- [[kb/sigma/rules/c4568f5d_131f_4e78_83d4_45b2da0ec4f1-communication_to_localtonet_tunneling_service_initiated_linux|Communication To LocaltoNet Tunneling Service Initiated - Linux (high; linux / network_connection)]]
- [[kb/sigma/rules/cea2b7ea_792b_405f_95a1_b903ea06458f-suspicious_child_process_of_manage_engine_servicedesk|Suspicious Child Process Of Manage Engine ServiceDesk (high; windows / process_creation)]]

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

## Subtechniques

### T1102.001: Dead Drop Resolver

^t1102001-dead-drop-resolver

Adversaries may use an existing, legitimate external Web service to host information that points to additional command and control (C2) infrastructure. Adversaries may post content, known as a dead drop resolver, on Web services with embedded (and often obfuscated/encoded) domains or IP addresses. Once infected, victims will reach out to and be redirected by these resolvers.

Popular websites and social media acting as a mechanism for C2 may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google or Twitter, makes it easier for adversaries to hide in expected noise. Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection.

Use of a dead drop resolver may also protect back-end C2 infrastructure from discovery through malware binary analysis while also enabling operational resiliency (since this infrastructure may be dynamically changed).

### T1102.002: Bidirectional Communication

^t1102002-bidirectional-communication

Adversaries may use an existing, legitimate external Web service as a means for sending commands to and receiving output from a compromised system over the Web service channel. Compromised systems may leverage popular websites and social media to host command and control (C2) instructions. Those infected systems can then send the output from those commands back over that Web service channel. The return traffic may occur in a variety of ways, depending on the Web service being utilized. For example, the return traffic may take the form of the compromised system posting a comment on a forum, issuing a pull request to development project, updating a document hosted on a Web service, or by sending a Tweet. 

Popular websites and social media acting as a mechanism for C2 may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google or Twitter, makes it easier for adversaries to hide in expected noise. Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection. 

### T1102.003: One-Way Communication

^t1102003-one-way-communication

Adversaries may use an existing, legitimate external Web service as a means for sending commands to a compromised system without receiving return output over the Web service channel. Compromised systems may leverage popular websites and social media to host command and control (C2) instructions. Those infected systems may opt to send the output from those commands back over a different C2 channel, including to another distinct Web service. Alternatively, compromised systems may return no output at all in cases where adversaries want to send instructions to systems and do not want a response.

Popular websites and social media acting as a mechanism for C2 may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google or Twitter, makes it easier for adversaries to hide in expected noise. Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection.

## Mitigations

- [[M1021-restrict_web-based_content|M1021: Restrict Web-Based Content]]
- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]

## Tools
- [[brute_ratel_c4|Brute Ratel C4 (S1063)]]
- [[ngrok|ngrok (S0508)]]


## Platforms

- ESXi
- Linux
- Windows
- macOS

