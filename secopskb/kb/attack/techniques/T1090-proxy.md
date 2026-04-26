---
mitre_id: "T1090"
mitre_name: "Proxy"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--731f4f55-b6d0-41d1-a7a9-072a66389aea"
mitre_created: "2017-05-31T21:31:08.479Z"
mitre_modified: "2025-10-24T17:48:57.330Z"
mitre_version: "3.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1090/"
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
  - "D3-CAA"
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

Adversaries may use a connection proxy to direct network traffic between systems or act as an intermediary for network communications to a command and control server to avoid direct connections to their infrastructure. Many tools exist that enable traffic redirection through proxies or port redirection, including [[htran|HTRAN (S0040)]], ZXProxy, and ZXPortMap. (Citation: Trend Micro APT Attack Tools) Adversaries use these types of proxies to manage command and control communications, reduce the number of simultaneous outbound network connections, provide resiliency in the face of connection loss, or to ride over existing trusted communications paths between victims to avoid suspicion. Adversaries may chain together multiple proxies to further disguise the source of malicious traffic.

Adversaries can also take advantage of routing schemes in Content Delivery Networks (CDNs) to proxy command and control traffic.

## Workspace

- [[workspaces/attack/techniques/T1090-proxy-note|Open workspace note]]

![[workspaces/attack/techniques/T1090-proxy-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/19bf6fdb_7721_4f3d_867f_53467f6a5db6-communication_to_ngrok_tunneling_service_linux|Communication To Ngrok Tunneling Service - Linux (high; linux / network_connection)]]
- [[kb/sigma/rules/1d08ac94_400d_4469_a82f_daee9a908849-communication_to_ngrok_tunneling_service_initiated|Communication To Ngrok Tunneling Service Initiated (high; windows / network_connection)]]
- [[kb/sigma/rules/32410e29_5f94_4568_b6a3_d91a8adad863-pua_fast_reverse_proxy_frp_execution|PUA - Fast Reverse Proxy (FRP) Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/36440e1c_5c22_467a_889b_593e66498472-malicious_ip_address_sign_in_suspicious|Malicious IP Address Sign-In Suspicious (high; azure / riskdetection)]]
- [[kb/sigma/rules/3ab65069_d82a_4d44_a759_466661a082d1-communication_to_localtonet_tunneling_service_initiated|Communication To LocaltoNet Tunneling Service Initiated (high; windows / network_connection)]]
- [[kb/sigma/rules/5498fc09_adc6_4804_b9d9_5cca1f0b8760-opencanary_httpproxy_login_attempt|OpenCanary - HTTPPROXY Login Attempt (high; opencanary / application)]]
- [[kb/sigma/rules/5bed80b6_b3e8_428e_a3ae_d3c757589e41-rdp_over_reverse_ssh_tunnel_wfp|RDP over Reverse SSH Tunnel WFP (high; windows / security)]]
- [[kb/sigma/rules/62f7c9bf_9135_49b2_8aeb_1e54a6ecc13c-tor_client_browser_execution|Tor Client/Browser Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/64d51a51_32a6_49f0_9f3d_17e34d640272-ngrok_usage_with_remote_desktop_service|Ngrok Usage with Remote Desktop Service (high; windows / terminalservices-localsessionmanager)]]
- [[kb/sigma/rules/68d37776_61db_42f5_bf54_27e87072d17e-pua_nps_tunneling_tool_execution|PUA - NPS Tunneling Tool Execution (high; windows / process_creation)]]
- 11 more in the generated source index

### Atomic Tests

- [[kb/atomic/tests/0ac21132_4485_4212_a681_349e8a6637cd-connection_proxy|Connection Proxy (sh; linux, macos)]]
- [[kb/atomic/tests/12631354_fdbc_4164_92be_402527e748da-tor_proxy_usage_macos|Tor Proxy Usage - MacOS (sh; macos)]]
- [[kb/atomic/tests/14d55ca0_920e_4b44_8425_37eedd72b173-psiphon|Psiphon (powershell; windows)]]
- [[kb/atomic/tests/5ff9d047_6e9c_4357_b39b_5cf89d9b59c7-tor_proxy_usage_debian_ubuntu_freebsd|Tor Proxy Usage - Debian/Ubuntu/FreeBSD (sh; linux)]]
- [[kb/atomic/tests/648d68c1_8bcd_4486_9abe_71c6655b6a2c-connection_proxy_for_macos_ui|Connection Proxy for macOS UI (sh; macos)]]
- [[kb/atomic/tests/7b9d85e5_c4ce_4434_8060_d3de83595e69-tor_proxy_usage_windows|Tor Proxy Usage - Windows (powershell; windows)]]
- [[kb/atomic/tests/b8223ea9_4be2_44a6_b50a_9657a3d4e72a-portproxy_reg_key|portproxy reg key (powershell; windows)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0011-command_and_control|TA0011: Command and Control]]

## D3FEND

- [[D3-APCA-application_protocol_command_analysis|D3-APCA: Application Protocol Command Analysis]]
- [[D3-CAA-connection_attempt_analysis|D3-CAA: Connection Attempt Analysis]]
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

