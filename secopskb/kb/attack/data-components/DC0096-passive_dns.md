---
mitre_id: "DC0096"
mitre_name: "Passive DNS"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--cc150ad8-ecfa-4340-9aaa-d21165873bd4"
mitre_created: "2021-10-20T15:05:19.275Z"
mitre_modified: "2025-10-21T15:10:28.402Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "data-component"
tags:
  - "attack"
  - "data-component"
  - "detection"
  - "telemetry"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

"Domain Name: Passive DNS" captures logged historical and real-time domain name system (DNS) data. This includes records of domain-to-IP address resolutions over time, enabling analysts to track the evolution of domain infrastructure, uncover historical patterns of use, and detect malicious activities tied to domains and their associated IP addresses. Examples: 

- Historical Resolutions
- Shared IP Usage
- Temporal Patterns
- Malicious Domain Clustering
- Historical Lookback

This data component can be collected through the following measures:

- Passive DNS Platforms: Use platforms that specialize in passive DNS collection and analysis:
   - Tools: Farsight DNSDB, RiskIQ PassiveTotal, PassiveDNS.
- Threat Intelligence Feeds: Integrate passive DNS data from commercial or open-source threat intelligence providers.
- Custom DNS Collectors: Deploy custom tools to capture DNS traffic at the network level for analysis.
- Cloud DNS Services: Leverage cloud DNS services (e.g., AWS Route 53, Azure DNS) that maintain DNS query logs.

## Workspace

- [[workspaces/attack/data-components/DC0096-passive_dns-note|Open workspace note]]

![[workspaces/attack/data-components/DC0096-passive_dns-note]]

