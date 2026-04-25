---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-DCE"
d3fend_name: "Dead Code Elimination"
d3fend_ontology_id: "d3f:DeadCodeElimination"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ADeadCodeElimination/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 20:43:29"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Removing unreachable or "dead code" from compiled source code.

## Workspace

- [[workspaces/defend/techniques/D3-DCE-dead_code_elimination-note|Open workspace note]]

![[workspaces/defend/techniques/D3-DCE-dead_code_elimination-note]]

## Parent Technique

- [[D3-AH-application_hardening|D3-AH: Application Hardening]]

## Knowledge Base Article

## How it works

Dead code is code that is considered unreachable by normal program execution. Dead code can be created by adding code under a condition that never evaluates to true. Dead code should be removed since this type of code can produce unexpected results, if accidentally or maliciously forced to execute.

Dead code identification is typically performed by algorithms that implement program flows analysis looking for unreachable code. The dead code is eliminated by instructing compilers to remove the code through compiler flags, i.e., '-fdce' is used for Dead Code Elimination.

## Considerations

Code can also be deemed unreachable for certain run-time conditions. Different deployed systems and environments may contain some code that is unreachable for the given environment. This technique does not consider run-time conditions for unreachable code.

## Ontology Relationships

- [[D3-AH-application_hardening|D3-AH: Application Hardening]]