### T1090.001: Internal Proxy

^t1090001-internal-proxy

Adversaries may use an internal proxy to direct command and control traffic between two or more systems in a compromised environment. Many tools exist that enable traffic redirection through proxies or port redirection, including [[htran|HTRAN (S0040)]], ZXProxy, and ZXPortMap. (Citation: Trend Micro APT Attack Tools) Adversaries use internal proxies to manage command and control communications inside a compromised environment, to reduce the number of simultaneous outbound network connections, to provide resiliency in the face of connection loss, or to ride over existing trusted communications paths between infected systems to avoid suspicion. Internal proxy connections may use common peer-to-peer (p2p) networking protocols, such as SMB, to better blend in with the environment.

By using a compromised internal system as a proxy, adversaries may conceal the true destination of C2 traffic while reducing the need for numerous connections to external systems.

### T1090.002: External Proxy

^t1090002-external-proxy

Adversaries may use an external proxy to act as an intermediary for network communications to a command and control server to avoid direct connections to their infrastructure. Many tools exist that enable traffic redirection through proxies or port redirection, including [[htran|HTRAN (S0040)]], ZXProxy, and ZXPortMap. (Citation: Trend Micro APT Attack Tools) Adversaries use these types of proxies to manage command and control communications, to provide resiliency in the face of connection loss, or to ride over existing trusted communications paths to avoid suspicion.

External connection proxies are used to mask the destination of C2 traffic and are typically implemented with port redirectors. Compromised systems outside of the victim environment may be used for these purposes, as well as purchased infrastructure such as cloud-based resources or virtual private servers. Proxies may be chosen based on the low likelihood that a connection to them from a compromised system would be investigated. Victim systems would communicate directly with the external proxy on the Internet and then the proxy would forward communications to the C2 server.

### T1090.003: Multi-hop Proxy

^t1090003-multi-hop-proxy

Adversaries may chain together multiple proxies to disguise the source of malicious traffic. Typically, a defender will be able to identify the last proxy traffic traversed before it enters their network; the defender may or may not be able to identify any previous proxies before the last-hop proxy. This technique makes identifying the original source of the malicious traffic even more difficult by requiring the defender to trace malicious traffic through several proxies to identify its source.

For example, adversaries may construct or use onion routing networks – such as the publicly available [[tor|Tor (S0183)]] network – to transport encrypted C2 traffic through a compromised population, allowing communication with any device within the network.(Citation: Onion Routing) Adversaries may also use operational relay box (ORB) networks composed of virtual private servers (VPS), Internet of Things (IoT) devices, smart devices, and end-of-life routers to obfuscate their operations.(Citation: ORB Mandiant) 

In the case of network infrastructure, it is possible for an adversary to leverage multiple compromised devices to create a multi-hop proxy chain (i.e., [[T1584-compromise_infrastructure#^t1584008-network-devices|T1584.008: Network Devices]]). By leveraging [[T1601-modify_system_image#^t1601001-patch-system-image|T1601.001: Patch System Image]] on routers, adversaries can add custom code to the affected network devices that will implement onion routing between those nodes. This method is dependent upon the [[T1599-network_boundary_bridging|T1599: Network Boundary Bridging]] method allowing the adversaries to cross the protected network boundary of the Internet perimeter and into the organization’s Wide-Area Network (WAN).  Protocols such as ICMP may be used as a transport.  

Similarly, adversaries may abuse peer-to-peer (P2P) and blockchain-oriented infrastructure to implement routing between a decentralized network of peers.(Citation: NGLite Trojan)

### T1090.004: Domain Fronting

^t1090004-domain-fronting

Adversaries may take advantage of routing schemes in Content Delivery Networks (CDNs) and other services which host multiple domains to obfuscate the intended destination of HTTPS traffic or traffic tunneled through HTTPS. (Citation: Fifield Blocking Resistent Communication through domain fronting 2015) Domain fronting involves using different domain names in the SNI field of the TLS header and the Host field of the HTTP header. If both domains are served from the same CDN, then the CDN may route to the address specified in the HTTP header after unwrapping the TLS header. A variation of the the technique, "domainless" fronting, utilizes a SNI field that is left blank; this may allow the fronting to work even when the CDN attempts to validate that the SNI and HTTP Host fields match (if the blank SNI fields are ignored).

For example, if domain-x and domain-y are customers of the same CDN, it is possible to place domain-x in the TLS header and domain-y in the HTTP header. Traffic will appear to be going to domain-x, however the CDN may route it to domain-y.

## Mitigations

- [[M1020-ssl_tls_inspection|M1020: SSL/TLS Inspection]]
- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]

## Tools
- [[frp|FRP (S1144)]]
- [[htran|HTRAN (S0040)]]
- [[netsh|netsh (S0108)]]
- [[ngrok|ngrok (S0508)]]
- [[poshc2|PoshC2 (S0378)]]
- [[quasarrat|QuasarRAT (S0262)]]
- [[remcos|Remcos (S0332)]]


## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

