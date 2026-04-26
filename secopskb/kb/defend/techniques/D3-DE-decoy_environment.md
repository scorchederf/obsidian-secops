---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-DE"
d3fend_name: "Decoy Environment"
d3fend_ontology_id: "d3f:DecoyEnvironment"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ADecoyEnvironment/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1082"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

A Decoy Environment comprises hosts and networks for the purposes of deceiving an attacker.

## Workspace

- [[workspaces/defend/techniques/D3-DE-decoy_environment-note|Open workspace note]]

![[workspaces/defend/techniques/D3-DE-decoy_environment-note]]

## Child Techniques

- [[D3-CHN-connected_honeynet|D3-CHN: Connected Honeynet]]
- [[D3-IHN-integrated_honeynet|D3-IHN: Integrated Honeynet]]
- [[D3-SHN-standalone_honeynet|D3-SHN: Standalone Honeynet]]

## Related ATT&CK Techniques

- [[T1082-system_information_discovery|T1082: System Information Discovery]]

## Knowledge Base Article

## Technique Overview

Systems in a decoy environment are typically configured so that some detectable means of communication does not have any legitimate business purpose.  Any communication via these means should be logged and analyzed to find potential indicators of compromise for a possible past or future attack against other systems.

