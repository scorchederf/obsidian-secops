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
build_date: "2026-04-23 22:40:56"
build_source: "script"
---

# D3-IHN: Integrated Honeynet

The practice of setting decoys in a production environment to entice interaction from attackers.

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

## Workspace

- [[kb/notes/d3fend/techniques/d3-ihn-notes|Open workspace note]]

