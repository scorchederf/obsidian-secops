---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-BDI"
d3fend_name: "Broadcast Domain Isolation"
d3fend_ontology_id: "d3f:BroadcastDomainIsolation"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ABroadcastDomainIsolation/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Broadcast isolation restricts the number of computers a host can contact on their LAN.

## Workspace

- [[workspaces/defend/techniques/D3-BDI-broadcast_domain_isolation-note|Open workspace note]]

![[workspaces/defend/techniques/D3-BDI-broadcast_domain_isolation-note]]

## Parent Technique

- [[D3-NI-network_isolation|D3-NI: Network Isolation]]

## Knowledge Base Article

## How it works
Software Defined Networking, or other network encapsulation technologies intercept host broadcast traffic then route it to a specified destination per a configured policy.

This can be implemented within hypervisors, networking hardware (WAPs, switches, routers), or virutal hardware.

## Considerations
This technique is highly dependent on network infrastructure and networking requirements.

## Ontology Relationships

- [[D3-NI-network_isolation|D3-NI: Network Isolation]]

