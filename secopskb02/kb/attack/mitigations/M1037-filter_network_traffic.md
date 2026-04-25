---
mitre_id: "M1037"
mitre_name: "Filter Network Traffic"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--20f6a9df-37c4-4e20-9e47-025983b1b39d"
mitre_created: "2019-06-11T16:33:55.337Z"
mitre_modified: "2024-12-11T19:43:03.354Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1037/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "mitigation"
tags:
  - "attack"
  - "mitigation"
  - "defense"
  - "countermeasure"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Employ network appliances and endpoint software to filter ingress, egress, and lateral network traffic. This includes protocol-based filtering, enforcing firewall rules, and blocking or restricting traffic based on predefined conditions to limit adversary movement and data exfiltration. This mitigation can be implemented through the following measures:

Ingress Traffic Filtering:

- Use Case: Configure network firewalls to allow traffic only from authorized IP addresses to public-facing servers.
- Implementation: Limit SSH (port 22) and RDP (port 3389) traffic to specific IP ranges.

Egress Traffic Filtering:

- Use Case: Use firewalls or endpoint security software to block unauthorized outbound traffic to prevent data exfiltration and command-and-control (C2) communications.
- Implementation: Block outbound traffic to known malicious IPs or regions where communication is unexpected.

Protocol-Based Filtering:

- Use Case: Restrict the use of specific protocols that are commonly abused by adversaries, such as SMB, RPC, or Telnet, based on business needs.
- Implementation: Disable SMBv1 on endpoints to prevent exploits like EternalBlue.

Network Segmentation:

- Use Case: Create network segments for critical systems and restrict communication between segments unless explicitly authorized.
- Implementation: Implement VLANs to isolate IoT devices or guest networks from core business systems.

Application Layer Filtering:

- Use Case: Use proxy servers or Web Application Firewalls (WAFs) to inspect and block malicious HTTP/S traffic.
- Implementation: Configure a WAF to block SQL injection attempts or other web application exploitation techniques.

## Workspace

- [[workspaces/attack/mitigations/M1037-filter_network_traffic-note|Open workspace note]]

![[workspaces/attack/mitigations/M1037-filter_network_traffic-note]]

## Mitigates Techniques

- [[T1021-remote_services|T1021: Remote Services]]
    - [[T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]]
    - [[T1021-remote_services#^t1021005-vnc|T1021.005: VNC]]
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
    - [[T1090-proxy#^t1090003-multi-hop-proxy|T1090.003: Multi-hop Proxy]]
- [[T1095-non-application_layer_protocol|T1095: Non-Application Layer Protocol]]
- [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[T1187-forced_authentication|T1187: Forced Authentication]]
- [[T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]]
- [[T1197-bits_jobs|T1197: BITS Jobs]]
- [[T1205-traffic_signaling|T1205: Traffic Signaling]]
- [[T1205-traffic_signaling|T1205: Traffic Signaling]]
    - [[T1205-traffic_signaling#^t1205001-port-knocking|T1205.001: Port Knocking]]
    - [[T1205-traffic_signaling#^t1205002-socket-filters|T1205.002: Socket Filters]]
- [[T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]
- [[T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]
    - [[T1218-system_binary_proxy_execution#^t1218012-verclsid|T1218.012: Verclsid]]
- [[T1219-remote_access_tools|T1219: Remote Access Tools]]
- [[T1219-remote_access_tools|T1219: Remote Access Tools]]
    - [[T1219-remote_access_tools#^t1219002-remote-desktop-software|T1219.002: Remote Desktop Software]]
- [[T1498-network_denial_of_service|T1498: Network Denial of Service]]
- [[T1498-network_denial_of_service|T1498: Network Denial of Service]]
    - [[T1498-network_denial_of_service#^t1498001-direct-network-flood|T1498.001: Direct Network Flood]]
    - [[T1498-network_denial_of_service#^t1498002-reflection-amplification|T1498.002: Reflection Amplification]]
- [[T1499-endpoint_denial_of_service|T1499: Endpoint Denial of Service]]
- [[T1499-endpoint_denial_of_service|T1499: Endpoint Denial of Service]]
    - [[T1499-endpoint_denial_of_service#^t1499001-os-exhaustion-flood|T1499.001: OS Exhaustion Flood]]
    - [[T1499-endpoint_denial_of_service#^t1499002-service-exhaustion-flood|T1499.002: Service Exhaustion Flood]]
    - [[T1499-endpoint_denial_of_service#^t1499003-application-exhaustion-flood|T1499.003: Application Exhaustion Flood]]
    - [[T1499-endpoint_denial_of_service#^t1499004-application-or-system-exploitation|T1499.004: Application or System Exploitation]]
- [[T1530-data_from_cloud_storage|T1530: Data from Cloud Storage]]
- [[T1537-transfer_data_to_cloud_account|T1537: Transfer Data to Cloud Account]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
    - [[T1552-unsecured_credentials#^t1552005-cloud-instance-metadata-api|T1552.005: Cloud Instance Metadata API]]
- [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]]
- [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]]
    - [[T1557-adversary-in-the-middle#^t1557001-llmnr-nbt-ns-poisoning-and-smb-relay|T1557.001: LLMNR/NBT-NS Poisoning and SMB Relay]]
    - [[T1557-adversary-in-the-middle#^t1557002-arp-cache-poisoning|T1557.002: ARP Cache Poisoning]]
    - [[T1557-adversary-in-the-middle#^t1557003-dhcp-spoofing|T1557.003: DHCP Spoofing]]
- [[T1570-lateral_tool_transfer|T1570: Lateral Tool Transfer]]
- [[T1572-protocol_tunneling|T1572: Protocol Tunneling]]
- [[T1599-network_boundary_bridging|T1599: Network Boundary Bridging]]
- [[T1599-network_boundary_bridging|T1599: Network Boundary Bridging]]
    - [[T1599-network_boundary_bridging#^t1599001-network-address-translation-traversal|T1599.001: Network Address Translation Traversal]]
- [[T1602-data_from_configuration_repository|T1602: Data from Configuration Repository]]
- [[T1602-data_from_configuration_repository|T1602: Data from Configuration Repository]]
    - [[T1602-data_from_configuration_repository#^t1602001-snmp-(mib-dump)|T1602.001: SNMP (MIB Dump)]]
    - [[T1602-data_from_configuration_repository#^t1602002-network-device-configuration-dump|T1602.002: Network Device Configuration Dump]]

