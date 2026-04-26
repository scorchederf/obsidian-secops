---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-CHN"
d3fend_name: "Connected Honeynet"
d3fend_ontology_id: "d3f:ConnectedHoneynet"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AConnectedHoneynet/"
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

A decoy service, system, or environment, that is connected to the enterprise network, and simulates or emulates certain functionality to the network, without exposing full access to a production system.

## Workspace

- [[workspaces/defend/techniques/D3-CHN-connected_honeynet-note|Open workspace note]]

![[workspaces/defend/techniques/D3-CHN-connected_honeynet-note]]

## Parent Technique

- [[D3-DE-decoy_environment|D3-DE: Decoy Environment]]

## Knowledge Base Article

## How it works
Decoy honeypots are deployed within the enterprise environment that emulate certain services or portions of an OS to attract attackers.

## Considerations
A connected honeynet provides a tradeoff between emulating certain functionality but not being as sophisticated as an integrated honeynet. The connected honeynet may not provide enough functionality to detect new attack patterns or zero day exploits but could provide enough functionality for specific known vulnerabilities.

## Ontology Relationships

- [[D3-DE-decoy_environment|D3-DE: Decoy Environment]]

