---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-NPC"
d3fend_name: "Null Pointer Checking"
d3fend_ontology_id: "d3f:NullPointerChecking"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ANullPointerChecking/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-23 22:40:56"
build_source: "script"
---

# D3-NPC: Null Pointer Checking

Checking if a pointer is NULL.

## Parent Technique

- [[D3-PV-pointer_validation|D3-PV: Pointer Validation]]

## Knowledge Base Article


## How it Works
Programmatically checking if a pointer is NULL before use.

## Considerations
* Pointers should be checked prior to use after they have, or may have been modified.
* Note that it may vary by circumstance whether the caller, or callee is responsible for checking if a pointer is NULL.
* Note: This resource should not be considered a definitive or exhaustive coding guideline.

## Ontology Relationships

- [[D3-PV-pointer_validation|D3-PV: Pointer Validation]]

## Workspace

- [[kb/notes/d3fend/techniques/d3-npc-notes|Open workspace note]]

