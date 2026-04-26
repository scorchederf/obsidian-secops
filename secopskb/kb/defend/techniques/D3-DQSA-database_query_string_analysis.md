---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-DQSA"
d3fend_name: "Database Query String Analysis"
d3fend_ontology_id: "d3f:DatabaseQueryStringAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ADatabaseQueryStringAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1190"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Analyzing database queries to detect [SQL Injection](https://capec.mitre.org/data/definitions/66.html).

## Workspace

- [[workspaces/defend/techniques/D3-DQSA-database_query_string_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-DQSA-database_query_string_analysis-note]]

## Parent Technique

- [[D3-PA-process_analysis|D3-PA: Process Analysis]]

## Related ATT&CK Techniques

- [[T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]]

## Knowledge Base Article

## How it works

Some implementations use software hooks to intercept function calls related to database query operations. Other implementations might intercept or collect network traffic. The database query string is then extracted and analyzed with various methods, for example:
* Detecting specific administrative SQL commands
* Anomalous sequences of commands when compared to a statistical baseline.
* Anomalous commands for a given user role.

## Considerations

Some capabilities sanitize queries before permitting them to be transmitted to the database. This incurs risks such altering data in an undesired way or breaking application functionality.

## Ontology Relationships

- [[D3-PA-process_analysis|D3-PA: Process Analysis]]

