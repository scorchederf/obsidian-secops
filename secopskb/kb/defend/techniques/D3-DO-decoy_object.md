---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-DO"
d3fend_name: "Decoy Object"
d3fend_ontology_id: "d3f:DecoyObject"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ADecoyObject/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 14:47:22"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

A Decoy Object is created and deployed for the purposes of deceiving attackers.

## Workspace

- [[notes/defend/techniques/D3-DO-decoy_object-note|Open workspace note]]

![[notes/defend/techniques/D3-DO-decoy_object-note]]

## Child Techniques

- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-DNR-decoy_network_resource|D3-DNR: Decoy Network Resource]]
- [[D3-DP-decoy_persona|D3-DP: Decoy Persona]]
- [[D3-DPR-decoy_public_release|D3-DPR: Decoy Public Release]]
- [[D3-DST-decoy_session_token|D3-DST: Decoy Session Token]]
- [[D3-DUC-decoy_user_credential|D3-DUC: Decoy User Credential]]

## Knowledge Base Article

## Technique Overview
Decoy objects are typically configured with detectable means of communication but do not have any legitimate business purpose. Any communication via or to these objects should be logged and analyzed to find potential indicators of compromise for a possible past or future attack against other systems.

