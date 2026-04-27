---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-APCA"
d3fend_name: "Application Protocol Command Analysis"
d3fend_ontology_id: "d3f:ApplicationProtocolCommandAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AApplicationProtocolCommandAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1001"
  - "T1001.001"
  - "T1001.002"
  - "T1001.003"
  - "T1003"
  - "T1003.006"
  - "T1008"
  - "T1011"
  - "T1011.001"
  - "T1018"
  - "T1020"
  - "T1020.001"
  - "T1021"
  - "T1021.001"
  - "T1021.002"
  - "T1021.003"
  - "T1021.004"
  - "T1021.005"
  - "T1021.006"
  - "T1021.007"
  - "T1021.008"
  - "T1029"
  - "T1030"
  - "T1041"
  - "T1047"
  - "T1048"
  - "T1048.001"
  - "T1048.002"
  - "T1048.003"
  - "T1071"
  - "T1071.001"
  - "T1071.002"
  - "T1071.003"
  - "T1071.004"
  - "T1071.005"
  - "T1090"
  - "T1090.001"
  - "T1090.002"
  - "T1090.003"
  - "T1090.004"
  - "T1095"
  - "T1098"
  - "T1098.001"
  - "T1102"
  - "T1102.001"
  - "T1102.002"
  - "T1102.003"
  - "T1104"
  - "T1105"
  - "T1110"
  - "T1110.003"
  - "T1110.004"
  - "T1132"
  - "T1132.001"
  - "T1132.002"
  - "T1185"
  - "T1189"
  - "T1190"
  - "T1197"
  - "T1199"
  - "T1204"
  - "T1204.001"
  - "T1205"
  - "T1205.001"
  - "T1205.002"
  - "T1207"
  - "T1210"
  - "T1218"
  - "T1218.003"
  - "T1219"
  - "T1219.001"
  - "T1219.002"
  - "T1219.003"
  - "T1498"
  - "T1498.001"
  - "T1498.002"
  - "T1499"
  - "T1499.002"
  - "T1542"
  - "T1542.005"
  - "T1546"
  - "T1546.003"
  - "T1546.008"
  - "T1550"
  - "T1550.001"
  - "T1550.004"
  - "T1557"
  - "T1557.001"
  - "T1557.002"
  - "T1557.003"
  - "T1557.004"
  - "T1558"
  - "T1558.003"
  - "T1563"
  - "T1563.001"
  - "T1563.002"
  - "T1565"
  - "T1565.002"
  - "T1566"
  - "T1566.001"
  - "T1566.002"
  - "T1567"
  - "T1567.001"
  - "T1567.002"
  - "T1567.003"
  - "T1567.004"
  - "T1568"
  - "T1568.001"
  - "T1568.002"
  - "T1568.003"
  - "T1570"
  - "T1571"
  - "T1572"
  - "T1573"
  - "T1573.001"
  - "T1573.002"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Analyzing application protocol level remote commands to detect unauthorized activity.

## Workspace

- [[workspaces/defend/techniques/D3-APCA-application_protocol_command_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-APCA-application_protocol_command_analysis-note]]

## Parent Technique

- [[D3-NTA-network_traffic_analysis|D3-NTA: Network Traffic Analysis]]

## Child Techniques

- [[D3-RFUM-remote_firmware_update_monitoring|D3-RFUM: Remote Firmware Update Monitoring]]

## Related ATT&CK Techniques

