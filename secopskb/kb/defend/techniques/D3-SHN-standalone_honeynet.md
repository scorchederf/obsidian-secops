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
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

An environment created for the purpose of attracting attackers and eliciting their behaviors that is not connected to any production enterprise systems.

## Workspace

- [[workspaces/defend/techniques/D3-SHN-standalone_honeynet-note|Open workspace note]]

![[workspaces/defend/techniques/D3-SHN-standalone_honeynet-note]]

## Parent Technique

- [[D3-DE-decoy_environment|D3-DE: Decoy Environment]]

## Knowledge Base Article

## How it works
A standalone honeynet does not directly interact with the real enterprise environment. It may be located near or in some portion of the enterprise address space, but it does not interact with enterprise resources.

## Considerations
A standalone honeynet is a lower risk to deploy compared to connected or integrated honeynets due to its isolation from the enterprise network. However, this comes at cost in loss of fidelity and realism. Significant extra effort must be made in order to make the environment look realistic.

## Ontology Relationships

- [[D3-DE-decoy_environment|D3-DE: Decoy Environment]]

