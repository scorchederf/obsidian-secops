---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-SHN"
d3fend_name: "Standalone Honeynet"
d3fend_ontology_id: "d3f:StandaloneHoneynet"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AStandaloneHoneynet/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-23 22:40:56"
build_source: "script"
---

# D3-SHN: Standalone Honeynet

An environment created for the purpose of attracting attackers and eliciting their behaviors that is not connected to any production enterprise systems.

## Parent Technique

- [[D3-DE-decoy_environment|D3-DE: Decoy Environment]]

## Knowledge Base Article

## How it works
A standalone honeynet does not directly interact with the real enterprise environment. It may be located near or in some portion of the enterprise address space, but it does not interact with enterprise resources.

## Considerations
A standalone honeynet is a lower risk to deploy compared to connected or integrated honeynets due to its isolation from the enterprise network. However, this comes at cost in loss of fidelity and realism. Significant extra effort must be made in order to make the environment look realistic.

## Ontology Relationships

- [[D3-DE-decoy_environment|D3-DE: Decoy Environment]]

## Workspace

- [[kb/notes/d3fend/techniques/d3-shn-notes|Open workspace note]]

