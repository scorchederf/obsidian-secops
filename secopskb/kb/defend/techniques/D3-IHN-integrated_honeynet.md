---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-IHN"
d3fend_name: "Integrated Honeynet"
d3fend_ontology_id: "d3f:IntegratedHoneynet"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AIntegratedHoneynet/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

The practice of setting decoys in a production environment to entice interaction from attackers.

## Workspace

- [[workspaces/defend/techniques/D3-IHN-integrated_honeynet-note|Open workspace note]]

![[workspaces/defend/techniques/D3-IHN-integrated_honeynet-note]]

## Parent Technique

- [[D3-DE-decoy_environment|D3-DE: Decoy Environment]]

## Knowledge Base Article

## How it works
Integrated honeynets use full production environments connected to the enterprise network, that utilize computing resources or software that attract attackers, and allow full interaction and access that provides a complete view of an attack.

## Considerations
An attacker with control of a system on an Integrated Honeynet could:
* try to attack other connected hosts on the network, its IP range of internal hosts not properly configured to react to connections from machines on the integrated honeynet, or position behind the firewall.
* exploit its position by eavesdropping on network traffic
If an attacker manages to stop the processes used to log an attack without setting off any alarms. [1]

1. Honeypots for Windows, Roger Grimes, 2005

## Ontology Relationships

- [[D3-DE-decoy_environment|D3-DE: Decoy Environment]]

