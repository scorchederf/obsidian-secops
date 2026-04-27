---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-EPL"
d3fend_name: "Physical Locking"
d3fend_ontology_id: "d3f:PhysicalLocking"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3APhysicalLocking/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Employ a mechanical locking device for securing moveable portions of physical barriers (e.g., doors, gates, drawers) in a secured position.

## Workspace

- [[workspaces/defend/techniques/D3-EPL-physical_locking-note|Open workspace note]]

![[workspaces/defend/techniques/D3-EPL-physical_locking-note]]

## Parent Technique

- [[D3-PAM-physical_access_mediation|D3-PAM: Physical Access Mediation]]

## Knowledge Base Article

## How it works

A physical mechanism which has a associated credential which when entered enables the lock bolt to operate, i.e. open or close.

## Considerations

* Consider that locks for specified materials should adhere to relevant regulations.

* Lock equipment cabinets when not needed for operation or safety; set OT asset keys of devices (e.g., PLCs and safety systems) to the “RUN” position unless otherwise specified.

* Locks and all associated hardware should be properly installed, operable, and free of substantive indications of tampering.

* Records should be maintained concerning maintenance performed, access, and any possible tampering marks or associated incidents.

* For locks operated by a physical key, a key management system should be implemented to manage and secure physical keys.

* Key locks should provide a high degree of resistance to opening by force and tampering techniques.

## Ontology Relationships

- [[D3-PAM-physical_access_mediation|D3-PAM: Physical Access Mediation]]

