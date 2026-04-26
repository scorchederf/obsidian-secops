---
mitre_id: "M1031"
mitre_name: "Network Intrusion Prevention"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--12241367-a8b7-49b4-b86e-2236901ba50c"
mitre_created: "2019-06-10T20:46:02.263Z"
mitre_modified: "2024-10-17T18:54:36.723Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1031/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "mitigation"
tags:
  - "attack"
  - "mitigation"
  - "defense"
  - "countermeasure"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Use intrusion detection signatures to block traffic at network boundaries.

## Workspace

- [[workspaces/attack/mitigations/M1031-network_intrusion_prevention-note|Open workspace note]]

![[workspaces/attack/mitigations/M1031-network_intrusion_prevention-note]]

## Mitigates Techniques

- [[T1001-data_obfuscation|T1001: Data Obfuscation]]
- [[T1001-data_obfuscation|T1001: Data Obfuscation]]
    - [[T1001-data_obfuscation#^t1001001-junk-data|T1001.001: Junk Data]]
    - [[T1001-data_obfuscation#^t1001002-steganography|T1001.002: Steganography]]
    - [[T1001-data_obfuscation#^t1001003-protocol-or-service-impersonation|T1001.003: Protocol or Service Impersonation]]
- [[T1008-fallback_channels|T1008: Fallback Channels]]
- [[T1029-scheduled_transfer|T1029: Scheduled Transfer]]
- [[T1030-data_transfer_size_limits|T1030: Data Transfer Size Limits]]
- [[T1041-exfiltration_over_c2_channel|T1041: Exfiltration Over C2 Channel]]
- [[T1046-network_service_discovery|T1046: Network Service Discovery]]
- [[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]]
- [[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]]
    - [[T1048-exfiltration_over_alternative_protocol#^t1048001-exfiltration-over-symmetric-encrypted-non-c2-protocol|T1048.001: Exfiltration Over Symmetric Encrypted Non-C2 Protocol]]
    - [[T1048-exfiltration_over_alternative_protocol#^t1048002-exfiltration-over-asymmetric-encrypted-non-c2-protocol|T1048.002: Exfiltration Over Asymmetric Encrypted Non-C2 Protocol]]
    - [[T1048-exfiltration_over_alternative_protocol#^t1048003-exfiltration-over-unencrypted-non-c2-protocol|T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol]]
- [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]
- [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]
    - [[T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]]
    - [[T1071-application_layer_protocol#^t1071002-file-transfer-protocols|T1071.002: File Transfer Protocols]]
    - [[T1071-application_layer_protocol#^t1071003-mail-protocols|T1071.003: Mail Protocols]]
    - [[T1071-application_layer_protocol#^t1071004-dns|T1071.004: DNS]]
    - [[T1071-application_layer_protocol#^t1071005-publish-subscribe-protocols|T1071.005: Publish/Subscribe Protocols]]
- [[T1090-proxy|T1090: Proxy]]
- [[T1090-proxy|T1090: Proxy]]
    - [[T1090-proxy#^t1090001-internal-proxy|T1090.001: Internal Proxy]]
    - [[T1090-proxy#^t1090002-external-proxy|T1090.002: External Proxy]]
- [[T1095-non-application_layer_protocol|T1095: Non-Application Layer Protocol]]
- [[T1102-web_service|T1102: Web Service]]
- [[T1102-web_service|T1102: Web Service]]
    - [[T1102-web_service#^t1102001-dead-drop-resolver|T1102.001: Dead Drop Resolver]]
    - [[T1102-web_service#^t1102002-bidirectional-communication|T1102.002: Bidirectional Communication]]
    - [[T1102-web_service#^t1102003-one-way-communication|T1102.003: One-Way Communication]]
- [[T1104-multi-stage_channels|T1104: Multi-Stage Channels]]
- [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[T1132-data_encoding|T1132: Data Encoding]]
- [[T1132-data_encoding|T1132: Data Encoding]]
    - [[T1132-data_encoding#^t1132001-standard-encoding|T1132.001: Standard Encoding]]
    - [[T1132-data_encoding#^t1132002-non-standard-encoding|T1132.002: Non-Standard Encoding]]
- [[T1204-user_execution|T1204: User Execution]]
- [[T1204-user_execution|T1204: User Execution]]
    - [[T1204-user_execution#^t1204001-malicious-link|T1204.001: Malicious Link]]
    - [[T1204-user_execution#^t1204003-malicious-image|T1204.003: Malicious Image]]
    - [[T1204-user_execution#^t1204004-malicious-copy-and-paste|T1204.004: Malicious Copy and Paste]]
    - [[T1204-user_execution#^t1204005-malicious-library|T1204.005: Malicious Library]]
- [[T1219-remote_access_tools|T1219: Remote Access Tools]]
- [[T1221-template_injection|T1221: Template Injection]]
- [[T1542-pre-os_boot|T1542: Pre-OS Boot]]
    - [[T1542-pre-os_boot#^t1542004-rommonkit|T1542.004: ROMMONkit]]
    - [[T1542-pre-os_boot#^t1542005-tftp-boot|T1542.005: TFTP Boot]]
- [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]]
- [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]]
    - [[T1557-adversary-in-the-middle#^t1557001-llmnr-nbt-ns-poisoning-and-smb-relay|T1557.001: LLMNR/NBT-NS Poisoning and SMB Relay]]
    - [[T1557-adversary-in-the-middle#^t1557002-arp-cache-poisoning|T1557.002: ARP Cache Poisoning]]
    - [[T1557-adversary-in-the-middle#^t1557003-dhcp-spoofing|T1557.003: DHCP Spoofing]]
    - [[T1557-adversary-in-the-middle#^t1557004-evil-twin|T1557.004: Evil Twin]]
- [[T1566-phishing|T1566: Phishing]]
- [[T1566-phishing|T1566: Phishing]]
    - [[T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]]
- [[T1568-dynamic_resolution|T1568: Dynamic Resolution]]
- [[T1568-dynamic_resolution|T1568: Dynamic Resolution]]
    - [[T1568-dynamic_resolution#^t1568002-domain-generation-algorithms|T1568.002: Domain Generation Algorithms]]
- [[T1570-lateral_tool_transfer|T1570: Lateral Tool Transfer]]
- [[T1571-non-standard_port|T1571: Non-Standard Port]]
- [[T1572-protocol_tunneling|T1572: Protocol Tunneling]]
- [[T1573-encrypted_channel|T1573: Encrypted Channel]]
- [[T1573-encrypted_channel|T1573: Encrypted Channel]]
    - [[T1573-encrypted_channel#^t1573001-symmetric-cryptography|T1573.001: Symmetric Cryptography]]
    - [[T1573-encrypted_channel#^t1573002-asymmetric-cryptography|T1573.002: Asymmetric Cryptography]]
- [[T1602-data_from_configuration_repository|T1602: Data from Configuration Repository]]
- [[T1602-data_from_configuration_repository|T1602: Data from Configuration Repository]]
    - [[T1602-data_from_configuration_repository#^t1602001-snmp-(mib-dump)|T1602.001: SNMP (MIB Dump)]]
    - [[T1602-data_from_configuration_repository#^t1602002-network-device-configuration-dump|T1602.002: Network Device Configuration Dump]]

