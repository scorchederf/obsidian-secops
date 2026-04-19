---
id: x-mitre-tactic--f72804c5-f15a-449e-a5da-2eecd181f813
name: Command and Control
created: 2018-10-17 00:14:20.652000+00:00
modified: 2025-04-25 14:45:36.561000+00:00
type: x-mitre-tactic
x_mitre_version: 1.0
x_mitre_domains: enterprise-attack
---

# Command and Control

The adversary is trying to communicate with compromised systems to control them.

Command and Control consists of techniques that adversaries may use to communicate with systems under their control within a victim network. Adversaries commonly attempt to mimic normal, expected traffic to avoid detection. There are many ways an adversary can establish command and control with various levels of stealth depending on the victim’s network structure and defenses.

## Properties

- id: x-mitre-tactic--f72804c5-f15a-449e-a5da-2eecd181f813
- name: Command and Control
- created: 2018-10-17 00:14:20.652000+00:00
- modified: 2025-04-25 14:45:36.561000+00:00
- type: x-mitre-tactic
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

## Related Techniques

- [[T1001-data_obfuscation|T1001: Data Obfuscation]]
    - [[T1001-data_obfuscation#^t1001001-junk-data|T1001.001: Junk Data]]
    - [[T1001-data_obfuscation#^t1001002-steganography|T1001.002: Steganography]]
    - [[T1001-data_obfuscation#^t1001003-protocol-or-service-impersonation|T1001.003: Protocol or Service Impersonation]]
- [[T1008-fallback_channels|T1008: Fallback Channels]]
- [[T1024-custom_cryptographic_protocol|T1024: Custom Cryptographic Protocol]]
- [[T1026-multiband_communication|T1026: Multiband Communication]]
- [[T1032-standard_cryptographic_protocol|T1032: Standard Cryptographic Protocol]]
- [[T1043-commonly_used_port|T1043: Commonly Used Port]]
- [[T1065-uncommonly_used_port|T1065: Uncommonly Used Port]]
- [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]
    - [[T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]]
    - [[T1071-application_layer_protocol#^t1071002-file-transfer-protocols|T1071.002: File Transfer Protocols]]
    - [[T1071-application_layer_protocol#^t1071003-mail-protocols|T1071.003: Mail Protocols]]
    - [[T1071-application_layer_protocol#^t1071004-dns|T1071.004: DNS]]
    - [[T1071-application_layer_protocol#^t1071005-publish-subscribe-protocols|T1071.005: Publish/Subscribe Protocols]]
- [[T1079-multilayer_encryption|T1079: Multilayer Encryption]]
- [[T1090-proxy|T1090: Proxy]]
    - [[T1090-proxy#^t1090001-internal-proxy|T1090.001: Internal Proxy]]
    - [[T1090-proxy#^t1090002-external-proxy|T1090.002: External Proxy]]
    - [[T1090-proxy#^t1090003-multi-hop-proxy|T1090.003: Multi-hop Proxy]]
    - [[T1090-proxy#^t1090004-domain-fronting|T1090.004: Domain Fronting]]
- [[T1092-communication_through_removable_media|T1092: Communication Through Removable Media]]
- [[T1094-custom_command_and_control_protocol|T1094: Custom Command and Control Protocol]]
- [[T1095-non-application_layer_protocol|T1095: Non-Application Layer Protocol]]
- [[T1102-web_service|T1102: Web Service]]
    - [[T1102-web_service#^t1102001-dead-drop-resolver|T1102.001: Dead Drop Resolver]]
    - [[T1102-web_service#^t1102002-bidirectional-communication|T1102.002: Bidirectional Communication]]
    - [[T1102-web_service#^t1102003-one-way-communication|T1102.003: One-Way Communication]]
- [[T1104-multi-stage_channels|T1104: Multi-Stage Channels]]
- [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[T1132-data_encoding|T1132: Data Encoding]]
    - [[T1132-data_encoding#^t1132001-standard-encoding|T1132.001: Standard Encoding]]
    - [[T1132-data_encoding#^t1132002-non-standard-encoding|T1132.002: Non-Standard Encoding]]
- [[T1172-domain_fronting|T1172: Domain Fronting]]
- [[T1188-multi-hop_proxy|T1188: Multi-hop Proxy]]
- [[T1205-traffic_signaling|T1205: Traffic Signaling]]
    - [[T1205-traffic_signaling#^t1205001-port-knocking|T1205.001: Port Knocking]]
    - [[T1205-traffic_signaling#^t1205002-socket-filters|T1205.002: Socket Filters]]
- [[T1219-remote_access_tools|T1219: Remote Access Tools]]
    - [[T1219-remote_access_tools#^t1219001-ide-tunneling|T1219.001: IDE Tunneling]]
    - [[T1219-remote_access_tools#^t1219002-remote-desktop-software|T1219.002: Remote Desktop Software]]
    - [[T1219-remote_access_tools#^t1219003-remote-access-hardware|T1219.003: Remote Access Hardware]]
- [[T1483-domain_generation_algorithms|T1483: Domain Generation Algorithms]]
- [[T1568-dynamic_resolution|T1568: Dynamic Resolution]]
    - [[T1568-dynamic_resolution#^t1568001-fast-flux-dns|T1568.001: Fast Flux DNS]]
    - [[T1568-dynamic_resolution#^t1568002-domain-generation-algorithms|T1568.002: Domain Generation Algorithms]]
    - [[T1568-dynamic_resolution#^t1568003-dns-calculation|T1568.003: DNS Calculation]]
- [[T1571-non-standard_port|T1571: Non-Standard Port]]
- [[T1572-protocol_tunneling|T1572: Protocol Tunneling]]
- [[T1573-encrypted_channel|T1573: Encrypted Channel]]
    - [[T1573-encrypted_channel#^t1573001-symmetric-cryptography|T1573.001: Symmetric Cryptography]]
    - [[T1573-encrypted_channel#^t1573002-asymmetric-cryptography|T1573.002: Asymmetric Cryptography]]
- [[T1659-content_injection|T1659: Content Injection]]
- [[T1665-hide_infrastructure|T1665: Hide Infrastructure]]
