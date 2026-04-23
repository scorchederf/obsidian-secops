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
build_date: "2026-04-23 22:40:56"
build_source: "script"
---

# D3-CHN: Connected Honeynet

A decoy service, system, or environment, that is connected to the enterprise network, and simulates or emulates certain functionality to the network, without exposing full access to a production system.

## Parent Technique

- [[D3-DE-decoy_environment|D3-DE: Decoy Environment]]

## Knowledge Base Article

## How it works
Decoy honeypots are deployed within the enterprise environment that emulate certain services or portions of an OS to attract attackers.

## Considerations
A connected honeynet provides a tradeoff between emulating certain functionality but not being as sophisticated as an integrated honeynet. The connected honeynet may not provide enough functionality to detect new attack patterns or zero day exploits but could provide enough functionality for specific known vulnerabilities.

## Ontology Relationships

- [[D3-DE-decoy_environment|D3-DE: Decoy Environment]]

## Workspace

- [[kb/notes/d3fend/techniques/d3-chn-notes|Open workspace note]]

