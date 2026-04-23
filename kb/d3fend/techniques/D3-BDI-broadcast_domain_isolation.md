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
build_date: "2026-04-23 22:40:56"
build_source: "script"
---

# D3-BDI: Broadcast Domain Isolation

Broadcast isolation restricts the number of computers a host can contact on their LAN.

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

## Workspace

- [[kb/notes/d3fend/techniques/d3-bdi-notes|Open workspace note]]

