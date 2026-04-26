---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-ISVA"
d3fend_name: "Inbound Session Volume Analysis"
d3fend_ontology_id: "d3f:InboundSessionVolumeAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AInboundSessionVolumeAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Analyzing inbound network session or connection attempt volume.

## Workspace

- [[workspaces/defend/techniques/D3-ISVA-inbound_session_volume_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-ISVA-inbound_session_volume_analysis-note]]

## Parent Technique

- [[D3-NTA-network_traffic_analysis|D3-NTA: Network Traffic Analysis]]

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
Network appliances are configured to alert on certain packets that typically are involved in DoS attacks. Typical packets include ICMP packets and SYN requests that are commonly used to flood networks. A sampling period is used to define a time window in which collected counts of the identified packets can be measured. If the collected number of packets exceeds a predefined limit then an alert is generated.

## Considerations
Scalability as volume of attacks increase; single servers may not have the memory and storage resources to handle high volumes of network traffic.

## Ontology Relationships

- [[D3-NTA-network_traffic_analysis|D3-NTA: Network Traffic Analysis]]

