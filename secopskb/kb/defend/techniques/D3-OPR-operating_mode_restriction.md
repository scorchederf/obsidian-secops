---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-OPR"
d3fend_name: "Operating Mode Restriction"
d3fend_ontology_id: "d3f:OperatingModeRestriction"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AOperatingModeRestriction/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Restricting unauthorized changes to the operating mode prevents devices from switching into inappropriate or vulnerable states during normal use.

## Workspace

- [[workspaces/defend/techniques/D3-OPR-operating_mode_restriction-note|Open workspace note]]

![[workspaces/defend/techniques/D3-OPR-operating_mode_restriction-note]]

## Parent Technique

- [[D3-AMED-access_mediation|D3-AMED: Access Mediation]]

## Knowledge Base Article

## How it works
Many OT Controllers use key switches to change the controller into different modes of operation. These modes of operation can include Program, Run, Remote, or Stop.

The key switch should be left in the appropriate key switch position, e.g., run or remote during normal operations.

Implement a key management procedure to include removing the physical key from the key switch when not in use.

## Ontology Relationships

- [[D3-AMED-access_mediation|D3-AMED: Access Mediation]]