- [[T1001-data_obfuscation|T1001: Data Obfuscation]]
- [[T1001-data_obfuscation#^t1001001-junk-data|T1001.001: Junk Data]]
- [[T1001-data_obfuscation#^t1001002-steganography|T1001.002: Steganography]]
- [[T1001-data_obfuscation#^t1001003-protocol-or-service-impersonation|T1001.003: Protocol or Service Impersonation]]
- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
- [[T1003-os_credential_dumping#^t1003006-dcsync|T1003.006: DCSync]]
- [[T1008-fallback_channels|T1008: Fallback Channels]]
- [[T1011-exfiltration_over_other_network_medium|T1011: Exfiltration Over Other Network Medium]]
- [[T1011-exfiltration_over_other_network_medium#^t1011001-exfiltration-over-bluetooth|T1011.001: Exfiltration Over Bluetooth]]
- [[T1018-remote_system_discovery|T1018: Remote System Discovery]]
- [[T1020-automated_exfiltration|T1020: Automated Exfiltration]]
- [[T1020-automated_exfiltration#^t1020001-traffic-duplication|T1020.001: Traffic Duplication]]
- [[T1021-remote_services|T1021: Remote Services]]
- [[T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]]
- [[T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]]
- [[T1021-remote_services#^t1021003-distributed-component-object-model|T1021.003: Distributed Component Object Model]]
- [[T1021-remote_services#^t1021004-ssh|T1021.004: SSH]]
- [[T1021-remote_services#^t1021005-vnc|T1021.005: VNC]]
- [[T1021-remote_services#^t1021006-windows-remote-management|T1021.006: Windows Remote Management]]
- [[T1021-remote_services#^t1021007-cloud-services|T1021.007: Cloud Services]]
- [[T1021-remote_services#^t1021008-direct-cloud-vm-connections|T1021.008: Direct Cloud VM Connections]]
- [[T1029-scheduled_transfer|T1029: Scheduled Transfer]]
- [[T1030-data_transfer_size_limits|T1030: Data Transfer Size Limits]]
- [[T1041-exfiltration_over_c2_channel|T1041: Exfiltration Over C2 Channel]]
- [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]
- [[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]]
- [[T1048-exfiltration_over_alternative_protocol#^t1048001-exfiltration-over-symmetric-encrypted-non-c2-protocol|T1048.001: Exfiltration Over Symmetric Encrypted Non-C2 Protocol]]
- [[T1048-exfiltration_over_alternative_protocol#^t1048002-exfiltration-over-asymmetric-encrypted-non-c2-protocol|T1048.002: Exfiltration Over Asymmetric Encrypted Non-C2 Protocol]]
- [[T1048-exfiltration_over_alternative_protocol#^t1048003-exfiltration-over-unencrypted-non-c2-protocol|T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol]]
- [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]
- [[T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]]
- [[T1071-application_layer_protocol#^t1071002-file-transfer-protocols|T1071.002: File Transfer Protocols]]
- [[T1071-application_layer_protocol#^t1071003-mail-protocols|T1071.003: Mail Protocols]]
- [[T1071-application_layer_protocol#^t1071004-dns|T1071.004: DNS]]
- [[T1071-application_layer_protocol#^t1071005-publish-subscribe-protocols|T1071.005: Publish/Subscribe Protocols]]
- [[T1090-proxy|T1090: Proxy]]
- [[T1090-proxy#^t1090001-internal-proxy|T1090.001: Internal Proxy]]
- [[T1090-proxy#^t1090002-external-proxy|T1090.002: External Proxy]]
- [[T1090-proxy#^t1090003-multi-hop-proxy|T1090.003: Multi-hop Proxy]]
- [[T1090-proxy#^t1090004-domain-fronting|T1090.004: Domain Fronting]]
- [[T1095-non-application_layer_protocol|T1095: Non-Application Layer Protocol]]
- [[T1098-account_manipulation|T1098: Account Manipulation]]
- [[T1098-account_manipulation#^t1098001-additional-cloud-credentials|T1098.001: Additional Cloud Credentials]]
- [[T1102-web_service|T1102: Web Service]]
- [[T1102-web_service#^t1102001-dead-drop-resolver|T1102.001: Dead Drop Resolver]]
- [[T1102-web_service#^t1102002-bidirectional-communication|T1102.002: Bidirectional Communication]]
- [[T1102-web_service#^t1102003-one-way-communication|T1102.003: One-Way Communication]]
- [[T1104-multi-stage_channels|T1104: Multi-Stage Channels]]
- [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[T1110-brute_force|T1110: Brute Force]]
- [[T1110-brute_force#^t1110003-password-spraying|T1110.003: Password Spraying]]
- [[T1110-brute_force#^t1110004-credential-stuffing|T1110.004: Credential Stuffing]]
- [[T1132-data_encoding|T1132: Data Encoding]]
- [[T1132-data_encoding#^t1132001-standard-encoding|T1132.001: Standard Encoding]]
- [[T1132-data_encoding#^t1132002-non-standard-encoding|T1132.002: Non-Standard Encoding]]
- [[T1185-browser_session_hijacking|T1185: Browser Session Hijacking]]
- [[T1189-drive-by_compromise|T1189: Drive-by Compromise]]
- [[T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]]
- [[T1197-bits_jobs|T1197: BITS Jobs]]
- [[T1199-trusted_relationship|T1199: Trusted Relationship]]
- [[T1204-user_execution|T1204: User Execution]]
- [[T1204-user_execution#^t1204001-malicious-link|T1204.001: Malicious Link]]
- [[T1205-traffic_signaling|T1205: Traffic Signaling]]
- [[T1205-traffic_signaling#^t1205001-port-knocking|T1205.001: Port Knocking]]
- [[T1205-traffic_signaling#^t1205002-socket-filters|T1205.002: Socket Filters]]
- [[T1207-rogue_domain_controller|T1207: Rogue Domain Controller]]
- [[T1210-exploitation_of_remote_services|T1210: Exploitation of Remote Services]]
- [[T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]
- [[T1218-system_binary_proxy_execution#^t1218003-cmstp|T1218.003: CMSTP]]
- [[T1219-remote_access_tools|T1219: Remote Access Tools]]
- [[T1219-remote_access_tools#^t1219001-ide-tunneling|T1219.001: IDE Tunneling]]
- [[T1219-remote_access_tools#^t1219002-remote-desktop-software|T1219.002: Remote Desktop Software]]
- [[T1219-remote_access_tools#^t1219003-remote-access-hardware|T1219.003: Remote Access Hardware]]
- [[T1498-network_denial_of_service|T1498: Network Denial of Service]]
- [[T1498-network_denial_of_service#^t1498001-direct-network-flood|T1498.001: Direct Network Flood]]
- [[T1498-network_denial_of_service#^t1498002-reflection-amplification|T1498.002: Reflection Amplification]]
- [[T1499-endpoint_denial_of_service|T1499: Endpoint Denial of Service]]
- [[T1499-endpoint_denial_of_service#^t1499002-service-exhaustion-flood|T1499.002: Service Exhaustion Flood]]
- [[T1542-pre-os_boot|T1542: Pre-OS Boot]]
- [[T1542-pre-os_boot#^t1542005-tftp-boot|T1542.005: TFTP Boot]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
- [[T1546-event_triggered_execution#^t1546003-windows-management-instrumentation-event-subscription|T1546.003: Windows Management Instrumentation Event Subscription]]
- [[T1546-event_triggered_execution#^t1546008-accessibility-features|T1546.008: Accessibility Features]]
- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
- [[T1550-use_alternate_authentication_material#^t1550001-application-access-token|T1550.001: Application Access Token]]
- [[T1550-use_alternate_authentication_material#^t1550004-web-session-cookie|T1550.004: Web Session Cookie]]
- [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]]
- [[T1557-adversary-in-the-middle#^t1557001-llmnr-nbt-ns-poisoning-and-smb-relay|T1557.001: LLMNR/NBT-NS Poisoning and SMB Relay]]
- [[T1557-adversary-in-the-middle#^t1557002-arp-cache-poisoning|T1557.002: ARP Cache Poisoning]]
- [[T1557-adversary-in-the-middle#^t1557003-dhcp-spoofing|T1557.003: DHCP Spoofing]]
- [[T1557-adversary-in-the-middle#^t1557004-evil-twin|T1557.004: Evil Twin]]
- [[T1558-steal_or_forge_kerberos_tickets|T1558: Steal or Forge Kerberos Tickets]]
- [[T1558-steal_or_forge_kerberos_tickets#^t1558003-kerberoasting|T1558.003: Kerberoasting]]
- [[T1563-remote_service_session_hijacking|T1563: Remote Service Session Hijacking]]
- [[T1563-remote_service_session_hijacking#^t1563001-ssh-hijacking|T1563.001: SSH Hijacking]]
- [[T1563-remote_service_session_hijacking#^t1563002-rdp-hijacking|T1563.002: RDP Hijacking]]
- [[T1565-data_manipulation|T1565: Data Manipulation]]
- [[T1565-data_manipulation#^t1565002-transmitted-data-manipulation|T1565.002: Transmitted Data Manipulation]]
- [[T1566-phishing|T1566: Phishing]]
- [[T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]]
- [[T1566-phishing#^t1566002-spearphishing-link|T1566.002: Spearphishing Link]]
- [[T1567-exfiltration_over_web_service|T1567: Exfiltration Over Web Service]]
- [[T1567-exfiltration_over_web_service#^t1567001-exfiltration-to-code-repository|T1567.001: Exfiltration to Code Repository]]
- [[T1567-exfiltration_over_web_service#^t1567002-exfiltration-to-cloud-storage|T1567.002: Exfiltration to Cloud Storage]]
- [[T1567-exfiltration_over_web_service#^t1567003-exfiltration-to-text-storage-sites|T1567.003: Exfiltration to Text Storage Sites]]
- [[T1567-exfiltration_over_web_service#^t1567004-exfiltration-over-webhook|T1567.004: Exfiltration Over Webhook]]
- [[T1568-dynamic_resolution|T1568: Dynamic Resolution]]
- [[T1568-dynamic_resolution#^t1568001-fast-flux-dns|T1568.001: Fast Flux DNS]]
- [[T1568-dynamic_resolution#^t1568002-domain-generation-algorithms|T1568.002: Domain Generation Algorithms]]
- [[T1568-dynamic_resolution#^t1568003-dns-calculation|T1568.003: DNS Calculation]]
- [[T1570-lateral_tool_transfer|T1570: Lateral Tool Transfer]]
- [[T1571-non-standard_port|T1571: Non-Standard Port]]
- [[T1572-protocol_tunneling|T1572: Protocol Tunneling]]
- [[T1573-encrypted_channel|T1573: Encrypted Channel]]
- [[T1573-encrypted_channel#^t1573001-symmetric-cryptography|T1573.001: Symmetric Cryptography]]
- [[T1573-encrypted_channel#^t1573002-asymmetric-cryptography|T1573.002: Asymmetric Cryptography]]

## Knowledge Base Article

## How it works
This technique requires the ability to parse application layer protocols to understand the commands being sent to a remote service. Signature-based or statistical analysis may be employed to identify unauthorized commands being sent. These commands can be observed by monitoring network traffic or application logs.

## Ontology Relationships

- [[D3-NTA-network_traffic_analysis|D3-NTA: Network Traffic Analysis]]

