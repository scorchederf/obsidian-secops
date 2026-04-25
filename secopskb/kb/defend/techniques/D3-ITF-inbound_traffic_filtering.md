---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-ITF"
d3fend_name: "Inbound Traffic Filtering"
d3fend_ontology_id: "d3f:InboundTrafficFiltering"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AInboundTrafficFiltering/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 14:47:22"
build_source: "script"
attack_technique_ids:
  - "T1190"
  - "T1498"
  - "T1498.001"
  - "T1498.002"
  - "T1499"
  - "T1499.002"
  - "T1566"
  - "T1566.001"
  - "T1566.002"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Restricting network traffic originating from untrusted networks destined towards a private host or enclave.

## Workspace

- [[notes/defend/techniques/D3-ITF-inbound_traffic_filtering-note|Open workspace note]]

![[notes/defend/techniques/D3-ITF-inbound_traffic_filtering-note]]

## Parent Technique

- [[D3-NTF-network_traffic_filtering|D3-NTF: Network Traffic Filtering]]

## Child Techniques

- [[D3-EF-email_filtering|D3-EF: Email Filtering]]

## Related ATT&CK Techniques

- [[T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]]
- [[T1498-network_denial_of_service|T1498: Network Denial of Service]]
- [[T1498-network_denial_of_service#^t1498001-direct-network-flood|T1498.001: Direct Network Flood]]
- [[T1498-network_denial_of_service#^t1498002-reflection-amplification|T1498.002: Reflection Amplification]]
- [[T1499-endpoint_denial_of_service|T1499: Endpoint Denial of Service]]
- [[T1499-endpoint_denial_of_service#^t1499002-service-exhaustion-flood|T1499.002: Service Exhaustion Flood]]
- [[T1566-phishing|T1566: Phishing]]
- [[T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]]
- [[T1566-phishing#^t1566002-spearphishing-link|T1566.002: Spearphishing Link]]

## Knowledge Base Article

## How it works
Inbound Traffic, in this context, is network traffic originating from an untrusted network towards a private host or enclave.
For example:

* An untrusted network host connecting to a internal commercial portal, shopping.example.com
* An external mail server connecting to an internal mail server, mail.example.com

Filtering policies are developed by administrators to meet business requirements and limit connectivity. These policies are implemented on edge devices such as firewalls, routers, and intrusion prevention systems. Examples of filters:

* Blocking incoming traffic from spoofed internally facing IP addresses
* Blocking specific ports and services from establishing connections
* Limiting specific IP ranges from connecting to the network
* Dynamic inbound filtering (Hole punching, STUN, NAT-T)

## Considerations
* Business requirements typically drive the development of filtering rulesets
* Protocols using non-standard ports may circumvent filtering technology, which does not detect application protocol based on traffic content

## Implementations
* OpenWRT (Embedded)
* Netfilter (Linux)
* Windows Firewall
* pf(BSD)

## Ontology Relationships

- [[D3-NTF-network_traffic_filtering|D3-NTF: Network Traffic Filtering]]

