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
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Enforce one-way network communication by preventing two-way communication.

## Workspace

- [[workspaces/defend/techniques/D3-DNL-directional_network_link-note|Open workspace note]]

![[workspaces/defend/techniques/D3-DNL-directional_network_link-note]]

## Parent Technique

- [[D3-NI-network_isolation|D3-NI: Network Isolation]]

## Knowledge Base Article

## How it works
Using a device such as a data diode, or otherwise enforcing unidirectional (one-way) network communication / data transfer, to physically prevent signals from traveling in the reverse direction.

Unidirectional network link enforcement is a security measure used to separate control and safety systems in operational technology (OT) environments. By employing physical data diodes, this approach ensures one-way communication, allowing information from safety systems to be viewed without permitting any modification or interference, thereby protecting the integrity of the safety system.



## Ontology Relationships

- [[D3-NI-network_isolation|D3-NI: Network Isolation]]

