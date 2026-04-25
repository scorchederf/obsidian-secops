---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-OTF"
d3fend_name: "Outbound Traffic Filtering"
d3fend_ontology_id: "d3f:OutboundTrafficFiltering"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AOutboundTrafficFiltering/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 20:43:29"
build_source: "script"
attack_technique_ids:
  - "T1001"
  - "T1001.001"
  - "T1001.002"
  - "T1001.003"
  - "T1008"
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
  - "T1090.002"
  - "T1090.003"
  - "T1090.004"
  - "T1095"
  - "T1102"
  - "T1102.001"
  - "T1102.002"
  - "T1102.003"
  - "T1104"
  - "T1105"
  - "T1132"
  - "T1132.001"
  - "T1132.002"
  - "T1189"
  - "T1197"
  - "T1204"
  - "T1204.001"
  - "T1219"
  - "T1219.001"
  - "T1219.002"
  - "T1219.003"
  - "T1567"
  - "T1567.001"
  - "T1567.002"
  - "T1567.003"
  - "T1567.004"
  - "T1568"
  - "T1568.001"
  - "T1568.002"
  - "T1568.003"
  - "T1571"
  - "T1572"
  - "T1573"
  - "T1573.001"
  - "T1573.002"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Restricting network traffic originating from a private host or enclave destined towards untrusted networks.

## Workspace

- [[workspaces/defend/techniques/D3-OTF-outbound_traffic_filtering-note|Open workspace note]]

![[workspaces/defend/techniques/D3-OTF-outbound_traffic_filtering-note]]

## Parent Technique

- [[D3-NTF-network_traffic_filtering|D3-NTF: Network Traffic Filtering]]

## Related ATT&CK Techniques

- [[T1001-data_obfuscation|T1001: Data Obfuscation]]
- [[T1001-data_obfuscation#^t1001001-junk-data|T1001.001: Junk Data]]
- [[T1001-data_obfuscation#^t1001002-steganography|T1001.002: Steganography]]
- [[T1001-data_obfuscation#^t1001003-protocol-or-service-impersonation|T1001.003: Protocol or Service Impersonation]]
- [[T1008-fallback_channels|T1008: Fallback Channels]]
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
- [[T1090-proxy#^t1090002-external-proxy|T1090.002: External Proxy]]
- [[T1090-proxy#^t1090003-multi-hop-proxy|T1090.003: Multi-hop Proxy]]
- [[T1090-proxy#^t1090004-domain-fronting|T1090.004: Domain Fronting]]
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
- [[T1189-drive-by_compromise|T1189: Drive-by Compromise]]
- [[T1197-bits_jobs|T1197: BITS Jobs]]
- [[T1204-user_execution|T1204: User Execution]]
- [[T1204-user_execution#^t1204001-malicious-link|T1204.001: Malicious Link]]
- [[T1219-remote_access_tools|T1219: Remote Access Tools]]
- [[T1219-remote_access_tools#^t1219001-ide-tunneling|T1219.001: IDE Tunneling]]
- [[T1219-remote_access_tools#^t1219002-remote-desktop-software|T1219.002: Remote Desktop Software]]
- [[T1219-remote_access_tools#^t1219003-remote-access-hardware|T1219.003: Remote Access Hardware]]
- [[T1567-exfiltration_over_web_service|T1567: Exfiltration Over Web Service]]
- [[T1567-exfiltration_over_web_service#^t1567001-exfiltration-to-code-repository|T1567.001: Exfiltration to Code Repository]]
- [[T1567-exfiltration_over_web_service#^t1567002-exfiltration-to-cloud-storage|T1567.002: Exfiltration to Cloud Storage]]
- [[T1567-exfiltration_over_web_service#^t1567003-exfiltration-to-text-storage-sites|T1567.003: Exfiltration to Text Storage Sites]]
- [[T1567-exfiltration_over_web_service#^t1567004-exfiltration-over-webhook|T1567.004: Exfiltration Over Webhook]]
- [[T1568-dynamic_resolution|T1568: Dynamic Resolution]]
- [[T1568-dynamic_resolution#^t1568001-fast-flux-dns|T1568.001: Fast Flux DNS]]
- [[T1568-dynamic_resolution#^t1568002-domain-generation-algorithms|T1568.002: Domain Generation Algorithms]]
- [[T1568-dynamic_resolution#^t1568003-dns-calculation|T1568.003: DNS Calculation]]
- [[T1571-non-standard_port|T1571: Non-Standard Port]]
- [[T1572-protocol_tunneling|T1572: Protocol Tunneling]]
- [[T1573-encrypted_channel|T1573: Encrypted Channel]]
- [[T1573-encrypted_channel#^t1573001-symmetric-cryptography|T1573.001: Symmetric Cryptography]]
- [[T1573-encrypted_channel#^t1573002-asymmetric-cryptography|T1573.002: Asymmetric Cryptography]]

## Knowledge Base Article

## How it works

Outbound traffic, in this context, is network traffic originating from a private host or enclave destined towards untrusted networks.
For example:

* An enterprise desktop intranet user connecting to www.example.com
* An internal mail server connecting to an external mail server, mail.example.com

Filtering is commonly implemented as firewall rulesets to limit outbound traffic permitted to egress a host or network. Firewalls are deployed either directly on hosts through kernel level software implementations or installed in-line directly on network links. There are benefits and disadvantages to each approach.

There are various strategies for developing filtering rulesets:

* Block everything by default
* Limit destination hosts
* Limit destination transport or application protocols
* Restrict content outbound (Ex. strings formatted as social security numbers, or proprietary data)

## Considerations
* Dynamic IP assignment creates challenges for Outbound Traffic Filtering because users are not necessarily associated with the same IP address. This can be addressed by linking IP address management information with the filtering logic.
* Connections using non-standard transport layer ports may circumvent outbound traffic filtering technology which does not detect application protocol based on traffic content.
* Business requirements typically drive the development of filtering rule sets.

## Implementations
- iptables (Linux)
- Windows Firewall
- pf (BSD)

## Ontology Relationships

- [[D3-NTF-network_traffic_filtering|D3-NTF: Network Traffic Filtering]]

