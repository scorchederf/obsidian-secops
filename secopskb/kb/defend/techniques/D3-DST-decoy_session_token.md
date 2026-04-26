---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-DST"
d3fend_name: "Decoy Session Token"
d3fend_ontology_id: "d3f:DecoySessionToken"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ADecoySessionToken/"
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

An authentication token created for the purposes of deceiving an adversary.

## Workspace

- [[workspaces/defend/techniques/D3-DST-decoy_session_token-note|Open workspace note]]

![[workspaces/defend/techniques/D3-DST-decoy_session_token-note]]

## Parent Technique

- [[D3-DO-decoy_object|D3-DO: Decoy Object]]

## Knowledge Base Article

## How it works
Usage of decoy session tokens may be monitored to track attacker behavior or otherwise control the beliefs of the attacker.

## Considerations
* Interaction and activity with the decoy session token must be constantly monitored and analyzed to detect unauthorized activity.
* Session tokens are typically short-lived and therefore the decoy must be continuously updated to provide the appearance of it being used in the production environment.
* Automated tools can assist with maintenance and updates by automatically adjusting the decoy session token and environment to mimic the production environment.

## Ontology Relationships

- [[D3-DO-decoy_object|D3-DO: Decoy Object]]

