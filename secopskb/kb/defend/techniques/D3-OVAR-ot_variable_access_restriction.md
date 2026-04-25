---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-OVAR"
d3fend_name: "OT Variable Access Restriction"
d3fend_ontology_id: "d3f:OTVariableAccessRestriction"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AOTVariableAccessRestriction/"
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

Assign read/write access controls on designated registers or data tags to prevent unauthorized writes.

## Workspace

- [[notes/defend/techniques/D3-OVAR-ot_variable_access_restriction-note|Open workspace note]]

![[notes/defend/techniques/D3-OVAR-ot_variable_access_restriction-note]]

## Parent Technique

- [[D3-AMED-access_mediation|D3-AMED: Access Mediation]]

## Knowledge Base Article

 ## How it works

Many OT Controllers and OT Communication Modules enable Read-Only or Read/Write access on a per-tag basis.

As an example, when configuring OT process tags which can be accessed using the Modbus protocol, configure the tag to a Modbus Input Register to leverage the protocol's registry ranges, restricting the ability of external sources to modify data.

In Siemens, each data block (DB) tag can be configured as "data block write-protected in the device."


## Ontology Relationships

- [[D3-AMED-access_mediation|D3-AMED: Access Mediation]]

