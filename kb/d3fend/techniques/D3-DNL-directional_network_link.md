---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-DNL"
d3fend_name: "Directional Network Link"
d3fend_ontology_id: "d3f:DirectionalNetworkLink"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ADirectionalNetworkLink/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-23 22:40:56"
build_source: "script"
---

# D3-DNL: Directional Network Link

Enforce one-way network communication by preventing two-way communication.

## Parent Technique

- [[D3-NI-network_isolation|D3-NI: Network Isolation]]

## Knowledge Base Article

## How it works
Using a device such as a data diode, or otherwise enforcing unidirectional (one-way) network communication / data transfer, to physically prevent signals from traveling in the reverse direction.

Unidirectional network link enforcement is a security measure used to separate control and safety systems in operational technology (OT) environments. By employing physical data diodes, this approach ensures one-way communication, allowing information from safety systems to be viewed without permitting any modification or interference, thereby protecting the integrity of the safety system.



## Ontology Relationships

- [[D3-NI-network_isolation|D3-NI: Network Isolation]]

## Workspace

- [[kb/notes/d3fend/techniques/d3-dnl-notes|Open workspace note]]

