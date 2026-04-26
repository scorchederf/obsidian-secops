---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-VTV"
d3fend_name: "Variable Type Validation"
d3fend_ontology_id: "d3f:VariableTypeValidation"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AVariableTypeValidation/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Ensuring that a variable has the correct type.

## Workspace

- [[workspaces/defend/techniques/D3-VTV-variable_type_validation-note|Open workspace note]]

![[workspaces/defend/techniques/D3-VTV-variable_type_validation-note]]

## Parent Technique

- [[D3-SCH-source_code_hardening|D3-SCH: Source Code Hardening]]

## Knowledge Base Article

## How it Works
A developer should consider how the variable will be used throughout the program and choose the correct variable type.
A developer should programmatically check if a variable has the correct (expected) type before using that variable.

## Considerations
* The result of an operation on an unexpected variable type will vary based on the language.
* Note: This resource should not be considered a definitive or exhaustive coding guideline.

## Ontology Relationships

- [[D3-SCH-source_code_hardening|D3-SCH: Source Code Hardening]]

